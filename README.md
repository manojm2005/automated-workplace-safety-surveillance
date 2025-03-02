# Automated Workplace Safety Surveillance

An advanced AI-powered **Automated Workplace Safety Surveillance ** system that detects the absence of Personal Protective Equipment (PPE) in real-time and issues voice alerts. This project enhances workplace safety by reducing human error and ensuring compliance with safety protocols.

## 📊 Key Features

- **Real-Time Detection:** Identifies the presence or absence of essential PPE such as Hardhats, Masks, and Safety Vests.
- **Voice Alert System:** Provides real-time voice alerts for missing PPE to ensure immediate action.
- **Optimized Performance:** Utilizes GPU acceleration (if available) for faster processing.
- **Flexible Input:** Works with both webcam and video files.
- **Intelligent Alert Mechanism:** Implements a 5-second cooldown between repeated alerts.

## 🛠️ Technologies Used

- **YOLOv8:** For high-speed and accurate object detection.
- **OpenCV:** For video frame capture and visualization.
- **pyttsx3:** For generating voice alerts.
- **Python Threading:** To manage non-blocking alert generation.

## 📂 Project Structure

```
├── Dataset for AWSS/      # Dataset for training or testing
├── Programs/              # Core implementation
│   ├── PPE_DETECTION_PRO.py  # Main detection and alert script
│   └── alert_systems.py      # Voice alert system
├── Video/                 # Video inputs for detection
├── Sample Output.mp4      # Example output demonstration
├── ppe_model.pt           # YOLO detection model
└── README.md              # Documentation
```

## 📌 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/manojm2005/automated-workplace-safety-surveillance.git
cd automated-workplace-safety-surveillance
```

### Step 2: Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Ensure Model Availability
Ensure `ppe_model.pt` is present in the root directory.

## ▶️ Usage

### 1. Run the System
For webcam input:
```python
python Programs/PPE_DETECTION_PRO.py
```

To process a video file, update the video path in `cap = cv2.VideoCapture()`.

### 2. Exit
Press `q` to stop the program.

## 🧠 How It Works

1. Capture video input (webcam or pre-recorded video).
2. Perform PPE detection using YOLO.
3. Identify and log missing PPE.
4. Trigger voice alerts every 5 seconds if safety violations are detected.

### 📹 Sample Output

https://github.com/user-attachments/assets/c5db4638-6a82-44bc-a846-7bf7187ca8fc

## 🛠️ Customization

1. **Modify Alert Frequency:** Adjust the `alert_interval` in `alert_systems.py`.
2. **Add New PPE Types:** Update the `classNames` list in `PPE_DETECTION_PRO.py`.

## 🔬 Testing

- Ensure the system correctly detects missing PPE.
- Confirm voice alerts are triggered with a delay of 5 seconds.

## 📈 Future Enhancements

- Support for additional PPE categories.
- Enhanced alert customization.
- Integration with IoT-based safety systems.

## 📧 Contact

For inquiries and collaboration, reach out to: `manojmuniyasamy21@gmail.com`

