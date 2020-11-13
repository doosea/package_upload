# -*- coding: utf-8 -*-

"""
@Time        : 2020/11/11
@Author      : dosea
@File        : __init__.py
@Description : 
"""
from ._version import __version__
from .handlers import setup_handlers


# 提供python 包名给server
def _jupyter_server_extension_paths():
    return [{"module": "package_upload"}]


# 注册新的handlers
def load_jupyter_server_extension(lab_app):
    """Registers the API handler to receive HTTP requests from the frontend extension.
    Parameters
    ----------
    lab_app: jupyterlab.labapp.LabApp
        JupyterLab application instance
    """
    url_path = "package_upload"
    setup_handlers(lab_app.web_app, url_path)
    lab_app.log.info(
        "Registered package_upload extension at URL path /{}".format(url_path)
    )
