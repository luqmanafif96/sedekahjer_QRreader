from qreader import QReader
import cv2
import os

# Directory containing the images
image_fold = "./image"  # Replace with your folder path

# Create a QReader instance
qreader = QReader()

# List to store the results
results = []

# Loop through all files in the image folder
for image_name in os.listdir(image_fold): 
    try:
        # Construct the full image path
        image_path = os.path.join(image_fold, image_name)

        # Check if the file is an image
        if image_name.lower().endswith(('.png', '.jpg', 'jpeg')): 
            # Read the image and convert to RGB format
            image_QR = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

            # Detect and decode the QR code in the image
            decode_text = qreader.detect_and_decode(image=image_QR)  

            if decode_text: 
                results.append(f"Decoded text for {image_name}: {decode_text}")
            else: 
                results.append(f"QR code not found in {image_name}")
        else: 
            results.append(f"Skipped file (not an image): {image_name}")
     
    except cv2.error as e:
        results.append(f"OpenCV error inside {image_name}: {e}")
    except FileNotFoundError:
        results.append(f"Error: Image file {image_name} not found.")
    except Exception as e:
        results.append(f"An unexpected error occurred with {image_name}: {e}")

# Display all results
for result in results:
    print(result)