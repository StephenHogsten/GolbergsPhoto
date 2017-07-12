from flask_wtf import FlaskForm
from flask_wtf.file import FileField

class PictureForm(FlaskForm):
    file_field = FileField('file_field')