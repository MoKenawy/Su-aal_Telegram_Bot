from telethon import events
from utils.function_refs import make_ref
from typing import List, Callable
from bot.config import config
from telethon.tl.functions.messages import SearchRequest
from telethon.tl.types import InputMessagesFilterEmpty
from bot import user_client
from utils.channel_manager import add_unique_message


handlers = []

@make_ref(handlers)
@events.register(events.NewMessage)
async def add_question(event):
    student_chat_id = int(config['student_chat_id'])
    channel_id = int(config['ques_channel_id'])
    if event.chat_id == student_chat_id :
        sender_id = str(event.sender_id)
        await add_unique_message(channel_id , text = event.message.text, sender_id= sender_id)



@make_ref(handlers)
@events.register(events.NewMessage(pattern="/info"))
async def chat_info(event):
    chat_id = event.chat_id
    chat_info = await get_chat_info(event, chat_id)
    print(f"chat_id : {chat_id}")
    print(f"chat_access_hash : {chat_info.access_hash}")
    print(f"chat_info : {chat_info}")

async def get_chat_info(event, chat_id):
    entity = await event.client.get_entity(entity = chat_id)
    return entity

# @make_ref(handlers)
# @events.register(events.NewMessage(pattern='/start'))
# async def handle_start_command(event):
#     # Respond with "bot is running" when the user sends "/start"
#     result = await event.respond("bot is running")
#     print(result)
#     print(event.id)

# @events.register(events.Raw)
# async def handle_start_command(event):
#     # Respond with "bot is running" when the user sends "/start"
#     # await event.respond("bot is running")
#     print(event)
#id=6699

# adding a question

# @make_ref(handlers)
# @events.register(events.NewMessage)
# async def handle_forwarded_messages(event):
#         student_name = "anon"
#         question_type = "anon"
#         question = ''
#         client = event.client
#         msg_id = event.id
#         question = event.message.text

#         ques_chat_id = int(config['ques_group_id'])
#         chat_id = event.chat_id

#         msg = f"اسم الطالب : {student_name} \n نوع السؤال : {question_type} \n السؤال : {question} \n"
        
#         comp_message =  f"'{msg}' from chat : {str(chat_id)}"     
#         await client.send_message(entity = ques_chat_id, message = msg)



# @make_ref(handlers)
# @events.register(events.NewMessage)
# async def get_chat_id(event):
#     entity = await event.client.get_entity(entity = int(config['ques_group_id']))
#     print(f"entity : {str(entity)}")





# async def get_thread(query):
#     ques_group_id = int(config['ques_group_id'])
#     channel_access_hash = int(config['channel_access_hash'])
#     group_access_hash=5842564660985677183


#     print(query)
#     result = await user_client(SearchRequest(
#           peer = ques_group_id,
#           q= query,
#           filter = InputMessagesFilterEmpty(),
#           min_date= 0,
#           max_date= 1,
#           offset_id= 0,
#           add_offset=0,
#           limit= 20,
#           min_id= 0,
#           max_id= 10000,
#           hash= group_access_hash
#           ))
#     return result

# @make_ref(handlers)
# @events.register(events.NewMessage())
# async def ask_question(event):
#     client = event.client
#     channel_id = int(config['ques_channel_id'])
#     ques_group_id = int(config['ques_group_id'])

#     thread_id = None
#     student_chat_id = -1001948247254
#     question = event.message.text
#     if event.chat_id == student_chat_id :      
#         sender_id = event.sender_id

#         test =  f"user_id : {sender_id}"
#         test = "1234567890"

#         threads = await get_thread(test)

#         print(f"threads found = {threads.count}")


#         if (threads != None) and threads.count <= 0:
#            thread_id = await client.send_message(entity= channel_id, message = str(test))
#            await user_client.send_message(entity= channel_id, message = question, comment_to= thread_id)

#         else :
#             print(f"------------------")
#             msg_id = threads.messages[0].id
#             await client.send_message(entity= ques_group_id, message = question, reply_to = msg_id)


        #threads = await get_thread(test)
        #print(f"threads found = {threads.count}")
        #print(f"threads found = {len(threads.messages)}")
        # thread_id = threads.messages[0].id
        # print(f"thread id : {thread_id}")






