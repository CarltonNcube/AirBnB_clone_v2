#!/usr/bin/python3
"""
Fabric script that distributes an archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ["54.173.251.99", "52.91.125.177"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/0-use_a_private_key"


def do_deploy(archive_path):
    """Distributes an archive to the web servers."""
    if not exists(archive_path):
        print(f"Error: Archive file {archive_path} does not exist.")
        return False

    try:
        # Extract filename and name without extension
        file_name = archive_path.split("/")[-1]
        name_no_ext = file_name.split(".")[0]

        # Set up path
        path = "/data/web_static/releases/"

        # Upload the archive to /tmp/
        put(archive_path, '/tmp/')

        # Create a new release directory
        run('mkdir -p {}{}/'.format(path, name_no_ext))

        # Extract the contents of the archive to the new release directory
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, name_no_ext))

        # Remove the uploaded archive from /tmp/
        run('rm /tmp/{}'.format(file_name))

        # Move contents to the release directory
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, name_no_ext))

        # Remove unnecessary web_static directory
        run('rm -rf {}{}/web_static'.format(path, name_no_ext))

        # Remove the current symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('ln -s {}{}/ /data/web_static/current'.format(path, name_no_ext))

        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Error during deployment: {e}")
        return False
