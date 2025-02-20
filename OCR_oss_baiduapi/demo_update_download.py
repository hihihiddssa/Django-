import oss2
from itertools import islice

# 1 代码嵌入方式配置

##配置项
# 填写RAM用户的访问密钥（AccessKey ID和AccessKey Secret）。
accessKeyId = 'LTAI5tDm2HTxTUJBKq4AUjRY'
accessKeySecret = '42gWcGvXwunVHdjmpTPiBSfeFNMziK'
# 使用代码嵌入的RAM用户的访问密钥配置访问凭证。
auth = oss2.Auth(accessKeyId, accessKeySecret)

# endpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
endpoint = 'http://	oss-cn-beijing.aliyuncs.com'

# 填写Bucket名称。
bucketName = 'agacila'
bucket = oss2.Bucket(auth, endpoint, bucketName)



##操作项
# # 上传文件到OSS。
# # objectName（oss端路径）由包含文件后缀，不包含Bucket名称组成的Object完整路径，例如abc/efg/123.jpg。
# objectName = 'xxxx.png'
# # localFile由本地文件路径（要上传文件路径）加文件名包括后缀组成，例如/users/local/myfile.txt。
# localFile = 'C:\\Users\\agaci\\Desktop\\qqq.png'
# bucket.put_object_from_file(objectName, localFile)
# # 生成下载链接
# fileLink = 'http://'+bucketName+'.oss-cn-beijing.aliyuncs.com/'+objectName
# print(fileLink)


# #下载OSS文件到本地文件。
# # objectName由包含文件后缀，不包含Bucket名称组成的Object完整路径，例如abc/efg/123.jpg。
# # localFile由本地文件路径加文件名包括后缀组成，例如/users/local/myfile.txt。
# bucket.get_object_to_file('xxxx.png', 'C:\\Users\\agaci\\Desktop\\download_files\\download.png')

# # oss2.ObjectIterator用于遍历文件。列举10个文件
# for b in islice(oss2.ObjectIterator(bucket), 10):
#     print(b.key)

# # 列举Bucket下的所有文件。
# for obj in oss2.ObjectIterator(bucket):
#     print(obj.key)

# # 列举指定前缀的所有文件
# # 列举fun文件夹下的所有文件，包括子目录下的文件。
# for obj in oss2.ObjectIterator(bucket, prefix='fun/'):
#     print(obj.key)

# # 列举指定起始位置后的所有文件
# # 列举指定字符串之后的所有文件。即使存储空间中存在marker的同名object，返回结果中也不会包含这个object。
# for obj in oss2.ObjectIterator(bucket, marker="x2.txt"):
#     print(obj.key)
#
# # 列举指定目录下的文件和子目录
# # 列举fun文件夹下的文件与子文件夹名称，不列举子文件夹下的文件。
# for obj in oss2.ObjectIterator(bucket, prefix = 'fun/', delimiter = '/'):
#     # 通过is_prefix方法判断obj是否为文件夹。
#     if obj.is_prefix():  # 判断obj为文件夹。
#         print('directory: ' + obj.key)
#     else:                # 判断obj为文件。
#         print('file: ' + obj.key)
#
# # 获取指定目录下的文件大小
# def CalculateFolderLength(bucket, folder):
#     length = 0
#     for obj in oss2.ObjectIterator(bucket, prefix=folder):
#         length += obj.size
#     return length
# for obj in oss2.ObjectIterator(bucket, delimiter='/'):
#     if obj.is_prefix():  # 判断obj为文件夹。
#         length = CalculateFolderLength(bucket, obj.key)
#         print('directory: ' + obj.key + '  length:' + str(length) + "Byte.")
#     else: # 判断obj为文件。
#         print('file:' + obj.key + '  length:' + str(obj.size) + "Byte.")
