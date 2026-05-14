import os

from github import Github, Auth, UnknownObjectException

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

auth = Auth.Token(GITHUB_TOKEN)

g = Github(auth=auth)

user = g.get_user()
print(f"user: {user.login}")
print("=" * 30)

for repo in user.get_repos():
    print(f"repo: {repo.name}")
    print(f"stars: {repo.stargazers_count}")

    try:
        commits = repo.get_commits()
        print(f"total commits: {commits.totalCount}")
    except Exception as e:
        print("コミットが取得できませんでした")

    print("_" * 30)