#! /usr/bin/python3.6

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/test_system/server/')
from main import app as application
application.secret_key = '1289ehwdfsb9843tbfv'
