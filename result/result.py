import requests
from bs4 import BeautifulSoup

# Define the URL for the result page
url = "https://web.bisemultan.edu.pk/ajax/res2.php"

# Create or open a CSV file to store the results
with open("result.csv", 'a') as f:
    # Write the header row with column names
    f.write("Roll_no,Name,Urdu,English,Islamic_Education,Pakistan_Studies,Physics,Chemistry,Biology\n")

# Ask the user for the starting roll number
roll = input("Enter your starting roll number: ")

# Wait for user confirmation before proceeding
input("Press enter to continue...")

# Convert the starting roll number to an integer
roll = int(roll)

# Infinite loop to fetch results
while True:
    # Define the payload for the POST request
    payload = {
        "rno": str(roll),
        "session": "cyNmMzI4dzRzZ2kxMjAyM3Ay",
        "appear_level": "cyNmMzI4dzRzZ3BhcnQy"
    }

    # Send a POST request to the URL
    response = requests.post(url, data=payload)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(f"Roll No.: {roll} ✅")
    else:
        print(f"Request failed with status code: {response.status_code}")

    # Close the response object
    response.close()

    # Get the HTML response content
    html_response = response.text

    # Check if the "Record Not Found" message is present in the response
    if "Record Not Found For Given Roll No" in html_response:
        print(f"Result not found for Roll No.: {roll}")
        break

    # Parse the HTML response with BeautifulSoup
    soup = BeautifulSoup(html_response, 'html.parser')

    # Find div elements containing Roll No. and Name
    div_elements = soup.find_all('div')
    roll_no = None
    name = None
    for div in div_elements:
        text = div.text.strip()
        if text == "Roll No.":
            roll_no = div.find_next('strong').text.strip()
        elif text == "Name":
            name = div.find_next('strong').text.strip()

    # Find all rows with subject information
    rows = soup.find_all('tr', {'style': 'text-align: center;'})
    subject_names = []
    percentiles = []
    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 9:
            subject_name = columns[0].strong.text.strip()
            percentile = columns[7].strong.text.strip()
            subject_names.append(subject_name)
            percentiles.append(percentile)

    # Combine percentiles into a comma-separated string
    percentiles_str = ",".join(percentiles)

    # Create a string with the information for the CSV file
    information = [roll_no, ",", name, ",", percentiles_str, "\n"]

    # Append the information to the CSV file
    with open("result.csv", 'a') as f:
        f.writelines(information)

    # Increment the roll number for the next iteration
    roll += 1
