#!/bin/bash
docker run -it --rm \
  --gpus all \
  -v $(pwd):/workspace \
  -p 8888:8888 \
  --name ocr-container \
  ocr-gpu bash