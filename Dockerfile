FROM ubuntu:22.04

# Устанавливаем Tesseract и зависимости
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-rus \
    libtesseract-dev \
    poppler-utils \
    python3-pip \
    && apt-get clean

# Устанавливаем Python-библиотеки
RUN pip3 install flask pillow pytesseract pdf2image

# Копируем API
COPY app.py /app/app.py
WORKDIR /app

EXPOSE 5000

CMD ["python3", "app.py"]
