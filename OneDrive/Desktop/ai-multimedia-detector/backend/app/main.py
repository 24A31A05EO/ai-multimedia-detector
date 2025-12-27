from fastapi import FastAPI, UploadFile, File, Form
from app.detectors.images import detect_image
from app.detectors.videos import detect_video
from app.detectors.audio import detect_audio
from app.detectors.url_web import detect_url
from app.detectors.email import detect_email

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/detect/image")
async def image_detection(file: UploadFile = File(...)):
    data = await file.read()
    return detect_image(data)

@app.post("/detect/video")
async def video_detection(file: UploadFile = File(...)):
    data = await file.read()
    return detect_video(data)

@app.post("/detect/audio")
async def audio_detection(file: UploadFile = File(...)):
    data = await file.read()
    return detect_audio(data)

@app.post("/detect/url")
async def url_detection(url: str = Form(...)):
    return await detect_url(url)

@app.post("/detect/email")
async def email_detection(headers: str = Form(...), body: str = Form(...)):
    return await detect_email(headers, body)

