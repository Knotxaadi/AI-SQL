import os
import eel
from engine.features import *

eel.init('web')

playassistantsound()

#os.system('start msedge.exe --app="http://127.0.0.1:3000/charlie/web/index.html"')

eel.start('charlie\web\index.html', mode='chrome')