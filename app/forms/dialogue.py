from wtforms import Form, StringField, TextAreaField
from wtforms.validators import DataRequired


class Dialogue(Form):
    """ Class used for handling the user input in the dialogue with Emily """
    user_answer_one = TextAreaField("How would you reply to Emely's question?", validators=[DataRequired()])
    user_follow_up_one = TextAreaField("What would Emely's follow-up question be to your answer?", validators=[DataRequired()])
    user_answer_two = TextAreaField("How would you answer Emely's follow-up question?", validators=[DataRequired()])
    user_follow_up_two = TextAreaField("What would Emely's follow-up question be to this answer?", validators=[DataRequired()])