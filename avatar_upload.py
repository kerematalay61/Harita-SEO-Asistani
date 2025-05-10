"""
Kullanıcıların profil fotoğrafı yüklemesini ve saklamasını sağlar.
"""
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "static/avatars"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_avatar(file, username):
    if file and allowed_file(file.filename):
        filename = secure_filename(f"{username}_avatar.{file.filename.rsplit('.', 1)[1].lower()}")
        path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(path)
        return path
    return None
