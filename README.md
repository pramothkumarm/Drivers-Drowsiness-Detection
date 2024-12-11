# Driver Drowsiness Detection

## Overview
The Driver Drowsiness Detection system is designed to enhance road safety by identifying signs of driver fatigue in real-time. This project uses machine learning and computer vision techniques to monitor driver behavior and detect drowsiness, ensuring proactive measures can be taken to prevent accidents.

---

## Features
- **Real-time Monitoring:** Detects driver drowsiness using live video feeds.
- **Facial Landmarks Detection:** Analyzes eye and mouth movements to identify drowsiness.
- **Simple Classification:** Uses a classification model to predict drowsiness state without audio alerts.
- **Cross-Platform Compatibility:** Can be implemented on various platforms using Python.

---

## Prerequisites
### Hardware
- Webcam or any camera device for video feed.

### Software
- Python (3.7 or above)
- Required libraries:
  - `OpenCV`
  - `dlib`
  - `imutils`
  - `scipy`

---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/drivers-drowsiness-detection.git
   cd drivers-drowsiness-detection
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure you have a camera connected to your system.

---

## How It Works
1. **Facial Landmarks Detection:**
   - The system detects key facial landmarks (eyes, nose, mouth).
2. **Eye Aspect Ratio (EAR):**
   - Calculates the ratio of distances between predefined eye landmarks.
   - If the EAR falls below a threshold for a defined period, it indicates drowsiness.
3. **Mouth Aspect Ratio (MAR):**
   - Measures yawning by analyzing mouth opening movements.
4. **Simple Classification:**
   - Uses a classification model to identify drowsiness based on EAR and MAR without triggering audio alerts.

---

## Usage
1. Run the script:
   ```bash
   python drowsiness_detection.py
   ```
2. The system will start capturing video from the connected camera.
3. The drowsiness state will be displayed on the screen.

---

## Configuration
- Modify the thresholds in the script to adjust sensitivity:
  - `EAR_THRESHOLD`: Minimum EAR value to indicate eye closure.
  - `EAR_CONSEC_FRAMES`: Number of consecutive frames to detect drowsiness.
  - `MAR_THRESHOLD`: Minimum MAR value to indicate yawning.

---

## Directory Structure
```
.
├── drowsiness_detection.py  # Main script
├── requirements.txt         # Dependencies
├── README.md                # Project documentation
└── models                   # Pretrained models (if any)
```

---

## Demo
Include a video or image showing the system in action.

---

## Future Enhancements
- Integration with IoT devices for real-time vehicle control.
- Improved accuracy using deep learning models (e.g., CNN, YOLO).
- Multi-camera support for detecting driver distraction.

---

## Contributors
- [Your Name](https://github.com/your-profile)

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

