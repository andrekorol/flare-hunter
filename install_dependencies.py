import os
import shutil

repositories = ["pycallisto", "urldl"]
for repo_name in repositories:
    if os.path.isdir(repo_name):
        shutil.rmtree(repo_name)
    repo_url = f"https://github.com/andrekorol/{repo_name}.git"
    clone_cmd = f"git clone {repo_url}"
    os.system(clone_cmd)
    top_dir = os.getcwd()
    os.chdir(repo_name)
    #  os.system("git checkout xticks")
    #  os.system("cat pycallisto/fitsread.py")
    os.system("python setup.py install")
    os.chdir(top_dir)
    shutil.rmtree(repo_name)
