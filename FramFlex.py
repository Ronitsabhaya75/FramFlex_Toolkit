''' 
import 2 libraries cv2(opening camera) and matplotlib.pyplot(working on graphs)
'''
import cv2
import matplotlib.pyplot as plt

'''
this function reads the pre-define front-face reading Xml file which will be installed when installing opnecv(cv2)
'''
def readingfile():
    face_cap = cv2.CascadeClassifier("/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/cv2/data/haarcascade_frontalface_default.xml")
    return face_cap

'''
this function open up the camera and capture the video
if it's not the frame it break the loop and exits
'''
def opencam(face_cap):

    video_cap = cv2.VideoCapture(1)


    while True:
        ret, video_data = video_cap.read()
        if not ret:
            break

        col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
        
        face = face_cap.detectMultiScale(
            col,
            scaleFactor = 1.1, 
            minNeighbors = 7,
            minSize = (30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE
        )


#this block of code is used for creating rectangle

        for(x,y,w,h) in face:
            cv2.rectangle(video_data, (x,y),(x+w,y+h),(120,120,120),2)
        cv2.imshow("Live Cam", video_data)

        key = cv2.waitKey(1)

        if key == ord("c"):
            print("Close succesfully")
            break

    video_cap.release()
    cv2.destroyAllWindows()


'''
this function open up the camera and capture the outline
if it's not the frame it break the loop and exits 

Canny() function in OpenCV performs edge detection on an image
'''
def outline(face_cap):
    video_cap = cv2.VideoCapture(1)


    while True:
        ret, video_data = video_cap.read()

        if not ret:
            break

        gray = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)

        edges = cv2.Canny(gray, 100, 200)

        cv2.imshow('Outline Cam', edges)

        key = cv2.waitKey(1)
        if key == ord('c'):
            print("Close succesfully")
            break

    video_cap.release()
    cv2.destroyAllWindows()


'''
this function open up the camera and capture the cartoon
if it's not the frame it break the loop and exits 

bilateralFilter replaces the intensity of each pixel with a weighted average of intensity values from nearby pixels
median blur takes the median of all the pixels under the kernel area and the central element is replaced with this median value
adapative threshold the algorithm determines the threshold for a pixel based on a small region around it
'''

def cartoon(face_cap):
    video_cap = cv2.VideoCapture(1)


    while True:
        ret, frame = video_cap.read()

        if not ret:
            break

        color = cv2.bilateralFilter(frame, 9, 9, 7)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
        blur = cv2.medianBlur(gray, 7)
        edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
        frame_edge = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
        cartoon = cv2.bitwise_and(color, frame_edge)
    
        cv2.imshow('Cartoonized', cartoon)

        if cv2.waitKey(1) == ord('c'):
            print("Close succesfully")
            break
    video_cap.release()
    cv2.destroyAllWindows()


'''
this function is used for knowing the number of pixels in particular frame.
interactive mode build plots from the command line and want to see the effect of each command while you are building the figure.

axis 1 shows the camera and axis 2 shows the histogram within the pause of 1 second
ravel fnuction convert the 2 dimensional array to 1 dimesional
'''
def numberofpixelsingrayframe():
    plt.ion()


    fig, (ax1, ax2) = plt.subplots(1, 2)
    video_cap = cv2.VideoCapture(1)

    while True:
        ret, video_data = video_cap.read()
        if not ret:
            break

        col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
        ax1.clear()
        ax1.imshow(col, cmap='gray')
        ax1.set_title('Video Feed')

        ax2.clear()
        ax2.hist(col.ravel(), bins=256, range=[0, 256], color='black', alpha=0.75)
        ax2.set_title('Intensity Histogram')
        ax2.set_xlabel('frame')
        ax2.set_ylabel('number of pixels')

        plt.draw()
        plt.pause(1)

        key = cv2.waitKey(1)
        if key == ord("c"):
            print("Closing the application...")
            break
    
    plt.ioff()
    video_cap.release()
    cv2.destroyAllWindows()

'''
this function is used for knowing the number of pixel in color frame.
interactive mode build plots from the command line and want to see the effect of each command while you are building the figure.

axis 1 shows the camera and axis 2 shows the histogram within the pause of 1 second
ravel fnuction convert the 2 dimensional array to 1 dimesional
'''
def numberofpixelsincolorframe():
    plt.ion()
    fig, (ax1, ax2) = plt.subplots(1, 2)
    video_cap = cv2.VideoCapture(1)
    
    while True:
        ret,video_data = video_cap.read()
        if not ret:
            break
        col = cv2.cvtColor(video_data, cv2.COLOR_BGR2RGB)
        ax1.clear()
        ax1.imshow(col)
        ax1.set_title('Video Feed')

        ax2.clear()
        ax2.hist(col.ravel(), bins=256, range=[0, 256], color='black', alpha=0.75)
        ax2.set_title('Intensity Histogram')
        ax2.set_xlabel('frame')
        ax2.set_ylabel('number of pixels')
       
        plt.draw()
        plt.pause(1) 

        if cv2.waitKey(1) == ord("c"):
            print("Closing the application...")
            break
    plt.ioff()
    video_cap.release()
    cv2.destroyAllWindows()

# Main code
face_cap = readingfile()

i = int(input(
              " press c to close the live cam\n"
              "Enter the camera thing you want see:\n 1. Live Cam\n 2. Number of pixels in a frame\n\n "
              )
            )
if i == 1:
    choice = int(input("What type of live cam:\n 1. Simple\n 2. outline\n 3. cartoon\n\n"))
    if choice == 1:
        opencam(face_cap)
        
    elif choice == 2:
        outline(face_cap)
    
    elif choice == 3:
        cartoon(face_cap)

elif i == 2:
    choice = int(input("What type of live cam:\n 1. graph of pixels in gray frame\n 2. graph of pixels in color frame\n\n"))
    if choice == 1:
        numberofpixelsingrayframe()

    elif choice == 2:
        numberofpixelsincolorframe()