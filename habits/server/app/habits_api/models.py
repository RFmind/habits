from datetime import datetime
from app import db

class Habit(db.Model):

    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    activities = db.relationship('Activity', backref=db.backref('habit', lazy=True))

    def __repr__(self):
        return '<Habit id={} name={} />'.format(self.id, self.name)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def json_fields(self):
        return ['id', 'name']


class Activity(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    trigger_time = db.Column(db.DateTime, default=datetime.utcnow)
    habit_id = db.Column(db.Integer, db.ForeignKey('habit.id'))

    def as_dict(self):
        return {
            'trigger_time': self.trigger_time.strftime('%Y-%m-%dT%H:%M:%S')
        }
