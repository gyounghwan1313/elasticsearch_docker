
from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from es_search import search_by_kor_nm, search_by_eng_nm

# Initialize FastAPI app
app = FastAPI(title="단어 사전", description="LLM기반의 컬럼 논리명, 물리명 생성 API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 허용할 도메인을 명시. "*"는 모든 도메인 허용.
    allow_credentials=True,
    allow_methods=["*"],  # 허용할 HTTP 메서드. "*"는 모든 메서드 허용.
    allow_headers=["*"],  # 허용할 HTTP 헤더.
)


# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI application!"}


class SearchByKorNm(BaseModel):
    kor_nm: str


class SearchByEngNm(BaseModel):
    eng_nm: str


@app.post("/search/kornm")
def read_item(request: SearchByKorNm):
    print(request)
    print(request.kor_nm)
    return search_by_kor_nm(index="data_dict", search_word=request.kor_nm)

@app.post("/search/engnm")
def read_item(request: SearchByEngNm):
    print(request)
    return search_by_eng_nm(index="data_dict", search_word=request.eng_nm)