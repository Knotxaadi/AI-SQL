import csv
import openpyxl
import webview

def process_csv(file_path):
    """
    Processes a CSV file and returns its content as a nested list.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)
            return rows  # Return rows as a nested list
    except Exception as e:
        return [[f"Error reading CSV file: {e}"]]

def process_excel(file_path):
    """
    Processes an Excel file and returns its content as a nested list.
    """
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        rows = [[cell.value for cell in row] for row in sheet.iter_rows()]
        return rows  # Return rows as a nested list
    except Exception as e:
        return [[f"Error reading Excel file: {e}"]]

def process_file(file_path):
    """
    Determines the file type and processes it accordingly.
    """
    if file_path.endswith('.csv'):
        return process_csv(file_path)
    elif file_path.endswith(('.xls', '.xlsx')):
        return process_excel(file_path)
    else:
        return [["Unsupported file type! Please upload a CSV or Excel file."]]

class API:
    def open_file(self):
        """
        Opens a file dialog for the user to select a file.
        """
        from tkinter import Tk, filedialog

        # Open file dialog
        root = Tk()
        root.withdraw()  # Hide the main window
        file_path = filedialog.askopenfilename(
            filetypes=[("Supported Files", "*.csv *.xls *.xlsx"),
                       ("CSV files", "*.csv"),
                       ("Excel files", "*.xls *.xlsx")]
        )
        if not file_path:
            return [["No file selected!"]]

        # Process the file and return the result as a nested list
        result = process_file(file_path)
        return result

# HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Uploader</title>
</head>
<body>
    <h1>Upload CSV or Excel File</h1>
    <button onclick="selectFile()">Select File</button>
    <div id="output" style="margin-top: 20px; white-space: pre-wrap;"></div>
    <script>
        async function selectFile() {
            // Call the Python function to open the file dialog and get the file content
            const result = await pywebview.api.open_file();
            document.getElementById('output').innerHTML = JSON.stringify(result, null, 2); // Display as JSON
        }
    </script>
</body>
</html>
"""

if __name__ == "__main__":
    # Create an API instance
    api = API()

    # Create a pywebview window
    webview.create_window("File Uploader", html=html_content, js_api=api)

    # Start the pywebview application
    webview.start()
