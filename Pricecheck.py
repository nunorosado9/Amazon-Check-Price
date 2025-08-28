import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL='https://www.amazon.es/-/pt/dp/B0BTZB7F88/ref=sr_1_1_mod_primary_new?adgrpid=159790286542&dib=eyJ2IjoiMSJ9.mU27cwptUy7PTxaJ31s2PacQ1R-ly-Sn3IsLuzrijOAPC03ZmWZhss9Ds9bje4QJOYIhqhpryoTxiNzLHB--046t5LZqQuaXh44ct-AEAgdPw-xw-ceRUE-XP6ciwFkDqgmPxinzNLS345DzyTkmIrFU_2ll7quAeRhoxpqf4IVg56-9mxtNFekZ_ymKCHJQfGs1jKg2SsskI0W-kCHkrIpQ-M-UG8ERnCBiksxeK2DhpWWgLsLEF3aDpwxO2QmcrKuMJPpWvbSvfNKVOnpx4My3a2OsEImsBLiQoCi49dU.9Lo9jCXwKGdmZloknimUquOiIpPP_rzTYlic6okrZ6A&dib_tag=se&hvadid=699683466930&hvdev=c&hvlocphy=20878&hvnetw=g&hvqmt=e&hvrand=9634700195006419138&hvtargid=kwd-2358435535883&hydadcr=17111_2268852&keywords=ryzen+7+5700x3d+amazon&mcid=8daf6ea3ddb13baf875f9a7ad72ef9c4&qid=1756393922&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sr=8-1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 OPR/120.0.0.0'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find("span", class_="a-offscreen").get_text()
    converted_price = float(price[0:3])

    if(converted_price < 320):
        send_email()
        
    print(converted_price)
    print(title.strip())

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('nunor200@gmail.com', 'dbnt fmky iwwv cjpn')

    subject = 'O PRECO DO PROCESSADOR BAIXOU!'
    body = 'VE AGORA NA AMAZON https://www.amazon.es/-/pt/dp/B0BTZB7F88/ref=sr_1_1_mod_primary_new?adgrpid=159790286542&dib=eyJ2IjoiMSJ9.mU27cwptUy7PTxaJ31s2PacQ1R-ly-Sn3IsLuzrijOAPC03ZmWZhss9Ds9bje4QJOYIhqhpryoTxiNzLHB--046t5LZqQuaXh44ct-AEAgdPw-xw-ceRUE-XP6ciwFkDqgmPxinzNLS345DzyTkmIrFU_2ll7quAeRhoxpqf4IVg56-9mxtNFekZ_ymKCHJQfGs1jKg2SsskI0W-kCHkrIpQ-M-UG8ERnCBiksxeK2DhpWWgLsLEF3aDpwxO2QmcrKuMJPpWvbSvfNKVOnpx4My3a2OsEImsBLiQoCi49dU.9Lo9jCXwKGdmZloknimUquOiIpPP_rzTYlic6okrZ6A&dib_tag=se&hvadid=699683466930&hvdev=c&hvlocphy=20878&hvnetw=g&hvqmt=e&hvrand=9634700195006419138&hvtargid=kwd-2358435535883&hydadcr=17111_2268852&keywords=ryzen+7+5700x3d+amazon&mcid=8daf6ea3ddb13baf875f9a7ad72ef9c4&qid=1756393922&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sr=8-1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'nunor200@gmail.com',
        'nunor200@gmail.com',
        msg
    )
    print('O EMAIL FOI ENVIADO!')

    server.quit()

while(True):
    check_price()
    time.sleep(86400)