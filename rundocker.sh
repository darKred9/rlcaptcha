#!/bin/bash
docker run -it --rm \
  --gpus all \
  -v $(pwd):/workspace \
  -p 8888:8888 \
  --name ocr-container \
  --entrypoint /bin/bash \
  ocr-gpu \
  -c "pip install --root-user-action=ignore pytesseract && apt-get update && apt-get install -y tesseract-ocr && bash"