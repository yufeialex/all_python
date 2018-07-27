from alva.dao.MonodbDao import MongoDbBase


def find():
    mongo = MongoDbBase()
    a = {'video_id': '100.mp4'}
    b = mongo.find_one_data('action_rec_middle_file', a)
    print(b)


if __name__ == '__main__':
    find()
