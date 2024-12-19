import os
import webview
#import engine.command as ec



#os.system('start msedge.exe --app="http://127.0.0.1:3000/charlie/web/index.html"')

def hello():
    print("Hello world!")

window = webview.create_window('Simple JS-Python Interaction', 'web/index.html',width=1560, height=900)

window.expose(hello)

webview.start()