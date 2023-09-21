#!/usr/bin/python3

import subprocess
import requests
import os
import random

TOKEN = os.getenv('GITHUB_TOKEN')
REPO_OWNER = 'umerm64'
REPO_NAME = 'HelloWorld'
BASE_BRANCH = 'main'
HEAD_BRANCH = str(random.randint(0, 1000)) + '-patch-' + str(random.randint(0, 1000))
PR_TITLE = 'quantum testing'
PR_BODY = 'quantum testing'

# Step 0: Append a line to readme.md
new_line = 'This is the appended line.\t' + str(random.randint(0, 1000))
with open('readme.md', 'a') as file:
    file.write(new_line)
    file.close()

# Step 1: Commit changes
commit_message = 'patch'
subprocess.check_call(['git', 'add', '-A'])
subprocess.check_call(['git', 'commit', '-m', commit_message])

# Step 2: Push changes to GitHub
remote_name = 'origin'
subprocess.check_call(['git', 'push', remote_name, HEAD_BRANCH])

# Step 3: Open a Pull Request
headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

data = {
    'title': PR_TITLE,
    'body': PR_BODY,
    'head': HEAD_BRANCH,
    'base': BASE_BRANCH
}

response = requests.post(
    f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls',
    headers=headers,
    json=data
)

if response.status_code == 201:
    print(f'Pull request created successfully: {response.json()["html_url"]}')
else:
    print(f'Failed to create pull request. Status code: {response.status_code}. Response: {response.text}')
