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

    def union_insert(self, firstSql, secondSql):
        """
        连表插入-->第一个表的Id与第二张表关联
        :param firstSql: 
        :param secondSql: 其中关联表的Id用`{0}`替代
        :return: 
        """
        db = self.db
        cursor = db.cursor(pymysql.cursors.DictCursor)
        try:
            # 执行第一张主表的插入
            cursor.execute(firstSql)
            # 获取当前插入数据的Id
            currentId = cursor.lastrowid
            # 第二张表插入的sql
            secondSql = secondSql.format(currentId)
            # 将第一张表的Id放进第一张表中作为参数传递
            cursor.execute(secondSql)
            db.commit()

            a = True

        except Exception as e:

            db.rollback()

            a = e
        db.close()

        return a
