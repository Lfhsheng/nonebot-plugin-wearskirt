from nonebot.plugin import on_fullmatch
from nonebot.plugin import on_command
from nonebot import require
from nonebot.adapters import Event
require('nonebot_plugin_localstore')
from nonebot_plugin_localstore import get_data_file
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.log import logger
from nonebot.plugin import PluginMetadata
from nonebot.rule import is_type
from nonebot import get_driver
from nonebot import get_bot
from .config import Config
from .wear_skirt import Skirt
from os.path import exists
import sqlite3

plugin_config = Config.parse_obj(get_driver().config)
path = get_data_file('wear_skirt', 'data.db')
wear_skirt_command = on_command('wear_skirt', aliases={'女装'}, rule=is_type(GroupMessageEvent))
wear_skirt_board_command = on_command('wear_skirt_board', aliases={'女装板'}, rule=is_type(GroupMessageEvent))
__plugin_meta__ = PluginMetadata(
    name='女装 !',
    description='Nonebot 赛博女装插件',
    usage=(
        '''
        使用 /女装 或 /wear_skirt 进行女装
        使用 /女装板 或 /wear_skirt_board 查看女装信息
        '''
    ),
    type='application',
    homepage='https://github.com/Lfhsheng/nonebot-plugin-wearskirt',
    config=Config,
    supported_adapters=None,
)

def init():
    base = sqlite3.connect(path)
    cursor = base.cursor()
    cursor.execute(plugin_config.INIT_WEAR_SKIRT_BASE)
    base.commit()
    base.close()

skirt = Skirt()

@wear_skirt_command.handle()
async def wear_skirt_function(event: Event):
    user_id = event.get_user_id()
    bot = get_bot()
    info = await bot.get_stranger_info(user_id=int(user_id), no_cache=False)
    nickname = info['nickname']
    if not exists(path):
        logger.info(plugin_config.DATA_BASE_NOT_FOUND)
        init()
    logger.info(f'可爱的 {nickname} ({user_id}) 正在女装!')
    await wear_skirt_command.finish(await skirt.wear_skirt(int(user_id)), reply_message=True)

@wear_skirt_board_command.handle()
async def wear_skirt_board_function(event: GroupMessageEvent):
    await wear_skirt_command.finish(await skirt.wear_skirt_board(event.group_id), reply_message=True)
