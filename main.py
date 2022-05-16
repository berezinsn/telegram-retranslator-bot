#!/usr/bin/env python3

import config
import json
import re
from pyrogram import Client
from pyrogram import filters


# Validate Telegram post function
def validate_post(post: str):
    for prohibited_word in config.black_list:
        if re.search(prohibited_word, post) is not None:
            return True
    return False


# Client part
api_id = config.client_api_id
api_hash = config.client_api_hash
source_chat_id = config.source_chat_id
destination_chat_id = config.destination_chat_id

app = Client("service_account", api_id, api_hash)
f = filters.chat(source_chat_id)


@app.on_message(f)
def event_copy_handler(target_chat, message):

    message_str_content = str(message)

    message_json_content = json.loads(message_str_content)

    post = message_json_content["text"]

    if validate_post(post) is False:
        message.copy(chat_id=destination_chat_id, caption="")
    else:
        print("Message will not be posted due to prohibited words" + "\n" + post)


app.run()

