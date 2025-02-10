import requests
import json
import pandas as pd
import time

# Define the API endpoint and headers
api_endpoint = "https://your-URL.elsevierpure.com/ws/api/persons/"  # Replace with the actual API endpoint
headers = {
    "api-key": "Your-API-key",  # Replace with your actual API key
    "Content-Type": "application/json"
}

# Function to read student data from an Excel file
def read_student_data_from_excel(file_path):
    df = pd.read_excel(file_path)
    return df

# Function to create the JSON data for a student
def create_student_json(first_name, last_name, bepress_id, organization_uuid, email):
    student_json = {
        "name": {
            "firstName": first_name,
            "lastName": last_name
        },
        "studentOrganizationAssociations": [
            {
                "typeDiscriminator": "StudentOrganizationAssociation",
                "affiliationId": "",
                "organization": {
                    "systemName": "Organization",
                    "uuid": organization_uuid
                },
                "emails": [
                    {
                        "value": email,
                        "type": {
                            "uri": "/dk/atira/pure/person/personemailtype/email",
                            "term": {
                                "en_US": "Email"
                            }
                        }
                    }
                ],
                "period": {
                    "startDate": "2025-01-01"  # Example start date, replace if needed
                },
                "primaryAssociation": False,
                "awardGained": "",
                "programme": ""
            }
        ],
        "selectedForProfileRefinementService": False,
        "gender": {
            "uri": "/dk/atira/pure/person/gender/unknown",
            "term": {
                "en_US": "Unknown"
            }
        },
        "visibility": {
            "key": "FREE",
            "description": {
                "en_US": "Public - No restriction"
            }
        },
        "identifiers": [
            {
                "typeDiscriminator": "ClassifiedId",
                "id": bepress_id,
                "type": {
                    "uri": "/dk/atira/pure/person/personsources/bepressid",
                    "term": {
                        "en_US": "bepress ID"
                    }
                }
            }
        ],
        "customDefinedFields": {},
        "systemName": "Person"
    }
    return student_json

# Function to upload student data
def upload_student_data(student_json):
    response = requests.put(api_endpoint, headers=headers, json=student_json)
    if response.status_code == 201:
        return response.json()
    else:
        print(f"Failed to upload student data: {response.status_code}")
        print(response.text)
        return None

# Main function to process and upload students
def main():
    excel_file_path = "students_data.xlsx"  # Replace with the path to your Excel file
    student_data = read_student_data_from_excel(excel_file_path)

    for index, row in student_data.iterrows():
        first_name = row["firstName"]
        last_name = row["lastName"]
        bepress_id = row["Bepress id"]
        organization_uuid = row["organization"]
        email = row["email"]

        # Create the student JSON
        student_json = create_student_json(first_name, last_name, bepress_id, organization_uuid, email)

        # Print the JSON data for debugging
        print("JSON data to be sent:")
        print(json.dumps(student_json, indent=4))

        # Upload the student data
        uploaded_student = upload_student_data(student_json)

        # Print the response for verification
        if uploaded_student:
            print(f"Successfully uploaded student: {first_name} {last_name}")
            print(json.dumps(uploaded_student, indent=4))
        else:
            print(f"Failed to upload student: {first_name} {last_name}")

        # Introduce a delay of 1 second between processing each item
        time.sleep(1)

# Example usage
if __name__ == "__main__":
    main()