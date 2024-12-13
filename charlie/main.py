import os
import eel

eel.init('www')

os.system('start msedge.exe --app="http://127.0.0.1:3000/charlie/www/index.html"')

eel.start('index.html',mode=None,host='localhost',block=True)