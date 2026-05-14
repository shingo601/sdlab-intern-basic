import os
from datetime import datetime, timedelta, timezone

import matplotlib.pyplot as plt
from github import Github, Auth

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

auth = Auth.Token(GITHUB_TOKEN)
g = Github(auth=auth)

repo = g.get_repo("spring-projects/spring-framework")

print(f"対象リポジトリ: {repo.full_name}")
print("-" * 30)

one_week_ago = datetime.now(timezone.utc) - timedelta(days=7)

daily_counts = {}

issues = repo.get_issues(state='all', since=one_week_ago)

for issue in issues:
    if issue.pull_request is not None:
        continue

    date_str = issue.created_at.strftime("%Y-%m-%d")

    if date_str in daily_counts:
        daily_counts[date_str] += 1
    else:
        daily_counts[date_str] = 1

for date, count in sorted(daily_counts.items()):
    print(f"{date}: {count}")

sorted_dates = sorted(daily_counts.keys())
counts = [daily_counts[date] for date in sorted_dates]

plt.figure(figsize=(10,5))
# align ではなく color に修正
plt.bar(sorted_dates, counts, color='skyblue')
plt.title("Daily Issue Counts (Last 7 days)")
plt.xlabel("Date")
plt.ylabel("Number of issues")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()