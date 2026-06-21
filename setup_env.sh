#!/bin/bash

echo "Updating system and installing Tesseract OCR..."
sudo apt-get update
sudo apt-get install -y tesseract-ocr
sudo apt-get install -y tesseract-ocr-hin  # Hindi Pack
sudo apt-get install -y tesseract-ocr-tel  # Telugu Pack
sudo apt-get install -y fonts-indic        # Essential Indic Fonts

echo "Installing Python dependencies from requirements.txt..."
pip install -r requirements.txt

echo "Setup Complete. You may need to restart your runtime if on Colab."
