# **PythonSeleniumBDDFramework**

In this selenium python project BDD Framework created along with selenium python to automate web test cases and api testing. I have also added the allure reports to display the full and detailed presentation of the test result. 

## Installation: 
  
## Approach 1
  
  Run the following command and it will install all the packages listed in requirement.txt file
      
        pip install -r requirement.txt

## Approach 2

  
  ## 1)To run tests first need to install Selenium
        pip install selenium

  ## 2)Install Webdriver Manager
        pip install webdriver-manager

  ## 3)Install Behave
        pip install behave

  ## 4)Install Appium to run mobile test cases
        pip install Appium-Python-Client

  ## 5)Install Allure to generate the report
        pip install allure-behave
        pip install allure-python-commons

## Execution:

  ## 6)To run all the feature file
        behave Features -f allure_behave.formatter:AllureFormatter -o Report_Json

  ## 7)To run single feature file
        behave Features/BMI_alculator.feature -f allure_behave.formatter:AllureFormatter -o Report_Json

  ## 8)To run test cases using Tag name from single feature file                                    
        behave Features/BMI_alculator.feature --tags=mobile  -f allure_behave.formatter:AllureFormatter -o Report_Json

  ## 9)To run test cases using Tag name from all feature files
        behave Features --tags=mobile  -f allure_behave.formatter:AllureFormatter -o Report_Json

## Report Generation: 

  ## 10)To generate HTML report from JSON report
        allure generate Report_Json -o Report_Html --clean



