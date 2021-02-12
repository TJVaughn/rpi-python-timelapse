from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
sleep(5)

for i in range(1, 2520):
	camera.capture(f'./captures/2-12-21/000{i}.jpg')
	print(f'photo {i} taken')
	sleep(10)

camera.stop_preview()
