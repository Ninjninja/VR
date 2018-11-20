import cv2

cam = cv2.VideoCapture(1)

cv2.namedWindow("test")

img_counter = 0
imgpoints = []
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

while True:
    ret, frame = cam.read()
    if not ret:
        break
    # cv2.imshow("test", frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)
    if ret == True:
        # objpoints.append(objp)
        cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        # imgpoints.append(corners)
        print(corners)
        cv2.drawChessboardCorners(frame, (7, 6), corners, ret)
    cv2.imshow("test", frame)
    k = cv2.waitKey(50)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        # cv2.imwrite(img_name, frame)
        # cv2.imshow(frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()