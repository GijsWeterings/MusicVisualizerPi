import os
import time

os.system("omxplayer -o local /home/pi/data/carnaval.mp3  &")
time.sleep(0.55)
os.system("aplaymidi --port 14 /home/pi/data/carnaval.mid")
