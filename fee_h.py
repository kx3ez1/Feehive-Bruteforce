def send_message(notification_text):
  token = "1683909489:AAGqJjv4wgUsgRO2YyrZgJlG1IgQPgVZtEQ"
  chat_id = '769149529'
  url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={notification_text}"
  import requests
  requests.get(url).json()

def send_sticker(status=True):
  fail_sticker = "CAACAgIAAxkBAAIFnGHAv3GveQEkUacua3sL0Z-Mq3XfAAJ_AwACbbBCAxZG7mi_FYixIwQ"
  success_sticker = "CAACAgIAAxkBAAIFn2HAwBzjUAm9k5s0RQdf8ynX1pbSAAIxAwACbbBCA5qcE5gargaAIwQ"
  if status:
    token = "1683909489:AAGqJjv4wgUsgRO2YyrZgJlG1IgQPgVZtEQ"
    chat_id = '769149529'
    url = f"https://api.telegram.org/bot{token}/sendAnimation?chat_id={chat_id}&animation={success_sticker}"
    import requests
    requests.get(url).json()
  else:
    token = "1683909489:AAGqJjv4wgUsgRO2YyrZgJlG1IgQPgVZtEQ"
    chat_id = '769149529'
    url = f"https://api.telegram.org/bot{token}/sendAnimation?chat_id={chat_id}&animation={fail_sticker}"
    import requests
    requests.get(url).json() 
def login_feehive(vtuno,password):
  print('vtuno : ',vtuno)
  print('password : ',password)
  import requests
  #from termcolor import colored
  r = requests.Session()
  #host = "https://www.vijayabankonline.com"                #site changed
  host = "https://feehive.bankofbaroda.co.in"
  #url = 'https://www.vijayabankonline.com/FeeHiveWeb/FeeHive/Login/VELTECHUNI'
  url = 'https://feehive.bankofbaroda.co.in/FeeHiveWeb/FeeHive/Login/VELTECHUNI'
  match_text = 'Incorrect Username or Password.'
  headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
  "Accept": "*/*",
  'Host': "feehive.bankofbaroda.co.in",
  'Referer': 'https://www.google.com/'

  }
  data = r.get(url,headers=headers)
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
  "Accept": "*/*",
  'Host': "feehive.bankofbaroda.co.in",
  'Referer': 'https://www.google.com/'}
  data = r.get(url,headers=headers)
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(data.text,'html.parser')
  CaptchaImage = soup.find_all('img',attrs={'id':'CaptchaImage'})[0]
  captcha_url = host+CaptchaImage['src']
  headers['Referer'] = 'https://feehive.bankofbaroda.co.in/FeeHiveWeb/FeeHive/Login/VELTECHUNI'
  data = r.get(captcha_url,headers=headers)
  with open('captcha.png','wb+') as f:
    f.write(data.content)
  #from IPython.display import Image,display
  #display(Image(data=data.content))
  def img_to_text():
    import requests
    api_key = 'acc_6ecfbafd28b72c3'
    api_secret = '92d392f59cdc3c8708411b4375523635'
    image_path = 'captcha.png'
    response = requests.post(
        'https://api.imagga.com/v2/text',
        auth=(api_key, api_secret),
        files={'image': open(image_path, 'rb')})
    img_data = response.json()
    captcha_text = img_data['result']['text'][0]['data']
    return captcha_text
  CaptchaDeText = lambda text:text.split('=')[-1]
  img_text = img_to_text()
  img_text = img_text.replace('.','')
  img_text = img_text.replace(':','')
  img_text = img_text.replace(',','')
  img_text = img_text.replace('*','')
  print('image text : ',img_text)
  data = {
      "Username":vtuno,
      "Password":password,
      "chkTerms":"Remember+Me",
      "CaptchaDeText":CaptchaDeText(captcha_url),
      "CaptchaInputText":img_text
  }
  rsp1 = r.post(url,headers=headers,data=data)
  if match_text in rsp1.text:
    #print(colored('Incorrect Password','red'))
    print("Login Failed")
    send_message("Feehive Login Failed"+"\n"+vtuno+"\n"+password)
    send_sticker(False)
    #push = pb.push_file(file_url="https://e7.pngegg.com/pngimages/907/821/png-clipart-thumbs-down-emoji-smiley-emoji-face-emoticon-thumb-smiley-thumbnail.png", file_name="Failed.png", file_type="image/png")
  elif 'Error: captcha is not valid!' in rsp1.text:
    #print(colored('captcha is nor valid','red'))
    print('-'*35)
    login_feehive(vtuno,password)
  else:
    #print(colored('Login Success','green'))
    print("Login Success")
    send_message("Feehive Login Success"+"\n"+vtuno+"\n"+password)
    send_sticker(True)
    #push = pb.push_file(file_url="https://i.pinimg.com/originals/74/fb/dc/74fbdc181cf987f832be99b71810b682.png", file_name="success.png", file_type="image/png")
  print('-'*35)

'''with open('data.txt','r') as f:
  credentials = f.readlines()
for password in credentials:
  login_feehive('vtu14236',password,pb)'''
import time
all_count = 1
while True:
    print(all_count)
    login_feehive('vtu14201',"Bharath2384")
    time.sleep(60*60)
    all_count = all_count+1
    
