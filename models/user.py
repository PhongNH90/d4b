from mongoengine import Document, IntField, StringField, ListField, DictField

class User(Document):
    em = StringField() # email
    password = StringField()
    name = StringField()
    username = StringField()
    # fr_name = StringField()
    gender = StringField()
    birth = StringField()
    age = IntField()
    img = StringField()
    city = StringField()
    hobby = StringField()
    like = IntField()
    interest = ListField()
    follow_list = ListField()
    phone = IntField()
    fb = StringField() # facebook
    description =StringField() # tự mô tả ban thân
    stt = StringField() # Trạng thái: chỉ có 1 trạng thái hiển thị trên trang cá nhân
