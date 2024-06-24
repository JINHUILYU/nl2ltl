from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
from openai import OpenAI

app = Flask(__name__)
CORS(app)

# 设置OpenAI API密钥


client = OpenAI(
    api_key=key,
    base_url="https://api.moonshot.cn/v1",
)

history = [
    {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，"
                                  "准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，"
                                  "不可翻译成其他语言。"}
]


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
    print(response_data)
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True)
