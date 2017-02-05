import os
import time
import sys
os.system("mpg123 -q %s.mp3 &" % sys.argv[1])
time.sleep(0.55)
os.system("aplaymidi --port 14 %s.mid" % sys.argv[1])