FROM tensorflow/tensorflow:2.16.1-gpu

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    git curl wget \
    libgl1 libglib2.0-0 ffmpeg \
    tesseract-ocr \
    && apt clean

RUN python --version

RUN pip install --upgrade pip && pip install \
    keras-ocr \
    easyocr \
    opencv-python \
    pillow \
    pytesseract \
    torch torchvision torchaudio \
    stable-baselines3 gym numpy

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

RUN echo 'PS1="\[\e[32m\]\u@\h:\w\$\[\e[m\] "' >> /root/.bashrc

WORKDIR /workspace
ENV PYTHONPATH=/workspace