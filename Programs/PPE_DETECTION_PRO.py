from ultralytics import YOLO
import cv2
import torch
from alert_systems import generate_alert  # Importing the alert function

# Ensure GPU is used if available
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Using device: {device}")

# Initialize webcam

cap = cv2.VideoCapture(0)  # For Webcam
cap.set(3, 1400)
cap.set(4, 720)

#cap = cv2.VideoCapture("C:/Users/manoj/PycharmProjects/Automation and Human Error Mitigation/.venv/Video/ppe_video.mp4")

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Load YOLO model on GPU
model = YOLO("ppe.pt").to(device)

# Class labels
classNames = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone',
              'Safety Vest', 'machinery', 'vehicle']

while True:
    success, img = cap.read()

    if not success:
        print("End of video or failed to read frame.")
        break

    # Run YOLO model on frame
    results = model(img, stream=True)

    # Collect missing PPE
    missing_ppe = []

    # Process detection results
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box coordinates
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # Confidence score
            conf = round(float(box.conf[0]), 2)

            # Class ID and name
            cls = int(box.cls[0])
            currentClass = classNames[cls]

            # Set bounding box color based on detection
            if currentClass in ['NO-Hardhat', 'NO-Mask', 'NO-Safety Vest']:
                color = (0, 0, 255)  # Red for missing PPE
                missing_ppe.append(currentClass.replace("NO-", ""))
            elif currentClass in ['Hardhat', 'Mask', 'Safety Vest']:
                color = (0, 255, 0)  # Green for detected PPE
            else:
                color = (255, 0, 0)  # Blue for other objects

            # Draw bounding box
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)

            # Display class name and confidence
            label = f"{currentClass} {conf:.2f}"
            text_size, _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)
            text_w, text_h = text_size

            cv2.rectangle(img, (x1, y1 - text_h - 10), (x1 + text_w, y1), color, -1)
            cv2.putText(img, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # Trigger voice alert
    generate_alert(missing_ppe)

    # Show frame
    cv2.imshow("Detecting...", img)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
