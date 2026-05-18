# SauceDemo Playwright Automation Framework

**Playwright + Python + Pytest**.

## Technology
- Playwright
- Python 3.11+
- Pytest + Allure reporting
- Page Object Model (POM)
- Data-driven testing

## Running tests

```bash
# Activate the environment
source venv/bin/activate

# Set dependencies
pip install -r requirements.txt

# Run all tests
pytest tests/

# Run with the Allure report
pytest tests/ --alluredir=reports/allure-results
allure serve reports/allure-results