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
        "章节的中文绘本文字内容。每个章节字数在300字左右，章节情节要非常起伏波动，细节描绘的很好。每章主题前用#标记，章节内容前用$标记"
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
        print(f"Chapter {i} Title: {chapter_title}")

        cleaned_text = remove_extra_whitespace(chapter_content)
        new_slide = {'image': 'image_path',
                     'text': f"Chapter {i} Title: {chapter_title}\n{cleaned_text}"}
        slides_data.append(new_slide)

        print(f"Chapter {i} Content: {cleaned_text}")
        # print(new_slide.text)