import requests
import json

# Replace this with your GitHub username
username = "tanishanand548"

# GitHub API URL to fetch user events (e.g., commits, pull requests)
url = f"https://api.github.com/users/{username}/events/public"

# Send a GET request to the GitHub API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    events = response.json()

    # Count the number of commits (PushEvent type indicates commits)
    commit_count = len([event for event in events if event['type'] == 'PushEvent'])

    # Determine the rank based on commit count
    if commit_count > 100:
        rank = "R"  # Rank R for >100 commits
    elif commit_count > 50:
        rank = "B"  # Rank B for >50 commits
    else:
        rank = "Z"  # Rank C for <=50 commits

    print(f"Your GitHub activity rank: {rank}")
else:
    print("Failed to fetch data from GitHub API")
