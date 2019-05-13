
@route('/upload', method='POST')
def do_upload():
    category = request.forms.get('category')
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png', '.jpg', '.jpeg'):
        return 'File extension not allowed.'

    save_path = get_save_path_for_category(category)
    upload.save(save_path)  # appends upload.filename automatically
    return 'OK'