from pydantic import BaseModel

INIT_WEAR_SKIRT_BASE = '''
    CREATE TABLE WEAR_SKIRT(
        ID       INT  NOT NULL,
        DAY      INT,
        DATETIME TEXT
);'''
DATA_BASE_NOT_FOUND = '''未找到数据库, 正在新建.'''

WEAR_SKIRT_WAITING = '正在女装中, 请稍等…'
LOG_WEARING_SKIRT = '{user_name} 正在女装.'
WEAR_SKIRT_INSERT = 'INSERT INTO WEAR_SKIRT (ID, DAY, DATETIME) VALUES (?, ?, ?) '
WEAR_SKIRT_UPDATE_DAY = 'UPDATE WEAR_SKIRT SET DAY = ? WHERE ID = ? '
WEAR_SKIRT_UPDATE_DATETIME = 'UPDATE WEAR_SKIRT SET DATETIME = ? WHERE ID = ? '
WEAR_SKIRT_SUCCESS = '女装成功, 你已女装 {wear_skirt_day} 天.'
REPEAT_WEAR_SKIRT = '你今天已经女装过了qwq, 你已女装 {wear_skirt_day} 天, 真是个爱女装的好孩子 (划掉.'
NOT_CONTINUOUS_WEAR_SKIRT = '未连续女装, 你已女装 {wear_skirt_day} 天, 女装需要坚持.'

LOG_WEARING_SKIRT_BOARD = '{user_name} 正在查看女装龙虎榜中…'
NOBODY_WEAR_SKIRT = '目前无人女装<tg-spoiler> ,快使用 <code>/wear_skirt</code> 女装吧 </tg-spoiler>!'
WEAR_SKIRT_BOARD_INFO = '<a href="tg://user?id={user_id}" >{user_name}</a> 女装了 {day} 天.\n'


class Config(BaseModel):
    interrupt_wear_skirt_times: bool = False
