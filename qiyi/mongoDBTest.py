import datetime  # 引入time模块

from alva.dao.MonodbDao import MongoDbBase


# mongoDB中插入python的dict对象的时候，字段值是None是没有问题的
def mongo_test():
    db_res = {'tt': datetime.datetime.now(),
              "job_id": 'vhs-job-id123',
              "qipu_id": '1181511500',
              "res": None}
    db_res['highlight_score'] = None
    mongo = MongoDbBase()
    mongo.insert_one_data('basic_data_highlight_score', db_res)
    if db_res is not None:
        print("hh")
    else:
        print("ss")


if __name__ == '__main__':
    mongo_test()
