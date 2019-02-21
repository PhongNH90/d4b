from mongoengine import Document, IntField, StringField, ListField, DictField

class User(Document):
    username = StringField()
    password = StringField()
    name = StringField()
    fr_name = StringField()
    gender = StringField()
    birth = DictField()
    age = IntField()
    img = StringField()
    address = StringField()
    hobby = ListField()
    like = IntField()
    interest = ListField()
    em = StringField() # email
    phone = IntField()
    fb = StringField() # facebook
    description =StringField() # tự mô tả ban thân
    stt = StringField() # Trạng thái: chỉ có 1 trạng thái hiển thị trên trang cá nhân





