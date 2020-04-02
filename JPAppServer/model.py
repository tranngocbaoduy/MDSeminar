from JPAppServer import db
from datetime import datetime
from flask import current_app 
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import json

 
class JsonSerializable(object):
    def toJson(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.toJson()
 
class Vocabulary(db.Document): 
    hiragana = db.StringField(required=True)
    katakana = db.StringField()
    kanji = db.StringField()
    romanji = db.StringField()
    vi_translate = db.StringField()
    en_translate = db.StringField()
    lesson = db.StringField() 
    created_date = db.DateTimeField(default = datetime.utcnow())

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4) 
