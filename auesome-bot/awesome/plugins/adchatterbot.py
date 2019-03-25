from datetime import datetime
import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot import on_command, CommandSession




@on_command('add_adgroup',aliases=("+"),only_to_me = True)
async def add_adgroup(session:CommandSession):
    if len(session.current_arg_text.split('#')) == 1:
        admessage = session.current_arg_text.split('#')[0]+'#'+ad_message 
    else:
        admessage = session.current_arg_text
        

    if session.current_arg_text.split('#')[0].isdigit():
        async with AIOFile('./adgroup.txt','a+') as f:
            await f.write(admessage +'\n')
            await f.fsync()
        await session.send(f'添加成功 {admessage}')
    else:
        await session.send("添加失败，正确格式：+ 群号#内容 \n 如：+ 1122341#出一个校园网")

        
        
