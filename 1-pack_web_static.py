#!/usr/bin/python3
# Fabfile to generate a .tgz archive from the contents of web_static.
import os.path
from datetime import datetime
from fabric.api import local, settings


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
            dt.month, dt.day, dt.hour, dt.minute, dt.second)

    # Ensure the versions directory exists
    with settings(warn_only=True):
        local("mkdir -p versions")

    # Create the .tgz archive
    result = local("tar -cvzf {} web_static".format(file))

    if result.failed:
        return None

    return file
