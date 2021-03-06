<H1 align="center">
Quinterac BAT Enterprises π¦
</H1>
<H4 align="center">
CISC 327 Group Project</br>
</H4>

<p align="center">
<a href="https://github.com/tamirarnesty/bat-quinterac/actions"><img alt="CI Status" src="https://github.com/tamirarnesty/bat-quinterac/workflows/Python%20Application%20CI/badge.svg"></a> 
<a href="https://github.com/tamirarnesty/bat-quinterac/blob/master/LICENSE"><img alt="License" src="https://img.shields.io/cocoapods/l/Loaf.svg?style=flat"></a> 
<a href=""><img alt="Platform" src="https://img.shields.io/badge/platform-Terminal-green.svg"/></a> 
<a href=""><img alt="Python" src="https://img.shields.io/badge/language-Python-orange.svg"/></a>
</p>

## Authors
* Tamir Arnesty
* Aaron Safer-Rosenthal
* Ben Durston

## Project
Folder structure:
```
.
β   .gitignore
β   LICENSE
|   pytest.ini
β   README.md
β   requirements.txt ========> python dependencies, a MUST
β   setup.py
|
ββββ.github
β   ββββworkflows
β           pythonapp.yml =======> CI workflow for python
β
ββββquinterac
β   β   __init__.py
β   β   __main__.py
β   β   Account.py
β   β   app.py
β   β   Errors.py
β   β   formats.py
β   β   SessionHandler.py
β   β   transactionSummaryFile.txt
β   ββββvalidAccountsListFile.txt
β
ββββtests
    β   __init__.py
    β   TestCreateAccount.py
    β   TestDeleteAccount.py
    β   TestDeposit.py
    β   TestLogin.py
    β   TestLogout.py
    β   TestTransactionSummaryFile.py
    β   TestTransfer.py
    ββββTestWithdraw.py
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Testing

To run all the test code:

```
pytest
```

## Acknowledgement
The basis of this project was modelled after Professor Steven Ding's CISC 327 CI-Python project, which can be found [here](https://github.com/CISC-CMPE-327/CI-Python)
