# hyrenet-bugathon-qa-automation

# HyreNet BugAThon – Quality Assurance Automation Framework

## 📋 Project Overview

This repository contains a comprehensive **Selenium-based test automation framework** built for the **HyreNet BugAThon – Quality Assurance Automation Challenge**. The framework is designed to identify, reproduce, and document bugs in the HyreNet AI-powered assessment platform using industry-standard QA practices.

The project follows a clean **Page Object Model (POM)** architecture, supports **automated bug reporting**, captures **screenshots on failures**, and generates **HTML & Excel reports** suitable for hackathon evaluation.

---

## 🎯 Objective

To identify and document bugs across the following HyreNet modules:

* Login & Authentication
* Assessment Question Creation
* Test Template Management
* Test Scheduling & Management

---

## 🏗️ Project Structure

```
hyrenet-bugathon/
├── config/
│   └── config.ini              # Configuration settings
├── pages/
│   ├── base_page.py           # Base Page Object Model
│   ├── login_page.py          # Login page objects
│   ├── assessment_page.py     # Assessment page objects
│   ├── test_template_page.py  # Template page objects
│   └── test_schedule_page.py  # Scheduling page objects
├── tests/
│   ├── test_login.py          # Login test cases
│   ├── test_assessment.py     # Assessment test cases
│   ├── test_template.py       # Template test cases
│   └── test_scheduling.py     # Scheduling test cases
├── utils/
│   ├── bug_reporter.py        # Bug reporting utility
│   └── test_data_helper.py    # Test data generation
├── screenshots/               # Screenshots captured on failures
├── reports/                   # HTML reports & Excel bug reports
├── conftest.py               # Pytest fixtures and setup
├── pytest.ini                # Pytest configuration
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

---

## 🛠️ Tech Stack

* **Language**: Python 3.8+
* **Automation Tool**: Selenium WebDriver
* **Test Framework**: Pytest
* **Reporting**: pytest-html, openpyxl
* **Driver Management**: webdriver-manager
* **Design Pattern**: Page Object Model (POM)

---

## 📦 Installation

### Prerequisites

* Python 3.8 or higher
* pip package manager
* Google Chrome / Mozilla Firefox

### Setup Steps

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd hyrenet-bugathon
```

2. **Create and activate virtual environment**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Update the configuration file at `config/config.ini`:

```ini
[BASE]
url = https://app.hyrenet.in/
email = hyrenet+bugathon@guvi.in
password = hyrenettest@123
browser = chrome
headless = false
```

---

## 🚀 Running Tests

### Run all tests

```bash
pytest
```

### Run a specific module

```bash
pytest tests/test_login.py
```

### Run using markers

```bash
pytest -m login
pytest -m assessment
pytest -m security
```

### Run tests in parallel

```bash
pytest -n auto
```

### Generate HTML report

```bash
pytest --html=reports/report.html --self-contained-html
```

---

## 📊 Test Coverage

### 🔐 Login Module (7 Test Cases)

* Valid login
* Invalid credentials
* Empty field validation
* SQL injection testing
* XSS vulnerability testing
* Password visibility toggle
* Session handling

### 📝 Assessment Module (7 Test Cases)

* Question creation
* Empty field validation
* Duplicate titles
* Special characters
* XSS testing
* Maximum length validation
* Search functionality

### 📂 Template Module (6 Test Cases)

* Valid template creation
* Template without questions
* Negative duration validation
* Zero duration validation
* Delete functionality
* XSS testing

### 📅 Scheduling Module (7 Test Cases)

* Valid scheduling
* Past date validation
* Date range checks
* Invalid email handling
* Missing candidates
* SQL injection testing
* Concurrent scheduling conflicts

---

## 🐛 Bug Reporting

The framework automatically generates **Excel bug reports** for failed test cases containing:

* Bug ID
* Test Name
* Bug Title & Description
* Steps to Reproduce
* Expected vs Actual Results
* Severity & Priority
* Module Name
* Screenshot Reference

### 📁 Bug Report Location

```
reports/Bug_Report_YYYYMMDD_HHMMSS.xlsx
```

### 🚦 Severity Levels

* **Critical** – Security issues, crashes, data loss
* **High** – Core functionality broken
* **Medium** – Partial failure with workaround
* **Low** – UI or cosmetic issues

---

## 📈 Reports Generated

1. **HTML Test Execution Report** – `reports/report.html`
2. **Excel Bug Report** – `reports/Bug_Report_*.xlsx`
3. **Execution Logs** – `reports/test_execution.log`
4. **Screenshots** – `screenshots/`

---

## 🔍 Key Features

* Page Object Model architecture
* Automatic bug documentation
* Screenshot capture on failures
* Security testing (SQLi, XSS)
* Parallel execution support
* Clean and scalable framework

---

## 🧪 Writing New Tests (Sample)

```python
def test_example(driver, bug_reporter):
    page = YourPage(driver)
    page.perform_action()

    if not page.verify_result():
        bug_reporter.report_bug(
            test_name="test_example",
            bug_title="Sample Bug",
            description="Issue description",
            steps_to_reproduce="1. Step one\n2. Step two",
            expected_result="Expected behavior",
            actual_result="Actual behavior",
            severity="Medium"
        )
        pytest.fail("Test failed")
```

---

## 🔧 Troubleshooting

**WebDriver issue**

```bash
pip install --upgrade webdriver-manager
```

**Timeouts**

* Increase waits in `config.ini`

**Screenshots not saving**

```bash
mkdir screenshots
```

---

## 🔄 CI/CD Integration

### Jenkins Pipeline

```bash
pip install -r requirements.txt
pytest --html=reports/report.html
```

### GitHub Actions (Optional)

```yaml
name: Run Tests
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - run: pip install -r requirements.txt
      - run: pytest
```

---

## ✅ Deliverables Checklist

* Test Scenarios
* Test Cases
* Requirement Traceability Matrix (RTM)
* Bug Report (Excel)
* Automation Scripts
* HTML Reports
* Screenshots
* Execution Video
* GitHub Repository

---

## 🎥 Demo Video

https://drive.google.com/file/d/1L-lYi2vRkKZ7D3wZTRRS1bg99E-i4yJr/view?usp=drive_link

---

## 🔗 Submission Links

* **GitHub Repository**: <your-github-url>
* **Execution Video**: <video-link>
* **Bug Report**: <excel-link>
* **HTML Report**: <report-link>

---

**Last Updated**: January 31, 2026
**Version**: 1.0.0
**Author**: LOKESH B

> This project is created strictly for educational and evaluation purposes as part of the HyreNet BugAThon challenge.
