# import cv2
# import pickle


# width, height = 107, 48

# try:
#     with open('CarParkPos', 'rb') as f:
#         posList = pickle.load(f)
# except:
#     posList = []


# def mouseClick(events,x,y,flags,params):
#     if events == cv2.EVENT_LBUTTONDOWN:
#         posList.append((x,y))
#     if events == cv2.EVENT_RBUTTONDOWN:
#         for i, pos in enumerate(posList):
#             x1, y1 = pos
#             if x1 < x < x1 + width and y1 < y < y1 + height:
#                 posList.pop(i)
    
#     with open('CarParkPos', 'wb') as f:
#         pickle.dump(posList, f)

# while True:
#     img = cv2.imread('D:\Project_2\ParkingSpaces\ezgif-frame-001.jpg')
#     for pos in posList:
#         cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

#     cv2.imshow("Image", img)
#     cv2.setMouseCallback("Image", mouseClick)
#     cv2.waitKey(1)





# import cv2
# import pickle

# width, height = 107, 48

# # Load the list of positions (if available)
# try:
#     with open('CarParkPos', 'rb') as f:
#         posList = pickle.load(f)
# except:
#     posList = []

# # Mouse callback function
# def mouseClick(events, x, y, flags, params):
#     if events == cv2.EVENT_LBUTTONDOWN:
#         posList.append((x, y))
#     if events == cv2.EVENT_RBUTTONDOWN:
#         for i, pos in enumerate(posList):
#             x1, y1 = pos
#             if x1 < x < x1 + width and y1 < y < y1 + height:
#                 posList.pop(i)
    
#     # Save the updated positions to file
#     with open('CarParkPos', 'wb') as f:
#         pickle.dump(posList, f)

# # Open the video capture (0 for webcam, or provide path to a video file)

# while True:
#     cap = cv2.VideoCapture('D:\Project_2\ParkingSpaces\Khare_testvideo_03.mp4')
#     success, img = cap.read()  # Read a frame from the video
    
#     if not success:
#         break  # If no frame is read, exit the loop (end of video or error)

#     # Draw rectangles for each position in posList
#     for pos in posList:
#         cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

#     # Display the frame
#     cv2.imshow("Video", img)

#     # Set mouse callback function for drawing/removing rectangles
#     cv2.setMouseCallback("Video", mouseClick)

#     # Break the loop when 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the video capture and close all windows
# cap.release()
# cv2.destroyAllWindows()


import cv2
import pickle

width, height = 107, 48
# Load the list of positions (if available)
try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

# Mouse callback function
def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)
    
    # Save the updated positions to file
    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)

# Open the video capture (0 for webcam, or provide path to a video file)

# Get the original width and height of the video
# original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Set the window name
cv2.namedWindow("Video", cv2.WINDOW_NORMAL)  # Allow window to be resizable

while True:
    cap = cv2.VideoCapture('D:\Project_2\ParkingSpaces\carPark.mp4')
    success, img = cap.read()  # Read a frame from the video
    
    if not success:
        break  # If no frame is read, exit the loop (end of video or error)

    # Draw rectangles for each position in posList
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    # Display the original video frame (img) directly
    cv2.imshow("Video", img)

    # Set mouse callback function for drawing/removing rectangles
    cv2.setMouseCallback("Video", mouseClick)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()