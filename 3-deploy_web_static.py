#!/usr/bin/python3
from fabric.api import env
from os.path import exists
from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy

env.hosts = ['3.85.110.215', '34.238.38.171']

def deploy():
    archive = do_pack()
    if not archive:
        return False
    return do_deploy(archive)
