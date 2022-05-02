import datetime as dt

from . import db


class Opinion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    text = db.Column(db.Text, unique=True, nullable=False)
    source = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True, default=dt.datetime.now())
    added_by = db.Column(db.String(64))

    def to_dict(self):
        return dict(
            id=self.id,
            title=self.title,
            text=self.text,
            source=self.source,
            timestamp=self.timestamp,
            added_by=self.added_by
        )

    def from_dict(self, data):
        for field in ['title', 'text', 'source', 'added_by']:
            if field in data:
                setattr(self, field, data[field])

    def try_to_update(self, data: dict):
        self.title = data.get('title', self.title)
        self.text = data.get('text', self.text)
        self.source = data.get('source', self.source)
        self.added_by = data.get('added_by', self.added_by)
