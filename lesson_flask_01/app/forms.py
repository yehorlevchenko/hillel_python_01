from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    username = StringField('Author', validators=[DataRequired()])
    text = TextAreaField('Message', validators=[DataRequired()])
    is_important = BooleanField('Important')
    submit = SubmitField('Publish')
