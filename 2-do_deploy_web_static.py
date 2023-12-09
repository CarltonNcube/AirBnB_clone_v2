#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os.path
from fabric.api import env, put, run

env.hosts = ["54.173.251.99", "52.91.125.177"]


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if not os.path.exists(archive_path):
        return False

    file = os.path.basename(archive_path)
    name = os.path.splitext(file)[0]

    # Upload the archive to /tmp/ directory of the web server
    if put(archive_path, f"/tmp/{file}").failed:
        return False

    # Uncompress the archive to /data/web_static/releases/<archive filename without extension>
    if run(f"mkdir -p /data/web_static/releases/{name}/").failed:
        return False
    if run(f"tar -xzf /tmp/{file} -C /data/web_static/releases/{name}/").failed:
        return False

    # Delete the archive from the web server
    if run(f"rm /tmp/{file}").failed:
        return False

    # Delete the symbolic link /data/web_static/current from the web server
    if run("rm -rf /data/web_static/current").failed:
        return False

    # Create a new symbolic link /data/web_static/current on the web server
    if run(f"ln -s /data/web_static/releases/{name}/ /data/web_static/current").failed:
        return False

    return True

