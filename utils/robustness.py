import pytesseract
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from indic_transliteration import sanscript

def get_ocr_noise(text, lang='hin'):
    try:
        img = Image.new('RGB', (800, 100), color=(255, 255, 255))
        d = ImageDraw.Draw(img)
        # Fallback font handling
        font = ImageFont.load_default()
        d.text((10, 10), text, fill=(0, 0, 0), font=font)
        recovered = pytesseract.image_to_string(img, lang=lang)
        return recovered.strip() if recovered.strip() else text
    except:
        return text

def get_transliteration(text):
    return sanscript.transliterate(text, sanscript.DEVANAGARI, sanscript.ITRANS)
