from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email


class LibraryForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    title = StringField('title', validators=[DataRequired()])
    year = IntegerField('year', validators=[DataRequired()])


