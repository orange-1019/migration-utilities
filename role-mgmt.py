import pandas as pd
from github import Github

# Constants
CSV_FILE_PATH = 'path_to_your_csv_file.csv'
GITHUB_TOKEN = 'your_github_token'
ORGANIZATION_NAME = 'your_organization_name'

# Initialize GitHub instance
g = Github(GITHUB_TOKEN)
org = g.get_organization(ORGANIZATION_NAME)

# Read CSV file
df = pd.read_csv(CSV_FILE_PATH)

# Assign repos to groups or teams
for index, row in df.iterrows():
    repo_name = row['repo_name']
    team_name = row['group']

    # Get the repository
    repo = org.get_repo(repo_name)

    # Get the team
    team = org.get_team_by_slug(team_name)

    # Add the repository to the team
    team.add_to_repos(repo)
    print(f'Assigned {repo_name} to {team_name}')

print('All repositories have been assigned to their respective teams.')
