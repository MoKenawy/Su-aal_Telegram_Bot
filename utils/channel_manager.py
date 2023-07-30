from bot import user_client

async def add_unique_message(channel_id, text, sender_id):
    msg_id = await message_exist(channel_id, text= sender_id)
    if msg_id == -1 :
       msg_id = await user_client.send_message(entity= channel_id, message= sender_id)
    return await user_client.send_message(entity= channel_id, message= text, comment_to= msg_id)

async def message_exist(chat_id, text):
    messages = await get_message(chat_id, text)
    if len(messages) > 0:
        return messages[0].id
    else:
        return -1

async def get_message(chat_id, text):
    messages = []
    async for message in user_client.iter_messages(chat_id):
        if message.text == text:
            messages.append(message)
    return messages