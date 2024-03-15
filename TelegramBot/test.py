import requests
from bs4 import BeautifulSoup

# Login credentials
username = 'MUT22EE523'
password = 'Passd@123'

# Login URL
login_url = 'https://mits.etlab.app/student/assignments'

# Login data
login_data = {
    'username': username,
    'password': password
}

# Send login request
session = requests.Session()
login_response = session.post(login_url, data=login_data)

# Check if login was successful
if login_response.status_code == 200:
    # Scrape assignments
    assignments_page = session.get(login_url)
    soup = BeautifulSoup(assignments_page.content, 'html.parser')

    # Extract assignment information
    assignments = soup.find_all('tr')

    for assignment in assignments:
        columns = assignment.find_all('td')
        subject = columns[0].text.strip()
        semester = columns[1].text.strip()
        title = columns[2].text.strip()
        issued_on = columns[3].text.strip()
        last_date = columns[4].text.strip()
        status = columns[5].text.strip()

        print(f'Subject: {subject}')
        print(f'Semester: {semester}')
        print(f'Title: {title}')
        print(f'Issued On: {issued_on}')
        print(f'Last Date: {last_date}')
        print(f'Status: {status}')
        print('------------------------')

else:
    print('Login failed.')
