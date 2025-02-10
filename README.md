### README

## Bulk Student Upload Script

This script reads student data from an Excel file and uploads it to a specified API endpoint. The script creates JSON data for each student and sends it as a PUT request to the API.

### Prerequisites

- Python 3.x
- Required Python libraries:
  - `requests`
  - `pandas`
  - `openpyxl`

Install the required libraries using pip:

```sh
pip install requests pandas openpyxl
```

### Excel File Structure

The Excel file should contain the following columns:

- `firstName`
- `lastName`
- `Bepress id`
- `organization`
- `email`


### Script Usage

1. **Update the script with your API endpoint and API key:**

```python
api_endpoint = "https://your-URL.elsevierpure.com/ws/api/persons/"  # Replace with the actual API endpoint
headers = {
    "api-key": "Your-API-key",  # Replace with your actual API key
    "Content-Type": "application/json"
}
```

2. **Ensure the Excel file is in the correct format and update the file path in the script:**

```python
excel_file_path = "students_data.xlsx"  # Replace with the path to your Excel file
```

3. **Run the script:**

```sh
python create_students.py
```

### Notes

- The script reads the student data from the Excel file specified by `excel_file_path`.
- The script creates JSON data for each student using the `create_student_json` function.
- The script sends the JSON data as a PUT request to the API endpoint specified by `api_endpoint`.
- The script includes a delay of 1 second between processing each student to avoid overwhelming the server.

Make sure to replace the placeholder values in the script with your actual API endpoint, API key, and file paths.
