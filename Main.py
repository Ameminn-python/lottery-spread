import requests, bs4
import gspread
import json

#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials 

#2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

#認証情報設定
#ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
credentials = ServiceAccountCredentials.from_json_keyfile_name('秘密鍵のJSON', scope)

#OAuth2の資格情報を使用してGoogle APIにログインします。
gc = gspread.authorize(credentials)

#ここから下にスプレッドシートを操作する記述を書くよ
workbook = gc.open_by_key('スプレッドシートキー')
worksheet = workbook.get_worksheet('数値型でワークシート番号(start0)')


for i in range(1,100):
    for c in ['F','J','N']
    cell=c+str(i)
    area = 'A'+str(i)+':'+'K'+str(i)
    id = worksheet.acell(cell).value
    res = requests.get('https://twitter.com/'+id;)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    get_user = soup.select('#ユーザー名属性id')
    if get_user == None:
        worksheet.format(area, {'textFormat': {'bold': True}})
    else:
        pass
    






print(soup.h2)
