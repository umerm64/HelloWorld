#!/usr/bin/python3

import subprocess
import requests
import os
import random
import time
import json

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
subprocess.check_call(['git', 'branch', '-M', HEAD_BRANCH])

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
    print(response.json()['id'])
    time.sleep(5)
    res = requests.post(url="https://api.breu.ngrok.io/providers/github/artifact-ready", data=json.dumps({
            "pull_request_id": response.json()['id'],
            "image": "asia-southeast1-docker.pkg.dev/breu-dev/ctrlplane/helloworld:latest",
            "repo_id": response.json()['head']['repo']['id'],
            "registry": "GCPArtifactRegistry",
            "digest": "sha256:c7b06c949658f325997f1184b6a2dd1e1f1da29a12d7d18b574fcaeafced76d8",
            "installation_id": "41716466"
        }), headers={'X-API-KEY': 'GQePYF4lZv1cbawJZHEhLG.ssHEsxZQjjaWFVQf0j6ceH.DtFb1fN8Wftssz85kfcmiet38ZFIntmDZ9F2klxdsKdd60Dntnd1uJ1gifJTlEsXc'}
    )
    if (res.status_code == 200):
        print(res.content)
    else:
        print(res.status_code)
else:
    print(f'Failed to create pull request. Status code: {response.status_code}. Response: {response.text}')
