from flaskext.mysql import MySQL

import logging as logger

from app import appInstance


class Connection:
    conn = None

    def get_connection(self):
        try:
            mysql = MySQL()
            appInstance.config['MYSQL_DATABASE_USER'] = 'root'
            appInstance.config['MYSQL_DATABASE_PASSWORD'] = ''
            appInstance.config['MYSQL_DATABASE_DB'] = 'employee_monitoring'
            appInstance.config['MYSQL_DATABASE_HOST'] = 'localhost'
            mysql.init_app(appInstance)
            self.conn = mysql.connect()
            logger.debug("Connection Established")
        except Exception as e:
            logger.debug("Connection Failed" + str(e))

        return self.conn
