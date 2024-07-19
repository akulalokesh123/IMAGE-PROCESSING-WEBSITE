from flask import Flask, request, render_template, send_file
from PIL import Image, ImageEnhance, ImageFilter
import io
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('indeximg.html')

@app.route('/process', methods=['POST'])
def process_image():
    try:
        if 'file' not in request.files:
            return 'No file part'
        
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        
        if file:
            img = Image.open(file.stream)
            action = request.form.get('action')

            if action == 'resize':
                img = img.resize((300, 300))
            elif action == 'crop':
                img = img.crop((100, 100, 400, 400))
            elif action == 'black_white':
                img = img.convert('L')
            elif action == 'enhance_color':
                enhancer = ImageEnhance.Color(img)
                img = enhancer.enhance(2.0)
            elif action == 'sharpen':
                enhancer = ImageEnhance.Sharpness(img)
                img = enhancer.enhance(2.0)
            elif action == 'rotate':
                img = img.rotate(90)
            elif action == 'blur':
                img = img.filter(ImageFilter.BLUR)

            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format='JPEG')
            img_byte_arr.seek(0)

            return send_file(img_byte_arr, mimetype='image/jpeg')
    except Exception as e:
        return f'An error occurred: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
