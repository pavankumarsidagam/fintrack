import mongoengine as me
from datetime import datetime
from pytz import utc

class Transaction(me.Document):
    username = me.StringField(required=True)
    type = me.StringField(required=True)
    date = me.DateField(required=True)
    description = me.StringField()
    amount = me.FloatField()
    categories = me.DictField()

    created_at = me.DateTimeField(default=lambda: datetime.now(utc))
    updated_at = me.DateTimeField(default=lambda: datetime.now(utc))

    meta = {
        'collection': 'transactions'
    }

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now(utc)
        return super(Transaction, self).save(*args, **kwargs)

    def to_dict(self):
        return {
            "id": str(self.id),
            "username": self.username,
            "type": self.type,
            "date": self.date.isoformat() if self.date else None,
            "description": self.description,
            "amount": self.amount,
            "categories": self.categories,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
