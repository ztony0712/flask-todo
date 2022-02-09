# this is the file for data validation

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, NumberRange, length


class ItemForm(FlaskForm):
    title = StringField('title', validators=[length(min=1, max=50)])
    date = DateField('date', validators=[DataRequired()])
    code = StringField('code', validators=[length(min=0, max=50)])
    dcp = TextAreaField('dcp', validators=[length(min=0, max=500)])
    total = IntegerField('total', validators=[NumberRange(1,)])
    step = IntegerField('step', validators=[NumberRange(1,)])


class TitleForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
