## Github CLI Example Tool

This simple example CLI tool uses the Github GraphQL API query the last 3 releases or pull requests for a specified repository.

### Requirements:
[Python 3.8+](http://www.python.org/downloads/ "Python 3.8+") 

### Setup Instructions
Extract the contents of zip file to a directory, such as ./githubtool
 
Change to this directory and create a python virtual environment. This virtual environment will allow you to setup an isolated environment to install the required dependencies:

`cd ./githubtool`

`python3 -m venv venv`
 
Activate the virtual environment:

#### Linux/MacOS

`source venv/bin/activate`

#### Windows

`venv\Scripts\activate.bat`

Install the required dependencies within the virtual environment:

`pip3 install -r requirements.txt` 

### Github Authorization
A Github personal access token will need to be generated in order to access the API and query the data. If you already have a Github account, a personal access token can be generated at https://github.com/settings/tokens.  Please refer to the [Github Personal Access Token Docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token  "Github Personal Access Token Docs")  for more detailed instructions on how to do this. For the token access scope, no additional scopes need to be selected to access public repositories, but to access private repositories you'll need to additionally select the following scope:

`repo:status`

After creating your personal access token, you will need to add it to the .env file included in the package.  To do this, replace the "abc" string with the token you generated.

### Using the Tool
```
usage: githubtool.py [-h] (-r | -pr) owner repository

positional arguments:
  owner                The name of the user or organization owning the repository
  repository           The name of the repository

optional arguments:
  -h, --help           show this help message and exit
  -r, --releases       Outputs the repository's latest 3 releases
  -pr, --pullrequests  Outputs the repository's latest 3 pull requests
```

### Examples
Find the latest 3 releases in VueJS's Vitepress repository:

`python3 githubtool.py vuejs vitepress --releases`

Find the latest 3 pull requests in Microsoft's PowerToys repository:

`python3 githubtool.py microsoft powertoys --pullrequests`

When complete, you can deactivate the virtual environment using the command:

`deactivate`
