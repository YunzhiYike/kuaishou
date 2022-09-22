# 快手-微信小程序协议

## 说明：本项目为开源，仅供学习参考，请勿方法用途否则后果自负！

## [👉 视频传送门 🎬](https://www.bilibili.com/video/BV1iY4y1N76h?share_source=copy_web&vd_source=71e28910aae780b1b2052c3052b8a2e8)

## 🐂 功能支持
- [x] getInfo -- 通过用户ID获取用户信息 
- [x] getRecommend -- 获取推荐数据列表
- [x] like -- 点赞作品
- [x] comment -- 评论作品
- [x] getProfileFeeds -- 获取用户下所有视频
- [x] myFollow -- 获取关注数据列表 
- [x] live -- 获取直播列表
- [x] liveUserInfo -- 获取主播直播信息
- [x] liveComment -- 直播间发消息
- [x] follow -- 关注用户
- [x] collectAdd -- 添加作品收藏
- [x] collectDel -- 取消作品收藏
- [x] publish -- 上传图片作品


## 📖 使用说明

> 请在 Python3 环境运行

```python
if __name__ == '__main__':
    liveComment('主播ID', '消息内容')
```

## 📚 抓包教程
使用前需要用抓包工具获取账号token(t)，需要一定动手能力，获取后就是傻瓜式操作。

💻 PC端抓包工具：Fiddler、Http Debugger

📱 Android端抓包工具：HttpCarry

📱 iPhone端抓包工具：Stream

Android端抓包视频教程：http://u.ncii.cn/LIgVd

iPhone端抓包视频教程：http://u.ncii.cn/68dxv