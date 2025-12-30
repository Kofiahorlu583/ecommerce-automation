# E-Commerce Test Automation Framework

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Selenium](https://img.shields.io/badge/selenium-4.0+-green.svg)](https://www.selenium.dev/)
[![Tests](https://img.shields.io/badge/tests-4%2F4%20passing-brightgreen.svg)](https://github.com/Kofiahorlu583/ecommerce-automation)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 📋 Overview

Professional Selenium WebDriver test automation framework implementing Page Object Model (POM) design pattern for web application testing. Built with Python and pytest, featuring automated login functionality tests with comprehensive reporting.

## ✨ Key Features

- ✅ **Page Object Model (POM)** - Clean separation of test logic and page elements
- ✅ **Data-Driven Testing** - JSON-based test data management
- ✅ **Cross-Browser Support** - Chrome browser automation with WebDriver
- ✅ **Detailed Reporting** - HTML test reports with pass/fail status
- ✅ **Screenshot on Failure** - Automatic screenshot capture for failed tests
- ✅ **Reusable Components** - Base page class with common methods
- ✅ **Easy Configuration** - Centralized pytest configuration

## 🏗️ Project Structure
```
ecommerce-automation/
│
├── pages/                      # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py           # Base class with common methods
│   ├── login_page.py          # Login page objects and methods
│   └── home_page.py           # Home page objects and methods
│
├── tests/                      # Test cases
│   ├── __init__.py
│   └── test_login.py          # Login functionality tests
│
├── utilities/                  # Helper utilities
│   └── __init__.py
│
├── test_data/                  # Test data files
│   └── credentials.json       # User credentials
│
├── reports/                    # Test execution reports
├── screenshots/                # Failure screenshots
│
├── conftest.py                # Pytest fixtures and configuration
├── pytest.ini                 # Pytest settings
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- Google Chrome browser
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Kofiahorlu583/ecommerce-automation.git
cd ecommerce-automation
```

2. **Create virtual environment** (recommended)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 🧪 Running Tests

### Run All Tests
```bash
pytest tests/ -v
```

### Run Specific Test
```bash
pytest tests/test_login.py::TestLogin::test_valid_login -v
```

### Run Tests by Marker
```bash
# Run only smoke tests
pytest tests/ -m smoke -v

# Run only regression tests
pytest tests/ -m regression -v
```

### Generate HTML Report
```bash
pytest tests/ --html=reports/report.html --self-contained-html
```

### Run with Verbose Output
```bash
pytest tests/ -v -s
```

## 📊 Test Cases Covered

| Test ID | Test Case | Description | Status |
|---------|-----------|-------------|--------|
| TC_001 | test_valid_login | Verify successful login with valid credentials | ✅ PASS |
| TC_002 | test_invalid_password | Verify error message with invalid password | ✅ PASS |
| TC_003 | test_invalid_username | Verify error message with invalid username | ✅ PASS |
| TC_004 | test_logout | Verify successful logout functionality | ✅ PASS |

## 📈 Test Results
```
====================== test session starts ======================
platform win32 -- Python 3.14.2, pytest-7.4.3, pluggy-1.6.0
collected 4 items

tests/test_login.py::TestLogin::test_valid_login PASSED    [ 25%]
tests/test_login.py::TestLogin::test_invalid_password PASSED [ 50%]
tests/test_login.py::TestLogin::test_invalid_username PASSED [ 75%]
tests/test_login.py::TestLogin::test_logout PASSED          [100%]

====================== 4 passed in 91.20s =======================
```

## 🔧 Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.14** | Programming language |
| **Selenium WebDriver** | Browser automation |
| **Pytest** | Testing framework |
| **Page Object Model** | Design pattern |
| **HTML Reports** | Test reporting |

## 📝 Page Object Model Implementation

### Base Page
Common methods used across all pages:
- `find_element()` - Locate elements with explicit wait
- `click()` - Click elements safely
- `enter_text()` - Input text into fields
- `get_text()` - Retrieve element text
- `is_displayed()` - Check element visibility

### Login Page
- Navigate to login page
- Enter credentials
- Click login button
- Verify error messages

### Home Page
- Verify successful login
- Check logout button presence
- Perform logout action

## 🎯 Key Accomplishments

- ✅ Implemented industry-standard Page Object Model
- ✅ Achieved 100% test pass rate (4/4 tests)
- ✅ Created reusable test components
- ✅ Configured automated reporting
- ✅ Added error handling and screenshots

## 📚 Learning Outcomes

Through this project, I demonstrated proficiency in:
- Selenium WebDriver automation
- Python programming for testing
- Page Object Model design pattern
- Test framework configuration (pytest)
- Test data management
- Automated reporting
- Version control with Git/GitHub

## 🔮 Future Enhancements

- [ ] Add more test scenarios (registration, checkout, search)
- [ ] Implement parallel test execution
- [ ] Add CI/CD pipeline (GitHub Actions)
- [ ] Integrate with Allure reporting
- [ ] Add API testing integration
- [ ] Implement database validation
- [ ] Add cross-browser testing (Firefox, Edge)
- [ ] Create custom test utilities

## 📧 Contact

**Kofi Ahorlu** - Aspiring QA Engineer

- 📧 Email: [Kofi Sedoame](ahorlukofi335@gmail.com)
- 💼 LinkedIn: [Sedoame Ahorlu](www.linkedin.com/in/sedoame-ahorlu-a91bb5209 )
- 🐙 GitHub: [@Kofiahorlu583](https://github.com/Kofiahorlu583)

---

⭐ **Star this repository if you find it helpful!**

💬 **Feel free to fork and contribute!**

📝 **Open to feedback and suggestions!**
