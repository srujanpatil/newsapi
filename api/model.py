import mongoengine

#Article Document Model
class Article(mongoengine.Document):
    Link = mongoengine.fields.URLField(required=True, unique=True)
    Title = mongoengine.fields.StringField(required=True)
    Author = mongoengine.fields.StringField()
    Description = mongoengine.fields.StringField()    
    PubDate = mongoengine.fields.DateTimeField()
    Category = mongoengine.fields.ListField()
    meta = {
        "db_alias":"Test", 
        "collection":"Article",
        'indexes': [{
            'fields': ['$Title', "$Description", "$Category"],
            'default_language': 'english',
            'weights': {'Title': 10, 'Category': 5}
        }]
    }
    