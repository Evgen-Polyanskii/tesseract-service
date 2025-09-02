FROM ubuntu:22.04

# Устанавливаем Tesseract и зависимости
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-rus \
    python3-pip \
    python3-dev \
    && apt-get clean

# Устанавливаем Python-библиотеки
RUN pip3 install flask pillow pytesseract

# Копируем API
COPY app.py /app/app.py
WORKDIR /app

EXPOSE 5000

CMD ["python3", "app.py"]
