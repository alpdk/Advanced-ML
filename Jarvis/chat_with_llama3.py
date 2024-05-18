import os
import sys
import json

from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from speech_to_text import record_text
from text_to_speech import play_text_to_speech


def generate_sys_message(dict):
    res = "In this chat I would like to talk with you about"

    for i in dict.keys():
        for j in dict[i]:
            res += j + ', '

    res = res[:-2]

    res += ". Be reade to questions, about it"

    return res


def make_border():
    print("==================================")

def chat_with_llm():
    llm = ChatOllama(model="gemma:2b")

    prompt = SystemMessage(content=generate_sys_message({}))

    input_str = ""

    while True:
        if input_str == "Bye":
            break

        prompt = (
                prompt + "{input}"
        )

        make_border()
        print("User input:")
        input_str = record_text()

        print(input_str)

        make_border()

        chain = LLMChain(llm=llm, prompt=prompt)

        ai_message = chain.invoke(input=input_str)['text']

        print("Chat bot answer: ")
        print(ai_message)

        play_text_to_speech(ai_message)

        prompt = (
                prompt + HumanMessage(content=input_str) + AIMessage(content=ai_message)
        )

    make_border()


if __name__ == '__main__':
    chat_with_llm()
