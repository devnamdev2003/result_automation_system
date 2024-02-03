import os
import sys
import time
import shutil
import requests
from PIL import Image
from bs4 import BeautifulSoup
from selenium import webdriver
from pytesseract import pytesseract
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoAlertPresentException, InvalidSessionIdException

# find the link of capcha from source code


def find_src(source_code):
    HtmlCodeInListForm = source_code.split(" ")
    captcha_img_link = []
    for i in HtmlCodeInListForm:
        if 'src="CaptchaImage.axd?guid=' in i:
            captcha_img_link.append(i[5:-1])
    return captcha_img_link[0]

#  after getting link of captcha image this function download the captcha image


def download_image(url, image_name):
    file_name = image_name
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(res.raw, f)
        return True
    else:
        pass

# read text from image


def read_text(captcha_image):
    # path of tesseract.exe
    path_to_tesseract = r"E://Program Files//Tesseract-OCR//tesseract.exe"
    # image_path = r"./{captcha_image}"
    image_path = captcha_image
    img = Image.open(image_path)
    pytesseract.tesseract_cmd = path_to_tesseract

    # fetch text from image
    text = pytesseract.image_to_string(img)

    # covert text into upper format
    captcha = text.upper()

    # remove spaces
    captcha = captcha.replace(" ", "")

    # delete image
    os.remove(captcha_image)
    return captcha


def main():

    i = 1001  # starting rollnumber
    k = 0  # To close the program when all results are found
    print("1. Computer Science")
    print("2. Mechnical Engineering")
    print("3. Civil Engineering")
    print("4. Electrical Engineering")
    branch = input("Enter Branch Number: ")

    # sem = input("Enter semester: ")
    sem = "7"
    print("Semester is:7")

    # When user enter a wrong branch number
    try:
        j = int(branch)
    except ValueError:
        # when branch is wrong
        sys.exit("Values don't match")
    j = int(branch)

    # set roll number
    # Check user's input and set roll number accordingly
    if j == 1:
        en_num = "0967CS20"
        print("Your Starting Roll Number: ", en_num+str(i))
        input("Press Enter")
        filename = f'CS_{sem}thsem_result.csv'
    elif j == 2:
        en_num = "0967ME20"
        print("Your Starting Roll Number: ", en_num+str(i))
        input("Press Enter")
        filename = f'ME_{sem}thsem_result.csv'
    elif j == 3:
        en_num = "0967CE20"
        print("Your Starting Roll Number: ", en_num+str(i))
        input("Press Enter")
        filename = f'CE_{sem}thsem_result.csv'
    elif j == 4:
        en_num = "0967EX20"
        print("Your Starting Roll Number: ", en_num+str(i))
        input("Press Enter")
        filename = f'EX_{sem}thsem_result.csv'
    else:
        # when branch is wrong
        sys.exit("branch do not match")

    # open drive
    # path of chromedriver.exe
    # edge_driver_path = "msedgedriver.exe"
    edge_driver_path = os.path.abspath("msedgedriver.exe")

# Create a Microsoft Edge WebDriver instance
    driver = webdriver.Edge(executable_path=edge_driver_path)

# Set an implicit wait time (in seconds) for element locating
    driver.implicitly_wait(0.5)
    # driver = webdriver.Chrome("chromedriver.exe")
    # driver.implicitly_wait(0.5)
    # link of collage page
    driver.get("http://result.rgpv.ac.in/Result/ProgramSelect.aspx")
    radio = driver.find_element_by_id("radlstProgram_1")
    radio.click()
    while True:
        # set rollnumber

        en_num_format = en_num+str(i)
        # when roll number limit is reached
        if k > 4:
            break
        print(en_num+str(i))

        # file name of captcha image
        image = en_num_format+'.jpg'

        # get page source
        s = driver.page_source

        # functions
        link = find_src(s)
        url = f'http://result.rgpv.ac.in/result/{link}'
        download_image(url, image)
        captcha = read_text(image)

        # fill data like enrollment number, semester, captcha.
        Select(driver.find_element_by_xpath(
            '//*[@id="ctl00_ContentPlaceHolder1_drpSemester"]')).select_by_value(sem)  # select 4th sem
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="ctl00_ContentPlaceHolder1_TextBox1"]').send_keys(captcha)  # type captcha
        time.sleep(1)
        driver.find_element_by_xpath(
            '//*[@id="ctl00_ContentPlaceHolder1_txtrollno"]').send_keys(en_num_format)  # type roll number
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="ctl00_ContentPlaceHolder1_btnviewresult"]').send_keys(Keys.ENTER)  # press enter

        # handel alert, when captcha is wrong and enrollment number is not found
        time.sleep(2)
        alert = Alert(driver)
        try:
            alerttext = alert.text
            alert.accept()
        except NoAlertPresentException:
            pass
        except InvalidSessionIdException:
            pass
        s = driver.page_source

        # when captcha is correct featch from result page
        if "Total Credit" in s:
            soup = BeautifulSoup(s, 'html.parser')
            roll_nu = soup.find(
                'span', id='ctl00_ContentPlaceHolder1_lblRollNoGrading').get_text()
            name = soup.find(
                'span', id='ctl00_ContentPlaceHolder1_lblNameGrading').get_text()
            sgpa = soup.find(
                'span', id='ctl00_ContentPlaceHolder1_lblSGPA').get_text()
            cgpa = soup.find(
                'span', id='ctl00_ContentPlaceHolder1_lblcgpa').get_text()
            result = soup.find(
                'span', id='ctl00_ContentPlaceHolder1_lblResultNewGrading').get_text()
            name = name.replace(" ", "")
            name = name.replace("\n", " ")
            information = [roll_nu, ",", name,
                           ",", sgpa, ",", cgpa, ",", result, "\n"]

            # write result in CSV file
            with open(filename, 'a') as f:
                f.writelines(information)
            f.close()
            print("succesful")
            # Press reset information button
            driver.find_element_by_xpath(
                '//*[@id="ctl00_ContentPlaceHolder1_btnReset"]').send_keys(Keys.ENTER)
            i = i+1  # increment in enrollment number
            k = 0
        # when captcha is wrong and enrollment number is not found
        else:
            if "Result" in alerttext:  # enrollment number is not found
                driver.find_element_by_xpath(
                    '//*[@id="ctl00_ContentPlaceHolder1_btnReset"]').send_keys(Keys.ENTER)  # press reset button
                i = i+1  # increment in enrollment number
                k = k+1
                print("enrollment number is not found")
            else:  # when captcha is wrong clear input field
                driver.find_element_by_xpath(
                    '//*[@id="ctl00_ContentPlaceHolder1_TextBox1"]').clear()  # clear captcha
                driver.find_element_by_xpath(
                    '//*[@id="ctl00_ContentPlaceHolder1_txtrollno"]').clear()  # clear roll number
                print("captcha is wrong")
            continue


# main function
if __name__ == "__main__":
    main()
