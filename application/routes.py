# Import the libraries from third-party packages
from flask import render_template, request, redirect, url_for, flash, get_flashed_messages
import json

# Import the local modules
from application import app, db
from application.form import UserInput
from application.models import Expense




@app.route('/') #@app.route is a decorator to tell Flask what URL should trigger our function
def index():
    entries = Expense.query.order_by(Expense.date.desc()).all()


    return render_template('index.html', title = 'Home', entries = entries)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    form = UserInput()
    if form.validate_on_submit():
        entry = Expense(type=form.type.data, category=form.category.data, amount=form.amount.data)
        with app.app_context():
            db.session.add(entry)
            db.session.commit()
        flash(f'Expense/Income added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add.html', title = 'add', form = form)

@app.route('/delete/<int:entry_id>', methods=['GET', 'POST'])
def delete(entry_id):
    entry = Expense.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash(f'Expense/Income deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    income_vs_expense = db.session.query(db.func.sum(Expense.amount), Expense.type).group_by(Expense.type).order_by(Expense.type).all()

    category_comparison = db.session.query(db.func.sum(Expense.amount), Expense.category).group_by(Expense.category).order_by(Expense.category).all()

    dates = db.session.query(db.func.sum(Expense.amount), Expense.date).group_by(Expense.date).order_by(Expense.date).all()

    income_category = []
    for amounts, _ in category_comparison:
        income_category.append(amounts)

    income_expense = []
    for total_amount, _ in income_vs_expense:
        income_expense.append(total_amount)

    over_time_expenditure = []
    dates_label = []
    for amount, date in dates:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_expenditure.append(amount)

    return render_template('dashboard.html',
                            income_vs_expense=json.dumps(income_expense),
                            income_category=json.dumps(income_category),
                            over_time_expenditure=json.dumps(over_time_expenditure),
                            dates_label =json.dumps(dates_label)
                        )