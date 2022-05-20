import rclpy
from rclpy.node import Node
from rclpy import logging

import socket
import json
from time import sleep
from datetime import datetime

from std_msgs.msg import String

from dvl_interface.msg import DVL as DVL
from dvl_interface.msg import DVLBeam as DVLBeam
import select


oldJson = ""
theDVL = DVL()
beam0 = DVLBeam()
beam1 = DVLBeam()
beam2 = DVLBeam()
beam3 = DVLBeam()

class dvl_a50_py(Node):
	def __init__(self):
		global s, TCP_IP, TCP_PORT, do_log_raw_data
		super().__init__('dvl_a50_py')
		#IP ADDRESS
		TCP_IP = "192.168.194.95" #rclpy.get_param("~ip", "10.42.0.186")
		TCP_PORT = 16171 #rclpy.get_param("~port", 16171)
		#do_log_raw_data = rclpy.get_param("~do_log_raw_data", False)
	 
		self.connect()
		self.publisher_ = self.publisher()
		self.getData()
		self.i = 0

	def connect(self):
		global s, TCP_IP, TCP_PORT
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((TCP_IP, TCP_PORT))
			s.settimeout(1)
		except socket.error as err:
			print("socket error")
			sleep(1)
			self.connect()

	def getData(self):
		global oldJson, s
		raw_data = ""
		while not '\n' in raw_data:
			try:
				rec = s.recv(1) # Add timeout for that
				if len(rec) == 0:
					#rclpy.logerr("Socket closed by the DVL, reopening")
					print("socket closed")
					self.connect()
					continue
			except socket.timeout as err:
				#rclpy.logerr("Lost connection with the DVL, reinitiating the connection: {}".format(err))
				print("connection lost")
				self.connect()
				continue
			raw_data = raw_data + rec.decode('utf-8')
		raw_data = oldJson + raw_data
		oldJson = ""
		raw_data = raw_data.split('\n')
		oldJson = raw_data[1]
		raw_data = raw_data[0]
		return raw_data
	

	def publisher(self):
		#pub_raw = rclpy.Publisher('dvl/json_data', String, queue_size=10)
		#pub = rclpy.Publisher('dvl/data', DVL, queue_size=10)
		#pub_raw = self.create_publisher(String, 'dvl/json_data', 10)
		pub = self.create_publisher(DVL, 'dvl/data', 10)
		
		#while not rclpy.is_shutdown():
		while True:
			raw_data = self.getData()
			#if do_log_raw_data:
				#rclpy.loginfo(raw_data)
			#	print(raw_data)
			data = {}
			data = json.loads(raw_data)
			#pub_raw.publish(raw_data)
		
			#theDVL.header.stamp = rclpy.Time.now()
			#theDVL.header.frame_id = "dvl_link"
		
			if data.get('time'):
				print("time -->")
				print(data)
				try:
					theDVL.time_stamp = datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")
					theDVL.frame_id = "dvl_link"
			
					theDVL.time = data["time"]
					theDVL.velocity.x = float(data["vx"])
					theDVL.velocity.y = float(data["vy"])
					theDVL.velocity.z = float(data["vz"])
					theDVL.fom = data["fom"]
					theDVL.altitude = float(data["altitude"])
					theDVL.velocity_valid = data["velocity_valid"]
					theDVL.status = data["status"]
					theDVL.form = data["format"]

					beam0.id = data["transducers"][0]["id"]
					beam0.velocity = data["transducers"][0]["velocity"]
					beam0.distance = data["transducers"][0]["distance"]
					beam0.rssi = data["transducers"][0]["rssi"]
					beam0.nsd = data["transducers"][0]["nsd"]
					beam0.valid = data["transducers"][0]["beam_valid"]

					beam1.id = data["transducers"][1]["id"]
					beam1.velocity = data["transducers"][1]["velocity"]
					beam1.distance = data["transducers"][1]["distance"]
					beam1.rssi = data["transducers"][1]["rssi"]
					beam1.nsd = data["transducers"][1]["nsd"]
					beam1.valid = data["transducers"][1]["beam_valid"]

					beam2.id = data["transducers"][2]["id"]
					beam2.velocity = data["transducers"][2]["velocity"]
					beam2.distance = data["transducers"][2]["distance"]
					beam2.rssi = data["transducers"][2]["rssi"]
					beam2.nsd = data["transducers"][2]["nsd"]
					beam2.valid = data["transducers"][2]["beam_valid"]

					beam3.id = data["transducers"][3]["id"]
					beam3.velocity = data["transducers"][3]["velocity"]
					beam3.distance = data["transducers"][3]["distance"]
					beam3.rssi = data["transducers"][3]["rssi"]
					beam3.nsd = data["transducers"][3]["nsd"]
					beam3.valid = data["transducers"][3]["beam_valid"]

					theDVL.beams = [beam0, beam1, beam2, beam3]
					pub.publish(theDVL)
				except:
					print("failure in the DVL message")

			elif data.get('ts'):
				print("ts --> ")
				print(data)

				sleep(0.1)
			else:
				print("unknown message -->")
				print(data)
				sleep(0.1)

def main(args=None):
	
	rclpy.init(args=args)

	dvl_publisher = dvl_a50_py() 

	rclpy.spin(dvl_publisher)

	dvl_publisher.destroy_node()
	rclpy.shutdown()
	 

if __name__ == '__main__':
	main()