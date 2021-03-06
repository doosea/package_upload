import os
import json
from pathlib import Path

from notebook.base.handlers import APIHandler
from notebook.utils import url_path_join, url2path

import tornado
from tornado.web import StaticFileHandler


class RouteHandler(APIHandler):
    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server
    @tornado.web.authenticated
    def get(self):
        self.finish(json.dumps({"data": "This is /package_upload/hello endpoint!"}))

    @tornado.web.authenticated
    def post(self):
        # input_data is a dictionnary with a key "name"
        input_data = self.get_json_body()
        data = {"greetings": "Hello {}, enjoy JupyterLab!".format(input_data["name"])}
        self.finish(json.dumps(data))

    '''
        路径由前端传入：
         // Use the current path
        cwd = browserFactory.defaultBrowser.model.path;
    '''
    @tornado.web.authenticated
    def put(self):
        # input_data is a dictionnary with a key "path"
        input_data = self.get_json_body()
        path = input_data.get("path", "")
        realpath = self._get_realpath(path)
        print(realpath)
        data = {"realpath": str(realpath)}
        self.finish(json.dumps(data))

    def _get_realpath(self, path: str) -> Path:
        """Tranform notebook path to absolute path.

        Args:
            path (str): Path to be transformed

        Returns:
            Path: Absolute path
        """
        return Path(self.contents_manager.root_dir).absolute() / url2path(path)

def setup_handlers(web_app, url_path):
    host_pattern = ".*$"
    base_url = web_app.settings["base_url"]

    # Prepend the base_url so that it works in a jupyterhub setting
    route_pattern = url_path_join(base_url, url_path, "hello")
    handlers = [(route_pattern, RouteHandler)]
    web_app.add_handlers(host_pattern, handlers)

    # Prepend the base_url so that it works in a jupyterhub setting
    doc_url = url_path_join(base_url, url_path, "static")
    doc_dir = os.getenv(
        "JLAB_SERVER_EXAMPLE_STATIC_DIR",
        os.path.join(os.path.dirname(__file__), "static"),
    )
    handlers = [("{}/(.*)".format(doc_url), StaticFileHandler, {"path": doc_dir})]
    web_app.add_handlers(".*$", handlers)
