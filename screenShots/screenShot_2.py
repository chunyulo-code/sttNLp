import pyautogui
from datetime import datetime

myScreenshot = pyautogui.screenshot()
now = datetime.now()
current_time = now.strftime("%H-%M-%S")
myScreenshot.save(r'D:\sttNlp\screenShots' + "/" + current_time + '.png')