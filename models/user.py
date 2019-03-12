from mongoengine import Document, IntField, StringField, ListField, DictField,DateTimeField
import datetime

class User(Document):
    em = StringField() # email
    password = StringField()
    name = StringField()
    username = StringField()
    # fr_name = StringField()
    gender = StringField()
    birth = DateTimeField()
    age = IntField()
    img = StringField()
    city = StringField()
    sport = StringField()
    music = StringField()
    book = StringField()
    movie = StringField()
    food = StringField()
    drink = StringField()
    like = IntField()
    interest = ListField()
    follow_list = ListField()
    phone = IntField()
    fb = StringField() # facebook
    description =StringField() # tự mô tả ban thân
    stt = StringField() # Trạng thái: chỉ có 1 trạng thái hiển thị trên trang cá nhân
    active = IntField()