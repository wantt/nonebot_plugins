from datetime import datetime
import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot import on_command, CommandSession
from aiofile import AIOFile

from nonebot import permission as perm

ad_message='便宜出一个校园网，最好长期'

#@nonebot.scheduler.scheduled_job('cron',hour='10',minute='*')
#@nonebot.scheduler('cron',hour='10',minute='*')
@nonebot.scheduler.scheduled_job('cron',hour='*/5',minute='0')
async def _():
    bot = nonebot.get_bot()
    now  = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        adgroup=[]
        
        with open('./adgroup.txt','r') as f:
            for group_id in f.read().split('\n')[:-1]:  # [531481587,161631645]:
                groupid = group_id.split('#')[0]
                if groupid not in adgroup and groupid.isdigit():
                    adgroup.append(groupid)
                    print(groupid)
                    admessage = group_id.split('#')[1:]
                    await bot.send_group_msg(group_id=int(groupid), message=f'{"".join(admessage)}')
#                    await session.send(f'{group_id}定时发送成功')
       
    except CQHttpError:
        pass
#        await session.send('定时发送失败')
     

@on_command('add_adgroup',aliases=("+"),only_to_me = True,permission=perm.SUPERUSER)
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

        
        
        
@on_command('del_adgroup',aliases=("-"),only_to_me=True,permission=perm.SUPERUSER)
async def del_adgroup(session:CommandSession):
    print(session.current_arg_text)
    adgroups = []
    with open('./adgroup.txt','r') as f:
        for content in f.read().split('\n')[:-1]:
            group_id = content.split('#')[0]
            if content not in adgroups and group_id.isdigit():
                adgroups.append(content)
    if session.current_arg_text.split('#')[0].isdigit() and session.current_arg_text in adgroups:
        adgroups.remove(session.current_arg_text)
        await session.send(f'删除成功{session.current_arg_text}')
    else:
        await session.send(f'删除失败，不存在这条群发 {session.current_arg_text}')

    with open('./adgroup.txt','w+') as f:
        for group_id in adgroups:
            f.write(group_id + '\n')
    

@on_command('modifyDefaultMsg',aliases=('m'),only_to_me=True,permission=perm.SUPERUSER)
async def modifyDefaultMsg(session:CommandSession):
    ad_message = session.current_arg_text
    session.send(f'修改默认群发成功，现在的默认群发：{ad_message}')
    
@on_command('send_ad',aliases=('s'),only_to_me=True,permission=perm.SUPERUSER)
async def send_ad(session:CommandSession):
    bot = nonebot.get_bot()
    try:
        adgroup=[]
        with open('./adgroup.txt','r') as f:
            for group_id in f.read().split('\n')[:-1]:  # [531481587,161631645]:
                groupid = group_id.split('#')[0]
                if groupid not in adgroup and groupid.isdigit():
                    adgroup.append(groupid)
                    print(groupid)
                    admessage = group_id.split('#')[1:]
                    await bot.send_group_msg(group_id=int(groupid), message=f'{"".join(admessage)}')
                    await session.send(f'群{groupid}成功发送消息成功{admessage}')
       
    except CQHttpError:
        await session.send('发送失败')
@on_command('check_ad',aliases='c',only_to_me=True,permission=perm.SUPERUSER)
async def check_ad(session:CommandSession):
    adgroup= []
    with open('./adgroup.txt','r') as f:
        for message in f.read().split("\n")[:-1]:
            adgroup.append(message+'\n')
    await session.send(f'{"".join(adgroup)}')
@on_command('adhelp',aliases='h',only_to_me=True,permission=perm.SUPERUSER)
async def adhelp(session:CommandSession):
    await session.send(f'+: 添加群发,+ 123#出一个校园网  \n -:删除群发，- 123#出一个校园网 \n s:发送群发 s\n c: 查看群发 c \n m:修改默认群发 m 出一个校园网\n h:显示本帮主信息')
#@on_command()
