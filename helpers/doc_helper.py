# doc_helper.py
#
# This file provides helper functions for generating and processing document-related data.
# It includes:
# - Random Chinese name generation
# - Random timestamp generation within a given date range
# - Reading text files line-by-line for storage
# - Generating unique UUIDs
# - Creating structured metadata dictionaries for documents
# These utilities support preparing and managing data for Elasticsearch or other storage systems.

import random, uuid
from datetime import timedelta, datetime


# Generate random chinese names 随机生成中文名
def generate_rand_name() -> str:
    lastnames = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨"
    firstnames = "伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全"
    lastname = random.choice(lastnames)
    firstname = random.choice(firstnames) + random.choice(firstnames)
    return lastname + firstname


# Generate random timestamps 随机生成时间戳
def generate_rand_time(start_year, start_month, start_day, end_year, end_month, end_day) -> str:
    start = datetime(year=start_year, month=start_month, day=start_day)
    end = datetime(year=end_year, month=end_month, day=end_day)
    delta = end - start
    rand_second = random.randint(0, int(delta.total_seconds()))
    return str(start + timedelta(seconds=rand_second))


# Read text by line for storage 按行读取文本，方便后续储存
def file_reader(file_name) -> list:
    with open(file_name) as f:
        records: list[str] = f.read().splitlines()
        return records
        # print(type(f.read()))


# Generate random id 生成随机id
def generate_rand_id() -> str:
    return str(uuid.uuid4())


# Generate metadata for storage 生成元数据，方便后续储存
def generate_doc(title, keywords, who, when) -> dict:
    doc = {
        "title": title,
        "keywords": keywords,
        "created_by": who,
        "created_at": when
    }
    return doc
