# -*- coding: utf-8 -*-

"""
@Time        : 2020/11/11
@Author      : dosea
@File        : main
@Description : 
"""
import re
import sys

from jupyterlab.labapp import main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
