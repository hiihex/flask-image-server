from flask import Blueprint, request, jsonify, current_app, url_for, redirect
import os
from werkzeug.utils import secure_filename
import filetype

image_mod = Blueprint('image_mod', __name__, url_prefix='/image')


@image_mod.route('/upload', methods=["POST"])
def upload_image_post():
    image_file = request.files.get('image_file')
    if not image_file:
        return jsonify({"error": "You did not pass an image in your request"}), 400

    if not filetype.is_image(image_file):
        return jsonify({"error": "You passed a file that is not an image"}), 400

    filename = image_file.filename

    image_file.seek(0)
    image_file.save(os.path.join(f"{os.getcwd()}\\app\\static\\upload", filename))

    return jsonify({
        "status": "success",
        "image_path": f"http://{request.environ['SERVER_NAME']}:{request.environ['SERVER_PORT']}/static/upload/{filename}"
    })
