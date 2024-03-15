import json

def get_drive_link(document_name, file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            documents = data.get('notes', {})
            return documents.get(document_name, "Document not found.")
    except Exception as e:
        print("Error fetching document link:", e)
        return "An error occurred while fetching the document link."

# Example usage
if __name__ == "__main__":
    # Replace 'links.json' with the path to your JSON file
    file_path = 'links.json'
    document_name = input("Enter the document name: ")
    drive_link = get_drive_link(document_name, file_path)
    print("Drive link:", drive_link)
