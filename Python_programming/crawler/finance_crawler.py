
import random
import requests
from common import save_result_data, convert_date_string_to_ts

from datetime import *
from bs4 import BeautifulSoup


class InfoCrawler():
     
    def __init__(self):
        self.base_url = ""
        self.headers = {}
        self.user_agent_list = [
            #Chrome
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            #Firefox
            'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
            'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
            'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
        ]

    def set_random_user_agent(self):
        user_agent = random.choice(self.user_agent_list)
        self.headers['User-Agent'] = user_agent
        return user_agent
    

    def get_result_data(self, *args, **kwargs):
        # this method is the goal of class
        # argument should be considered with efficiency
        # if range input is date, date format is 'YYYY/MM/DD'
        pass

    def parse_page(self, raw_response):
        pass

    


class YahooFinanceCrawler(InfoCrawler):

    def __init__(self):
        super().__init__()
        self.set_random_user_agent()
        self.base_url = "https://query2.finance.yahoo.com/v8/finance/chart/{0}.KS?includeAdjustedClose=true&interval=1d&period1={1}&period2={2}"

    
    def get_result_data(self, target_code, from_date_str, to_date_str):
        from_ts = convert_date_string_to_ts(from_date_str)
        to_ts = convert_date_string_to_ts(to_date_str)
        target_url = self.base_url.format(target_code, from_ts, to_ts)
        res = requests.get(target_url,headers=self.headers)
        res_list = self.parse_page(res)
        return res_list


    def parse_page(self, res):
        res_list = []
        res_json = res.json()
        ts_list = res_json["chart"]["result"][0]["timestamp"]
        price_dict = res_json["chart"]["result"][0]["indicators"]["quote"][0]
        
        open_price_list = price_dict["open"]
        close_price_list = price_dict["close"]
        high_price_list = price_dict["high"]
        low_price_list = price_dict["low"]
        
        for ts, open_price, close_price, high_price,low_price in zip(ts_list,open_price_list,close_price_list,high_price_list,low_price_list):
            info_dict = {
                "ts":ts,
                "open": open_price,
                "close":close_price,
                "high":high_price,
                "low": low_price
            }
            res_list.append(info_dict)
            
        print(res_list)
        return res_list
        

class NaverFinanceCrawler(InfoCrawler):

    def __init__(self):
        super().__init__()
        self.base_url = "https://finance.naver.com"
        self.headers = {
            'User-Agent' : '',
            'referer': "https://finance.naver.com",
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        self.set_random_user_agent()


class NaverDiscussionCrawler(NaverFinanceCrawler):
    
    def __init__(self):
        super().__init__()
        self.base_url = self.base_url + "/item/board.naver"

    def get_result_data(self, code, from_page, to_page):
        # [{ts:INT , ant:FLOAT, for:FLOAT, inst:FLOAT }... ]
        total_info_list = []
        for page_idx in range(from_page,to_page+1):
            info_list = self.parse_page(code, page_idx)
            total_info_list += info_list
        return total_info_list

    def parse_page(self, code, page_idx):
        #content > div.section.inner_sub > table.type2 > tbody > tr:nth-child(3) > td:nth-child(1) > span
        info_dict_list=[]
        params_dict = {"code":str(code), "page":str(page_idx)}
        res  = requests.get(self.base_url,params=params_dict, headers=self.headers)
        html = res.text
        soup = BeautifulSoup(html,"html.parser")
        rows = soup.select('table.type2 tr')
        #print(rows)
        info_soup_list = [row for row in rows if str(row).find('mouseOver') >= 0]
        date_view_selector = 'td > span.tah'
    
        for info_soup in info_soup_list:
            #time
            date_view_list = info_soup.select(date_view_selector)

            date_info_str = date_view_list[0].text #2023.06.21 08:54
            year, month, day_and_time = date_info_str.split(".")
            day, time_info = day_and_time.split(" ")
            hour, minute = time_info.split(":")
            ts = datetime(
                int(year),
                int(month),
                int(day),
                int(hour),
                int(minute),
                0

            ).timestamp()


            #view
            view_count = int(date_view_list[1].text)
            info_dict = {"ts":ts,"view_count":view_count}
            info_dict_list.append(info_dict)
            
            
        return info_dict_list

    
    
class MarketBuyerInfoCrawler(NaverFinanceCrawler):

    def __init__(self):
        super().__init__()
        self.base_url = self.base_url + "/sise/investorDealTrendDay.naver"

    def get_result_data(self, from_page, to_page):
        # [{ts:INT , ant:FLOAT, for:FLOAT, inst:FLOAT }... ]

        total_info_list = []
        for page_idx in range(from_page, to_page+1):
            info_list = self.parse_page(page_idx)
            total_info_list += info_list
        return total_info_list

    def parse_page(self, page_idx):
        now = datetime.now()
        y = str(now.year)
        m = str(now.month).rjust(2,"0")
        d = str(now.day).rjust(2,"0")
        
        param_dict = {"bizdate": y+m+d, "page":str(page_idx)}
        res = requests.get(self.base_url, params=param_dict, headers=self.headers)
        html = res.text
        soup = BeautifulSoup(html, "html.parser")
        rows = soup.select('table.type_1 > tr')
        rows = rows[3:]

        info_soup_list = [row for row in rows if str(row).find("date") >= 0]

        info_dict_list = []
        
        for info_soup in info_soup_list:
            info_array = info_soup.select('td')
            #print(info_array[0])
            date_dot_string = info_array[0].text
            year, month, day = date_dot_string.split(".")
            year = "20" + year
            date_string = "{0}/{1}/{2}".format(year, month, day)
            ts = convert_date_string_to_ts(date_string)
            ant_net_amount = int(info_array[1].text.replace(",",""))
            for_net_amount = int(info_array[2].text.replace(",",""))
            inst_net_amount = int(info_array[3].text.replace(",",""))
            
            info_dict_list.append({
                "ts":ts,
                "ant_net_amount" : ant_net_amount,
                "for_net_amount" : for_net_amount,
                "inst_net_amount" : inst_net_amount,
            })
            
        return info_dict_list


if __name__=="__main__":
    # yfc = YahooFinanceCrawler()
    # res = yfc.get_result_data("000660","2023/01/01","2023/07/06")
    # save_result_data(res,"./test.csv")

    # mbc = MarketBuyerInfoCrawler()
    # res = mbc.get_result_data(1,10)
    # save_result_data(res,"./naverfinance.csv")
    
    ndc = NaverDiscussionCrawler()
    res = ndc.get_result_data("079940",2,10)
    save_result_data(res,"./naverdiscussion.csv")
