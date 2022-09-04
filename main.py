# project_1_sport_everyday
print('sport_everyday''\n''每日运动打卡')

"""
读取网络地址中的运动结果截图
"""
# 方案1 获取飞书文档中的图片信息
# 截图需要手动发送到飞书文档中
# read() 后如何获取图片信息?
from urllib.request import urlopen
url = urlopen('https://b1dd2mtcu7.feishu.cn/docx/doxcn89kJXOI9UbAvYWnKExIrwe')
print(url.read())
# urllib.urlretrieve(img_src,'E:/1.jpg')



# 方案2 获取百度网盘共享链接中的图片信息
# 截图后自动保存到同步相册自动上传
# read() 后如何获取图片信息?
from urllib.request import urlopen
url = urlopen('https://pan.baidu.com/s/1HKIPc-Qxza6NtPRMOCfcHA?pwd=py01#list/path=%2F%E9%A1%B9%E7%9B%AE')
print(url.read())
# urllib.urlretrieve(img_src,'E:/1.jpg')
