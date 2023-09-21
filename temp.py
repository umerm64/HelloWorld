import requests as req

res = req.post(url="https://api.breu.ngrok.io/providers/github/artifact-ready", data={
            "pull_request_id": "1524366665",
            "image": "asia-southeast1-docker.pkg.dev/breu-dev/ctrlplane/helloworld:latest",
            "repo_id": "690461443",
            "registry": "GCPArtifactRegistry",
            "digest": "sha256:c7b06c949658f325997f1184b6a2dd1e1f1da29a12d7d18b574fcaeafced76d8",
            "installation_id": "41716466"
        })
if (res.status_code == 200):
    print("artifacts pushed", res.content)
else:
    print("error in pushing artifacts", res.status_code, res.content)

