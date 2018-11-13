from flask import Flask

import logging as logger

logger.basicConfig(level="DEBUG")

appInstance = Flask(__name__)

# In Dubug mode
if __name__ == '__main__':
    logger.debug("Start Application..")
    from api import *
    appInstance.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
