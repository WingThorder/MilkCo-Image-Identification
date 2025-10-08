import cv2
import cv2.aruco as aruco
print(cv2.__version__)
# define a size of ArUco Marker
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_250)

# A funtion to generate an ArUco Marker
def ArUcoMarkerGeneration():
    #define the testing marker's id and its image size (pixels)
    marker_id = 23
    marker_size = 96

    #generate a ArUco marker from 1 - 5
    for i in range(5):
        marker_image = aruco.generateImageMarker(aruco_dict,i+1,marker_size)
        #adding a border for the marker. Otherwise, it can't detect correctly
        # marker_with_border = cv2.copyMakeBorder(
        #     marker_image, 20, 20, 20, 20,
        #     cv2.BORDER_CONSTANT, value=255)
        #export the marker to python file root
        output_file_name = "aruco_marker_"+str(i+1)+".png"
        cv2.imwrite("Aruco_Code_Generation/"+output_file_name, marker_image)

        print("ArUco marker saved as "+output_file_name)


# A function to read image file and detect if marker exists
def readArUcoMarker(scanningDirection):
    #load a marker's image
    # img = cv2.imread("MilkCo Process Cards/TransportDieselTruck.png",0)
    # img = cv2.imread("TransportDieselTruckTakenByiPhone(4284x5712).png",0)
    img = cv2.imread("MultipleCardsH.png",0)

    # Define a Aruco detector by given dictionary
    parameters = aruco.DetectorParameters()
    detector = aruco.ArucoDetector(aruco_dict,parameters)
    # Detect an image with the marker
    corners, ids, rejected = detector.detectMarkers(img)
    markers = []
    sorted_markers = []
    if ids is not None:
        print(ids.flatten())
        for i, marker_id in enumerate(ids.flatten()):
            marker_corners = corners[i][0] # return a list of x y coordinates of a marker
            corners_mean_of_x = marker_corners[:,0].mean() # calculating mean of x coordinate of four corners
            corners_mean_of_y = marker_corners[:,1].mean() # calculating mean of x coordinate of four corners
            markers.append({"id":marker_id, "XMean":corners_mean_of_x, "YMean": corners_mean_of_y})
        print(markers)
        if(scanningDirection == "Vertical"):
            sorted_markers = sorted(markers, key=lambda marker: marker["YMean"])
        elif(scanningDirection == "Horizontal"):
            sorted_markers = sorted(markers, key=lambda marker: marker["XMean"])
        elif(scanningDirection == "in terms of card ID"):
            sorted_markers = markers.sort(key= lambda marker: marker.get("id"))
        print(sorted_markers)
        sorted_ids = [marker["id"] for marker in sorted_markers]
        print(*sorted_ids)
    else:
        print("No markers detected")
# ArUcoMarkerGeneration()
userResponse = input("Which direction would you want to search? (Vertical, Horizontal, in terms of card ID): ")
readArUcoMarker(userResponse)


