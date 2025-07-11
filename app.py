from flask import Flask, request, render_template, send_file, send_from_directory
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont
import io, os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('indeximg.html')

@app.route('/process', methods=['POST'])
def process_image():
    file = request.files.get('file')
    if not file or file.filename == '':
        return 'No file provided', 400

    img = Image.open(file.stream)
    action = request.form.get('action')

    if action == 'resize':
        img = img.resize((300, 300))
    elif action == 'enhance':
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2.0)
    elif action == 'sharpen':
        img = img.filter(ImageFilter.SHARPEN)
    elif action == 'rotate':
        img = img.rotate(90)
    elif action == 'flip':
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif action == 'grayscale':
        img = img.convert("L")
    elif action == 'thumbnail':
        img.thumbnail((100, 100))
    elif action == 'blur':
        img = img.filter(ImageFilter.BLUR)
    elif action == 'watermark':
        watermark = Image.new("RGBA", img.size)
        draw = ImageDraw.Draw(watermark)
        font = ImageFont.load_default()
        draw.text((10, 10), "Watermark", fill=(255, 255, 255, 128), font=font)
        img = Image.alpha_composite(img.convert("RGBA"), watermark)
    elif action == 'passport_size':
        img = img.resize((413, 531))  # typical 2x2 inch at 300dpi
    else:
        return 'Invalid action', 400

    # Convert image to RGB before saving as JPEG
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    output = io.BytesIO()
    img.save(output, format='JPEG')
    output.seek(0)
    return send_file(output, mimetype='image/jpeg')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
