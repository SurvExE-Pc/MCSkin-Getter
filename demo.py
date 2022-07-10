from skin import getSkinUrl
import subprocess
def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

skin=input("Username:\n")
url=getSkinUrl(skin)
print(f"{skin}'s skin is on this url: {url}.")
copy2clip(url)
