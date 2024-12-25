'''
https://www.showapi.com/news/article/66e99c9c4ddd79f11a0c4f43
可以参考链接内容，生成repos.txt文件，以完成批量下载
'''

from git import Repo
import os, shutil, sys

path = './repos.txt'

with open(path, 'r') as f:
    repos = f.readlines()

num = len(repos)
for i, repo in enumerate(repos):
    repo = repo.strip()
    print(i+1, num)
    print(f'Downloading {repo}...')
    Repo.clone_from(repo, os.path.basename(repo))
print('All repos downloaded!')
