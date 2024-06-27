# 다음 사이트에서 원하는 지역 날씨 정보 크롤링 하기
import requests
from bs4 import BeautifulSoup

def get_weather_daum(location):
    base_url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q="
    search_query = location + "+날씨"

    url = base_url + search_query

    html_weather = requests.get(url).text
    soup_weather = BeautifulSoup(html_weather, 'lxml')

    # select에서 .은 하위 클래스를 뜻한다
    txt_temp = soup_weather.select_one('strong.txt_temp').text
    txt_weather = soup_weather.select_one('span.txt_weather').text

    #dl의 dl_weather 안에 있는 dd의 정보
    dl_weather = soup_weather.select('dl.dl_weather dd')

    # 변수 하나씩 넣어주는 방식. for 문에서 append 방식을 사용해도 된다.
    [wind_speed, humidity, pm10] = [x.text for x in dl_weather]

    return txt_temp, txt_weather, wind_speed, humidity, pm10

location = input("조회할 도시 입력 : ")
txt_temp, txt_weather, wind_speed, humidity, pm10 = get_weather_daum(location)

print("----[현재 날씨 정보]----")
print(f"설정 지역 : {txt_temp}")
print(f"설정 지역 : {txt_weather}")
print(f'현재 풍속 : {wind_speed}\n현재 습도 : {humidity}\n미세번지 : {pm10}')