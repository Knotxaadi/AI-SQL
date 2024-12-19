import webview

# Function to change background color
def change_background_color():
    return "background-color: blue;"

# Create a simple webview window
window = webview.create_window('Simple JS-Python Interaction', 'index.html')

# Expose the Python function to JavaScript
window.expose(change_background_color)

# Start the webview
webview.start()
