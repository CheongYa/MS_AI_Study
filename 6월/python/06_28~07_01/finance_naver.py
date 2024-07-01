# pandas 이용
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import streamlit as st # 추가

def get_exchange_rate_data(code, currency_name):
    df = pd.DataFrame()
    for page_num in range(1, 6):
        base_url = f"https://finance.naver.com/marketindex/exchangeDailyQuote.naver?marketindexCd=FX_{code}KRW&page={page_num}"
        temp = pd.read_html(base_url, encoding="cp949", header=1)

        # concat을 이용해 데이터 합치기
        df = pd.concat([df, temp[0]])

    total_rate_data_view(df, code, currency_name)

def total_rate_data_view(df, code, currency_name):
    # 그래프 한국어 폰트
    plt.rc('font', family='Malgun Gothic')

    # 원하는 열만 출력
    df_total = df[['날짜', '매매기준율', '사실 때', '파실 때', '보내실 때', '받으실 때']]

    # 데이터 표시
    # print(f"=== {currency_name[code_in - 1]} - {code} ===")
    st.subheader(f"{currency_name} : {code}")
    # print(df_total.head(20))
    st.dataframe(df_total.head(20))

    # 전체 차트 작성
    df_total_chart = df_total.copy()
    # index 값으로 날짜를 넣어준다.
    df_total_chart = df_total_chart.set_index('날짜')
    # [::-1]을 넣어줌으로서 역순으로 변경
    df_total_chart = df_total_chart[::-1]

    # 매매기준율을 값으로 잡고 그래프를 생성
    ax = df_total_chart['매매기준율'].plot(figsize=(15, 6), title = 'exchange rate')
    fig = ax.get_figure()
    st.pyplot(fig)

    # month_rate_data_view(df_totla)

# def month_rate_data_view(df_totla):
#     # 월 별 검색
#     # 날짜 컬럼의 형 변환(문자열 -> 날짜)
#     df_totla['날짜'] = df_totla['날짜'].str.replace(".", "").astype('datetime64[ms]') # str을 안 붙이면 하나만 일 때이다. str을 붙여야 전부 다 바뀐다.

#     # 월 컬럼 생성
#     df_totla['월'] = df_totla['날짜'].dt.month
#     month_in = int(input("검색할 월 입력: "))

#     #drop=True를 붙여야지만 인덱스를 리셋 시키면서 새로 생성하지 않음
#     month_df = df_totla.loc[df_totla['월'] == month_in, ['날짜', '매매기준율', '사실 때', '파실 때', '보내실 때', '받으실 때']][::-1].reset_index(drop=True)
#     print(f"=== {currency_name[code_in - 1]} - {code} ===")
#     print(month_df.head(20))

#     month_df_chart = month_df.copy()
#     month_df_chart = month_df_chart.set_index('날짜')
#     month_df_chart['매매기준율'].plot(figsize=(15, 6), title = 'exchange rate')
#     plt.show()

def exchange_main():     
    # 미국, 유럽연합, 일본 심볼
    currency_symbols_name = {'미국 달러':'USD', '유럽연합 유로':'EUR', '일본 엔':'JPY'}
    currency_name = st.selectbox("통화 선택", currency_symbols_name.keys())
    code = currency_symbols_name[currency_name]

    clicked = st.button("환율 데이터 가져오기")
    if clicked:
        get_exchange_rate_data(code, currency_name)

