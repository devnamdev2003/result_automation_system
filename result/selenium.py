from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
import time
from bs4 import BeautifulSoup
initial_roll_number = int(input("Enter the initial roll number: "))
input("press enter to continue...")
edge_driver_path = os.path.abspath("msedgedriver.exe")
driver = webdriver.Edge(executable_path=edge_driver_path)
driver.implicitly_wait(0.5)
driver.get('https://web.bisemultan.edu.pk/results-12/')
session_dropdown = Select(driver.find_element_by_id('session'))
session_dropdown.select_by_value('cyNmMzMwdzRzZ2kxMjAyM3Ay')
submit_button = driver.find_element_by_id('submitresult')
increment = 1
while True:
    roll_number_input = driver.find_element_by_id('rno')
    roll_number_input.clear()
    roll_number_input.send_keys(str(initial_roll_number))
    submit_button.click()
    time.sleep(2)
    initial_roll_number += increment
    s = driver.page_source
    soup = BeautifulSoup(s, 'html.parser')
    div_elements = soup.find_all('div')
    roll_no = None
    name = None
    for div in div_elements:
        text = div.text.strip()
        if text == "Roll No.":
            roll_no = div.find_next('strong').text.strip()
        elif text == "Name":
            name = div.find_next('strong').text.strip()
    if name is not None:
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
        percentiles_str = ",".join(percentiles)
        information = [roll_no, ",", name, ",", percentiles_str, "\n"]
        with open("result2.csv", 'a') as f:
            f.writelines(information)
    information = [roll_no, ",", name, ",", percentiles_str, "\n"]
    with open("result.csv", 'a') as f:
        f.writelines(information)
