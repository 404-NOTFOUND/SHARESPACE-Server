from flask import Flask, render_template, redirect, request, url_for, Blueprint
import os, base64
from werkzeug import secure_filename
from flask import current_app as app

main = Blueprint('main', __name__, template_folder='templates/main')
ALLOWED_EXTENSIONS = set(['.jpg', '.jpeg'])

def allowed_file(filename):
    return os.path.splitext(filename)[1] in ALLOWED_EXTENSIONS

@main.route('/view/<image_id>')
def view(image_id):
    image_id = base64.b64decode(image_id).decode()
    # for testing
    title = 'Petra'
    article = 'Petra, originally known to its inhabitants as Raqmu, is a historical and archaeological city in southern Jordan.'
    tags = ['cool', 'wow', 'beautiful']
    # 요청받은 id의 파일에 대한 정보(제목, 본문, 태그)를 가져와 템플릿으로 전달해야 함
    # 태그 정보가 없을 경우, image_classification으로 태그를 생성해 저장함.
    return render_template(
        'vrview/view.html', 
        image_url=image_id, 
        current_url=request.base_url,
        title=title,
        article=article, 
        tags=tags
    )

@main.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files: # no file part in POST request
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '': # no file selected
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # 이 부분에서 b64encode()하는 URL을 (외부에서 접속가능한) 정적 URL로 고칠 것
            # (해당 URL을 Google VR view에서 참조하기 때문)
            image_id = base64.b64encode(bytes(filename, 'UTF_8')).decode()
            return redirect('/view/' + image_id)
    return render_template('vrview/upload.html')

@main.route('/search')
def search():
    return 'unavailable at the moment'
