import cv2
import os

def extract_frames(video_path, output_folder):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    frame_count = 0
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Save the frame as an image file
        file_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        cv2.imwrite(file_path, frame)
        
        frame_count += 1

    # Release resources
    cap.release()
    print(f"Extraction complete. {frame_count} frames saved to '{output_folder}'.")

# Usage
path = os.getcwd()
extract_frames(os.path.join(path , 'Task.mp4'), 'frames')
