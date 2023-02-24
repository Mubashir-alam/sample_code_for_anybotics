import os
from std_msgs.msg import String
from datetime import datetime
import shutil 
from threading import Thread
import time as Timee
import rospy
from datetime import datetime
import datetime as dt

pub = rospy.Publisher('datetime_now', String, queue_size=10)
rospy.init_node('talker', anonymous=True)
copying_variable=0


def fun():
    while True:
        global x
        for x in range(12):
            cmd=f'rosbag record -O /home/mubashir/catkin_ws/src/germany1_trush/rosbag/{x}.bag /web_cam --duration 5 '
            os.system(cmd)
    
def callback(data):
    print(data.data)
    if data.data == "True":
        pub.publish(f"{datetime.now()}")
        print("Callback function ")
        copying()

def copying():
        values=x
        current_time = datetime.now()
        previous_time = datetime.now() - dt.timedelta(seconds=5)
        future_time =datetime.now() + dt.timedelta(seconds=10)

#uncomment this section if you want different formate 
        # current_time =current_time.strftime('%I:%M:%S %p')
        # previous_time=previous_time.strftime('%I:%M:%S %p')
        # future_time=future_time.strftime('%I:%M:%S %p')

        print(previous_time)
        print(current_time)
        print(future_time)
        
        pre_file=os.path.exists(f'/home/mubashir/catkin_ws/src/germany1_trush/rosbag/{x-1}.bag')
        if pre_file == True:
            origin_past=f'/home/mubashir/catkin_ws/src/germany1_trush/rosbag/{values-1}.bag'
            target_past=f'/home/mubashir/catkin_ws/src/germany1_trush/ros_bag_saved/{previous_time}.bag'
            shutil.copy(origin_past,target_past)
            print("previous file copied ")
            print(previous_time)

            #present file 
            Timee.sleep(5)
            origin_presnt=f'/home/mubashir/catkin_ws/src/germany1_trush/rosbag/{values}.bag'
            target_present=f'/home/mubashir/catkin_ws/src/germany1_trush/ros_bag_saved/{current_time}.bag'
            shutil.copy(origin_presnt,target_present)
            print("5 sec pass")
            print("current file copied")
            print(current_time)

            #future file
            Timee.sleep(10)
            origin_future=f'/home/mubashir/catkin_ws/src/germany1_trush/rosbag/{values+1}.bag'
            target_futuret=f'/home/mubashir/catkin_ws/src/germany1_trush/ros_bag_saved/{future_time}.bag'
            shutil.copy(origin_future,target_futuret)
            print("10 sec pass ")
            print("future file copied ")
            print(future_time)
        else:
            print("Wait for a while")

            
def listener():
     rospy.Subscriber("button_press", String, callback)
     rospy.spin()

if __name__ == '__main__':

    a = Thread(target = fun)
    b = Thread(target = listener)
    a.start()
    b.start()