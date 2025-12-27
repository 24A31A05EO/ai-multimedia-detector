import numpy as np
import cv2

def fft_artifact_score(image_bgr):
    # Convert image to grayscale
    gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

    # Apply FFT
    f = np.fft.fft2(gray)
    fshift = np.fft.fftshift(f)
    magnitude = 20 * np.log(np.abs(fshift) + 1e-8)

    # Analyze center vs edges
    h, w = magnitude.shape
    cy, cx = h // 2, w // 2
    center = magnitude[cy-10:cy+10, cx-10:cx+10].mean()
    edges = magnitude.mean() - center

    score = edges / (center + 1e-8)
    return float(np.clip(score / 10.0, 0.0, 1.0))
