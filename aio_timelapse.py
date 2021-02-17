import os
import moviepy.video.io.ImageSequenceClip
from picamera import PiCamera
from time import sleep
from datetime import date

#Helper functions ***************************************************************************************************************************
def get_num_vals(array, split):
	for i in range(0, len(array)):
		array[i] = array[i].split(split)
		array[i] = int(array[i][0])
	return array


def selection_sort_nums(arr):
	min_index = None
	temporary = None
	for curr in range(0, len(arr) - 1):
		min_index = curr
		for i in range(curr + 1, len(arr)):
			if arr[i] < arr[min_index]:
				min_index = i
		temporary = arr[curr]
		arr[curr] = arr[min_index]
		arr[min_index] = temporary


def sorted_num_vals_to_filenames(arr):
    for i in range(0, len(arr)):
        arr[i] = f"000{str(arr[i])}.jpg"
#Helper functions ***************************************************************************************************************************

today = str(date.today())

#Make new directory with todays date
os.system(f"cd ./captures && mkdir {today}")

#set length of timelapse
hours_of_time_lapse = 7.25
#set output fps
fps = 24


folder_to_read = today
folder = os.listdir(f"./captures/{folder_to_read}")

selection_sort_nums(get_num_vals(folder, '.jpg'))
sorted_num_vals_to_filenames(folder)

camera = PiCamera()
camera.start_preview()
sleep(5)

image_files = ['./captures/' + folder_to_read +'/'+img for img in folder if img.endswith(".jpg")]

photos_to_take = int(round(6 * 60 * hours_of_time_lapse))
print(photos_to_take)
for i in range(1, photos_to_take):
    camera.capture(f'./captures/{today}/000{i}.jpg')
    print(f'photo {i} taken')
    if(i > 1):
        clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
    sleep(10)

camera.stop_preview()


clip.write_videofile(f'./movies/timelapse_{folder_to_read}_{fps}fps.mp4')