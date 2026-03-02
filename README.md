# saucedemo-automation-
This project demonstrates structured automation development, proper test abstraction, and validation of both functional and security-related behaviors in a web-based e-commerce application.

📌 Project Description

This project contains automated test scripts developed as part of a Technical Assessment for the SDET position.

The automation framework is built using:

Python

Selenium WebDriver

Pytest

Page Object Model (POM) design pattern

The test automation covers the end-to-end functional flow of the SauceDemo application, including:

Login (valid & invalid scenarios)

Inventory display validation

Product sorting

Add to Cart & Remove from Cart

Checkout process

Logout & session validation

🏗 Framework Design

The framework follows the Page Object Model (POM) structure to ensure:

Separation of test logic and page logic

Better maintainability

Reusability of page components

Scalable test structure

Project structure:

pages/       → Page Object classes
tests/       → Test scenarios
utils/       → Driver, Logger, Screenshot utilities
conftest.py  → Pytest configuration
⚙️ Key Features Implemented

Automated WebDriver setup using webdriver-manager

Screenshot capture on test failure

Execution logging stored in log files

Modular page design

Assertion-based validation

Security validation (session invalidation, direct URL access)

🧪 Test Coverage Scope

Functional Coverage:

Authentication validation

Product sorting validation

Cart quantity synchronization

Checkout form validation

Access control validation

Non-Functional Observations:

Console error monitoring

Accessibility warnings detection

Monitoring API error reporting (Backtrace integration)

▶️ How to Run

Install dependencies:

pip install -r requirements.txt

Execute test:

pytest -v

Screenshots will be saved in:

/screenshots

Execution logs will be stored in:

/logs
📈 Objective

The goal of this automation is to demonstrate:

Test design capability

Automation framework design skill

Clean code structure

SDET-level implementation

Stability and security validation awareness
