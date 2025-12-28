import io
import librosa
import numpy as np

def detect_audio(data: bytes):
    # Load audio from bytes
    y, sr = librosa.load(io.BytesIO(data), sr=None)

    # Extract spectral features
    zcr = np.mean(librosa.feature.zero_crossing_rate(y))
    rolloff = np.mean(librosa.feature.spectral_rolloff(y=y, sr=sr))

    # Combine features into a confidence score
    score = min((zcr * 10 + rolloff / 10000) / 2, 1.0)

    return {
        "type": "audio",
        "is_fake": score > 0.6,
        "confidence": round(score, 2),
        "reason": "Synthetic spectral patterns detected" if score > 0.6 else "Natural audio characteristics"
    }
