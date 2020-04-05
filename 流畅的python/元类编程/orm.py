'''
Author       : ajin
Date         : 2020-04-04 19:24:59
Description  : 
email        : ajin_w@163.com
那曾梦想屠龙的少年，终会变成油腻的中年大叔，端坐于显示器前，从指尖流淌的代码，终会改变整个世界
'''

class Field:
    pass

class CharField(Field):
    def __init__(self, db_column, max_length = None):
        self._value = None
        self.db_column =db_column
        if max_length is None:
            raise ValueError("must need string length")
        self.max_length = max_length
    
    def __get__(self, instance, owner):
        return self._value
    
    def __set__(self, instance, val):
        if not isinstance(val, str):
            raise ValueError("must need str")
        if len(val) > self.max_length:
            raise ValueError("string length is too long")
        self._value = val




class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        if name == "BaseModel":
            return super().__new__(cls, name, bases, attrs, **kwargs)
        fields = {}
        for key, val in attrs.items():
            if isinstance(val, Field):
                fields[key] = val
        attrs_meta = attrs.get("Meta", None)
        _meta = {}
        db_table = name.lower()
        if attrs_meta is not None:
            table = getattr(attrs_meta, "db_table", None)
            if table is not None:
                db_table = table
        _meta["db_table"] = db_table
        attrs["_meta"] = _meta
        attrs["fields"] = fields
        del attrs["Meta"]
        # 元类编程中必须返回所以参数
        return super().__new__(cls, name, bases, attrs, **kwargs)

class BaseModel(metaclass=ModelMetaclass):
    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)
        return super().__init__()

    def save(self):
        field = []
        values = []
        for key, val in self.fields.items():
            db_column = val.db_column
            if db_column is None:
                db_column = key.lower()
            field.append(db_column)
            value = getattr(self, key)
            values.append(str(value)) 
        sql = "insert {db_table}({field}) values({values})".format(db_table = self._meta["db_table"], field = ",".join(field), values=",".join(values))
        print(sql)
class User(BaseModel):
    name = CharField(db_column="name", max_length=10)

    class Meta:
        db_table = "user"

if __name__ == "__main__":
    user = User(name = "ajin")
    user.name = "ajin"
    user.save()
