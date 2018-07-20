# coding = utf-8

'''

''''''
大家好，我是kevin。

我们的基础课更难的知识点已经全部讲完。接下来，是两道应用题。这两道应用题，多多少少都有些难度。第一道是文本题，第二道则是小游戏题。前者考知识点，后者考逻辑。前者偏坑爹（难），后者偏有趣（更难^_^），这两道应用题，会给大家足够的时间去思考，总结与回顾。

第一道题，是一道文本题。文件夹里有一个twitter数据挖掘的片段，每一行则是一个tweets（微博），里面有该微博的相关字段信息。
对应字段如下（每一个逗号分隔的，“”内的，则是字段的详细信息。空白则代表没有。）：
bid    消息ID 
uid     用户ID 
username 用户名  
ugrade 用户等级字段 
content(text) 微博内容
img(message包含图片链接) 
created_at 微博发布时间 
source(来源)
rt_num, 转发数 
cm_num, 评论数 
rt_uid, 转发UID
rt_username, 转发用户名
rt_v_class, 转发者等级 
rt_content, 转发内容 
rt_img, 转发内容所涉及图片 
src_rt_num, 源微博回复数 
src_cm_num, 源微博评论数 
gender,(用户性别) 
rt_mid（转发mid） 
geo 地区
lat() 经度
lon 纬度
place 地点
hashtags 
ats  @谁 
rt_hashtags, 回复标签
rt_ats, 回复@谁
v_url, 源微博URL 
rt_v_url 转发URL 

twitter文本附件的排序格式如下

fields=bid,uid,username,v_class,content,img,time,source,rt_num,cm_num,rt_uid,rt_username,rt_v_class,rt_content,rt_img,src_rt_num,src_cm_num,gender,rt_mid,location,rt_mid,mid,lat,lon,lbs_type,lbs_title,poiid,links,hashtags,ats,rt_links,rt_hashtags,rt_ats,v_url,rt_v_url

而童鞋们，则需要利用自己已经掌握的知识，对其进行一个基本的文本分析。


注意：请用utf-8格式打开此文件。

要求如下：
'''
import linecache
import time

data_keys = (
'bid', 'uid', 'username', 'v_class', 'content', 'img', 'created_at', 'source', 'rt_num', 'cm_num', 'rt_uid',
'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 'src_rt_num', 'src_cm_num', 'gender', 'rt_bid', 'location',
'rt_mid', 'mid', 'lat', 'lon', 'lbs_type', 'lbs_title', 'poiid', 'links', 'hashtags', 'ats', 'rt_links', 'rt_hashtags',
'rt_ats', 'v_url', 'rt_v_url')
keys = {data_keys[k]: k for k in range(0, len(data_keys))}
# print(keys)

twitter_line = linecache.getlines('twitter.txt')
twitter_lines = [x[1:-1].split('","') for x in twitter_line]
# print(twitter_lines[0:2])

print("1.该文本里，有多少个用户。（要求：输出为一个整数。）")
users = set([line[1] for line in twitter_lines])
users_total = len(users)
assert type(users_total) == int
print("user_total:%s" % users_total)

print("2.该文本里，每一个用户的名字。 （要求：输出为一个list。）")
users_name = set([line[2] for line in twitter_lines])
assert type(list(users_name)) == list
# print(list(users_name))
print("\n")

print("3.该文本里，有多少个2012年11月发布的tweets。 （要求：输出为一个整数。提示：请阅读python的time模块）")
line_from_2012_11 = list(filter(lambda line: line[keys['created_at']].startswith('2012-11'), twitter_lines))
line_total_from_2012_11 = len(line_from_2012_11)
print(line_total_from_2012_11)
print("\n")

print("4.该文本里，有哪几天的数据？ （要求：输出为一个list，例：['2012-03-04','2012-03-05']）")
total_days = [line[keys['created_at']].split(' ')[0] for line in twitter_lines]
lines_by_create = list(set(total_days))
lines_by_create.sort()
assert type(lines_by_create) == list
# print(lines_by_create)
print("\n")

print("5.该文本里，在哪个小时发布的数据最多？ （要求：输出一个整数。）")
hour = [int(x[keys['created_at']][11:13]) for x in twitter_lines]
total_by_hour = [(h, hour.count(h)) for h in range(0, 24)]
total_by_hour.sort(key=lambda k: k[1], reverse=True)
max_hour = total_by_hour[0][0]
assert type(max_hour) == int
print(max_hour)
print("\n")

