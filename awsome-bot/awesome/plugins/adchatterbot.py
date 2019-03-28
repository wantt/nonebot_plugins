import nonebot
from nonebot import permission as perm
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, NLPResult
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import chatterbot
import json
import re


if 1:
    chatbot = ChatBot("seven",
                    logic_adapters=['chatterbot.logic.BestMatch'],
            read_only=True)
    trainer = ListTrainer(chatbot)
    trainer.export_for_training('./my_export.json')


ad_private_message = '你好，我出校园网'
@on_natural_language(only_to_me=False)
async def _(session:NLPSession):
    rule=r'([收买求有租(有.*转让)].*[网(创翼)])(?![球拍站吧友速上址银页名])'
    if re.match(rule,session.msg):
        await session.send('你好，我出校园网',ensure_private = True)
    elif session.ctx['message_type']=='private':
        await session.send(f"{chatbot.get_response(session.msg)}")
        
#    elif '大家好' in session.msg:
#        await session.send('哦')
#    else:
#        grouplist=await session.bot.get_group_list()
#        if session.ctx['message_type'] == 'group':
##            print(session.ctx['user_id'])
#            print(session.ctx['group_id'])
#            if 1:#session.ctx['group_id'] == int('251347617'):
#                await session.send(message = 'hello',ensure_private = True)
#        elif session.ctx['message_type']=='discuss':
#            print(f"{session.ctx['discuss_id']}")
#    await    bot.send_private_msg(user_id=int(2188156040),message='123')
#    await bot.send_private_msg(user_id=int(1048517841),message='123')
#        await session.send(f"{chatbot.get_response(session.msg)}")


@on_command('gai_pri',aliases='k',only_to_me = True,permission=perm.SUPERUSER)
async def drop_bot(session:CommandSession):
    if (session.current_arg_text):
        print(session.current_arg_text)
        ad_private_message = session.current_arg_text
#    session.current_arg_text.split("#")

    
@on_command('drop_bot',aliases='d',only_to_me = True,permission=perm.SUPERUSER)
async def drop_bot(session:CommandSession):
    chatbot.storage.drop()
    await session.send("success drop")

@on_command('check_conv',aliases='x',only_to_me = True,permission=perm.SUPERUSER)
async def check_conv(session:CommandSession):
    all_conv = []
    num=0
    with open('./my_export.json','r') as f:
        load_dict = json.load(f)
        for k in load_dict.keys():
            for i in load_dict[k]:
                tmpconv = "#".join(i)
                all_conv.append(str(num)+'. ' + tmpconv)
                num +=1
        await session.send('\n\n'.join(all_conv))
        
'''
@on_command('gai_conv',aliases='g',only_to_me = True)
async def gai_conv(session:CommandSession):
    all_conv = []
    num=0
    with open('./my_export.json','r') as f:
        load_dict = json.load(f)
        for k in load_dict.keys():
            for i in load_dict[k]:
                tmpconv = "#".join(i)
                all_conv.append(str(num) + '  ' + tmpconv)
                num +=1
        await session.send("\n\n".join(all_conv))
        change_num = session.get('change_num',prompt="输入你要修改或者删除的数字：")
        print(change_num)
    if change_num.isdigit() and int(change_num) < num:
        del load_dict['conversations'][int(change_num)]
        with open('./my_export.json','w+') as f:
            json.dump(load_dict,f)
            chatbot.storage.drop()
            trainer.train(load_dict['conversations'])

        await session.send(load_dict['conversations'])
'''

@on_command('learn',aliases='l',only_to_me = True,permission=perm.SUPERUSER)
async def learn(session:CommandSession):
    list_text = session.current_arg_text.split('#')
    tmpconversation=[]
    if len(list_text) ==2:
        for con in list_text:
            tmpconversation.append(con)
        trainer.train(tmpconversation)
        await session.send("成功")
        trainer.export_for_training('./my_export.json')
    else:
        await session.send("格式错误，正确格式：l 问题#答案")
        
        
