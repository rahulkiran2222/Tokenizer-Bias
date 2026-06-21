import pytesseract
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from indic_transliteration import sanscript

def get_ocr_corrupted_text(text, font_path="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
    """Renders text, adds noise, and OCRs it back."""
    try:
        img = Image.new('RGB', (1000, 100), color=(255, 255, 255))
        d = ImageDraw.Draw(img)
        # Note: You need a Hindi/Telugu font installed in Colab
        font = ImageFont.load_default() 
        d.text((10, 10), text, fill=(0, 0, 0), font=font)
        
        # Add slight Gaussian noise
        img_array = np.array(img)
        noise = np.random.normal(0, 25, img_array.shape).astype(np.uint8)
        noisy_img = Image.fromarray(np.clip(img_array + noise, 0, 255))
        
        # Tesseract OCR
        recovered = pytesseract.image_to_string(noisy_img, lang='hin+tel')
        return recovered.strip()
    except:
        return text # Fallback

def transliterate_text(text, lang='hi'):
    """Hindi/Telugu to Latin (Romanized)"""
    if lang == 'hi':
        return sanscript.transliterate(text, sanscript.DEVANAGARI, sanscript.ITRANS)
    return text
