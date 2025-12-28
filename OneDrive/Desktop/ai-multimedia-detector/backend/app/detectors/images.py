import cv2
import numpy as np
from app.utils.fft import fft_artifact_score

def detect_image(data: bytes):
    # Decode image from bytes
    image_array = np.frombuffer(data, np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    if image is None:
        return {
            "type": "image",
            "is_fake": False,
            "confidence": 0.0,
            "reason": "Invalid image format"
        }

    # Use FFT-based heuristic to detect artifacts
    score = fft_artifact_score(image)

    return {
        "type": "image",
        "is_fake": score > 0.6,
        "confidence": round(score, 2),
        "reason": "High-frequency noise pattern detected" if score > 0.6 else "No significant artifacts found"
    }
