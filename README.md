# Automating Login Functionality Validation

## Overview
This project is an automation script designed to validate the login functionality of a sample website. Using Selenium WebDriver, the script automates the process of navigating to the website, entering login credentials, submitting the login form, and verifying the login status.

## Prerequisites
### Tools and Libraries
- **Programming Language**: Python 3.x
- **Automation Tool**: Selenium WebDriver
- **Browser Driver**: ChromeDriver or GeckoDriver
- **IDE/Editor**: PyCharm, VS Code, or equivalent

### Environment Setup
1. Install Python from the [official Python website](https://www.python.org/).
2. Install Selenium:
   ```bash
   pip install selenium
   ```
3. Download the browser driver for your preferred browser:
   - [ChromeDriver](https://chromedriver.chromium.org/)
   - [GeckoDriver](https://github.com/mozilla/geckodriver)
   
4. Ensure the browser version matches the driver version.

## How to Execute the Script
### Step 1: Clone the Repository
Download the project files or clone the repository:
```bash
git clone https://github.com/lakmina456/automation_testing

### Step 2: Open the Script
Open the Python script `login_automation.py` in your preferred IDE.

### Step 3: Configure the Browser Driver
Ensure the browser driver (e.g., `chromedriver.exe`) is in the system PATH or in the same directory as the script.

### Step 4: Run the Script
Execute the script from the terminal or IDE:
```bash
python login_automation.py
```

### Step 5: Observe the Output
- **Successful Login**: The script will print `Login Successful` and navigate to the user dashboard.
- **Failed Login**: The script will print `Login Failed` and display the error message.

## Test Data
### Valid Credentials:
- Username: `testuser`
- Password: `password123`

### Invalid Credentials:
- Username: `wronguser`
- Password: `wrongpassword`

## Expected Output
1. **Successful Login**:
   - Console Output: `Login Successful`
   - Visual Confirmation: The website navigates to the dashboard or displays a welcome message.

2. **Failed Login**:
   - Console Output: `Login Failed`
   - Visual Confirmation: The website shows an error message like `Invalid credentials`.

## File Structure
- `login_automation.py`: Python script for login functionality automation.
- `README.md`: Instructions for setting up and executing the script.

## Troubleshooting
- **Browser Driver Errors**: Ensure the driver is compatible with your browser version.
- **Element Not Found**: Verify the locators used in the script (e.g., `ID`, `XPath`).
- **Selenium Not Installed**: Ensure Selenium is installed using `pip install selenium`.

## Additional Notes
This project is for educational purposes only. The website URL used (`https://practicetestautomation.com/practice-test-login/`) is a placeholder and should be replaced with the actual target URL during testing.

---

Feel free to contact the author for further assistance or questions!
