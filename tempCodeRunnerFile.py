detected_img = aruco.drawDetectedMarkers(img.copy(), corners, ids)
        cv2.imshow("Detected ArUco", detected_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()