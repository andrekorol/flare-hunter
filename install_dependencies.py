import os
import shutil

repo_name = "pycallisto"
if os.path.isdir(repo_name):
    shutil.rmtree(repo_name)

repo_url = f"https://github.com/andrekorol/{repo_name}.git"
clone_cmd = f"git clone {repo_url}"
os.system(clone_cmd)
top_dir = os.getcwd()
os.chdir(repo_name)
os.system(f"python setup.py install")
os.chdir(top_dir)
shutil.rmtree(repo_name)
