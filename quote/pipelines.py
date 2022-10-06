# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
import pymysql

class QuotePipeline:
    # 初始化
    def __init__(self):
        # 连接到MySQL数据库
        self.connect = pymysql.connect(
            # 主机名
            host='localhost',
            # 用户名
            user='root',
            # 密码
            password='123456',
            # 数据库
            database='quote',
            # # 数据库编码
            charset='utf8mb4',
        )
        #将cursor改为cursor()
        self.cursor = self.connect.cursor()

    # 处理每一条数据
    def process_item(self, item, spider):
        #将单引号转译
        text = "'"+item.get('text', "").replace("'","\\'")+"'"''
        author = "'"+item.get('author', "").replace("'","\\'")+"'"
        tags = "'"+item.get('tags', "")+"'"
        author_born_date = "'"+item.get('author_born_date', "").replace("'", "\\'")[2:]+"'"
        author_born_location = "'"+item.get('author_born_location', "").replace("'", "\\'")+"'"
        author_description = "'" + item.get('author_description', "").replace("'", "\\'") + "'"

        # 构造SQL语句
        sql = 'insert into quote (text,author,tags,author_born_date,author_born_location,author_description) ' \
              'values(%s, %s, %s, %s, %s, %s)' % (text, author, tags, author_born_date, author_born_location, author_description)

        try:
            self.cursor.execute(sql)
            self.connect.commit()
            print("Success!")
        # except:
        except Exception as e:
            # ... PRINT THE ERROR MESSAGE ... #
            print("Failed!", e)
            self.connect.rollback()
        return item

    # 关闭爬虫
    def close_spider(self, spider):
        # 关闭连接
        self.connect.close()
