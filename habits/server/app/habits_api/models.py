from app import db

class Habit(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return '<Habit id={} name={}'.format(self.id, self.name)

    def save(self):
        db.session.add(self)
        db.session.commit()
