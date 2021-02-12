import moviepy.video.io.ImageSequenceClip
import os

folder_to_read = 'YOUR_PHOTOS_FILE'
fps = 24
folder = os.listdir(f"../inputs/{folder_to_read}")

def get_num_vals(array, split):
	for i in range(0, len(array)):
		array[i] = array[i].split(split)
		array[i] = int(array[i][0])
	return array

def selection_sort_nums(arr):
	min_index = None
	temporary = None
	for curr in range(0, len(arr) -1):
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


selection_sort_nums(get_num_vals(folder, '.jpg'))
sorted_num_vals_to_filenames(folder)

image_files = ['../inputs/' + folder_to_read+'/'+img for img in folder if img.endswith(".jpg")]
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile(f'../movies/timelapse_{folder_to_read}_{fps}fps.mp4')
