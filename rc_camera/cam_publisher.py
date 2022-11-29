import rclpy
from myinterface.msg import MyMsg
from rclpy.node import Node
import cv2
from multiprocessing import Process
import numpy as np
class CameraPublisher(Node) :
    
    def __init__(self) :
        super().__init__('camera_publisher_node')
        self.camera_publisher = self.create_publisher(MyMsg,'camera_topic',0)
        self.timer = self.create_timer (1,self.publish_camera_msg)
        
    def publish_camera_msg(self) :
        self.msg=MyMsg()
        self.msg.a = 0
        self.msg.b = 1
        self.camera_publisher.publish(self.msg)
        
    def CV_imput_camera(self) :
        capture = cv2.VideoCapture(0)
        while True :
            ref,frame = capture.read()
            mask= np.zeros_like(frame)
            
            gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            gray_frame_Canny = cv2.Canny(gray_frame,150,300)
            h,w=frame.shape[:2]
            lines = cv2.HoughLinesP(gray_frame_Canny,1,np.pi/180,140,200,0)
            for i in range(len(lines)) :
                for x1,y1,x2,y2 in lines[i] :
                    cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),3)
                
    
            cv2.imshow('3',frame)
            cv2.imshow('2',mask)
            cv2.imshow('1',gray_frame_Canny)
            print(mask.shape)
            key=cv2.waitKey(32)
            if key>0 :
                break
        

        
        
def main(args=None) :
    rclpy.init(args=args)
    node = CameraPublisher()
    p1=Process(target=node.CV_imput_camera)
    p1.start()
       
    rclpy.spin(node)
    
        
if __name__=='__main__' :
    main()
    