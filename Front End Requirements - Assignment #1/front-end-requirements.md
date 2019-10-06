# Front End Requirements
  [PDF Version](https://github.com/tamirarnesty/bat-quinterac/blob/master/Front%20End%20Requirements%20-%20Assignment%20%231/BAT-Enterprises%20Assignment%20%231.pdf)



## Login - Test Cases
---------------------
<p align="center">
  <img width="900"  src="images/login-transaction.png">
</p>


## Logout - Test Cases
----------------------
<p align="center">
  <img width="900"  src="images/logout-transaction.png">
</p>


## Create Account - Test Cases
------------------------------
<p align="center">
  <img width="900"  src="images/createacct-transaction.png">
</p>


## Delete Account - Test Cases
------------------------------
<p align="center">
  <img width="900"  src="images/deleteacct-transaction.png">
</p>


## Deposit - Test Cases
-----------------------
<p align="center">
  <img width="900"  src="images/deposit-transaction.png">
</p>


## Withdraw - Test Cases
------------------------
<p align="center">
  <img width="900"  src="images/withdraw-transaction.png">
</p>


## Transfer - Test Cases
-------------------------
<p align="center">
  <img width="900"  src="images/transfer-transaction.png">
</p>


## Valid Accounts List File - Test Cases
----------------------------------------
<p align="center">
  <img width="900"  src="images/valid-accounts-list-file.png">
</p>


## Transaction Summary File - Test Cases
----------------------------------------
<p align="center">
  <img width="900"  src="images/transaction-sum-file-1.png">
  <img width="900"  src="images/transaction-sum-file-2.png">
</p>


## Test Plan
------------
To run our tests, we will be using the unittest module that is built into python. All of our tests will be in their respective subdirectories within the test/ directory. For example, the tests for login will have the path /tests/test_login/. Within each subdirectory, there will also be a directory for the logs (i.e tests/test_login/logs/<date of test>.txt). To run our tests, we will write a script within the tests/ directory that will execute all of the tests and put their output in their respective log files. Since the project has quite a few unit tests, having the results put in a log will prevent the terminal from becoming cluttered, and the test results more readable.
