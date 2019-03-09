import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds147225.mlab.com:47225/date4u

host = "ds147225.mlab.com"
port = 47225
db_name = "date4u"
user_name = "teamcode"
password = "phongxautrai1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())