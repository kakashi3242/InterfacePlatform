import pymysql


class Database:
    def __init__(self):
        self.db = pymysql.connect(
            db = 'interface',
            user = 'root',
            passwd = '123456',
            # passwd = '123456789', # 本地
            # host = 'localhost',
            host = '192.168.20.43',
            # host = '192.168.20.101',
            port = 3306,
            charset = 'utf8'
        )

    def query(self, sql):
        """
        数据库查询
        :param sql: 查询sql
        :return: 查询结果
        """
        db = self.db
        cursor = db.cursor(pymysql.cursors.DictCursor)

        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        # print(result)
        # 关闭游标
        cursor.close()
        # 关闭连接
        db.close()

        return result

    def insert(self, sql):
        """
        数据库插入
        :param sql: 
        :return: 
        """
        db = self.db
        cursor = db.cursor(pymysql.cursors.DictCursor)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

        db.close()

    def test_insert(self, sql):
        """
        数据库插入
        :param sql: 
        :return: 
        """
        db = self.db
        cursor = db.cursor(pymysql.cursors.DictCursor)
        try:
            cursor.execute(sql)
            lastId = cursor.lastrowid
            db.commit()
        except Exception as e:
            lastId = e
            db.rollback()

        db.close()

        return lastId