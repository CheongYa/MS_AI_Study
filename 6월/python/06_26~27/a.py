import pandas as pd
import numpy as np
import streamlit as st

def Meteor_Shower():
    cities = pd.read_csv('data/cities.csv')
    constellations = pd.read_csv('data/constellations.csv')
    meteorshowers = pd.read_csv('data/meteorshowers.csv')
    moon_phases = pd.read_csv('data/moonphases.csv')

    months = {'january' : 1, 'february' : 2, 'march' : 3, 'april' : 4, 'may' : 5, 'june' : 6, 
            'july' : 7, 'august' : 8, 'september' : 9, 'october' : 10, 'november' : 11, 'december' : 12}
    meteorshowers['startmonth'] = meteorshowers['startmonth'].map(months)
    meteorshowers['bestmonth'] = meteorshowers['bestmonth'].map(months)
    meteorshowers['endmonth'] = meteorshowers['endmonth'].map(months)

    meteorshowers['startdate'] = 2020*10000 + meteorshowers['startmonth']*100 + meteorshowers['startday']
    meteorshowers['startdate'] = pd.to_datetime(meteorshowers['startdate'], format='%Y%m%d')

    meteorshowers['enddate'] = pd.to_datetime(2020*10000 + meteorshowers['startmonth']*100 + meteorshowers['startday'], format='%Y%m%d')

    moon_phases['month'] = moon_phases['month'].map(months)
    moon_phases['date'] = pd.to_datetime(2020*10000 + moon_phases['month']*100 + moon_phases['day'], format='%Y%m%d')


    # make dictionary
    phases = {np.nan:np.nan, 'first quarter':0.5, 'full moon':1, 'third quarter':0.5, 'new moon':0}
    # mapping
    moon_phases['percentage'] = moon_phases['moonphase'].map(phases)
    moon_phases = moon_phases.drop(['month','day','moonphase','specialevent'], axis=1)

    meteorshowers = meteorshowers.drop(['startmonth','startday','endmonth','endday','hemisphere'], axis=1)
    constellations = constellations.drop(['besttime'], axis=1)

    moon_phases_temp = moon_phases.copy()
    lastphase = 0
    for index, row in moon_phases.iterrows():
        if(pd.isnull(row['percentage'])):
            moon_phases.loc[index, 'percentage'] = lastphase
            # at을 통한 접근도 가능
            # moon_phases.at[index, 'percentage'] = lastphase
        else:
            lastphase = moon_phases.loc[index, 'percentage']

# 위도 가져오는 사용자 정의 함수
def Find_Latitude(city):
    # iloc[index]: loc가 series형태로 출력되므로 값만 불러오기 위해 사용
    return cities.loc[cities['city']==city, 'latitude'].iloc[0]

def Predict_Best_Shower_Viewing(city):
    shower_string = ""
    if city not in cities.values:
        shower_string = city + "는 현재 예측할 수 없습니다."
        return shower_string

    latitude = Find_Latitude(city)
    constellations_list = constellations.loc[(constellations['latitudestart']>=latitude) & (constellations['latitudeend']<=latitude), 'constellation'].tolist()

    if not constellations_list:
        shower_string = city + "에서는 볼 수 있는 유성우는 없습니다."
        return shower_string
    
    shower_string = city + '에서 유성우를 볼 수 있습니다.'
    
    return shower_string
    
incity = st.text_input('CITY(ENG): ')
st.write(Predict_Best_Shower_Viewing(incity))
