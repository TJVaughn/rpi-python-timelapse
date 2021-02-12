# Raspberry Pi, Python Timelapse

### Dependencies:
- PiCamera
- Moviepy

## How to get Started

1. Download this repo
2. Send the timelapse.py to your RasPi (I use VNC Viewer)
3. cd into the project folder in the terminal on your Pi
    - Create a captures directory
    - Create another directory inside of your choosing (current-date)
- projects
    - camera
        - timelapse.py
        - captures
            - date-of-timelapse
                - 0001.jpg
                - 0002.jpg
                - ...
                - 0002520.jpg
4. On your pi, run: python3 timelapse.py
    - The script is currently designed to take a photo once every 10 seconds, and the loop is set to go for 5 hours
5. Once the quantity of your choosing of photos have been taken, transfer them to your regular computer. You could choose to run the other script from the pi, but that will take a while.
6. Create a project folder for your timelapses (timelapse)
7. make src, inputs and movies directories in timelapse directory

- timelapse
    - inputs
        - date-of-timelapse
            - 0001.jpg
            - 0002.jpg
            - ...
            - 0002520.jpg
    - movies
        - timelapse_date-of-timelapse_24fps.mp4
    - src
        - make-vid-from-imgs.py
8. Place the make-vid-from-imgs.py file in the src folder
9. Change the variables to your folder and desired frames per second(fps)
10. In your terminal, in the src directory, run: python3 make-vid-from-imgs.py
11. Assuming everything went correctly, you should have a nice timelapse from your images taken on the raspi. 

This project assumes you have a RasPi, RaspberryPi OS and know how to connect the camera module. It also assumes you have the the knowledge to use the terminal to run basic commands. 

If you actually ran this program I would love to know how it went. You can give feedback on here or @TrevorHauck on twitter. I don't check my twitter too often so pardon me if it takes a while for me to get back to you. 

Have a great day!
