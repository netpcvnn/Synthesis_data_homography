import cv2
import numpy as np

frame= cv2.imread('sample_image.png',1)
# background= cv2.imread('background.png',cv2.IMREAD_UNCHANGE)
background= cv2.imread('museum.jpg',1)
# background   = cv2.resize(background, (0,0), fx=0.3, fy=0.3) 

frame = cv2.resize(frame, (0,0), fx=0.1, fy=0.1) 
# cv2.imshow("Input", frame)
# frame = cv2.resize(frame, (background.shape[1], background.shape[0]))
cols, rows = frame.shape[0], frame.shape[1]
# print(rows, cols

pts1 = np.float32([[50,50],[rows+50,40],[rows+100,cols+40],[0+50,cols+60]])
pts2 = np.float32([[0,0],[rows,0],[rows,cols],[0,cols]])

M = cv2.getPerspectiveTransform(pts2,pts1)

dst = cv2.warpPerspective(frame, M, (int(rows*2),int(cols*2)), cv2.BORDER_CONSTANT,borderValue=(255, 255, 255,1))

filler = cv2.convexHull(pts1)
# cv2.fillConvexPoly(background, filler, 1)
a3 = np.array( [[[50,50],[rows+50,40],[rows+100,cols+40],[0+50,cols+60]]], dtype=np.int32 )
# cv2.fillConvexPoly(background, np.array(filter, 'int32'), 1)
# cv2.fillPoly( background, a3, 255 )

newwarp = cv2.warpPerspective(frame, M, (background.shape[1], background.shape[0])) 
# cv2.imshow('ds', dst)
result= cv2.addWeighted(background, 1, newwarp, 1, 0)
cv2.imshow('bg', result)


cv2.waitKey(0)
cv2.destroyAllWindows()
