# **Python Selenium BDD Test Automation Framework**

[![LinkedIn](https://img.shields.io/badge/@LinkedIn-SpurQLabs-orange.svg)](https://www.linkedin.com/company/spurqlabs/mycompany/)

[![Blog](https://img.shields.io/badge/@Blog-SpurQLabs_Blogs-blue.svg)](https://spurqlabs.com/blogs/)

## **Description**

This repository contains a test framework using Selenium, written in Python, for automating web browser tests. It provides a structured and scalable framework for writing end-to-end tests using Selenium with Behave, and Python

### **Create BDD Framework**

- [Learn how to create a BDD Web Test Automation Framework using Python's Behave Library with Selenium](https://spurqlabs.com/python-selenium-framework/)

## **Features**

- Written in Python for strong typing and improved code quality
- Utilizes Selenium, a powerful and flexible web automation library
- Supports Behave for natural language behavior-driven development (BDD) style tests
- Includes built-in reporting using Allure for easy test result visualization
- Provides a set of utility functions and configurations for common test scenarios
- Supports parallel test execution for faster testing

## **Table of Contents**
- [Pre-Requitesites](#Pre-Requitesites)
- [Technology](#Technology_used_in_Framework)
- [Installation](#Installation)
- [Execution](#Execution)
- [Report-Generation](#Report_Generation )
- [Framework Structure](#Fmework_Structure)
- [Reports](#Generated_Reports)

## Pre-Requisite
### *Required tools for the project*

- Python
- Selenium
- allure-behave: 2.10.0
- allure-python-commons: 2.10.0
- behave: 1.2.6
- webdriver-manager: 3.8.3


## Technology_used_in_Framework
#### AUTOMATION:
- `Python`
- `Selenium`
- `Behave`
- `webdriver-manager`

#### REPORTING TOOL :
- `allure-behave- ^2.10.0`
- `allure-python-commons - ^2.10.0`
#### FRAMEWORK DESIGN PATTERN :
- `Behavior Driven Development (BDD)`
#### OS for Execution on Local:
- `Windows`

**Note:** 
##### Please make sure you have all technologies in your local machine installed or configured.

## Installation
### To Clone this repository to a local directory
Commands to clone and run the test cases<br />
- #### git clone: 
`https://github.com/spurqlabs/PythonSeleniumBDDFramework.git`

This command clone this repository to your local VS code.
- #### Install the dependencies mentioned in prerequisite

- Approach1
    
    Run the following command and it will install all the packages listed in requirement.txt file
      
        pip install -r requirement.txt

- Approach2

#### 1)To run tests first need to install Selenium
        pip install selenium

#### 2)Install Webdriver Manager
        pip install webdriver-manager

#### 3)Install Behave
        pip install behave

#### 4)Install Allure to generate the report
        pip install allure-behave
        
        pip install allure-python-commons

## Execution

#### 5)To run all the feature file
        behave Features -f allure_behave.formatter:AllureFormatter -o Report_Json

#### 6)To run single feature file
        behave Features/BMI_alculator.feature -f allure_behave.formatter:AllureFormatter -o Report_Json

#### 7)To run test cases using Tag name from single feature file                                    
        behave Features/BMI_alculator.feature --tags=mobile  -f allure_behave.formatter:AllureFormatter -o Report_Json

#### 8)To run test cases using Tag name from all feature files
        behave Features --tags=mobile  -f allure_behave.formatter:AllureFormatter -o Report_Json

## Report_Generation 

#### 9)To generate HTML report from JSON report
        allure generate Report_Json -o Report_Html --clean

## Framework_Structure

![image](https://user-images.githubusercontent.com/110516709/232678511-7f6131f9-195a-4098-ba2d-5a3c309cda2e.png)

### *Features*

- The feature file contains the test scenarios described in Gherkin Language. 
- The Scenarios are described in steps format using the keywords like Give, when, And, Then.

### *Environment File*

- Environment.py:
    - This file is used to initialize the browser with the help of before_scenario Hooks
    - The file also launches the application url in before hooks for every test scenarios
    - The file has after_step hooks which captures the screenshots of every steps mentioned in the feature File
    - The after_scenario hook is used to close the page and the browser.

### *Pages*

- The pages folder has the page object model of every feature file. 
- The each file from the page folder is consists of the locators used to locate the webelements and the required actions performed to validate the functionality of the respective web elements. 

### *Steps*

- The step file is used to map the steps described in the feature file.
- The fiel contains the multiple step files for each feature file and has the respective steps included

### *Resources*

- The resources has config.json file which contains the key and value pairs of the most frequently used data in the framework. For example web url. 

## Generated_Reports

### Report1:

![image](https://user-images.githubusercontent.com/110516709/232679329-8c70aa70-ddc1-485d-b935-85c6a6903c16.png)

### Report2: 

![image](https://user-images.githubusercontent.com/110516709/232679419-e97a481b-0c1c-42e8-923b-13a69e76a433.png)
