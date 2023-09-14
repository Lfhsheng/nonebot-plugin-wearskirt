from .config import Config
from nonebot import get_driver
from nonebot import get_bot
from nonebot_plugin_localstore import get_data_file
import sqlite3
import datetime

plugin_config = Config.parse_obj(get_driver().config)

class Skirt:
    path = get_data_file('wear_skirt', 'data.db')
    
    async def wear_skirt(self, user_id):
        bot = get_bot()
        base_connect = sqlite3.connect(self.path)
        cursor = base_connect.cursor()
        already_wear_skirt_id = base_connect.execute(''' SELECT * FROM WEAR_SKIRT''').fetchall()
        for user in already_wear_skirt_id:
            if user_id == user[0]:
                yesterday = datetime.date.today() - datetime.timedelta(days=1)
                if user[2] == str(yesterday):
                    wear_skirt_day = user[1] + 1
                    cursor.execute(plugin_config.WEAR_SKIRT_UPDATE_DAY, (wear_skirt_day, user[0]))
                    cursor.execute(plugin_config.WEAR_SKIRT_UPDATE_DATETIME, (datetime.date.today(), user[0]))
                    base_connect.commit()
                    return plugin_config.WEAR_SKIRT_SUCCESS.format(wear_skirt_day=wear_skirt_day)
                elif user[2] == str(datetime.date.today()):
                    wear_skirt_day = user[1]
                    return plugin_config.REPEAT_WEAR_SKIRT.format(wear_skirt_day=wear_skirt_day)
                else:
                    if plugin_config.interrupt_wear_skirt_times:
                        wear_skirt_day = 1
                        cursor.execute(plugin_config.WEAR_SKIRT_UPDATE_DAY, (1, user[0]))
                        cursor.execute(plugin_config.WEAR_SKIRT_UPDATE_DATETIME, (datetime.date.today(), user[0]))
                        base_connect.commit()
                        return plugin_config.NOT_CONTINUOUS_WEAR_SKIRT.format(wear_skirt_day=wear_skirt_day)
                    else:
                        wear_skirt_day = user[1] + 1
                        cursor.execute(plugin_config.WEAR_SKIRT_UPDATE_DAY, (wear_skirt_day, user[0]))
                        cursor.execute(plugin_config.WEAR_SKIRT_UPDATE_DATETIME, (datetime.date.today(), user[0]))
                        base_connect.commit()
                        return plugin_config.WEAR_SKIRT_SUCCESS.format(wear_skirt_day=wear_skirt_day)
        wear_skirt_day = 1
        cursor.execute(plugin_config.WEAR_SKIRT_INSERT, (user_id, 1, datetime.date.today()))
        base_connect.commit()
        return plugin_config.WEAR_SKIRT_SUCCESS.format(wear_skirt_day=wear_skirt_day)
    async def get_stranger_info(self, user_id):
        bot = get_bot()
        info = await bot.get_stranger_info(user_id=user_id, no_cache=False)
        return info['nickname']
    
    async def wear_skirt_board(self, group_id):
        bot = get_bot()
        base_connect = sqlite3.connect(self.path)
        already_wear_skirt_info = base_connect.execute('SELECT ID,DAY FROM WEAR_SKIRT').fetchall()
        group_member_info = bot.get_group_member_list(group_id=group_id)
        group_member_id= [user['user_id'] for user in (await group_member_info)]
        for user in already_wear_skirt_info:
            if not user[0] in group_member_id:
                already_wear_skirt_info.remove(user)
        result_list = [plugin_config.WEAR_SKIRT_BOARD_INFO.format(
            user_name=await self.get_stranger_info(user_id=user[0]), user_id=user[0], day=user[1]) for user in already_wear_skirt_info]
        result = ('\n'.join(result_list))
        if result == '':
            return plugin_config.NOBODY_WEAR_SKIRT
        return result
