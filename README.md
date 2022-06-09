This simple example CLI tool uses the Github GraphQL API query the last 3 releases or pull requests for a specified repository.

Requires Python 3.8+  https://www.python.org/downloads/

Extract contents of zip to a directory, such as ~/githubtool
 
Change to the directory and create a virtual environment to to run it in.
cd .\githubtool
python3 -m venv venv
 
Activate virtual environment
source venv/bin/activate
 
Install the required dependencies in the virtual environment
pip install -r requirements.txt 
 
Next, you'll need to create a personal access token from your Github account to query the data. More information can be find at https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token. No additional scopes are required to access public repositories, but to access private repositories you'll need to add the following scope:
repo:status

After creating your personal access token, you will need to be added to the .env file included in the package. Replace the "abc" string with the token you generated.

usage: githubtool.py [-h] (-r | -pr) owner repository

positional arguments:
  owner                The name of the user or organization owning the repository
  repository           The name of the repository

optional arguments:
  -h, --help           show this help message and exit
  -r, --releases       Outputs the repository's latest 3 releases
  -pr, --pullrequests  Outputs the repository's latest 3 pull requests
  
Examples:
python githubtool.py vuejs vitepress --releases
python githubtool.py microsoft powertoys --pullrequests


When complete, you can leave the virtual environment using the command:
deactivate
