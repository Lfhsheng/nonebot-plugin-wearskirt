from nonebot.plugin import on_command
from nonebot import require
from nonebot.adapters import Event
from nonebot_plugin_localstore import get_data_file
from nonebot.log import logger
from nonebot.plugin import PluginMetadata
from .config import *
from .Wear_skirt import *
import os
import sqlite3

require('nonebot_plugin_localstore')
path = get_data_file('wear_skirt', 'data.db')
skirt = on_command('wear_skirt', aliases={'女装'})
__plugin_meta__ = PluginMetadata(
    name="女装 !",
    description="Nonebot 赛博女装插件",
    usage=(
        "使用 /女装 或 /wear_skirt 进行女装"
    ),
    type="application",
    homepage="https://github.com/Lfhsheng/nonebot-plugin-wearskirt",
    config=Config,
    supported_adapters=None,
)

def init():
    base = sqlite3.connect(path)
    cursor = base.cursor()
    cursor.execute(INIT_WEAR_SKIRT_BASE)
    base.commit()
    base.close()


@skirt.handle()
async def skirt_function(event: Event):
    user_id = event.get_user_id()
    if not os.path.exists(path):
        logger.info(config.DATA_BASE_NOT_FOUND)
        init()
    logger.info(user_id + ' 正在女装!')
    await skirt.finish(wear_skirt(int(user_id), path))
