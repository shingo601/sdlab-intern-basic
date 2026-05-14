import glob
import os
import subprocess
import xml
import xml.etree.ElementTree as ET
from git import Repo

local_dir = "./commons-math-clone"

print("リポジトリを読み込んでいます")
repo = Repo(local_dir)

latest_commit = next(repo.iter_commits(max_count=1))
print(f"チェックアウト実行:{latest_commit.hexsha}(作成日:{latest_commit.committed_datetime})")


repo.git.checkout(latest_commit.hexsha)
print("=" * 50)

result = subprocess.run(
    ["mvn","test"],
    cwd=local_dir,
)

report_dir = os.path.join(local_dir, "**", "target", "surefire-reports")
xml_files = glob.glob(os.path.join(report_dir, "TEST-*.xml"))

if not xml_files:
    print("XMLファイルが見つかりません")
else:
    print(f"見つかったXMLファイル数: {len(xml_files)}件")

    total_tests = 0
    total_failures = 0
    total_errors = 0
    total_skipped = 0

    for xml_file in xml_files:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        total_tests += int(root.attrib.get('tests', 0))
        total_failures += int(root.attrib.get('failures', 0))
        total_errors += int(root.attrib.get('errors', 0))
        total_skipped += int(root.attrib.get('skipped', 0))

    successes = total_tests - total_failures - total_errors - total_skipped

    print("=" * 40)
    print(f"総テスト実行数 : {total_tests}件")
    print(f"成功 : {successes}件")
    print(f"失敗 : {total_failures}件")
    print(f"エラー : {total_errors}件")
    print(f"スキップ: {total_skipped}件")










