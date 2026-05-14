import os

from github import Github, Auth

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

auth = Auth.Token(GITHUB_TOKEN)

g = Github(auth=auth)

queries = [
    {"title": "全体", "query": "stars:>1"},
    {"title": "Java", "query": "language:java stars:>1"},
    {"title": "Python", "query": "language:python stars:>1"}
]

for q in queries:
    print(f"=== {q['title']} 上位10位 ===")

    repositories = g.search_repositories(query=q["query"], sort="stars", order="desc")

    for repo in repositories[:10]:
        print(f"リポジトリ名: {repo.full_name}")
        print(f"スター数: {repo.stargazers_count}")

        try:
            commits = repo.get_commits()
            print(f"総コミット数: {commits.totalCount}")
        except Exception as e:
            print("コミットが取得できませんでした")

        print("-" * 30)
    print("\n")