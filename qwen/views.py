import os
import json
from openai import OpenAI
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

def get_response(messages):
    client = OpenAI(
        # 如果您没有配置环境变量，请在此处用您的 API Key 进行替换
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    completion = client.chat.completions.create(model="qwen-plus", messages=messages)
    return completion


messages = []

@csrf_exempt
def get_user_input(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        question = data.get('question')
        return question
    else:
        return None

# 假设这是在一个 Django 的视图函数中
def some_view(request):
    print('test')
    #assistant_output = "欢迎光临百炼手机商店，您需要购买什么尺寸的手机呢？"
    #print(f"模型输出：{assistant_output}\n")

    #if  "我已了解您的购买意向" not in assistant_output:

    user_input = get_user_input(request)
    print(user_input)

    # 将用户问题信息添加到 messages 列表中
    messages.append({"role": "user", "content": user_input})
    assistant_output = get_response(messages).choices[0].message.content
    # 将大模型的回复信息添加到 messages 列表中
    messages.append({"role": "assistant", "content": assistant_output})
    print(f"模型输出：{assistant_output}")
    print("\n")

    return JsonResponse({'response': messages})



#这是demo里的代码修改后的（可以用）
# def get_response(messages):
#     client = OpenAI(
#         # 如果您没有配置环境变量，请在此处用您的 API Key 进行替换
#         api_key=os.getenv("DASHSCOPE_API_KEY"),
#         base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
#     )
#     completion = client.chat.completions.create(model="qwen-plus", messages=messages)
#     return completion
#
#
# messages = [
#     {
#         "role": "system",
#         "content": """你是一名百炼手机商店的店员，你负责给用户推荐手机。手机有两个参数：屏幕尺寸（包括 6.1 英寸、6.5 英寸、6.7 英寸）、分辨率（包括 2K、4K）。
#         你一次只能向用户提问一个参数。如果用户提供的信息不全，你需要反问他，让他提供没有提供的参数。如果参数收集完成，你要说：我已了解您的购买意向，请稍等。""",
#     }
# ]
#
# @csrf_exempt
# def get_user_input(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         question = data.get('question')
#         return question
#     else:
#         return None
#
# # 假设这是在一个 Django 的视图函数中
# def some_view(request):
#     print('test')
#     assistant_output = "欢迎光临百炼手机商店，您需要购买什么尺寸的手机呢？"
#     print(f"模型输出：{assistant_output}\n")
#
#     if  "我已了解您的购买意向" not in assistant_output:
#
#         user_input = get_user_input(request)
#         print(user_input)
#
#         # 将用户问题信息添加到 messages 列表中
#         messages.append({"role": "user", "content": user_input})
#         assistant_output = get_response(messages).choices[0].message.content
#         # 将大模型的回复信息添加到 messages 列表中
#         messages.append({"role": "assistant", "content": assistant_output})
#         print(f"模型输出：{assistant_output}")
#         print("\n")
#         # 等待新的 POST 请求
#         while True:
#             new_user_input = get_user_input(request)
#             if new_user_input:
#                 break
#     return JsonResponse({'response': messages})