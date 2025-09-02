from flask import Flask, request, jsonify
from PIL import Image, UnidentifiedImageError
from pdf2image import convert_from_bytes
import pytesseract
import io

app = Flask(__name__)

@app.route("/ocr", methods=["POST"])
def ocr():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    filename = file.filename.lower()

    text = ""

    try:
        if filename.endswith(".pdf"):
            # Конвертируем PDF в список изображений
            images = convert_from_bytes(file.read())
            for page_num, img in enumerate(images, start=1):
                page_text = pytesseract.image_to_string(img, lang='rus')
                text += f"\n--- Page {page_num} ---\n{page_text}"
        else:
            # Работаем с обычными изображениями
            img = Image.open(file.stream)
            text = pytesseract.image_to_string(img, lang='rus')

        return jsonify({"text": text})

    except UnidentifiedImageError:
        return jsonify({"error": "Uploaded file is not a valid image"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
