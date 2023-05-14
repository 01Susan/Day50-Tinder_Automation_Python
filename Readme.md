# Tinder Automation Script

This is a Python script that automates the process of logging in to Tinder, navigating through the notification and location popups, and then finding a girl to dislike on the app. The script uses the Selenium library to automate the interactions with the Tinder web application and uses environment variables to store sensitive login credentials.

## Requirements
- Python 3.6 or higher
- Selenium
- ChromeDriver
- dotenv

## Installation
1. Clone this repository to your local machine
2. Install the required libraries by running `pip install selenium dotenv`
3. Download the ChromeDriver executable that matches your Chrome browser version and place it in the `chromedriver_win32` directory
4. Create a `.env` file in the project directory and add your Tinder account email and password in the format `EMAIL=your_email` and `PASSWORD=your_password`
5. Run the script by running `python tinder_automation.py` in the command line

## Disclaimer
This script is for educational purposes only and should not be used for any illegal or unethical purposes. The developer is not responsible for any consequences that may arise from using this script.