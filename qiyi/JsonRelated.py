import json, os

if __name__ == '__main__':
    # data = '{"task_id":"1","video_url":"http://cdn-proxy.qiyi.domain/videos/v0/20171027/e7/ad/9aff7283f8af78dcb5d35c5243a2d292.f4v"}'
    # data = json.loads(data)

    # aa = os.listdir("D:")
    # print(aa)

    file = "/data/2.f4v"
    cmd = 'ffmpeg -i {} -c copy -y {}.ts'.format(file, os.path.splitext(file)[0])
    print(cmd)
