import json

import requests as requests

# 配置数据
__NS_sig3 = '必填'
__NS_sig3_origin = '必填'
headers = {
    'content-type': 'application/json',
    'cookie': '必填',
    'Referer': 'https://servicewechat.com/wx79a83b1a1e8a7978/609/page-frame.html'
}


# 获取个人信息
def getInfo(eid):
    url = f'https://wxmini-api.uyouqu.com/rest/wd/wechatApp/user/profile?__NS_sig3={__NS_sig3}&__NS_sig3_origin={__NS_sig3_origin}'
    data = {
        'eid': eid
    }
    res = requests.post(url, headers=headers, data=json.dumps(data))
    res = json.loads(res.content)
    print(res)


# 获取推荐数据列表
def getRecommend():
    url = f'https://wxmini-api.uyouqu.com/rest/wd/wechatApp/feed/recommend?__NS_sig3={__NS_sig3}&__NS_sig3_origin={__NS_sig3_origin}'
    data = {
        "count": 20,
        "portal": 1,
        "pageType": 2,
        "needLivestream": True,
        "pcursor": 21,
        "sourceFrom": 2,
    }
    res = requests.post(url, headers=headers, data=json.dumps(data)).content.decode('utf-8')
    res = json.loads(res)
    feeds = res['feeds']
    data_list = []

    for item in feeds:
        item = dict(item)
        temp = {
            'headUrl': item.get('headUrl'),  # 头像地址
            'forwardCount': item.get('forwardCount'),  # 关注次数
            'commentCount': item.get('commentCount'),  # 评论次数
            'likeCount': item.get('likeCount'),  # 点赞次数
            'viewCount': item.get('viewCount'),  # 播放次数
            'shareCount': item.get('shareCount'),  # 分享次数
            'kwaiId': item.get('kwaiId'),  # 快手ID
            'userId': item.get('userId'),  # 用户ID
            'photoId': item.get('photoId'),  # photo ID
            'userName': item.get('userName'),  # 用户名称
            'userSex': item.get('userSex'),  # 用户性别
            'caption': item.get('caption'),  # 说明
            'mainMvUrls': item.get('mainMvUrls')  # mv视频地址
        }
        print(temp)
        data_list.append(temp)

    return data_list


# 点赞
def like(userId, photoId, cancel=0):
    url = f'https://wxmini-api.uyouqu.com/rest/wd/wechatApp/photo/like?__NS_sig3={__NS_sig3}&__NS_sig3_origin={__NS_sig3_origin}'
    data = {
        "photoId": photoId,
        "userId": userId,
        "cancel": cancel
    }
    res = requests.post(url, headers=headers, data=json.dumps(data)).content.decode('utf-8')
    res = json.loads(res)
    print(res)


# 评论
def comment(userId, photoId, content):
    url = f'https://wxmini-api.uyouqu.com/rest/wd/wechatApp/photo/comment/add?__NS_sig3={__NS_sig3}&__NS_sig3_origin={__NS_sig3_origin}'
    data = {
        "photoId": photoId,
        "photoAuthorId": userId,
        "content": content
    }
    res = requests.post(url, headers=headers, data=json.dumps(data)).content.decode('utf-8')
    res = json.loads(res)
    print(res)


# 获取用户下所有视频
def getProfileFeeds(userId, pcursor=None, count=12):
    url = f'https://wxmini-api.uyouqu.com/rest/wd/wechatApp/feed/profile?__NS_sig3={__NS_sig3}&__NS_sig3_origin={__NS_sig3_origin}'
    data = {
        "count": count,
        "eid": userId,
        "pcursor": pcursor
    }
    res = requests.post(url, headers=headers, data=json.dumps(data)).content.decode('utf-8')
    res = json.loads(res)
    print(res)


# 获取关注数据列表
def myFollow(pcursor=0, clientRealReportData='', count=12):
    url = f'https://wxmini-api.uyouqu.com/rest/wd/wechatApp/feed/myfollow?__NS_sig3={__NS_sig3}&__NS_sig3_origin={__NS_sig3_origin}'
    data = {
        "count": count,
        "pcursor": pcursor,
        "productionFeature": 2,
        'clientRealReportData': clientRealReportData
    }
    res = requests.post(url, headers=headers, data=json.dumps(data)).content.decode('utf-8')
    res = json.loads(res)
    print(res)


# 获取直播列表 pcursor游标 ，tabId: 1精选、7卖货、3游戏、11颜值
def live(pcursor=0, tabId=1):
    url = f'https://wxmini-api.uyouqu.com/rest/wd/wechatApp/live/feed/square/more?__NS_sig3={__NS_sig3}&__NS_sig3_origin={__NS_sig3_origin}&pcursor={pcursor}&tabId={tabId}'
    res = requests.get(url, headers=headers).content.decode('utf-8')
    res = json.loads(res)
    print(res)


# 获取主播直播信息
def liveUserInfo(eid, source=9):
    url = f'https://wxmini-api.uyouqu.com/rest/wd/wechatApp/live/byUser?__NS_sig3={__NS_sig3}&__NS_sig3_origin={__NS_sig3_origin}'
    data = {
        "eid": eid,
        "source": source,
    }
    res = requests.post(url, headers=headers, data=json.dumps(data)).content.decode('utf-8')
    res = json.loads(res)
    print(res)


# 直播间发消息
def liveComment(liveStreamId, content):
    url = f'https://wxmini-api.uyouqu.com/rest/wd/wechatApp/live/comment?__NS_sig3={__NS_sig3}&__NS_sig3_origin={__NS_sig3_origin}'
    data = {
        "liveStreamIdStr": liveStreamId,
        "content": content,
    }
    res = requests.post(url, headers=headers, data=json.dumps(data)).content.decode('utf-8')
    res = json.loads(res)
    print(res)


# 关注 touid关注人ID ftype：1关注 2取消关注
def follow(touid, ftype=1):
    url = f'https://wxmini-api.uyouqu.com/rest/wd/wechatApp/relation/follow?__NS_sig3={__NS_sig3}&__NS_sig3_origin={__NS_sig3_origin}'
    data = {
        "touid": touid,
        "ftype": ftype,
        "page_ref": 84
    }
    res = requests.post(url, headers=headers, data=json.dumps(data)).content.decode('utf-8')
    res = json.loads(res)
    print(res)


# 添加作品收藏
def collectAdd(photoId):
    url = 'https://wxmini-api.uyouqu.com/rest/wd/wechatApp/collect/add'
    data = {
        "photoId": photoId
    }
    res = requests.post(url, headers=headers, data=json.dumps(data)).content.decode('utf-8')
    res = json.loads(res)
    print(res)


# 取消作品收藏
def collectDel(photoId):
    url = 'https://wxmini-api.uyouqu.com/rest/wd/wechatApp/collect/delete'
    data = {
        "photoId": photoId
    }
    res = requests.post(url, headers=headers, data=json.dumps(data)).content.decode('utf-8')
    res = json.loads(res)
    print(res)


if __name__ == '__main__':
    print('hello')
