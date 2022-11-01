import cv2

# Read the input image
# img = cv2.imread('/home/digital/selvapriyanka/AI-ML/gaze-correction/20221021_155557.jpg')

# Convert into grayscale

# Load the cascade
face_cascade = cv2.CascadeClassifier('face.xml')

# Detect faces
image = cv2.imread('/home/digital/selvapriyanka/AI-ML/gaze-correction/20221021_155557.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
image_array=[]

# Draw rectangle around the faces and crop the faces
def detect_face(faces):
    for (x, y, w, h) in faces:
        # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        faces = image[(y-10):y + h, (x-10):x + w]
        cv2.imshow("face",faces)
        cv2.imwrite("jeevi.jpg",faces)
        size = (faces.shape[1],faces.shape[0])
        return faces,size
faces,size=detect_face(faces)
# result = cv2.VideoWriter('cropped_jeevi.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),15, size)

# i=0
# while i<500:
#   print(i)
#   i+=1
#   image_array.append(faces)

# for i in range(len(image_array)):
#   result.write(image_array[i])
# result.release()
