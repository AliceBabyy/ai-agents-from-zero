from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv(encoding="utf-8")

model = ChatOpenAI(
    model = "qwen3.8-flash",
    api_key = os.getenv("aliQwen-api"),
    base_url="https://maas.qianwenaiapi.com/compatible-mode/v1"
)

def main():
    # 1. 只用解析器
    # parser = JsonOutputParser()
    # result = model.invoke("请用 JSON 返回：name、age")
    # print(result)
    # data = parser.invoke(result)
    # print(data)

    # 2. 只用结构化输出
    # class Person(TypedDict):
    #     name: str
    #     age: int
    # structured_model = model.with_structured_output(Person)
    # result = structured_model.invoke("请返回一个人物信息")
    # print(result)

    # 3. 同时用机构化输出和解析器
    class Person(TypedDict):
        name:str
        age:int
    structured_model = model.with_structured_output(Person)
    result = structured_model.invoke("请返回一个人物信息")
    # 在这加解析器或额外校验处理，此处暂时没加
    print(result)


if __name__ == "__main__":
    main()