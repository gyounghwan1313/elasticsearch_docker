from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

# Elasticsearch 연결
es = Elasticsearch(['http://localhost:9200'],basic_auth=("elastic", "1q2w3e"))


# 대량 삽입을 위한 데이터 준비
def generate_actions():
    documents = [
        {
            "kor_nm": "한글명1",
            "synonym": ["동의어1", "동이어2"],
            "desc": "설명1",
            "eng_short_nm": "SHORT1",
            "eng_full_nm": "FULL NAME 1"
        },
        {
            "kor_nm": "한글명2",
            "synonym": ["동의어1", "동이어2"],
            "desc": "설명2",
            "eng_short_nm": "SHORT2",
            "eng_full_nm": "FULL NAME 2"
        }
    ]

    for doc in documents:
        yield {
            "_index": "data_dict",
            "_source": doc
        }


# bulk API를 사용한 대량 삽입
success, failed = bulk(es, generate_actions())
