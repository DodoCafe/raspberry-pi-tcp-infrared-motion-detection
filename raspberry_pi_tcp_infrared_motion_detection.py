import RPi.GPIO as gpio
import socket

INFRARED_MOTION_SENSOR_GPIO_PIN = 23
SERVER_APPLICATION_IPV4 = '192.168.31.222'
SERVER_APPLICATION_PORT_NUMBER = 5005
BACKLOG = 1
MESSAGE = 'Motion detected'

def initialize_infrared_motion_sensor():
	gpio.setmode(gpio.BCM)
	gpio.setwarnings(False)
	gpio.setup(INFRARED_MOTION_SENSOR_GPIO_PIN, gpio.IN)

def establish_tcp_connection_and_send_message_on_motion_detected():
	listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket of address (and protocol) family IPv4.
	listen_socket.bind((SERVER_APPLICATION_IPV4, SERVER_APPLICATION_PORT_NUMBER))
	listen_socket.listen(BACKLOG)
	connection_socket, client_application_id = listen_socket.accept()
	print('Client application ID: ', client_application_id)
	while True:
		if (gpio.input(INFRARED_MOTION_SENSOR_GPIO_PIN)):
			print(MESSAGE)
			connection_socket.send(bytes(MESSAGE, 'ascii'))
			break
	connection_socket.close()
	listen_socket.close()

initialize_infrared_motion_sensor()
establish_tcp_connection_and_send_message_on_motion_detected()
