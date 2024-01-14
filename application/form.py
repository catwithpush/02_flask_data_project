from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class UserInput(FlaskForm):
    type = SelectField('Type', choices=[('Income', 'Income'), ('Expense', 'Expense')], validators=[DataRequired()])
    category = SelectField('Category', choices=[('Food', 'Food'), 
                                                   ('Transport', 'Transport'), 
                                                   ('Entertainment', 'Entertainment'), 
                                                   ('Others', 'Others')], validators=[DataRequired()])
    amount = IntegerField('Amount', validators=[DataRequired()])
    submit = SubmitField('Generate Report')

