# -*-coding:utf-8-*-
import pymysql
# import pytesseract

from PIL import Image
from config.conf import host, port, user, passwd, db, charset

class Mysql():
    def __init__(self):
        # 打开数据库连接
        self.db = pymysql.connect(
            host='175.178.2.78',
            port = 3306,
            user = 'root',
            passwd = 'mogu2018',
            db = 'courses_seleting_sys',
            charset = 'utf8',
            # host = host,
            # port = port,
            # user = user,
            # passwd = passwd,
            # db = db,
            # charset = charset
        )
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()

    # def getData(self):
    #     # 使用 cursor() 方法创建一个游标对象 cursor
    #     db = self.db
    #     cursor = self.cursor
    #     sql = "SELECT id,order_st,book_password,begin_prov,begin_city,begin_area,begin_addr_detail,end_prov,end_city,\
    #             end_area,end_addr_detail,price,amount,sender_name,sender_tel,receiver_tel,wl_moto,insurance,\
    #             is_weight,is_load,self_send,self_receive,had_password,st_del,pay_way FROM book"
    #     try:
    #         # 执行sql语句
    #         cursor.execute(sql)
    #         # 提交到数据库执行
    #         db.commit()
    #         # 获取所有记录列表
    #         dataName = ["id","order_st","book_password","begin_prov","begin_city","begin_area","begin_addr_detail","end_prov","end_city",\
    #             "end_area","end_addr_detail","price","amount","sender_name","sender_tel","receiver_tel","wl_moto","insurance",\
    #             "is_weight","is_load","self_send","self_receive","had_password","st_del","pay_way"]
    #         results = cursor.fetchall()
    #         data = []
    #         for row in results:
    #             index = {}
    #             for i in range(len(dataName)):
    #                 index[dataName[i]] = row[i]
    #             data.append(index)
    #         return data
    #
    #     except:
    #         print("Error: unable to fecth data")
    #     # 关闭数据库连接
    #     db.close()

    def sql(self,sql):
        db = self.db
        cursor = self.cursor
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            # 获取所有记录列表
            results = cursor.fetchall()
            return results
        except:
            print("Error: unable to fecth data")
            db.rollback()
        # 关闭数据库连接
        db.close()


    def sql2(self,sql,courseID):
        db = self.db
        cursor = self.cursor
        try:
            # 执行sql语句
            cursor.execute(sql,(courseID))
            # 提交到数据库执行
            db.commit()
            # 获取所有记录列表
            results = cursor.fetchall()
            return results
        except:
            print("Error: unable to fecth data")
            db.rollback()
        # 关闭数据库连接
        db.close()

if __name__ == '__main__':
    # sql = "select max(upload_date) from t_homework where update_user_id in (select id from t_user where username = '201944101202')"
    # result = Mysql().sql(sql)[0][0]
    # print(result)
    # result.strftime('%Y-%m-%d %H:%M:%S')
    # print(result.strftime('%Y-%m-%d %H:%M:%S'))
    # text = pytesseract.image_to_string(Image.open('python.png'),lang='chi_sim')
    # print(text)
    pass
