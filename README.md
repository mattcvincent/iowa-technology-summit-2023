# AI-Assisted Software Engineering Demo

## Setup

### System Prerequisites

* Install [git](https://git-scm.com/downloads), [python 3.9+](https://www.python.org/downloads/)

### Additional Recommendations

* Install [Visual Studio Code](https://code.visualstudio.com/download)
  * Install these [Extensions](https://marketplace.visualstudio.com/VSCode): 
    * [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
      * COMMAND-SHIFT-P: Python: Create Environment > Venv 
      * (Creates a `.venv` virtualenvironment in the current workspace)
      * `source .venv/bin/activate` 
    * [Markdown Preview](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-preview-github-styles)
      * COMMAND-K V: preview side-by-side

### Setup Before Chat

```
source .venv/bin/activate
cd project
pip3 install -r requirements.txt
touch .env
echo "ACTITIME_URL=https://demo.actitime.com/api/v1/" >> .env
echo "ACTITIME_USERNAME=admin" >> .env
echo "ACTITIME_PASSWORD=manager" >> .env
```

Add these GitHub Actions secrets:
* `ACTITIME_PASSWORD`, `ACTITIME_URL`, `ACTITIME_USERNAME`, `AWS_ROLE`



## Useful Commands & Resources

### Commands

```bash
python -m unittest discover -s tests
coverage run -m unittest discover -s tests
coverage report && coverage html && open htmlcov/index.html

python -m unittest discover -s tests -p "test_*"
python -m unittest discover -s tests -p "integration_test_*"
```
#### Markdown

To open a separate preview window, use the keyboard shortcut `Ctrl+Shift+V`.

To open side by side, use the keyboard shortcut `Ctrl+K V`.



### Resources

* [https://demo.actitime.com/api/v1/swagger](https://demo.actitime.com/api/v1/swagger)
* [https://demo.actitime.com/api/v1/swagger.json](https://demo.actitime.com/api/v1/swagger.json)
* [.gitignore](https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore)

## Solution

[Solution here](https://github.com/mattcvincent/ai-assisted)

## Todo

Tag v2.0 which will be 7 or so steps in...