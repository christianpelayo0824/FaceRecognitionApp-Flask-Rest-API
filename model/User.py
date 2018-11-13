from config.DatabaseConfig import Connection
from flask import jsonify

import pymysql
import logging as logger


class User:
    conn = Connection()
    db = conn.get_connection()

    def get_all_user(self):
        try:
            cursor = self.db.cursor(pymysql.cursors.DictCursor)
            cursor.execute('SELECT * FROM employee')
            data = cursor.fetchall()
        except Exception as e:
            logger.debug("Failed to Fetch" + str(e))
        finally:
            cursor.close()
        return data

    def get_user_by_id(self, id):
        try:
            cursor = self.db.cursor(pymysql.cursors.DictCursor)
            cursor.execute('SELECT * FROM employee where empid = ' + str(id))
            data = cursor.fetchone()
        except Exception as e:
            logger.debug('Error: ' + str(e))
        finally:
            cursor.close()
        return data

    def delete_user(self, id):
        try:
            cursor = self.db.cursor()
            cursor.execute('DELETE FROM employee WHERE empid = ' + str(id))
            self.db.commit()
            data = jsonify({
                'message': 'Deleted Succesfully'
            })
        except Exception as e:
            logger.debug('Error: ' + str(e))
        finally:
            cursor.close()
        return data
