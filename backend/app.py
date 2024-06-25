from flask import Flask, request, jsonify
from flask_cors import CORS
# import openai
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)

# 设置OpenAI API密钥
keyfile = os.path.join(os.path.pardir, "keys\\kimi.txt")
key = open(keyfile).readline().strip("\n")  # 从keyfile中读取API密钥, 此处为kimi

client = OpenAI(
    api_key=key,
    base_url="https://api.moonshot.cn/v1",
)

history = []


def init():
    # 读取prompt
    promptFile = os.path.join(os.path.pardir, "prompts\\kimi.txt")
    try:
        with open(promptFile, encoding='utf-8') as file:
            prompt = file.readline().strip("\n")  # 从prompt file中读取prompt, 此处为kimi
    except UnicodeDecodeError as e:
        print(f"Error reading file {promptFile}: {e}")
    history.append({"role": "system", "content": prompt})


@app.route('/process', methods=['POST'])
def process_data():
    data = request.json.get('inputData')
    print(data)
    history.append({"role": "user", "content": data})
    completion = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=history,
        temperature=0.3,
        timeout=15,
    )
    # 获取处理后的数据
    processed_data = completion.choices[0].message.content.strip()
    print(processed_data)
    history.append({"role": "assistant", "content": processed_data})
    # 获取处理后的数据
    response_data = {'processedData': processed_data}
    return jsonify(response_data)


if __name__ == '__main__':
    init()
    app.run(debug=True)
