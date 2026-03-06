import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

# Existing imports including RAMOS
# EJERCICIOS import

# All RAMOS configuration

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def render_portada():
    # Existing implementation
    pass

def render_seccion_pdf():
    # Existing implementation
    pass

def render_python():
    # Existing implementation
    pass

# New function allowing users to upload files
@app.route('/upload', methods=['POST'])
def render_upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return jsonify({'message': 'File uploaded successfully'}), 201

# Update router to handle the upload section

if __name__ == '__main__':
    app.run()
