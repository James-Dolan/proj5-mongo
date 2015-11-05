from flask.ext.wtf import Form

from wtforms import TextField, TextAreaField, SubmitField

class MemoForm(Form):
	date = TextField("Date")
	memo = TextField("Memo")
	submit = SubmitField("Submit")
class IndexForm(Form):
	submit = SubmitField("remove")
