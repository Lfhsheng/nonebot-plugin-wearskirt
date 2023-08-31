from .config import *
from nonebot import get_driver
import sqlite3
import datetime

plugin_config = Config.parse_obj(get_driver().config)


def wear_skirt(user_id, data_base_path):
    base_connect = sqlite3.connect(data_base_path)
    cursor = base_connect.cursor()
    already_wear_skirt_id = base_connect.execute('SELECT * FROM WEAR_SKIRT').fetchall()
    for user in already_wear_skirt_id:
        if user_id == user[0]:
            yesterday = datetime.date.today() - datetime.timedelta(days=1)
            if user[2] == str(yesterday):
                wear_skirt_day = user[1] + 1
                cursor.execute(WEAR_SKIRT_UPDATE_DAY, (wear_skirt_day, user[0]))
                cursor.execute(WEAR_SKIRT_UPDATE_DATETIME, (datetime.date.today(), user[0]))
                base_connect.commit()
                return WEAR_SKIRT_SUCCESS.format(wear_skirt_day=wear_skirt_day)
            elif user[2] == str(datetime.date.today()):
                wear_skirt_day = user[1]
                return REPEAT_WEAR_SKIRT.format(wear_skirt_day=wear_skirt_day)
            else:
                if plugin_config.interrupt_wear_skirt_times:
                    wear_skirt_day = 1
                    cursor.execute(WEAR_SKIRT_UPDATE_DAY, (1, user[0]))
                    cursor.execute(WEAR_SKIRT_UPDATE_DATETIME, (datetime.date.today(), user[0]))
                    base_connect.commit()
                    return NOT_CONTINUOUS_WEAR_SKIRT.format(wear_skirt_day=wear_skirt_day)
                else:
                    wear_skirt_day = user[1] + 1
                    cursor.execute(WEAR_SKIRT_UPDATE_DAY, (wear_skirt_day, user[0]))
                    cursor.execute(WEAR_SKIRT_UPDATE_DATETIME, (datetime.date.today(), user[0]))
                    base_connect.commit()
                    return WEAR_SKIRT_SUCCESS.format(wear_skirt_day=wear_skirt_day)
    wear_skirt_day = 1
    cursor.execute(WEAR_SKIRT_INSERT, (user_id, 1, datetime.date.today()))
    base_connect.commit()
    return WEAR_SKIRT_SUCCESS.format(wear_skirt_day=wear_skirt_day)


'''todo
def wear_skirt_board(data_base_path):
    base_connect = sqlite3.connect(data_base_path)
    already_wear_skirt_id = base_connect.execute('SELECT ID,DAY FROM WEAR_SKIRT').fetchall()
    result = ''
    for user in already_wear_skirt_id:
        result += WEAR_SKIRT_BOARD_INFO.format(
            user_id=str(user[0]), day=user[1])
    if result == '':
        return NOBODY_WEAR_SKIRT
    return result
'''
