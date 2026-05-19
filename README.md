# SauceDemo Playwright Automation Framework

 **Playwright + Python**.

## About the project

A demo project showcasing QA automation engineering skills.  
Includes **UI Automation**, **API Testing** and best practices.

## Technologies and Tools

- **Playwright** + Python (synchronous API)
- **Pytest** + Allure Reporting
- **Page Object Model (POM)** + BasePage
- **Data-driven testing**
- **Requests** — API Automation
- **Postman** + Newman (`/postman`)
- **YAML Config**
- **GitHub Actions** (CI/CD)

## Project Structure

qa-playwright-practice/
├── pages/                   
├── tests/                   
├── config/                   
├── utils/                   
├── data/                    
├── postman/                
├── .github/workflows/        
├── reports/                  
├── screenshots/              
├── pytest.ini
├── requirements.txt
└── README.md

## Running tests

# All tests
(`/pytest tests/ -q`)

# Generating the Allure report
- **pytest tests/ --alluredir=reports/allure-results**
- **allure serve reports/allure-results**

# API tests only
- **pytest tests/test_api.py -q**

## What has been implemented
- **UI Automation**

- **Successful and failed login (data-driven)**
- **The complete end-to-end process of purchasing a product**
- **Shopping Cart and Checkout**

## API Automation

- **Tests using the library requests**
- **Postman collection (postman/SauceDemo_API_Collection.json)**

## Best Practices

- **Page Object Model**
- **YAML configuration**
- **Automatic screenshots when the app crashes**
- **Logging**
- **Test markers (@smoke, @e2e, @api)**
- **Allure reports**