import numpy as np
from PIL import Image
from keras.src.saving import load_model
import numpy as np
from keras.src.saving import load_model
from keras.src.utils import img_to_array
import os

PATH_TO_MODEL_FILE = "model.h5"
IMAGE_SIZE = (32, 32)
ALPHABET = [
    {"letter": "alef", "letter-ar": "ألف", "letter-index": 0},
    {"letter": "beh", "letter-ar": "باء", "letter-index": 1},
    {"letter": "teh", "letter-ar": "تاء", "letter-index": 2},
    {"letter": "theh", "letter-ar": "ثاء", "letter-index": 3},
    {"letter": "jeem", "letter-ar": "جيم", "letter-index": 4},
    {"letter": "hah", "letter-ar": "حاء", "letter-index": 5},
    {"letter": "khah", "letter-ar": "خاء", "letter-index": 6},
    {"letter": "dal", "letter-ar": "دال", "letter-index": 7},
    {"letter": "thal", "letter-ar": "ذال", "letter-index": 8},
    {"letter": "reh", "letter-ar": "راء", "letter-index": 9},
    {"letter": "zah", "letter-ar": "زاى", "letter-index": 10},
    {"letter": "seen", "letter-ar": "سين", "letter-index": 11},
    {"letter": "sheen", "letter-ar": "شين", "letter-index": 12},
    {"letter": "sad", "letter-ar": "صاد", "letter-index": 13},
    {"letter": "dad", "letter-ar": "ضاد", "letter-index": 14},
    {"letter": "tah", "letter-ar": "طاء", "letter-index": 15},
    {"letter": "zah", "letter-ar": "ظاء", "letter-index": 16},
    {"letter": "ain", "letter-ar": "عين", "letter-index": 17},
    {"letter": "ghain", "letter-ar": "غين", "letter-index": 18},
    {"letter": "feh", "letter-ar": "فاء", "letter-index": 19},
    {"letter": "qaf", "letter-ar": "قاف", "letter-index": 20},
    {"letter": "kaf", "letter-ar": "كاف", "letter-index": 21},
    {"letter": "lam", "letter-ar": "لام", "letter-index": 22},
    {"letter": "meem", "letter-ar": "ميم", "letter-index": 23},
    {"letter": "noon", "letter-ar": "نون", "letter-index": 24},
    {"letter": "heh", "letter-ar": "هاء", "letter-index": 25},
    {"letter": "waw", "letter-ar": "واو", "letter-index": 26},
    {"letter": "yeh", "letter-ar": "ياء", "letter-index": 27},
]


def process_image(image_path: str) -> dict:
    try:
        img = Image.open(image_path).convert("L")  # Convert to grayscale
        img = img.resize(IMAGE_SIZE)  # Resize image to 32x32
        img_arr = np.array(img)  # Convert image to numpy array
        # img_arr = 255 - img_arr  # Invert image (assuming black char with white background)
        # img_arr = img_arr / 255.0  # Normalize pixel values to range [0, 1]
        img_arr = img_arr.reshape(
            (1, IMAGE_SIZE[0], IMAGE_SIZE[1], 1)
        )  # Reshape to match model input shape
        model = load_model(PATH_TO_MODEL_FILE)
        prediction = model.predict(np.expand_dims(img_to_array(img), axis=0))
        idx = np.argmax(prediction)
        confidence = (prediction[0][idx]) * 100
        print("Confidence: ", confidence)
        print("Prediction: ", idx, "th letter")
        print("ALPHABET = ", ALPHABET[idx])
        ALPHABET[idx]["confidence"] = confidence
        result = {"has_error": False, "data": ALPHABET[idx], "error": None}
        os.remove(image_path)
        return result
    except Exception as e:
        return {"has_error": True, "data": None, "error": str(e), "confidence": None}

print(np.__version__)