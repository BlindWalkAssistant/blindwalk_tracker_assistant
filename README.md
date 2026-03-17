# blindwalk_tracker_assistant
# 👁️ BlindWalk Assistant

An AI-powered real-time object detection and voice guidance system designed to assist visually impaired individuals in navigating safely.

---

## 🚀 Features

- 🔍 Real-time object detection using YOLO
- 🎯 Detects obstacles like people, vehicles, stairs, etc.
- 📏 Distance estimation for nearby objects
- 🔊 Voice alerts for detected obstacles
- 📱 Can be integrated with mobile camera or webcam
- ⚡ Lightweight and optimized for real-time performance

---

## 🧠 How It Works

1. The camera captures live video feed.
2. Each frame is passed to the trained YOLO model.
3. The model detects objects and draws bounding boxes.
4. Distance is estimated based on object size/position.
5. Important alerts are converted into speech output.
6. The user hears real-time voice guidance.

---

## 🏗️ Tech Stack

- Python 🐍
- OpenCV
- YOLO (Ultralytics)
- PyTorch
- Text-to-Speech (pyttsx3 / gTTS)

---

## 📂 Project Structure

```
BlindWalkAssistant/
│── models/
│   └── best.pt
│
│── src/
│   ├── voice_alert.py
│   ├── distance_estimator.py
│   └── utils.py
│
│── main.py
│── requirements.txt
│── README.md
```





---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/BlindWalkAssistant.git
```
```bash
cd BlindWalkAssistant
```


###  instal dependencies
```bash
pip install -r requirements.txt
```


### RUN the model
```bash
python run.py
```