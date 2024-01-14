from application import app, db
from datetime import datetime

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime.utcnow, nullable=False)
    type = db.Column(db.String(30), default='Income', nullable=False)
    category = db.Column(db.String(30), default='Food', nullable=False)
    amount = db.Column(db.Float, nullable=False)

    def __str__(self) -> str:
        return str(self.id)

if __name__ == '__main__':
    with app.app_context():
        #db.create_all()
        entry1 = Expense(type='Income', category='Salary', amount=10000)