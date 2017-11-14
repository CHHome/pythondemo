#ORM的编写


class Field(object):

    def __init__(self, name, colnum_type):
        self.name =name
        self.colnum_type = colnum_type

    def __str__(self):
        return  '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModeMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        maps = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                maps[k] = v
                # attrs.pop(k)放在这里是错误的，不能再遍历中改变dict的大小
        for k in maps.keys():
            attrs.pop(k)
        attrs['__maps__'] = maps
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModeMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        values = []
        for k, v in self.__maps__.items():
            fields.append(v.name)
            params.append('?')
            values.append(self[k])
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('values: %s' % values)


#user表
class User(Model):
    id = IntegerField('id')
    username = StringField('username')


#score表
class Score(Model):
    id = IntegerField('id')
    score = IntegerField('score')
    stard = StringField('stard')


u = User(id=1, username='chan')
u.save()

s = Score(id=1, score=90, stard='yes')
s.save()