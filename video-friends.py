import cv2
import os

# Directory containing your images
image_directory = 'D:\Byjus coding\project 105\Images'

# List all image files in the directory
image_files = [os.path.join(image_directory, f) for f in os.listdir(image_directory) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

# Sort the image files if they are not in the desired order
image_files.sort()

# Video output file name
output_video = 'output_video.mp4'

# Video frame width and height (adjust as needed)
frame_width = 1920
frame_height = 1080

# Frames per second (FPS) of the output video
fps = 30

# Initialize the video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can also try 'XVID' or 'MJPG' if 'mp4v' doesn't work
out = cv2.VideoWriter(output_video, fourcc, fps, (frame_width, frame_height))

# Loop through the image files and add them to the video
for image_file in image_files:
    img = cv2.imread(image_file)
    if img is not None:
        img = cv2.resize(img, (frame_width, frame_height))
        out.write(img)

# Release the video writer
out.release()

print(f'Video saved as {output_video}')
