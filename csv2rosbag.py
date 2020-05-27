import pandas as pd
df = pd.read_csv('my_csv_file.csv')
# for row in range(df.shape[0]):
#     print(df['timestamp][row])
import rospy
import rosbag
from sensor_msgs.msg import Imu, NavSatFix

with rosbag.Bag('output.bag', 'a') as bag:
    for row in range(df.shape[0]):
        # print(df['timestamp'][row])
        timestamp = rospy.Time.from_sec(df['timestamp'][row])
        imu_msg = Imu()
        imu_msg.header.stamp = timestamp
        imu_msg.angular_velocity.x = df['a_v_x'][row]
        print(df['a_v_x'][row])

        # Populate the data elements for IMU
        # e.g. imu_msg.angular_velocity.x = df['a_v_x'][row]

        bag.write("/imu", imu_msg, timestamp)

        gps_msg = NavSatFix()
        gps_msg.header.stamp = timestamp

        # Populate the data elements for GPS

        # bag.write("/gps", gpu_msg, timestamp)
