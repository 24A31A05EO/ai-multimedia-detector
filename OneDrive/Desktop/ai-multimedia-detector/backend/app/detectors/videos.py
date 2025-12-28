import cv2
import numpy as np
import tempfile

def detect_video(data: bytes):
    # Save video temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
        tmp.write(data)
        tmp_path = tmp.name

    cap = cv2.VideoCapture(tmp_path)
    frame_count = 0
    inconsistencies = 0

    prev_frame = None

    while True:
        ret, frame = cap.read()
        if not ret or frame_count > 100:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if prev_frame is not None:
            diff = cv2.absdiff(prev_frame, gray)
            mean_diff = np.mean(diff)
            if mean_diff > 25:  # Arbitrary threshold for inconsistency
                inconsistencies += 1

        prev_frame = gray
        frame_count += 1

    cap.release()

    confidence = min(inconsistencies / max(frame_count, 1), 1.0)

    return {
        "type": "video",
        "is_fake": confidence > 0.5,
        "confidence": round(confidence, 2),
        "reason": "Frame inconsistencies detected" if confidence > 0.5 else "No major inconsistencies"
    }

