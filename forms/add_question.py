from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddQuestionForm(FlaskForm):
    text = StringField('Текст вопроса', validators=[DataRequired()])
    answer = StringField('Правильный вариант ответа', validators=[DataRequired()])
    comments = StringField('Комментарии к ответу на вопрос')
    category = StringField('Категория')
    wrong_answer1 = StringField('Неправильные варианты ответа', validators=[DataRequired()])
    wrong_answer2 = StringField('', validators=[DataRequired()])
    wrong_answer3 = StringField('', validators=[DataRequired()])
    submit = SubmitField('Отправить')