#コミットメッセージ: commit.message
#コミット作成日: commit.committed_datetime
#変更ファイル: commit.stats.files （ファイルごとの詳細）
#変更行数: commit.stats.total （全体の追加・削除行数）

import os
from email import message

from git import Repo

repo_url = "https://github.com/apache/commons-math"
local_dir = "./commons-math-clone"

if os.path.exists(local_dir):
    print("ローカルに存在するため、ローカルデータを読み込みます")
    repo = Repo(local_dir)

else:
    print(f"'{repo_url}'を'{local_dir}'にクローンしています")
    repo = Repo.clone_from(repo_url, local_dir)
    print("クローンが完了しました")

print("=" * 50)

commits = list(repo.iter_commits(max_count=10))
for commit in commits:
    date = commit.committed_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f"作成日:{date}")

    message = commit.message
    print(f"メッセージ:{message}")

    change_files = list(commit.stats.files.keys())
    if len(change_files) > 3:
        print(f"変更ファイル:{change_files[:3]} ...他{len(change_files)-3}件")
    else:
        print(f"変更ファイル:{change_files}")

    stats = commit.stats.total
    print(f"変更ファイル数:{stats['files']}")
    print(f"変更行数:{stats['lines']} 行 (追加: {stats['insertions']}, 削除: {stats['deletions']})")

    print("=" * 50)
