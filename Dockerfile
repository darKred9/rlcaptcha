FROM nvidia/cuda:12.2.0-base-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
    python3 python3-pip python3-venv git curl wget \
    libgl1 libglib2.0-0 ffmpeg \
    && apt clean

# install pip
RUN pip3 install --upgrade pip

# install general pkgs 
RUN pip3 install \
    tensorflow \
    keras-ocr \
    easyocr \
    opencv-python pillow

# install pytorch
RUN pip3 install \
    torch torchvision torchaudio \
    --index-url https://download.pytorch.org/whl/cu118

WORKDIR /workspace
