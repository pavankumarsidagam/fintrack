import mongoengine as me

class Category(me.Document):
    name = me.StringField(required=True)
    type = me.StringField(required=True, choices=["income", "expense"])
    iconLib = me.StringField(required=True)
    iconName = me.StringField(required=True)
    colorClass = me.StringField(required=True)

    meta = {'collection': 'categories'} 