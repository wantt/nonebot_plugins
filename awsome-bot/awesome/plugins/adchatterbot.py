import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot import on_command, CommandSession

from nonebot import on_natural_language, NLPSession, NLPResult


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import json

if 1:
    chatbot = ChatBot("seven",
            logic_adapters=['chatterbot.logic.BestMatch'],
            read_only=True)
    trainer = ListTrainer(chatbot)
    trainer.export_for_training('./my_export.json')

@on_natural_language(only_to_me=True)
async def _(session:NLPSession):
    await session.send(f"{chatbot.get_response(session.msg)}")


@on_command('check_conv',aliases='x',only_to_me = True)
async def check_conv(session:CommandSession):
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


@on_command('learn',aliases='l',only_to_me = True)
async def learn(session:CommandSession):
    list_text = session.current_arg_text.split('#')
    tmpconversation=[]
    if len(list_text) >=2:
        for con in list_text:
            tmpconversation.append(con)
        trainer.train(tmpconversation)
        await session.send("成功")
        trainer.export_for_training('./my_export.json')
    else:
        await session.send("格式错误，正确格式：l 问题#答案")
        
        
