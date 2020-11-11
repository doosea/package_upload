#　jupyterlab 插件开发

[Extension Developer Guide](https://jupyterlab.readthedocs.io/en/stable/developer/extension_dev.html)

##　简单示例
需要的环境：　miniconda

1. 创建conda虚拟环境 `jupyterlab-ext`, 并按装相应的包

    - `conda create -n jupyterlab-ext --override-channels --strict-channel-priority -c conda-forge -c anaconda jupyterlab cookiecutter nodejs git`
    - `conda activate jupyterlab-ext`
2.  新建一个 git 仓库

3. 使用`cookiecutter` 创建模板项目
    
    - `cookiecutter https://github.com/jupyterlab/extension-cookiecutter-ts`
    
4. build 并按装 自己的插件

   - `jlpm install` : 
   - `jupyter labextension install . --no-build` : 安装但是不build 
  
5. 查看自己的服务
    
    - `jupyter lab --watch` : 浏览器默认自动开启 `jupyterlab` 服务
    - 打开 google 浏览器的开发者工具，查看console, 会显示：`JupyterLab extension jupyterlab_apod is activated!`
 
6. terminal按两次 `ctrl + c`, 关掉jupyterlab服务
 
7. 本地初始化仓库，连接远程仓库
    
    - git remote add origin "xxx.git"    
    - git init
    - git add .
    - git commit -m "init rep"
    - git push origin master
8.  编译与查看
    - jlpm run build
    - jlpm run watch
    - jupyter lab build
    - jupyter lab 