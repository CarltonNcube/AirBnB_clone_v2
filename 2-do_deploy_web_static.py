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
    if not os.path.isfile(archive_path):
        return False

    file = os.path.basename(archive_path)
    name = os.path.splitext(file)[0]

    remote_tmp = "/tmp/{}".format(file)
    remote_release = "/data/web_static/releases/{}/".format(name)

    try:
        put(archive_path, remote_tmp)
        run("rm -rf {}".format(remote_release))
        run("mkdir -p {}".format(remote_release))
        run("tar -xzf {} -C {}".format(remote_tmp, remote_release))
        run("rm {}".format(remote_tmp))
        run("mv {}/web_static/* {}".format(remote_release, remote_release))
        run("rm -rf {}/web_static".format(remote_release))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(remote_release))
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
