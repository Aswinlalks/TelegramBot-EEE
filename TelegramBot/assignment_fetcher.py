import requests
from bs4 import BeautifulSoup

def fetch_assignments(username, password):
    # URL for login
    login_url = "https://mits.etlab.app/user/login"

    # Create a session
    session = requests.Session()

    # Login payload
    login_payload = {
        'LoginForm[username]': username,
        'LoginForm[password]': password,
    }

    # Send a POST request to login
    login_response = session.post(login_url, data=login_payload)

    # Check if login was successful
    if login_response.status_code == 200:
        # Now, you can access the assignments page
        assignments_url = "https://mits.etlab.app/student/assignments"
        assignments_response = session.get(assignments_url)

        # Parse the HTML content of the assignments page
        soup = BeautifulSoup(assignments_response.content, 'html.parser')
        assignment_details = []

        # Extract assignment details
        assignment_rows = soup.find_all('tr', class_=lambda x: x and ('odd' in x or 'even' in x))
        for row in assignment_rows:
            columns = row.find_all('td')
            subject = columns[0].text.strip()
            last_date = columns[4].text.strip()
            assignment_details.append({'subject': subject, 'last_date': last_date})

        return assignment_details

    else:
        print("Failed to login. Status code:", login_response.status_code)
        return None
