import os

from github import Github, Auth

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

auth = Auth.Token(GITHUB_TOKEN)
g = Github(auth=auth)

repo = g.get_repo("spring-projects/spring-framework")
print(f"対象リポジトリ:{repo.full_name}")
print("=" * 30)

print("Pull requests status")
print("=" * 30)
pulls = repo.get_pulls(state='all', sort='created', direction='desc')

total_prs = 0
merged_prs = 0
rejected_prs = 0
open_prs = 0

for pr in pulls[:100]:
    total_prs += 1

    if pr.state == 'open':
        open_prs += 1
    elif pr.merged:
        merged_prs += 1
    elif pr.state == 'closed'and not pr.merged:
        rejected_prs += 1

print(f"取得総数: {total_prs}件")
print(f" - 審査中(open): {open_prs}件")
print(f" - マージ済み(Merged):{merged_prs}件")
print(f" - 却下(Rejected):{rejected_prs}件")
print("=" * 30)


print("Github actions status")
print("=" * 30)
runs = repo.get_workflow_runs()

total_runs = 0
success_runs = 0
failure_runs = 0
other_runs = 0

for run in runs[:100]:
    total_runs += 1

    if run.conclusion == 'success':
        success_runs += 1
    elif run.conclusion == 'failure':
        failure_runs += 1
    else:
        other_runs += 1

print(f"取得総数: {total_runs}件")
print(f" - 成功 (success): {success_runs}件")
print(f" - 失敗 (Failuer):{failure_runs}件")
print(f" - その他 (other):{other_runs}件")


