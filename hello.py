# 取得目前的日期與時間
from datetime import datetime

# 定義 hello 函數，接收一個字串參數 name
def hello(name: str) -> None:
    # 取得現在的時間，格式化成字串（年-月-日 時:分:秒）
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 輸出問候語句和目前時間的訊息
    print(f"Hello {name}，現在是時間是 {now}")

    """
    來自 dev 的註解
    """