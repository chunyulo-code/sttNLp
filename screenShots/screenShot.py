import pyscreenshot as ImageGrab
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H-%M-%S")

# 擷取全螢幕畫面
img = ImageGrab.grab()
imgName = current_time + ".png"
# 儲存檔案
img.save("./screenShots/"+imgName)