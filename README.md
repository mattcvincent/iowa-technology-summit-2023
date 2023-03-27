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

### Git 

```
git tag -a v0.0 -m "before chat 1"
git push origin v0.0
git tag -d v0.0
git push origin --delete v0.0
git checkout v0.0
git switch -
```


### Resources

* [https://demo.actitime.com/api/v1/swagger](https://demo.actitime.com/api/v1/swagger)
* [https://demo.actitime.com/api/v1/swagger.json](https://demo.actitime.com/api/v1/swagger.json)
* [.gitignore](https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore)



### Steps

| Steps | Tag  | Name              | Description |
|-------|------|-------------------|-------------|
| 0.0   | [v0.0](https://github.com/mattcvincent/ai-assisted/tree/v0.0) | Starting point | Before 1st chat |
| 1.0   | [v1.0](https://github.com/mattcvincent/ai-assisted/tree/v1.0) | Chat 1 | Directory structure, failing test |
| 1.1   | [v1.1](https://github.com/mattcvincent/ai-assisted/tree/v1.1) | Chat 1 | Implementation |
| 2.0   | [v2.0](https://github.com/mattcvincent/ai-assisted/tree/v2.0) | Chat 2 | Stub class, fail for right reasons |
| 2.1   | [v2.1](https://github.com/mattcvincent/ai-assisted/tree/v2.1) | Chat 2 | Implementation |
| 3.0   | [v3.0](https://github.com/mattcvincent/ai-assisted/tree/v3.0) | Chat 3 | See the test fail |
| 3.1   | [v3.1](https://github.com/mattcvincent/ai-assisted/tree/v3.1) | Chat 3 | Implementation |
| 4.0   | [v4.0](https://github.com/mattcvincent/ai-assisted/tree/v4.0) | Chat 4 | Coverage report |
| 5.0   | [v5.0](https://github.com/mattcvincent/ai-assisted/tree/v5.0) | Chat 5 | Omit  `tests/` |
| 5.1   | [v5.1](https://github.com/mattcvincent/ai-assisted/tree/v5.1) | Chat 5 | Implementation |
| 6.0   | [v6.0](https://github.com/mattcvincent/ai-assisted/tree/v6.0) | Chat 6 | Next unit test (params) |
| 6.1   | [v6.1](https://github.com/mattcvincent/ai-assisted/tree/v6.1) | Chat 6 | Implementation |
| 7.0   | [v7.0](https://github.com/mattcvincent/ai-assisted/tree/v7.0) | Chat 7 | Pagination |
| 7.1   | [v7.1](https://github.com/mattcvincent/ai-assisted/tree/v7.1) | Chat 7 | Implementation |
| 8.0   | [v8.0](https://github.com/mattcvincent/ai-assisted/tree/v8.0) | Chat 8 | Test exception |
| 8.1   | [v8.1](https://github.com/mattcvincent/ai-assisted/tree/v8.1) | Chat 8 | Implementation |
| 9.0   | [v9.0](https://github.com/mattcvincent/ai-assisted/tree/v9.0) | Chat 9 | Integartion Test |
| 9.1   | [v9.1](https://github.com/mattcvincent/ai-assisted/tree/v9.1) | Chat 9 | Implementation |
| 10.0   | [v10.0](https://github.com/mattcvincent/ai-assisted/tree/v10.0) | Chat 10 | CI/CD |
| 10.1   | [v10.1](https://github.com/mattcvincent/ai-assisted/tree/v10.1) | Chat 10 | Implementation |
| 11.0   | [v11.0](https://github.com/mattcvincent/ai-assisted/tree/v11.0) | Chat 11 | Flatten the data |
| 11.1   | [v11.1](https://github.com/mattcvincent/ai-assisted/tree/v11.1) | Chat 11 | Implementation |
| 12.0   | [v12.0](https://github.com/mattcvincent/ai-assisted/tree/v12.0) | Chat 12 | Flatten the data |
| 12.1   | [v12.1](https://github.com/mattcvincent/ai-assisted/tree/v12.1) | Chat 12 | Implementation |
| 13.0   | [v13.0](https://github.com/mattcvincent/ai-assisted/tree/v13.0) | Chat 13 | Cloudformation |
| 13.1   | [v13.1](https://github.com/mattcvincent/ai-assisted/tree/v13.1) | Chat 13 | Implementation |
| 14.0   | [v14.0](https://github.com/mattcvincent/ai-assisted/tree/v14.0) | Chat 14 | Apply Cloudformation |
| 14.0   | [v14.1](https://github.com/mattcvincent/ai-assisted/tree/v14.1) | Chat 14 | Implementation |
| 15.0   | [v15.0](https://github.com/mattcvincent/ai-assisted/tree/v15.0) | Chat 15 | Load the Lake |
| 15.0   | [v15.1](https://github.com/mattcvincent/ai-assisted/tree/v15.1) | Chat 15 | Implementation |
| 16.0   | [v16.0](https://github.com/mattcvincent/ai-assisted/tree/v16.0) | Chat 16 | Deploy |
| 16.0   | [v16.1](https://github.com/mattcvincent/ai-assisted/tree/v16.1) | Chat 16 | Implementation |