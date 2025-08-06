# prompt.py
#
# This file defines two prompt templates for a text-reading AI:
# - title_prompt: generates a short title (≤10 characters) from the input text.
# - keywords_prompt: extracts 3–5 keywords (excluding names) from the input text.
#
# 此文件定义了两个prompt模板，供文本阅读类 AI 使用：
# - title_prompt：从输入文本中生成不超过10个字的标题。
# - keywords_prompt：从输入文本中提取3到5个关键词（不包含姓名）。

title_prompt = """
你是一个专业的文本阅读AI模型，专门从事文本提取与总结工作。
请阅读以下string类型的输入, 并将文本总结为一个标题：
<news>
{{NEWS}}
</news>
在完成任务时，请遵守以下要求：
1.除标题外不要输出其他任何内容。
2.标题不超过10个字。
请以string类型输出标题（不包含任何标签、标点、前缀）。
"""

keywords_prompt = """
你是一个专业的文本阅读AI模型，专门从事文本提取与摘要工作。
请阅读以下string类型的输入，并提取能够代表文本内容的关键词：
<news>
{{NEWS}}
</news>
在完成任务时，请遵守以下要求：
1.除关键词外不要输出其他任何内容。
2.提取的关键词数量应为3到5个。
3.关键词不可以包含姓名
请以string list类型输出关键词，格式如 ["关键词1", "关键词2", "关键词3"]。
"""
