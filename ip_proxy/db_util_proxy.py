'''
操作数据库表ip_Proxy的工具类
'''
import pymysql

def insertOne(proxy,delay):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "bhy980226275", "kyc_server")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # SQL 插入语句
    sql = "insert into ip_proxy(proxy,create_time,delay) VALUES (%s,now(),%s)"
    try:
        # 执行sql语句
        cursor.execute(sql,(proxy,delay))
        # 执行sql语句
        db.commit()
        print("数据保存成功")
    except Exception as e:
        # 发生错误时回滚
        db.rollback()
        print(e)

    # 关闭数据库连接
    db.close()

def find_all_proxy():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "bhy980226275", "kyc_server")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "select proxy from ip_proxy"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        result = cursor.fetchall()
        print("数据查询成功")
        return result
    except Exception as e:
        # 发生错误时回滚
        db.rollback()
        print(e)
    # 关闭数据库连接
    db.close()

def delete_by_proxy(proxy):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "bhy980226275", "kyc_server")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "delete from ip_proxy where proxy = '" + proxy + "'"
    try:
        # 执行sql语句
        cursor.execute(sql)
        db.commit()
        print("数据删除成功:"+proxy)
    except Exception as e:
        # 发生错误时回滚
        db.rollback()
        print(e)
    # 关闭数据库连接
    db.close()

# insertOne("1.1.1.1","2s")
# delete_by_proxy("1.1.1.1")