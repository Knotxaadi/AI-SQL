import webview

# Python function that will be called by JavaScript
def get_message():
    return "Hello from Python automatically!"

# Create the webview window and expose the Python function to JavaScript
window = webview.create_window("PyWebview Example", "index.html", 
                               js_api={"get_message": get_message})

# Start the webview application
webview.start()
