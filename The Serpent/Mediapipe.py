import cv2
import mediapipe as mp
from mediapipe.tasks.python import vision

model_path = r"C:\your\path\to\face_landmarker.task"

# Globals to hold latest results
latest_result = None

def result_callback(result, output_image, timestamp_ms):
    global latest_result
    latest_result = result  # just store results for main loop

# Setup options
BaseOptions = mp.tasks.BaseOptions
FaceLandmarker = vision.FaceLandmarker
FaceLandmarkerOptions = vision.FaceLandmarkerOptions
VisionRunningMode = vision.RunningMode

options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=result_callback,
    num_faces=1
)

# Open webcam
cap = cv2.VideoCapture(0)

with FaceLandmarker.create_from_options(options) as landmarker:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        h, w, _ = frame.shape

        # Convert to MediaPipe Image
        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        )

        # Get timestamp for async mode
        timestamp_ms = int(cap.get(cv2.CAP_PROP_POS_MSEC))
        landmarker.detect_async(mp_image, timestamp_ms)

        # Draw landmarks if available
        if latest_result and latest_result.face_landmarks:
            for face_landmarks in latest_result.face_landmarks:
                for lm in face_landmarks:
                    x, y = int(lm.x * w), int(lm.y * h)
                    cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

        # Show only ONE window
        cv2.imshow("Face Landmarks (LIVE_STREAM)", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
            break

cap.release()
cv2.destroyAllWindows()
