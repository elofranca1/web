from flask import Flask, jsonify
import random
import re
from flask import Flask, render_template, request
import json
import asyncio
from fastapi_poe.types import ProtocolMessage
from fastapi_poe.client import get_bot_response


def remove_extra_whitespace(text):
    cleaned_text = re.sub(r'\s+', '', text)
    return cleaned_text

async def get_responses(api_key, prompt):
    message = ProtocolMessage(role="user", content=prompt)
    response = ''
    async for partial in get_bot_response(messages=[message], bot_name="Assistant", api_key=api_key):
        # 处理服务器返回值: 是一个键值对，其中键为'text'的包含有效文本数据，全部汇总到response变量然后返回
      for key, value in partial:
        if key == 'text':
          response += value
    return response

api_key = "c0OKzOfyf9r9IWUOmmyQilBHfSt-7ZmhJk5hWyAsVYo"

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


        # ...更多slides
    
    return render_template('index.html')


@app.route('/generate-monster', methods=['GET'])
def randomGenerate():
    # 调用 Generate 函数生成数据
    monster_info = Generate()
    # 返回 JSON 响应
    print(monster_info)
    return jsonify(monster_info)


@app.route('/submit-data', methods=['POST'])
def submit_data():
    data = request.json
    selected_scene = data.get('selected_scene')
    monster_name = data.get('monster_name')
    monster_personality = data.get('monster_personality')
    monster_ability = data.get('monster_ability')
    selected_theme = data.get('selected_theme')
    selected_length = data.get('selected_length')
    story_summary = data.get('story_summary')

    print("Selected Scene:", selected_scene)
    print("Monster Name:", monster_name)
    print("Monster Personality:", monster_personality)
    print("Monster Ability:", monster_ability)
    print("Selected Theme:", selected_theme)
    print("Selected Length:", selected_length)
    print("Story Summary:", story_summary)

    send_message = "你是一个绘本内容生成器。帮我以中国山海经为故事背景，以"+selected_scene+"为故事发生地理位置，以"+monster_name+"妖兽为故事主角，妖兽的能力是"+monster_ability+"性格是"+monster_personality + \
        "。以"+story_summary + "为故事内容，以"+selected_theme+"为故事核心内涵，生成有"+selected_length + \
        "章节的中文绘本文字内容。每个章节字数在300字左右，章节情节要非常起伏波动，细节描绘的很好。每章主题前用#标记，章节内容前用一个$标记"
    print(send_message)

    server_message = asyncio.run(get_responses(api_key, send_message))

    matches = re.findall(r'#([^$]+)\s+\n+\$([^#]+)',
                         server_message, re.MULTILINE | re.DOTALL)

    # 初始化章节主题和内容的列表
    them = []
    content = []

    slides_data = []

    # 提取章节主题和内容，并存储到对应的列表中
    for match in matches:
        chapter_title = match[0].strip()
        chapter_content = match[1].strip()
        them.append(chapter_title)
        content.append(chapter_content)
    print(server_message)

    # 打印章节主题和内容
    for i, (chapter_title, chapter_content) in enumerate(zip(them, content), start=1):

        cleaned_text = remove_extra_whitespace(chapter_content)
        new_slide = {'image': 'image_path',
                     'text': f"{chapter_title}\n{cleaned_text}"}
        slides_data.append(new_slide)

        #print(f"Chapter {i} Content: {cleaned_text}")
        # print(new_slide.text)


    return render_template('pages.html', slides=slides_data)


   


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=80,
        debug=False
    )
