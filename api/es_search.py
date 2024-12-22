
from elasticsearch import Elasticsearch

es = Elasticsearch(['http://localhost:9200'],basic_auth=("elastic", "1q2w3e"))



def search_by_kor_nm(index: str, search_word: str):
  query_search_by_kor_nm = {
    "query": {
      "multi_match": {
        "query": "{kor_nm}",
        "fields": [
          "kor_nm",
          "synonym"
        ]
      }
    }
  }
  query_search_by_kor_nm['query']['multi_match']['query'] = search_word
  data = es.search(index=index, body=query_search_by_kor_nm)
  return [i["_source"] for i in data.body['hits']['hits']]


def search_by_eng_nm(index: str, search_word: str):
  query_search_by_eng_nm = {
    "query": {
      "multi_match": {
        "query": "{kor_nm}",
        "fields": [
          "eng_short_nm",
          "eng_full_nm"
        ]
      }
    }
  }
  query_search_by_eng_nm['query']['multi_match']['query'] = search_word
  data = es.search(index=index, body=query_search_by_eng_nm)
  return [i["_source"] for i in data.body['hits']['hits']]
