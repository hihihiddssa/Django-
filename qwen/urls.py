from django.urls import path
from qwen.views import *


#这里现在是二级路由表了
urlpatterns = [

    path('ask/', some_view),#当http请求是qwen/ask时，使用ask函数处理


]


'''
import os
from openai import OpenAI


def get_response(messages):
    client = OpenAI(
        # 如果您没有配置环境变量，请在此处用您的API Key进行替换
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    completion = client.chat.completions.create(model="qwen-plus", messages=messages)
    return completion


messages = [
    {
        "role": "system",
        "content": """你是一名百炼手机商店的店员，你负责给用户推荐手机。手机有两个参数：屏幕尺寸（包括6.1英寸、6.5英寸、6.7英寸）、分辨率（包括2K、4K）。
        你一次只能向用户提问一个参数。如果用户提供的信息不全，你需要反问他，让他提供没有提供的参数。如果参数收集完成，你要说：我已了解您的购买意向，请稍等。""",
    }
]
assistant_output = "欢迎光临百炼手机商店，您需要购买什么尺寸的手机呢？"
print(f"模型输出：{assistant_output}\n")
while "我已了解您的购买意向" not in assistant_output:
    user_input = input("请输入：")
    # 将用户问题信息添加到messages列表中
    messages.append({"role": "user", "content": user_input})
    assistant_output = get_response(messages).choices[0].message.content
    # 将大模型的回复信息添加到messages列表中
    messages.append({"role": "assistant", "content": assistant_output})
    print(f"模型输出：{assistant_output}")
    print("\n")

请参考这里的代码。我要实现以下功能。
input输入用户回答部分，我希望能通过post方法实现。我会通过postman来发送post数据。格式如下：{"question":"这是一个测试问题"}

我使用的是Django框架，路由如下：path('ask/', main) main再view.py里面

'''