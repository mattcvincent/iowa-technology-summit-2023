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
* (`AWS_ROLE` is output from the CloudFormation stack you in `Prerequisites` below)



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

### Prerequisites

The final steps ([Chat 15](chat/15.md) and [Chat 16](chat/16.md) of this project assume you've connected GitHub with your AWS account like shown below and you have replaced `SomeTypeOfAccessNeededToCreateABucket` with an appropriate policy of your choice): 

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Connect GitHub to AWS
Parameters:
  GitHubOrg:
    Type: String
  RepositoryName:
    Type: String
  OIDCProviderArn:
    Description: ARN for the GitHub OIDC Provider.
    Default: ""
    Type: String

Conditions:
  CreateOIDCProvider: !Equals 
    - !Ref OIDCProviderArn
    - ""

Resources:
  Role:
    Type: AWS::IAM::Role
    Properties:
      RoleName: GitHubActionsRole
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/SomeTypeOfAccessNeededToCreateABucket
      AssumeRolePolicyDocument:
        Statement:
          - Effect: Allow
            Action: sts:AssumeRoleWithWebIdentity
            Principal:
              Federated: !If 
                - CreateOIDCProvider
                - !Ref GithubOidc
                - !Ref OIDCProviderArn
            Condition:
              StringLike:
                token.actions.githubusercontent.com:sub: !Sub repo:${GitHubOrg}/iowa-technology-summit-2023:*
                token.actions.githubusercontent.com:aud: sts.amazonaws.com

  GithubOidc:
    Type: AWS::IAM::OIDCProvider
    Condition: CreateOIDCProvider
    Properties:
      Url: https://token.actions.githubusercontent.com
      ClientIdList: 
        - sts.amazonaws.com
      ThumbprintList:
        - 6938fd4d98bab03faadb97b34396831e3780aea1

Outputs:
  Role:
    Value: !GetAtt Role.Arn 
```
