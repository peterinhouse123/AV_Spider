# -*- coding: UTF-8 -*-
import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Net:
    def __init__(self):
        pass

    def Get(self,url,header_string="",cookie="",SSL_verify=0):

        header_dict = self.get_header_dict(header_string)


        rs = requests.get(url,headers=header_dict,verify=SSL_verify,cookies=cookie)

        return rs
    def Download(self,url,local_filename=None):
        if local_filename == None:
            local_filename = url.split('/')[-1]
        # NOTE the stream=True parameter
        r = requests.get(url, stream=True)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush() commented by recommendation from J.F.Sebastian
        return local_filename

    # 將文字header變成字典
    def get_header_dict(self,string):
        string = string.replace("https://", "https#")
        string = string.replace("http://", "http#")
        arr = string.split("###")

        end = dict()
        for item in arr:
            if item != "":
                temp = item.split(":")
                temp[1] = temp[1].replace("https#", "https://")
                temp[1] = temp[1].replace("http#", "http://")
                end[temp[0].strip()] = temp[1].strip()
        return end

    # 用正則表達式取得文字
    def preg_get_word(self,preg_word, num, text, mode=0):

        try:

            patte = re.compile(preg_word)
            grk = patte.search(text)

            if num == "all":
                bb = re.findall(preg_word, text)
                rs = bb
                if len(rs) == 0:
                    rs = "empty_data"
            else:
                rs = grk.group(num)
                if mode == "test":
                    print("正則表達式:" + preg_word + "\n 結果:" + rs.encode("utf-8"))

        except:

            rs = "empty_data"

        return rs


if __name__ == "__main__":
    obj = Net()
    #模擬測試
    header_str = "Host: class.ruten.com.tw###Connection: keep-alive###Cache-Control: max-age=0###Upgrade-Insecure-Requests: 1###User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36###Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8###Accept-Encoding: gzip, deflate###Accept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7###If-Modified-Since: Mon, 30 Jul 2018 19:28:15 GMT###"
    url = "http://class.ruten.com.tw/user/index00.php?s=dodo790119&d=5216722&o=0&m=1"
    rs = obj.Get(url,header_string=header_str)
    print(rs.content.decode())
    # print(rs)