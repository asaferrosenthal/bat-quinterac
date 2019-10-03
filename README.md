# bat-quinterac
CISC 327 Group Project

[![](https://github.com/tamirarnesty/bat-quinterac/workflows/Python%20Application%20CI/badge.svg)](https://github.com/tamirarnesty/bat-quinterac/actions)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg?style=flat-square&color=brightgreen)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)

## Authors
* Tamir Arnesty
* Aaron Safer-Rosenthal
* Ben Durston

Folder structure:
```
.
│   .gitignore
│   LICENSE
│   README.md
│   requirements.txt ========> python dependencies, a MUST
│
├───.github
│   └───workflows
│           pythonapp.yml =======> CI workflow for python
│
└───package
        app.py
        test_app.py   ==========> test file
        __init__.py
        
```

To run all the test code:

```
pytest
```
