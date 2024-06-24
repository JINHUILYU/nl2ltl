# from openai import OpenAI
#
# client = OpenAI(
#     api_key="sk-qYCYHDTH7Wi95Xax51AopGV2TCmy0v3FPLI7rFryrtn7yCCm",
#     base_url="https://api.moonshot.cn/v1",
# )
#
# history = [
#     {"role": "system",
#      "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"}
# ]
#
#
# def chat(query, history):
#     history.append([{
#         "role": "user",
#         "content": query
#     }])
#     completion = client.chat.completions.create(
#         model="moonshot-v1-8k",
#         messages=history,
#         temperature=0.3,
#     )
#     result = completion.choices[0].message.content
#     history.append([{
#         "role": "assistant",
#         "content": result
#     }])
#     return result
#
#
# print(chat("地球的自转周期是多少？", history))
# print(chat("月球呢？", history))

# import openai
#
# # 设置OpenAI API密钥
# openai.api_key = 'sk-qYCYHDTH7Wi95Xax51AopGV2TCmy0v3FPLI7rFryrtn7yCCm'
#
# def chat(question, history=None):
#     if history is None:
#         history = []
#
#     try:
#         completion = openai.ChatCompletion.create(
#             model="moonshot-v1-8k",
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant."},
#                 *history,
#                 {"role": "user", "content": question}
#             ],
#             timeout=15,  # API请求超时时间（秒）
#         )
#         response = completion.choices[0].message['content'].strip()
#         history.append({"role": "user", "content": question})
#         history.append({"role": "assistant", "content": response})
#         return response
#     except openai.error.OpenAIError as e:
#         print(f"Error occurred: {e}")
#         return str(e)
#
# # 示例调用
# history = []
# print(chat("地球的自转周期是多少？", history))

# import os
# from openai import OpenAI
#
# client = OpenAI(
#     # This is the default and can be omitted
#     # api_key=os.environ.get("sk-qYCYHDTH7Wi95Xax51AopGV2TCmy0v3FPLI7rFryrtn7yCCm"),
#     api_key="sk-qYCYHDTH7Wi95Xax51AopGV2TCmy0v3FPLI7rFryrtn7yCCm"
# )
#
# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Say this is a test",
#         }
#     ],
#     model="moonshot-v1-8k",
#     timeout=15,
# )
#
# print(chat_completion.choices[0].message.content)

key = 'sk-bU4z1Lbf84DoevKy7Av3rcTB39IaHhlao8QLjv01D6vmJUkf'

from openai import OpenAI

client = OpenAI(
    api_key=key,
    base_url="https://api.moonshot.cn/v1",
)

completion = client.chat.completions.create(
    model="moonshot-v1-8k",
    messages=[
        {"role": "system",
         "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"},
        {"role": "user", "content": "编程判断 3214567 是否是素数。"}
    ],
    tools=[{
        "type": "function",
        "function": {
            "name": "CodeRunner",
            "description": "代码执行器，支持运行 python 和 javascript 代码",
            "parameters": {
                "properties": {
                    "language": {
                        "type": "string",
                        "enum": ["python", "javascript"]
                    },
                    "code": {
                        "type": "string",
                        "description": "代码写在这里"
                    }
                },
                "type": "object"
            }
        }
    }],
    temperature=0.3,
    timeout=15,
)

print(completion.choices[0].message)