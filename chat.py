from flask import Flask, request, render_template, send_file
from PIL import Image, ImageEnhance, ImageFilter
import io

app = Flask(__name__)
#python -c "import flask; print(flask.__version__)"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_image():
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
        elif action == 'color_enhance':
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(2.0)
        elif action == 'sharpen':
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(2.0)
        elif action == 'rotate':
            img = img.rotate(90)
        elif action == 'watermark':
            watermark = Image.open('watermark.png').convert("RGBA")
            img.paste(watermark, (0, 0), watermark)
        elif action == 'blur':
            img = img.filter(ImageFilter.GaussianBlur(5))
        
        img_io = io.BytesIO()
        img.save(img_io, 'JPEG')
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
