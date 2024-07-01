# 파일 불러오기
import pandas as pd
import numpy as np
import streamlit as st

def Meteor_shower():
    meteorshowers = pd.read_csv("data/meteorshowers.csv")
    moonphases = pd.read_csv("data/moonphases.csv")
    constellations = pd.read_csv("data/constellations.csv")
    cities = pd.read_csv("data/cities.csv")

    # 딕셔너리(dic) 형식으로 1~12월의 정보를 months에 저장
    months = {'january' : 1, 'february' : 2, 'march' : 3, 'april' : 4, 'may' : 5, 'june' : 6, 'july' : 7, 'august' : 8, 'september' : 9, 'october' : 10, 'november' : 11, 'december' : 12}

    # meteorshowers의 startmonth 정보를 months와 매칭시켜 값을 변경시킴
    meteorshowers['startmonth'] = meteorshowers['startmonth'].map(months)
    meteorshowers['bestmonth'] = meteorshowers['bestmonth'].map(months)
    meteorshowers['endmonth'] = meteorshowers['endmonth'].map(months)

    # startday 컬럼 생성 후 숫자 데이터를 날짜 데이터로 변환
    meteorshowers['startday'] = pd.to_datetime(2020 * 10000 + meteorshowers['startmonth'] * 100 + meteorshowers['startday'], format = '%Y%m%d')

    # 미션 1) meteorshowers 데이터프레임에 'enddate' 컬럼 생성
    meteorshowers['enddate'] = pd.to_datetime(2020 * 10000 + meteorshowers['endmonth'] * 100 + meteorshowers['endday'], format = '%Y%m%d')

    moonphases['month'] = moonphases['month'].map(months)

    # 미션 2) moonphases 데이트프레임에 'date' 컬럼 생성
    moonphases['date'] = pd.to_datetime(2020 * 10000 + moonphases['month'] * 100 + moonphases['day'], format='%Y%m%d')

    phases = {'first quarter' : 0.5, 'full moon' : 1, 'third quarter' : 0.5, 'new moon' : 0}

    # moonphases['percentage'] 컬럼을 생성하며 moonphases['moonphase'] 딕셔너리(phases)와 매핑
    moonphases['percentage'] = moonphases['moonphase'].map(phases)

    # drop을 이용하여 필요가 없는 데이터 삭제, inplace=True를 이용해 실제 데이터에 적용
    moonphases.drop(['month', 'day', 'moonphase', 'specialevent'], axis=1, inplace=True)

    # constellations와 meteorshowers의 정보 중 필요없는 부분을 제거
    constellations.drop('besttime', axis=1, inplace=True)
    meteorshowers = meteorshowers.drop(['startmonth', 'startday', 'endmonth', 'endday', 'hemisphere'], axis=1)

    # 데이터프레임의 한 행 씩 가져와 index와 row에 넣어준다.
    # pandas에 있는 isnull을 사용하여 선택한 부분에 NaN(비어있는 값)이 있다면 1 반환
    for index, row in moonphases.iterrows():
        pd.isnull(row['percentage'])

    # 다음 활용을 위해 복사
    moonphases1=moonphases.copy()

    # 비어있는 값을 lastphase로 채워주며 비어있지 않다면 lastphase를 index 값으로 채워주기
    lastphase = 0
    for index, row in moonphases.iterrows():
        if pd.isnull(row['percentage']):
            moonphases.loc[index, 'percentage'] = lastphase
        else:
            lastphase = moonphases.loc[index, 'percentage']

    # cities의 city 값과 latitude 값만 확인
    cities[['city', 'latitude']]

    # cities의 city값이 Abu Dhabi의 정보를 가져오는데 latitude 값만 확인
    cities[cities['city'] == 'Abu Dhabi']['latitude']

    # 위와 동일한 기능
    cities.loc[cities['city'] == 'Abu Dhabi', 'latitude']

    incity = input('city: ')
    print(predict_best_shower_viewing(incity, cities, constellations))

# 위도 가져오는 사용자 정의 함수
# 함수를 사용하여 입력 된 city(도시의 이름)을 받아 위도를 반환시켜준다.
# iloc를 사용하여 첫 번째 값을 선택한다.
def predict_best_shower_viewing(city, cities, constellations):
    shower_string = ""
    if city not in cities.values:
        shower_string = city + "는 현재 예측할 수 없습니다."
        return shower_string

    latitude = cities.loc[cities['city'] == city, 'latitude'].iloc[0]

    constellations_list = constellations.loc[(constellations['latitudestart'] >= latitude) & (constellations['latitudeend'] <= latitude), 'constellation'].tolist()

    if not constellations_list:
        shower_string = city + "에서는 볼 수 있는 유성우는 없습니다."
        return shower_string
    
    shower_string = city + "에서는 유성우를 볼 수 있습니다."
    return shower_string

if __name__ == '__main__':
    Meteor_shower()
# incity = st.text_input('city: ')
# st.write(predict_best_shower_viewing(incity))

