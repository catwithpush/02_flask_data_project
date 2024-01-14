from application import app ,db
from application.models import Expense

if __name__ == '__main__':
    app.run(debug=True)



    ### DB Creation ###
    # entry1 = Expense(type='Income', category='Salary', amount=10000)
    # entry2 = Expense(type='Expense', category='Food', amount=1000)
    # entry3 = Expense(type='Expense', category='Food', amount=500)
    # with app.app_context():
    #     db.session.add(entry1)
    #     db.session.add(entry2)
    #     db.session.add(entry3)
    #     db.session.commit()
    #     query = Expense.query.all()
    #     print(query)
    #     for q in query:
    #         print(q.id, q.date, q.type, q.category, q.amount)

