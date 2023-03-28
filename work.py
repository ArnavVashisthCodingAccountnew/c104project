import cv2
import numpy


imago = cv2.imread('solar-system.jpg')
cv2.putText(imago,'Sun',(20,300), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255))
cv2.putText(imago,'Mercury',(115,180), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255))
cv2.putText(imago,'Venus',(190,260), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255))
cv2.putText(imago,'Earth',(266,160), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255))
cv2.putText(imago,'Mars',(362,260), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255))
cv2.putText(imago,'Jupiter',(520,260), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,0))
cv2.putText(imago,'Saturn',(766,140), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255))
cv2.putText(imago,'Uranus',(966,140), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255))
cv2.putText(imago,'Neptune',(1086,140), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(255,255,255))

cv2.imshow('Solar System', imago)
cv2.imwrite('solar-system-new-named.jpg', imago)
cv2.waitKey(0)
