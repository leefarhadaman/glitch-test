from flask import Flask, request, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_image():
    print('Hello')
    if 'image' not in request.files:
        return 'No image uploaded', 400

    image_file = request.files['image']
    if image_file.filename == '':
        return 'No selected image', 400

    try:
        # Open the uploaded image
        img = Image.open(io.BytesIO(image_file.read()))
        # Convert the image to grayscale
        img = img.convert('L')
        # Save the grayscale image to a BytesIO object
        output = io.BytesIO()
        img.save(output, format='JPEG')
        output.seek(0)
        # Return the processed image to the client
        return send_file(output, mimetype='image/jpeg')
    except Exception as e:
        return f'Error processing image: {str(e)}', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

