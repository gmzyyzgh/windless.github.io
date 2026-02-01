#dfsdfsdfasdfasfasdf
import akshare as ak
from datetime import datetime, timedelta


def get_dynamic_date_range():

    # 获取当前时间
    #now = datetime.now()
    now = datetime(year=2025, month=3, day=31)
    yesterday = (now - timedelta(days=3)).strftime('%Y%m%d')
    preday = (now - timedelta(days=4)).strftime('%Y%m%d')
    return preday, yesterday


def check_volume_growth(code):
    """检查单只股票成交量翻倍"""
    try:
        df = ak.stock_zh_a_hist(symbol=code, period="daily", start_date=get_dynamic_date_range()[0],
                                end_date=get_dynamic_date_range()[1])
        #print(df)
        if df.empty:
            return

        preday_vol = df.iloc[0]['成交量']
        yesterday_vol = df.iloc[1]['成交量']

        # 合理性校验
        if preday_vol <= 0 or yesterday_vol <= 0:  # or preday_vol * 10 < yesterday_vol:
            return
        if preday_vol * 3 < yesterday_vol:   #昨日成交量超过前日成交量5位的股票名称
            print(f"异常波动股票: {code} | 前日成交量: {preday_vol} | 昨日成交量: {yesterday_vol}")
    except Exception as e:
        print(f"{code}数据获取失败: {e}")


def main():
    """主程序逻辑"""
    stock_list = ak.stock_zh_a_spot_em()  # 获取实时股票列表
    print(stock_list['代码'])
    for code in stock_list['代码']:
        check_volume_growth(code)


if __name__ == "__main__":
    main()