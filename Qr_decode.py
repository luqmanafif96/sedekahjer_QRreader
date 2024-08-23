from qreader import QReader
import cv2
import os
#check the directory => refering to the folder
image_fold = "./image"


# Create a QReader instance
qreader = QReader()
# loop the file image folder 
for image_name in os.listdir(image_fold) : 

    # we construct the path image 
    try : 
        image_path = os.path.join(image_fold,image_name)

        if image_name.lower().endswith(('.png','.jpg','jpeg')) : 

            #find the image 
            image_QR = cv2.cvtColor(cv2.imread(image_path),cv2.COLOR_BAYER_BG2BGR)  

    
"""try:
    # Get the image that contains the QR code
    image = cv2.cvtColor(cv2.imread("./image/Bandar_cassia.jpg"), cv2.COLOR_BGR2RGB)

    # Use the detect_and_decode function to get the decoded text
    decoded_text = qreader.detect_and_decode(image=image)
    
    if decoded_text:
        print(f"Decoded text: {decoded_text}")
    else:
        print("No QR code detected.")
"""
except cv2.error as e:
    print("OpenCV error:", e)
except FileNotFoundError:
    print("Error: Image file not found.")
except Exception as e:
    print("An unexpected error occurred:", e)
