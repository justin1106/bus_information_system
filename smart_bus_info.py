import requests, pprint, time
from bs4 import BeautifulSoup
import pygame as pg
import config 

Width = 800
Height = 600
Screen = pg.display.set_mode((Width, Height))

pg.display.set_caption('스마트 버스정류장 정보시스템')
pg.init()
url1 = 'http://ws.bus.go.kr/api/rest/stationinfo/getStationByUid'

f = open('config.txt', 'r', encoding='utf-8')
t = f.read().split(':')
tem = None
weather = None
news = None
b_st = t[1]
b_id = t[2]
w_url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={t[0]}+날씨'
n_url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101'
bus = []
b_num = []
def font_render(size, text, pos, color):
    Font_T = pg.font.Font("font/NanumGothic.ttf", int(size))
    msg = Font_T.render(str(text), True, color)
    Screen.blit(msg, pos)
def b_info(bus_id):
    global bus, tem, weather, news, n_url, url1, w_url, b
    
    params = {
        "serviceKey": config.SERVICE_KEY,
        "arsId": bus_id,
        "resultType": "json"
    }
    response = requests.get(url1, params=params)
    if response.status_code == 200:
        r_obj = response.json()
        pprint.pprint(r_obj)
        index = 0
        r = 1
        while not len(bus) == 2:
            item = r_obj['msgBody']['itemList'][index]
            b = item['arrmsg1'].split('[')
            # if i['arrmsg1'] != '운행종료' and i['arrmsg1'] != '출발대기' and i['arrmsg1'] != '곧 도착':
            if not item['arrmsg1'] in ['운행종료', '출발대기', '곧 도착']:
                if not b[1][0] == '0':
                    b = item['arrmsg1'].split('[')
                    # print(b[1][0])
                    index +=1
                    bus.append([b[1][0], item['arrmsg1']])
                    b_num.append(item['busRouteAbrv'])
            elif item['arrmsg1'] == '곧 도착' :
                
                index += 1
                bus.append([0, item['arrmsg1']])
                b_num.append(item['busRouteAbrv'])
            elif item['arrmsg1'] in ['운행종료', '출발대기']:
                index += 1
            else:
                index += 1
                bus.append([0, item['arrmsg1']])
                b_num.append(item['busRouteAbrv'])
        if len(bus) == 0:
            bus.append([-1, item['arrmsg1']])
            bus.append([-1, item['arrmsg1']])
        if len(bus) == 1:
            bus.append([-1, item['arrmsg1']])
                
    # response2 = requests.get(w_url)
    # if response2.status_code == 200:
    #     htmlsource = response2.content
    #     soup = BeautifulSoup(htmlsource, 'html.parser')
    #     tem = soup.find(class_='temperature_text').find('strong').text[5:8]
    #     # print(tem)
    #     weather = soup.find(class_='weather before_slash').text
    #     # print(weather)
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept-Encoding": "*",
        "Connection": "keep-alive"
    }
    # response_n = requests.get(n_url, headers=headers)
    # if response_n.status_code == 200:
    #     html_n = response_n.content
    #     soup_n = BeautifulSoup(html_n, 'html.parser')
    #     news = soup_n.find(class_='cluster_item').find(class_='cluster_text_headline').text

b_info(b_id)
Running = True
loop = 0
while Running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Running = False
    Screen.fill((150,150,150))
    font_render(60, f'{t[0]} 스마트 정보 시스템', (70, 10), (0, 0, 0))
    font_render(25, f'{t[0]}의 현재 날씨: 섭씨 {tem}도, {weather}', (180, 85), (0, 0, 0))
    
    pg.draw.rect(Screen, (255, 255, 255), (0, 130, 800, 400))
    pg.draw.line(Screen, (0, 0, 0), (100, 270), (700, 270), 5)
    pg.draw.line(Screen, (0, 0, 0), (100, 460), (700, 460), 5)
    
    bus_img = pg.image.load('./bus_blue.png')
    bus_img = pg.transform.scale(bus_img, (100, 50))
    if not bus[0][0] == 0:
        for i in range(int(bus[0][0])+1):
            pg.draw.circle(Screen, (0, 0, 0), (600/int(bus[0][0])*i+100, 270), 5)
    else:
        for i in range(2):
            pg.draw.circle(Screen, (0, 0, 0), (600/1*i+100, 270), 5)
    if int(bus[0][0]) > 0:
        Screen.blit(bus_img, (60, 220))
        font_render(30, b_num[0], (100 - (len(b_num[0][0])*10), 180), (0, 0, 0))
    elif int(bus[0][0]) == 0:
        Screen.blit(bus_img, (360, 220))
        font_render(30, b_num[0], (360, 180), (0, 0, 0))
    font_render(25, b_st, (670, 290), (0, 0, 0))
    font_render(25, bus[0][1], (30, 300), (0, 0, 0))

    if not bus[1][0] == 0:
        for i in range(int(bus[1][0])+1):
            pg.draw.circle(Screen, (0, 0, 0), (600/int(bus[1][0])*i+100, 460), 5)
    else:
        for i in range(2):
            pg.draw.circle(Screen, (0, 0, 0), (600/1*i+100, 460), 5)
    if int(bus[1][0]) > 0:
        Screen.blit(bus_img, (60, 410))
        font_render(30, b_num[1], (100 - (len(b_num[1][0])*10), 370), (0, 0, 0))
    elif int(bus[1][0]) == 0:
        Screen.blit(bus_img, (360, 410))
        font_render(30, b_num[1], (360, 370), (0, 0, 0))
    font_render(25, b_st, (670, 480), (0, 0, 0))
    font_render(25, bus[1][1], (30, 480), (0, 0, 0))

    font_render(25, f'버스도착정보({b_st})', (250, 130), (0, 0, 0))
    font_render(25, f"뉴스: '{news}'", (50, 550), (0, 0, 0))
    
    n = 0
    num = 0
    
    if loop % 100 == 0:
        bus.clear()
        f = open('config.txt', 'r', encoding='utf-8')
        t = f.read().split(':')

        b_st = t[1]
        b_id = t[2]
        f.close()
        b_info(b_id)
        loop = 0
        
    num = 0
    
    
    loop += 1
    time.sleep(0.1)
    pg.display.update()
pg.quit()
