import cv2
from deepface import DeepFace

def recognize_emotion():
    cap = cv2.VideoCapture(0)  # Open webcam

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            break

        try:
            # Analyze the face and predict emotions
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

            # Extract the dominant emotion
            emotion = result[0]['dominant_emotion']

            # Display the emotion on the video feed
            cv2.putText(frame, f"Emotion: {emotion}", (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        except Exception as e:
            print(f"Error: {e}")

        # Show the video feed
        cv2.imshow("Facial Emotion Recognition", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Run the function
recognize_emotion()