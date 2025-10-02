import cv2
import cv2.aruco as aruco
print(cv2.__version__)
# define a size of ArUco Marker
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_250)

def ArUcoMarkerGeneration():
    

    #define the testing marker's id and its image size (pixels)
    marker_id = 23
    marker_size = 200

    #generate a ArUco marker
    marker_image = aruco.generateImageMarker(aruco_dict,marker_id,marker_size)
    #adding a border for the marker. Otherwise, it can't detect correctly
    marker_with_border = cv2.copyMakeBorder(
        marker_image, 20, 20, 20, 20,
        cv2.BORDER_CONSTANT, value=255)
    #export the marker to python file root
    cv2.imwrite("aruco_marker_23.png", marker_with_border)

    print("ArUco marker saved as aruco_marker_23.png")

def readArUcoMarker():
    #load a marker's image
    img = cv2.imread("MilkCo Process Cards/Air_Distribution.png",0)
    print(img)


    parameters = aruco.DetectorParameters()

    detector = aruco.ArucoDetector(aruco_dict,parameters)
    corners, ids, rejected = detector.detectMarkers(img)
    if ids is not None:
        print("Detected IDs:", ids.flatten())
    else:
        print("No markers detected")
readArUcoMarker()
