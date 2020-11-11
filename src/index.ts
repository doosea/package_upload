import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { requestAPI } from './api';

/**
 * Initialization data for the package_upload extension.
 */
const extension: JupyterFrontEndPlugin<void> = {
  id: 'package-upload',
  autoStart: true,
  activate: async (app: JupyterFrontEnd) => {
    console.log('JupyterLab extension package-upload is activated!');

    // GET request
    try {
      const data = await requestAPI<any>('package_upload');
      console.log(data);
      console.log('现在进行get请求');
    } catch (reason) {
      console.error(`Error on GET /jlab-ext-example/hello.\n${reason}`);
    }
  }
};

export default extension;
