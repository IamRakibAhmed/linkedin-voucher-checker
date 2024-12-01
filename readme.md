# **LinkedIn Voucher Checker**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green?logo=selenium&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-blue?logo=pandas&logoColor=white)
![OpenPyXL](https://img.shields.io/badge/OpenPyXL-Excel_Integration-green)

A Python Selenium-based project designed to automate the process of validating LinkedIn URLs. The script logs into LinkedIn, processes each URL from a given list, checks their status, and handles errors gracefully while maintaining a clean, professional code structure.

---

## **Features**
- **Automated Login**: Logs into LinkedIn using your credentials.
- **URL Validation**:
  - Detects "Offer unavailable" messages.
  - Halts execution on "Something went wrong" and updates the URL list accordingly.
- **Excel Integration**: Dynamically updates the input Excel file to retain only unprocessed URLs.
- **Logs**:
  - Detailed logging for each step of the process.
  - Logs stored in a dedicated log file for easy debugging.
- **Error Handling**: Graceful termination and updates on encountering issues.

---

## **Project Structure**
```
linkedin-voucher-checker/
│
├── main.py                # Main entry point for the application
├── config.py              # Configuration file for credentials and paths
├── utils/
│   ├── __init__.py        # Package initialization
│   ├── logger.py          # Logging setup
│   ├── file_handler.py    # Excel file handling (load and update URLs)
├── services/
│   ├── __init__.py        # Package initialization
│   ├── linkedin_service.py  # Selenium-based LinkedIn interactions
├── requirements.txt       # Required Python libraries
├── README.md              # Project documentation
└── urls.xlsx              # Excel file containing the list of LinkedIn URLs
```

---

## **Requirements**
- ![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white) Python 3.8+
- ![Selenium](https://img.shields.io/badge/Selenium-Automation-green?logo=selenium&logoColor=white) Selenium
- ![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-blue?logo=pandas&logoColor=white) Pandas
- ![OpenPyXL](https://img.shields.io/badge/OpenPyXL-Excel_Integration-green) OpenPyXL

Install the required libraries using:
```bash
pip install -r requirements.txt
```

---

## **Setup Instructions**

### 1. **Clone the Repository**
```bash
git clone https://github.com/your-username/linkedin-voucher-checker.git
cd linkedin-voucher-checker
```

### 2. **Add Your Credentials**
Edit the `config.py` file to include your LinkedIn email and password:
```python
# config.py
LINKEDIN_EMAIL = "your_email@example.com"  # Replace with your LinkedIn email
LINKEDIN_PASSWORD = "your_password"  # Replace with your LinkedIn password
```

### 3. **Prepare the Input File**
Place your `urls.xlsx` file in the project root. Ensure it contains a column named `URLs` with the LinkedIn links to validate.

### 4. **Run the Script**
```bash
python main.py
```

---

## **Logs**
- Logs are stored in `logs/linkedin_checker.log`.
- The log file contains detailed information about the execution, including:
  - Login status.
  - Status of each URL processed (`Valid`, `Skipped`, or `Unchecked`).
  - Errors and exceptions, if any.

---

## **Outputs**
1. **Updated URLs File**:
   - The script updates `urls.xlsx` to retain only the unprocessed URLs if "Something went wrong" is encountered.

2. **Valid URLs**:
   - Valid URLs are saved in a new Excel file named `valid_urls.xlsx`.

---

## **Error Handling**
- **"Something went wrong"**:
  - Logs the error and updates `urls.xlsx` to exclude already-processed URLs.
  - Halts further processing.
  
- **Other Errors**:
  - Logs exceptions with the corresponding URL for debugging.

---

## **Contributing**
Contributions to enhance the project are welcome! Here's how you can help:
1. Fork the repository.
2. Create a new branch (`feature/new-feature`).
3. Commit your changes (`git commit -m "Add some new feature"`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Author**
Developed with ❤️ by [Rakib Ahmed](https://www.linkedin.com/in/iamrakibahmed/).

---