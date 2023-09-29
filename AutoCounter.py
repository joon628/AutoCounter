import pyautogui 
from PIL import ImageGrab
import Detector as dt

def screenshot():
    img = ImageGrab.grab()
    img.save("./screenshot.png")

def autoclick_coordinates(coordinates):
    for coordinate in coordinates:
        pyautogui.click(coordinate[0], coordinate[1])

def get_coordinates():
    coordinates = dt.run_detection()
    return coordinates

def run():
    screenshot()
    coordinates = get_coordinates()
    autoclick_coordinates(coordinates)
    

