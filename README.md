# Facial Emotion Recognition

This project uses OpenCV and DeepFace to recognize emotions from a live webcam feed.

## Features
- Captures real-time video using a webcam.
- Detects and analyzes facial expressions.
- Displays the detected emotion on the video feed.
- Press 'q' to exit the application.

## Requirements
Ensure you have Python installed, then install the required dependencies:
```bash
pip install opencv-python deepface
```

## Usage
Run the script using:
```bash
python emotion.py
```

## How It Works
1. The script captures frames from the webcam.
2. It uses DeepFace to analyze facial expressions and detect emotions.
3. The detected emotion is displayed on the video feed.
4. The video feed continues until 'q' is pressed.

## Troubleshooting
- If the webcam does not open, check if it's being used by another application.
- If DeepFace throws an error, try setting `enforce_detection=True` to ensure a face is detected.
- If performance is slow, consider resizing the frame before analysis.

## License
This project is open-source and free to use for educational purposes.

