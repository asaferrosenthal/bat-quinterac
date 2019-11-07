<H1 align="center">
Quinterac BAT Enterprises 🦇
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
│   .gitignore
│   LICENSE
|   pytest.ini
│   README.md
│   requirements.txt ========> python dependencies, a MUST
│   setup.py
|
├───.github
│   └───workflows
│           pythonapp.yml =======> CI workflow for python
│
├───quinterac
│   │   __init__.py
│   │   __main__.py
│   │   Account.py
│   │   app.py
│   │   Errors.py
│   │   formats.py
│   │   SessionHandler.py
│   │   transactionSummaryFile.txt
│   └───validAccountsListFile.txt
│
└───tests
    │   __init__.py
    │   TestCreateAccount.py
    │   TestDeleteAccount.py
    │   TestDeposit.py
    │   TestLogin.py
    │   TestLogout.py
    │   TestTransactionSummaryFile.py
    │   TestTransfer.py
    └───TestWithdraw.py
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
