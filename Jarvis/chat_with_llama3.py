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
        if input_str.lower() == "bye":
            break

        prompt = (
                prompt + "{input}"
        )

        make_border()

        print("User input:")

        input_str = ""

        while True:
            input_str = record_text()

            if input_str != "":
                break

            print("Repeat request again: ")

        print(input_str)

        make_border()

        chain = prompt | llm

        ai_res_message = ""

        ai_chunk_message = ""

        for chunk in chain.stream(input=input_str):

            ai_chunk_message += chunk.content

            if (("." in ai_chunk_message or
                "!" in ai_chunk_message or
                "?" in ai_chunk_message) and
                    any(c.isalpha() for c in ai_chunk_message)):
                print(ai_chunk_message, end="")

                play_text_to_speech(ai_chunk_message)

                ai_res_message += ai_chunk_message
                ai_chunk_message = ""

        print("")

        prompt = (
                prompt + HumanMessage(content=input_str) + AIMessage(content=ai_res_message)
        )

    make_border()


if __name__ == '__main__':
    chat_with_llm()
