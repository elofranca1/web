from flask import Flask, jsonify
import random
from flask import Flask, render_template, request
import json
import asyncio
from fastapi_poe.types import ProtocolMessage
from fastapi_poe.client import get_bot_response

app = Flask(__name__)


def Generate():
    # 示例：生成随机妖兽信息
    names = ["火焰妖兽", "水波妖兽", "雷电妖兽", "大地妖兽"]
    personalities = ["勇敢", "聪明", "忠诚", "机智"]
    abilities = ["喷火", "水箭", "闪电", "地震"]

    return {
        "name": random.choice(names),
        "personality": random.choice(personalities),
        "ability": random.choice(abilities)
    }


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-monster', methods=['GET'])
def randomGenerate():
    # 调用 Generate 函数生成数据
    monster_info = Generate()
    # 返回 JSON 响应
    print(monster_info)
    return jsonify(monster_info)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=80,
        debug=False
    )
