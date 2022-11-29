import rclpy
from rclpy.node import Node
from myinterface.msg import MyMsg

class CameraSubscriber(Node) :
    def __init__ (self) :
        super().__init__('camera_subscriber_node')
        self.camera_subscriber = self.create_subscription(
            MyMsg , 'camera_topic' , self.subscribe_msg,0
        )
        
    def subscribe_msg(self,msg) :
        self.get_logger().info('msg : {0}'.format(msg.a))
        

def main (args=None) :
    rclpy.init(args=args)
    node = CameraSubscriber()
    rclpy.spin(node)
    
if __name__=='__main__' :
    main()