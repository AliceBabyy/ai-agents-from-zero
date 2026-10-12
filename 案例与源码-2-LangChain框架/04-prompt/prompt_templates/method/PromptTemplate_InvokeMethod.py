"""
【案例】PromptTemplate 的 invoke() 方法

对应教程章节：第 13 章 - 提示词与消息模板 → 6、文本提示词模板（PromptTemplate）

知识点速览：
- `invoke(...)` 返回的不是普通字符串，而是 `PromptValue`，更适合衔接 LangChain 的链式调用。
- 对 `PromptTemplate` 来说，返回值通常是 `StringPromptValue`；你可以继续 `.to_string()`，也可以 `.to_messages()`。
- 其中 `.to_messages()` 常见会转成单条 `HumanMessage`，它是把文本 Prompt 包装成消息的一种统一方式。
"""

from langchain_core.prompts import PromptTemplate

def main():
    # ---------- 1. 创建模板 ----------
    template = PromptTemplate.from_template(
        "你是一个专业的{role}工程师，请回答我的问题给出回答，我的问题是：{question}"
    )
    # 返回的是一个StringPromptValue类，该类继承自PromptTemple，是封装纯文本类提示词的类
    # 该类实现了__str__，所以直接打印可显示字符串

    # ---------- 2. 用 invoke 传入变量（字典），得到 PromptValue 对象 ----------
    prompt = template.invoke({"role": "python开发", "question": "冒泡排序怎么写？"})
    # invoke是langchain的Tunable接口的标准方法，所有可运行组件（模型、模版、解析器）都有invoke方法
    print(prompt)
    print(type(prompt))
    print()

    # ---------- 3. 从 PromptValue 取内容：to_string() 得到整段字符串 ----------
    print(prompt.to_string()) # to_string是去除整段字符串，对应type是str类型
    print(type(prompt.to_string())) # 跟上面直接输出的区别就是，上面拿到的类型是一个StringPromptValue对象，不是str
    print()

    # ---------- 4. to_messages()：转成「消息列表」，可接入需要多角色消息的链 ----------
    print(prompt.to_messages())
    print(type(prompt.to_messages())) # list类型


"""
【输出示例】
text='你是一个专业的python开发工程师，请回答我的问题给出回答，我的问题是：冒泡排序怎么写？'
<class 'langchain_core.prompt_values.StringPromptValue'>

你是一个专业的python开发工程师，请回答我的问题给出回答，我的问题是：冒泡排序怎么写？
<class 'str'>

[HumanMessage(content='你是一个专业的python开发工程师，请回答我的问题给出回答，我的问题是：冒泡排序怎么写？', additional_kwargs={}, response_metadata={})]
<class 'list'>
"""

if __name__ == "__main__":
    main()