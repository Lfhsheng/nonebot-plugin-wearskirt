from pydantic import BaseModel


class Config(BaseModel):
    INIT_WEAR_SKIRT_BASE: str = '''
    CREATE TABLE WEAR_SKIRT(
        ID       INT  NOT NULL,
        DAY      INT,
        DATETIME TEXT
);'''
    DATA_BASE_NOT_FOUND: str = '''未找到数据库, 正在新建.'''
    WEAR_SKIRT_WAITING: str = '正在女装中, 请稍等…'
    LOG_WEARING_SKIRT: str = '{user_name} 正在女装.'
    WEAR_SKIRT_INSERT: str = '''
    INSERT INTO WEAR_SKIRT (ID, DAY, DATETIME) VALUES (?, ?, ?) '''
    WEAR_SKIRT_UPDATE_DAY: str = 'UPDATE WEAR_SKIRT SET DAY = ? WHERE ID = ? '
    WEAR_SKIRT_UPDATE_DATETIME: str = '''
    UPDATE WEAR_SKIRT SET DATETIME = ? WHERE ID = ? '''
    WEAR_SKIRT_SUCCESS: str = '女装成功, 你已女装 {wear_skirt_day} 天.'
    REPEAT_WEAR_SKIRT: str = '''你今天已经女装过了qwq, 你已女装 {wear_skirt_day} 天, 真是个爱女装的好孩子 (划掉.'''
    NOT_CONTINUOUS_WEAR_SKIRT: str = '未连续女装, 你已女装 {wear_skirt_day} 天, 女装需要坚持.'
    LOG_WEARING_SKIRT_BOARD: str = '{user_name} 正在查看女装龙虎榜中…'
    NOBODY_WEAR_SKIRT: str = '目前无人女装!'
    WEAR_SKIRT_BOARD_INFO: str = '{user_name} ({user_id}) 女装了 {day} 天.'
    interrupt_wear_skirt_times: bool = False
