import oss2
from itertools import islice
from aip import AipOcr
import os
import time


##配置项
# 填写RAM用户的访问密钥（AccessKey ID和AccessKey Secret）。
accessKeyId = 'LTAI5tDm2HTxTUJBKq4AUjRY'
accessKeySecret = '42gWcGvXwunVHdjmpTPiBSfeFNMziK'
# 使用代码嵌入的RAM用户的访问密钥配置访问凭证。
auth = oss2.Auth(accessKeyId, accessKeySecret)
# endpoint填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss - cn - hangzhou.aliyuncs.com。
endpoint = 'http://oss-cn-beijing.aliyuncs.com'
# 填写Bucket名称。
bucketName = 'agacila'
bucket = oss2.Bucket(auth, endpoint, bucketName)

# 百度 OCR 的配置信息（你需要在百度云平台申请）
APP_ID = '115581793'
API_KEY = 'bYEZROoQ9lHVlFd7vW6noWTt'
SECRET_KEY = 'c2z6uTi6ZHdOCYErtB9AsRstNGXwp7UO'
# 初始化百度 OCR 客户端
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 文件路径
# 读取文件路径
read_path = 'C:\\Users\\agaci\\Desktop\\download_files\\download.png'


##定义方法
# 读取文件
def get_file_content(filePath):
    try:
        with open(filePath, 'rb') as fp:
            return fp.read()
    except Exception as e:
        print(f"读取文件出错: {e}")
        return None


##操作项
# 下载OSS文件到本地文件。
# objectName由包含文件后缀，不包含Bucket名称组成的Object完整路径，例如abc/efg/123.jpg。
# localFile由本地文件路径加文件名包括后缀组成，例如/users/local/myfile.txt。
bucket.get_object_to_file('xxxx.png', read_path)


# 检查文件是否存在
file_path = read_path
if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
    print("文件不存在或者为空")
else:
    # 进行 OCR 识别
    image = get_file_content(file_path)
    if image:
        try:
            result = client.basicGeneral(image)
            time.sleep(0.5)
            # 提取并打印识别出的文字
            if 'words_result' in result:
                recognized_text = " ".join([words['words'] for words in result['words_result']])
                print("文件路径:", read_path)
                print("识别的文字内容:", recognized_text)
            else:
                print("OCR 识别结果中没有文字信息")
        except Exception as e:
            print(f"百度 OCR 服务调用出错: {e}")
    else:
        print("无法读取文件内容进行 OCR 识别")
