# pytest-allure-selenium-example

Installation
1. Install python version 3+
2. Install pytest
``pip install pytest``
3. Install selenium
``pip install selenium``
4. Install Allure for pytest
``pip install allure-pytest``
5. Install Allure.<br>
   For Mac
   ``brew install allure``

Run tests
1. Run command in terminal 
``pytest simpleTest.py --alluredir=<path to you project>/allure-results``
2. Generate and open allure report
``allure serve <path to you project>/allure-results``

Result<br>
![Report](screen/report.png?raw=true)