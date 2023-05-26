#1.access_gitlab.py

import gitlab

gitlab_url = "https://gitlab.com"

api_key = "glpat-aUnzEnxbEXfq2n-YrcHf"
gl = gitlab.Gitlab(gitlab_url, private_token=api_key)  #session=True

group_path = "group12153421"
group = gl.groups.get(group_path)

repositories = group.projects.list(all=True)
for repo in repositories:
    print(repo.get_id())
#projects = gl.projects.get(id=44292581)
#file = projects.files.get("RahulS141999/clusterrole-crb", ref= "main")
#print(projects.file)


#'RahulS141999/clusterrole-crb'
'''import requests

gitlab_url =  "https://gitlab.com/dashboard/projects"
api_key = "glpat-aUnzEnxbEXfq2n-YrcHf"

headers = { "private-token": api_key}

response = requests.get(gitlab_url + "projects", headers = headers)

if response.status_code == 200:
    projects = response.json()
    for project in projects:
        print(project["name"])
else:
    print("Error:", response.text)'''

#for github github_login.py

from github import Github

api_key = "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"
g =Github(api_key)

user = g.get_user()
repositories = user.get_repos()

for repo in repositories:
    print(repo.full_name)




