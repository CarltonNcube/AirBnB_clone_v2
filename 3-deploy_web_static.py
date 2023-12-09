#!/usr/bin/python3
# Fabfile to create and distribute an archive to web servers.
from fabric.api import env, local, run
from datetime import datetime
from os.path import isfile
from pathlib import Path

env.hosts = ["54.173.251.99", "52.91.125.177"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/0-use_a_private_key"

def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
    )
    if not Path("versions").is_dir():
        local("mkdir -p versions")
    result = local("tar -cvzf {} web_static".format(file))
    return file if result.succeeded else None

def do_deploy(archive_path):
    """Distribute an archive to web servers.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not isfile(archive_path):
        return False

    file = Path(archive_path).name
    name = file.split(".")[0]

    remote_tmp = "/tmp/{}".format(file)
    remote_release = "/data/web_static/releases/{}/".format(name)

    try:
        local("fab -f 2-do_deploy_web_static.py do_deploy:archive_path={}"
              .format(archive_path))
        return True
    except Exception as e:
        print(e)
        return False

def deploy():
    """Create and distribute an archive to web servers."""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
