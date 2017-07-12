from flask import render_template, request, send_file, Response
from app import app
from .forms import PictureForm

@app.route('/', methods=['GET'])
def picture_form():
    form = PictureForm()
    return render_template('upload_picture.html', form=form)

@app.route('/pic', methods=['POST'])
def pic():
    form = PictureForm()
    upload = form.file_field.data
    return Response(upload.read(), mimetype='image/gif')