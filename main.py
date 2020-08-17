import numpy as np
import cv2
import pyautogui



def a(ex,ey,x,y):
    ex=int(ex)
    ey=int(ey)
    x=int(x)
    y=int(y)

    if ex<x:
        l=abs(ex-x)*5
        #print('右移',l)
        pyautogui.moveRel(l,0,duration=0.25)
    
    if ex>x:
        l=abs(ex-x)*5
        #print('左移',l)
        pyautogui.moveRel(-l,0,duration=0.25)
    if ey>y:
        l=abs(ey-y)*5
        #print('上移',l)
        pyautogui.moveRel(0,-l,duration=0.25)
    if ey<y:

        l=abs(ey-y)*5
        pyautogui.moveRel(0,l,duration=0.25)

size=pyautogui.size()
pyautogui.moveTo(size[0]/2,size[1]/2)

detector_face = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
detector_face.load('haarcascades/haarcascade_frontalface_default.xml')

detector_eye = cv2.CascadeClassifier('haarcascades/haarcascade_eye_tree_eyeglasses.xml')
detector_eye.load('haarcascades/haarcascade_eye_tree_eyeglasses.xml')
#创建一个VideoCapture项目，0代表选择第一个设备
cap = cv2.VideoCapture(0)

#设定文字
org = (100, 200)
fontFace = cv2.FONT_HERSHEY_COMPLEX
fontScale = 1
fontcolor = (0, 255, 0) # BGR
thickness = 1 
lineType = 4
bottomLeftOrigin = 1
xxr=630
yyr=350

  
while(True):
    # 捕捉每一帧图像，返回两个参数ret为是否返回图片（True or False），frame为返回的图片
    ret, frame = cap.read()
    frame_turn=cv2.flip(frame,1)
     # 通过cv2.cvtColor转换颜色格式为灰度模式
    gray = cv2.cvtColor(frame_turn, cv2.COLOR_BGR2GRAY)

    #放入选择器
    faces = detector_face.detectMultiScale(gray, 1.3, 5)

    #框选人脸
    for (x, y, w, h) in faces:
        #将宽变为一半，只进行半边脸的计算
        woo=int(w)/2
        w=np.int32(woo)
        #print(w)
        #框脸
        cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face_re=frame_turn[y:y+h, x:x+w]
        face_re_g=gray[y:y+h, x:x+w]
        #print(face_re)
        #print(x,type(y))
        
        #找眼睛
        
        eyes = detector_eye.detectMultiScale(face_re)
        for(ex,ey,ew,eh) in eyes:
            '''
                if cv2.waitKey(1) & 0xFF == ord('a'):
                    print('左上角',eyes_re_g.shape,xr,yr)
                    print(len(eyes))
                    print(eyes[0])
                    print(eyes[1])
            '''

            eyes_re_g=face_re_g[ey:ey+eh, ex:ex+ew]
            #框眼睛
            cv2.rectangle(face_re_g,(ex,ey),(ex+ew,ey+eh),(0,255,0),1)

            circles= cv2.HoughCircles(eyes_re_g,cv2.HOUGH_GRADIENT,1,50,param1=150,param2=10,minRadius=5,maxRadius=16)

            if str(circles) != 'None':
                for circle in circles[0]:
                    xr=int(circle[0])
                    yr=int(circle[1])
                    rr=int(circle[2])
                    #print(xr,yr,rr)
                    eyes_re_g=cv2.circle(eyes_re_g,(xr,yr),2,(255,255,255),2,8,0)

                    xr=int(x)+int(ex)+int(xr)
                    yr=int(y)+int(ey)+int(yr)

                    # a(xxr,yyr,xr,yr)
                    #print(xxr,yyr,xr,yr)
                    xxr=xr
                    yyr=yr

                    #print(xr,yr)
                    #获取瞳孔坐标
                    #T_L_X=
                    #T_L_Y=
                    #T_R_X=
                    #T_R_Y=
                        
     # 播放每一帧图像

    cv2.putText(gray, 'abc', org, fontFace, fontScale, fontcolor, thickness, lineType)
    cv2.imshow('frame',gray)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
# 最后要记得释放capture
cap.release()
cv2.destroyAllWindows()