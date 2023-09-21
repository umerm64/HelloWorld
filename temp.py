import requests as req
import json

res = req.post(url="http://localhost:8000/providers/github/artifact-ready", data=json.dumps({
            "pull_request_id": "1524366665",
            "image": "asia-southeast1-docker.pkg.dev/breu-dev/ctrlplane/helloworld:latest",
            "repo_id": "690461443",
            "registry": "GCPArtifactRegistry",
            "digest": "sha256:c7b06c949658f325997f1184b6a2dd1e1f1da29a12d7d18b574fcaeafced76d8",
            "installation_id": "41716466"
        }), headers={
            'X-API-KEY': 'GQePYF4lZv1cbawJZHEhLG.ssHEsxZQjjaWFVQf0j6ceH.DtFb1fN8Wftssz85kfcmiet38ZFIntmDZ9F2klxdsKdd60Dntnd1uJ1gifJTlEsXc',
            'Content-Type': 'application/json'
        }
    )
if (res.status_code == 200):
    print("artifacts pushed", res.content)
else:
    print("error in pushing artifacts", res.status_code, res.content)

