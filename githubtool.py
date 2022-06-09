from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
from argparse import ArgumentParser
from os import path
from dotenv import dotenv_values

# Fetch the user's github personal access token from .env file
my_path = path.abspath(path.dirname(__file__))
ENV_PATH = path.join(my_path, ".env")
environment = dotenv_values(ENV_PATH)

# Initialize the possible command line arguments available to the user when running the program
# The owner and repository positional arguments are required for every run
parser = ArgumentParser()
parser.add_argument("owner", help="The name of the user or organization owning the repository")
parser.add_argument("repository", help="The name of the repository")

# The argument group requires selection of one, and only one, of the provided arguments (--releases or -pullrequests)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument(
    "-r",
    "--releases",
    action="store_true",
    help="Outputs the repository's latest 3 releases",
)
group.add_argument(
    "-pr",
    "--pullrequests",
    action="store_true",
    help="Outputs the repository's latest 3 pull requests",
)

args = parser.parse_args()

# Initialize our transport request object with user's the personal access token to call Github's GraphQL endpoint
transport = RequestsHTTPTransport(
    url="https://api.github.com/graphql",
    headers={"Authorization": "bearer " + environment["github_token"]},
    verify=True,
    retries=3,
)

# Initialize the client. We'll use introspection to fetch the GraphQL schema from the endpoint at runtime
client = Client(transport=transport, fetch_schema_from_transport=True)

# Map the specified owner/repository arguments to a dictionary that will be used in the GraphQL queries
params = {"owner": args.owner, "name": args.repository}


def get_latest_releases(client, params):
    """
    Queries the GitHub GraphQL endpoint and prints the 3 latest releases from a repository.

    :param client: GraphQL request client
    :type client: :class:`gql.Client` object
    :param params: Variables to include in the GraphQL request
    :type params: dict
    """
    # Build the GraphQL query
    query = gql(
        """
        query getLatestReleases($owner: String!, $name: String!) { 
          repository(owner: $owner, name: $name) { 
            releases(last: 3) {
              edges {
                node {
                  name
                }
              }
            }
          }
        }
        """
    )

    # Make the request against the API endpoint
    try:
        result = client.execute(query, variable_values=params)
    except Exception as ex:
        print(f"Failed querying API: {ex}.")
        return
    print(f"The latest releases in {params['owner']}/{params['name']}:")
    # Output the JSON results to a readable list
    for i in result["repository"]["releases"]["edges"]:
        print(i["node"]["name"])


def get_latest_pull_requests(client, params):
    """
    Queries the GitHub GraphQL endpoint and prints the 3 latest pull requests from a repository.

    :param client: GraphQL request client
    :type client: :class:`gql.Client` object
    :param params: Variables to include in the GraphQL request
    :type params: dict
    """

    # Build the GraphQL query
    query = gql(
        """
      query getLatestPullRequests($owner: String!, $name: String!) {
        repository(owner: $owner, name: $name) {
          pullRequests(last: 3) {
            edges {
              node {
                title
                number
              }
            }
          }
        }
      }
      """
    )

    # Make the request against the API endpoint
    try:
        result = client.execute(query, variable_values=params)
    except Exception as ex:
        print(f"Failed querying API: {ex}.")
        return
    print(f"The latest pull requests in {params['owner']}/{params['name']}:")
    # Output the JSON results to a readable list
    for i in result["repository"]["pullRequests"]["edges"]:
        print(f"{i['node']['number']}: {i['node']['title']}")


if args.releases:
    get_latest_releases(client, params)
elif args.pullrequests:
    get_latest_pull_requests(client, params)
