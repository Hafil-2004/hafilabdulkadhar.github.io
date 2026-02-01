import cv2
import os
import numpy as np
from keras.models import load_model
from pygame import mixer

# Initialize sound
mixer.init()
try:
    sound = mixer.Sound('alarm.wav')
except Exception as e:
    print(f"Error loading sound: {e}")
    sound = None

# Load Haar cascades for face and eyes
detector = {
    'face': cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml'),
    'left_eye': cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_lefteye_2splits.xml'),
    'right_eye': cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_righteye_2splits.xml')
}

# Load model
try:
    model = load_model('CNN__model.h5')
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
score = 0
thicc = 2

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector['face'].detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))
    rpred, lpred = [1], [1]  # Default: Eyes open

    for (fx, fy, fw, fh) in faces:
        cv2.rectangle(frame, (fx, fy), (fx + fw, fy + fh), (255, 0, 0), 2)
        
        roi_gray = gray[fy:fy + fh, fx:fx + fw]
        
        left_eye = detector['left_eye'].detectMultiScale(roi_gray)
        right_eye = detector['right_eye'].detectMultiScale(roi_gray)
        
        if len(left_eye) > 0:
            (ex, ey, ew, eh) = left_eye[0]
            l_eye = roi_gray[ey:ey + eh, ex:ex + ew]
            l_eye = cv2.resize(l_eye, (100, 100)) / 255.0
            l_eye = np.expand_dims(l_eye.reshape(100, 100, 1), axis=0)
            if model:
                lpred = np.argmax(model.predict(l_eye), axis=1)
            cv2.rectangle(frame, (fx + ex, fy + ey), (fx + ex + ew, fy + ey + eh), (0, 255, 0), 2)
        
        if len(right_eye) > 0:
            (ex, ey, ew, eh) = right_eye[0]
            r_eye = roi_gray[ey:ey + eh, ex:ex + ew]
            r_eye = cv2.resize(r_eye, (100, 100)) / 255.0
            r_eye = np.expand_dims(r_eye.reshape(100, 100, 1), axis=0)
            if model:
                rpred = np.argmax(model.predict(r_eye), axis=1)
            cv2.rectangle(frame, (fx + ex, fy + ey), (fx + ex + ew, fy + ey + eh), (0, 255, 0), 2)
    
    if rpred[0] == 0 and lpred[0] == 0:
        score += 1
        cv2.putText(frame, "Drowsy", (10, 50), font, 1, (0, 0, 255), 2)
    else:
        score = max(0, score - 1)
        cv2.putText(frame, "Awake", (10, 50), font, 1, (0, 255, 0), 2)
    
    if score > 10 and sound:
        try:
            sound.play()
        except Exception as e:
            print(f"Sound play error: {e}")
    
    cv2.imshow('Drowsiness Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
