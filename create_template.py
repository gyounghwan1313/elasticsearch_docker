
import json

mapping = {
    "dynamic": "false",
    "dynamic_templates": [],
    "properties": {
        # 필드 추가
    }
  }



synonym = {
    "synonym": {
        "type": "text",
        "analyzer": "nori_analyzer",
        "fields": {
            "ngram": {
                "type": "text",
                "analyzer": "ngram_analyzer",
            },
            "keyword": {"type": "keyword"},
        },
    }
}


kor_nm = {
    "kor_nm": {
        "type": "text",
        "analyzer": "nori_analyzer",
        "fields": {
            "ngram": {
                "type": "text",
                "analyzer": "ngram_analyzer",
            },
            "keyword": {"type": "keyword"},
        },
    }
}


desc= {
    "desc": {
        "type": "text",
        "analyzer": "nori_analyzer",
        "fields": {
            "ngram": {
                "type": "text",
                "analyzer": "ngram_analyzer",
            },
            "keyword": {"type": "keyword"},
        },
    }
}

eng_short_nm= {
    "eng_short_nm": {
        "type": "text",
        "analyzer": "nori_analyzer",
        "fields": {
            "ngram": {
                "type": "text",
                "analyzer": "ngram_analyzer",
            },
            "keyword": {"type": "keyword"},
        },
    }
}

eng_full_nm= {
    "eng_full_nm": {
        "type": "text",
        "analyzer": "nori_analyzer",
        "fields": {
            "ngram": {
                "type": "text",
                "analyzer": "ngram_analyzer",
            },
            "keyword": {"type": "keyword"},
        },
    }
}

mapping.keys()
mapping['properties']["kor_nm"]=kor_nm["kor_nm"]
mapping['properties']["synonym"]=synonym["synonym"]
mapping['properties']["desc"]=desc["desc"]
mapping['properties']["eng_short_nm"]=eng_short_nm["eng_short_nm"]
mapping['properties']["eng_full_nm"]=eng_full_nm["eng_full_nm"]

print(json.dumps(mapping))


### Setting
import json


setting = {
    "index": {
        "analysis": {
            "filter": {
                "nori_part_of_speech": {
                    "type": "nori_part_of_speech",
                    "stoptags": [
                        "E",
                        "IC",
                        "J",
                        "MAG",
                        "MAJ",
                        "MM",
                        "SP",
                        "SSC",
                        "SSO",
                        "SC",
                        "SE",
                        "XPN",
                        "XSA",
                        "XSN",
                        "XSV",
                        "UNA",
                        "NA",
                        "VSV",
                    ],
                }
            },
            "analyzer": {
                "ngram_analyzer": {
                    "filter": ["lowercase"],
                    "type": "custom",
                    "tokenizer": "ngram_tokenizer",
                },
                "nori_analyzer": {
                    "filter": ["lowercase", "nori_part_of_speech"],
                    "type": "custom",
                    "tokenizer": "nori_tokenizer",
                },
            },
            "tokenizer": {
                "ngram_tokenizer": {
                    "token_chars": ["letter", "digit"],
                    "min_gram": "2",
                    "type": "ngram",
                    "max_gram": "3",
                },
                "nori_tokenizer": {
                    "type": "nori_tokenizer",
                    "decompound_mode": "mixed",
                    "discard_punctuation": "true",
                },
            },
        },
        "routing": {"allocation": {"include": {"_tier_preference": "data_content"}}},
    }
}


print(json.dumps(setting))