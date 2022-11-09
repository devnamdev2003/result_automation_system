## Get results of all students using `Web Scraping` and `Automation`

>**URL of video**: [YouTube](https://youtu.be/_ziAOyhLPk0)

---
>**Aim**

The aim of this project is to get the result of all the students of any college in one go instead of getting one by one.

>**Why did i make this project**

If a person wants to see the result of any student, then he visits the website of the college. And checks the result by filling the details like roll number, course, year and captcha of that student. But if he wants to see the result of all the students together, then he will fill the details of all students one by one and then see the result of all the students. But it is a time-consuming process. So, to overcome this problem I made a project which shows the result of all the students in one go. in the form of an excel sheet.

>**Working**

When my program starts, it goes to the website where college student’s results are uploaded. And by visiting that website fills the details of the students one by one and extracts the marks of the students from the result shown.and also stores those marks in excel file.

>**Technology used**
- Programming Language: Python
- Web scraping: By BeautifulSoup
- Download image: By shutil (Download Image From URL)
- Image to text convert: By pytesseract (To read captcha)
- Web Automation: By Selenium 
- Webdriver: Chrome

>**Installtion**

- Simple steps for tesseract installation in windows.

  - Download tesseract exe from https://github.com/UB-Mannheim/tesseract/wiki.

  - Install this exe in `C:\Program Files (x86)\Tesseract-OCR`

  - Open virtual machine command prompt in windows or anaconda prompt.

  - Run `pip install pytesseract`

  - To test if tesseract is installed type in python prompt:

>**Future**

This project is not enough to check the results of college students. Rather, with the help of this project, you can also get the data of those websites automatically. Whose data you get one after the other.

>**Conclusion**

I think this project can be used to analyses the result of the student like who is the topper of the class. How many students failed in the class and how many passed in the class? and to know the overall pass percentage of the class.