print("6.该文本里，输出在每一天发表tweets最多的用户。（要求：输出一个字典。例如 {'2012-03-04':'agelin','2012-03-5':'twa'}）")
dateline_by_user = {k: dict() for k in lines_by_create}
for line in twitter_lines:
    dateline = line[keys['created_at']].split(' ')[0]
    username = line[keys['username']]
    if dateline_by_user[dateline].__contains__(username):
        dateline_by_user[dateline][username] += 1
    else:
        dateline_by_user[dateline][username] = 1

# print(dateline_by_user)
for k, v in dateline_by_user.items():
    us = list(v.items())
    us.sort(key=lambda k: k[1], reverse=True)
    # dateline_by_user[k] = {us[0][0]:us[0][1]}
    dateline_by_user[k] = us[0][0]
print(dateline_by_user)

print("7. 请按照时间顺序输出 2012-11-03 每个小时的发布tweets的频率（要求：输出为一个list [(1,20),(2,30)] 代表1点发了20个tweets，2点发了30个tweets）")
dateline_by_2012_11_03 = list(filter(lambda line: line[keys['created_at']].startswith('2012-11-03'), twitter_lines))
hours_by_2012_11_03 = {str(i): 0 for i in range(0, 24)}
for line in dateline_by_2012_11_03:
    hours = line[keys['created_at']][11:13]
    hours_by_2012_11_03[str(int(hours))] += 1
# print(hours)
hour_timeline_from_2012_11_03 = [(k, v) for k, v in hours_by_2012_11_03.items()]
hour_timeline_from_2012_11_03.sort(key=lambda k: int(k[0]))
print(hour_timeline_from_2012_11_03)

print("8. 统计该文本里，来源的相关信息和次数，比如（输出一个list。例如[('Twitter for Android',1),('TweetList!',1)]）")
source = set([k[keys['source']] for k in twitter_lines])
source_dirc = {s: 0 for s in source}
for line in twitter_lines:
    source_line = line[keys['source']]
    source_dirc[source_line] += 1
source_list = [(k, v) for k, v in source_dirc.items()]
source_list.sort(key=lambda k: k[1], reverse=True)
print(type(source_list))

print("9. 计算转发URL中：以：'https://twitter.com/umiushi_no_uta'开头的有几个。(要求，输出一个整数。)")
total_rt_v_url = 0
for line in twitter_lines:
    if line[keys['rt_v_url']].startswith('https://twitter.com/umiushi_no_uta'):
        total_rt_v_url += 1
print(total_rt_v_url)

print("10. UID为573638104的用户 发了多少个微博 （要求：输出一个整数）")
uid_57 = 0
for line in twitter_lines:
    if line[keys['uid']] == '573638104':
        uid_57 += 1
print(uid_57)

print("11. 定义一个函数，该函数可放入任意多的用户uid参数（如果不存在则返回null），函数返回发微薄数最多的用户uid。")


def get_user_by_max_tweers(*uids):
    '''
    @deprecated: 参数可为任意字符串或数字
    '''
    if len(uids) > 0:
        uids = list(filter(lambda u: type(u) == int or u.isdigit(), uids))
        all_uid_bid = {k: 0 for k in uids}
        for line in twitter_lines:
            uid = line[keys['uid']]
            if uid in uids:
                all_uid_bid[uid] += 1
        all_uid_bid_list = [(k, v) for k, v in all_uid_bid.items()]
        all_uid_bid_list.sort(key=lambda k: k[1], reverse=True)
        print(all_uid_bid_list)
        return all_uid_bid_list
    else:
        return "null"


# get_user_by_max_tweers('127202a4619', '128750960', '631977040', '596099558', '727599906', '187569243', '297121262')
get_user_by_max_tweers()

print("12. 该文本里，谁发的微博内容长度最长 （要求：输出用户的uid，字符串格式。）")
max_contenx = 0
uid_content_length = [(line[keys['uid']], len(line[keys['content']])) for line in twitter_lines]
uid_content_length.sort(key=lambda k: k[1], reverse=True)
i = 0
while i <= len(uid_content_length):
    length1 = uid_content_length[i][1]
    i += 1
    length2 = uid_content_length[i][1]
    if length2 < length1:
        print(uid_content_length[0:i])
        break

print("13. 该文本里，谁转发的URL最多 （要求：输出用户的uid，字符串格式。）")

'''
14. 该文本里，11点钟，谁发的微博次数最多。 （要求：输出用户的uid，字符串格式。）

15. 该文本里，哪个用户的源微博URL次数最多。 （要求：输出用户的uid，字符串格式。）
'''
