# Automated College Result Scraper


The "RGPV Result Scraper" is a Python script designed to automate the process of extracting student result data from the [Rajiv Gandhi Proudyogiki Vishwavidyalaya](http://result.rgpv.ac.in/result/BErslt.aspx) (RGPV) website. This script enables users to retrieve results for specific branches of study and semesters, subsequently saving the scraped data into CSV files for further analysis or record-keeping.

## Key Features:

1. **Web Scraping:** The script utilizes web scraping techniques to access and extract information from the RGPV result portal.

2. **Captcha Handling:** It automates the entry of captchas using Optical Character Recognition (OCR) with Tesseract, enabling the bypassing of security measures.

3. **Customization:** Users can select their desired branch of study and semester before initiating the scraping process, allowing flexibility in result retrieval.

4. **Data Export:** The extracted result data, including student roll numbers, names, SGPA, CGPA, and results, is organized and saved in CSV files.

## Overview

This Python script automates the process of scraping student result data from the Rajiv Gandhi Proudyogiki Vishwavidyalaya (RGPV) website. The script allows you to retrieve and store student results for specific branches and semesters in a CSV file.

## Table of Contents

- [Automated College Result Scraper](#automated-college-result-scraper)
  - [Key Features:](#key-features)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [YouTube Video Tutorial](#youtube-video-tutorial)
  - [Prerequisites](#prerequisites)
  - [Getting Started](#getting-started)
  - [Usage](#usage)
  - [Adapting the Code](#adapting-the-code)
  - [Configuration](#configuration)
  - [Installing Tesseract OCR](#installing-tesseract-ocr)
    - [Step 1: Download and Install Tesseract OCR](#step-1-download-and-install-tesseract-ocr)
    - [Step 2: Verify the Installation](#step-2-verify-the-installation)
    - [Step 3: Using Tesseract OCR](#step-3-using-tesseract-ocr)
    - [Step 4: Update the path](#step-4-update-the-path)
  - [Workflow](#workflow)
  - [Note](#note)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)


## YouTube Video Tutorial

You can watch the video tutorial on how to use this project by clicking on the following image:

[![Watch the video](https://img.youtube.com/vi/_ziAOyhLPk0/0.jpg)](https://www.youtube.com/watch?v=_ziAOyhLPk0)


## Prerequisites

Before using this script, make sure you have the following dependencies installed:

- Python 3.x
- Microsoft Edge WebDriver (msedgedriver.exe)
- Required Python libraries (can be installed via pip):
  - selenium
  - requests
  - Pillow (PIL)
  - BeautifulSoup4 (bs4)
  - pytesseract
  - pandas (for data manipulation, optional)

## Getting Started

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/devnamdev2003/result_automation_system.git
   ```

2. Navigate to the project directory:

   ```shell
   cd result_automation_system
   ```

3. Install the required Python libraries:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

1. Edit the `main()` function in the `project.py` script to customize the scraping parameters such as the branch, semester, and starting roll number.

2. Ensure that you have the `msedgedriver.exe` WebDriver executable placed in the project directory.

3. Run the script:

   ```shell
   python project.py
   ```

4. The script will start scraping student results and save them to CSV files in the project directory.




## Adapting the Code

To adapt this code for your college, follow these steps:

1. **Edit `project.py`**:
   - Open the `project.py` script in a text editor or code editor of your choice.
   - Modify the code in the `main()` function to match your college's website structure. Specifically, adjust the following:
     - The URL of your college's result page.
     - The HTML elements and XPaths used for interacting with the web page.
     - The logic for handling captcha and extracting result data.

2. **Customize Parameters**:
   - Customize parameters like the branch number, semester, starting roll number, and any other relevant information specific to your college.

3. **Test the Code**:
   - Test the modified code with a few sample roll numbers to ensure it works correctly for your college.

## Configuration

You can customize the following parameters in the `main()` function of `project.py`:

- `branch`: Enter the branch number according to your college's branch codes.
- `sem`: Set the semester for which you want to scrape results.
- Starting roll number (`i`) and the roll number format (`en_num`) should match your college's enrollment number format.

## Installing Tesseract OCR

[Tesseract OCR](https://github.com/tesseract-ocr/tesseract) is an open-source optical character recognition engine that is widely used for text recognition in images. To use Tesseract OCR in your project, follow these steps to install it on your system:

### Step 1: Download and Install Tesseract OCR

- **Windows**:
  - Download the Tesseract OCR installer for Windows from the [Tesseract GitHub releases](https://github.com/tesseract-ocr/tesseract/releases) page. Look for the latest version suitable for your system (e.g., `tesseract-ocr-w64-setup-vX.X.X.exe`).
  - Run the installer and follow the installation instructions. Make sure to select the option to add Tesseract to your system's PATH during installation.

- **Linux** (Debian/Ubuntu):
  - Open a terminal and run the following commands to install Tesseract:

    ```shell
    sudo apt update
    sudo apt install tesseract-ocr
    sudo apt install libtesseract-dev
    ```

- **macOS** (Homebrew):
  - If you don't have Homebrew installed, install it by following the instructions at [Homebrew](https://brew.sh/).
  - Open a terminal and run the following command to install Tesseract:

    ```shell
    brew install tesseract
    ```

### Step 2: Verify the Installation

To verify that Tesseract OCR is installed correctly, open a terminal or command prompt and run the following command:

```shell
tesseract --version
```

You should see the Tesseract OCR version information, indicating that the installation was successful.

### Step 3: Using Tesseract OCR

You can now use Tesseract OCR in your Python scripts or applications. Make sure to install the `pytesseract` Python library, which provides a Python wrapper for Tesseract OCR. You can install it using `pip`:

```shell
pip install pytesseract
```

Refer to the [pytesseract documentation](https://pypi.org/project/pytesseract/) for information on how to use Tesseract OCR with Python.

### Step 4: Update the path

- Set the path to Tesseract executable. Replace this path with your Tesseract installation path.
- Example: If Tesseract is installed at "C://Program Files//Tesseract-OCR//tesseract.exe", set it as follows:
  
  `tesseract_path = r"C://Program Files//Tesseract-OCR//tesseract.exe"`


```python
def read_text(captcha_image):
    tesseract_path = r"E://Program Files//Tesseract-OCR//tesseract.exe"   
    # Rest of your code...
```
## Workflow

1. **Import Libraries:**

   The script starts by importing necessary Python libraries, including those for web scraping, web automation, image processing, and file handling.

2. **Helper Functions:**

   - `find_src(source_code)`: This function parses the HTML source code of a web page to locate and extract the URL of the captcha image.
   - `download_image(url, image_name)`: Downloads the captcha image from a given URL and saves it locally with the specified name.
   - `read_text(captcha_image)`: Reads text from a captcha image using Tesseract OCR, cleans the extracted text, and deletes the image file.

3. **Main Function (`main()`):**

   - User Input:
     - The user is prompted to choose a branch of study by entering a number (e.g., Computer Science, Mechanical Engineering, etc.).
     - The user is prompted to enter a semester number (hardcoded as "6" in this script).

   - Browser Automation:
     - A WebDriver for Microsoft Edge is initiated (or the browser of your choice) for web automation using Selenium.
     - An implicit wait is set for element locating (0.5 seconds).

   - Website Navigation:
     - The script navigates to the RGPV result page (http://result.rgpv.ac.in/Result/ProgramSelect.aspx).
     - It selects the appropriate program (radlstProgram_1), which corresponds to the program for undergraduate results.

   - Loop Over Roll Numbers:
     - Inside a while loop, the script performs the following steps repeatedly:
       - Enrollment Number Generation
       - Captcha Image Download
       - Captcha Text Extraction
       - Form Filling and Submission

   - Handling Scenarios:
     - The script handles three possible scenarios after form submission:
       - Correct Captcha
       - Enrollment Number Not Found
       - Wrong Captcha

4. **Main Execution:**

   - Finally, the script checks if it's being run as the main program (`if __name__ == "__main__":`) and calls the `main()` function to start the scraping process.


## Note

- Ensure you have Microsoft Edge WebDriver (or the appropriate WebDriver for your browser) installed and set the `edge_driver_path` variable in the script to its location.

- Make sure you have the correct branch and semester selected before running the script.

- The script may require adjustments if the structure of the RGPV result page changes.
- This project's flexibility and functionality make it a valuable tool for academic institutions or individuals seeking to automate the retrieval of student result data from the RGPV website. It is essential to keep the script up to date with any changes in the structure of the result portal to ensure its continued effectiveness.

Happy scraping!
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script was developed as part of a college project to automate result retrieval.
- Thanks to the open-source community for providing tools and libraries used in this project.

Feel free to contribute to the project or report issues on the GitHub repository.

---