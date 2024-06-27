import pandas as pd
import matplotlib.pyplot as plt
import warnings

# 그래프 한국어 폰트
plt.rc("font", family="Malgun Gothic")
# 경고문 삭제
warnings.filterwarnings("ignore")


def get_exchange_rate_data():
    df_rates = pd.DataFrame()
    for page_num in range(1, 11):
        url = f"https://land.naver.com/news/trendReport.naver?page={page_num}"
        data = pd.read_html(url)
        df = data[0]
        temp = df.copy()

        # % 를 공백( )으로 바꾸
        df_temp = temp["제목"].str.replace("%", "")

        # 전국, 서울, 수도권 지우
        regions = ["전국", "서울", "수도권"]
        for region in regions:
            df_temp = df_temp.str.replace(region, "")

        # ']'를 기준으로 나누기. expand=True를 이용해 컬럼을 완전히 나눔.
        df_temp = df_temp.str.split("]", expand=True)

        # , 를 기준으로 나누기
        df_temp = df_temp[1].str.split(",", expand=True)

        # object인 타입을 float 형식으로 변환
        df_temp = df_temp.astype(float)

        # regions가 가지고 있는 값을 컬럼의 이름으로 temp에 생성
        temp[regions] = df_temp

        # df_rate 생성
        df_rate = temp[["등록일"] + regions + ["번호"]]

        df_rates = pd.concat([df_rates, df_rate])

    df_rates = df_rates[::-1].reset_index(drop=True)
    print(df_rates)
    df_rates.head(30).plot(x="등록일", y=["전국", "서울", "수도권"], figsize=(15, 6))
    plt.show()

    month_df_rates = df_rates.copy()
    year_df_rates = df_rates.copy()

    month_rate_data_view(month_df_rates)
    year_rate_data_view(year_df_rates)


# 월별 그룹화 추이 분석
def month_rate_data_view(df_rates):
    df_rates["등록일"] = (
        df_rates["등록일"].str.replace(".", "").astype("datetime64[ms]")
    )
    df_rates["월"] = df_rates["등록일"].dt.month
    month_in = int(input("검색할 월 입력: "))

    month_df = df_rates.loc[
        df_rates["월"] == month_in, ["등록일", "전국", "서울", "수도권", "번호"]
    ].reset_index(drop=True)
    print(month_df.head(20))

    month_df_chart = month_df.copy()
    month_df_chart = month_df_chart.set_index("등록일")
    month_df_chart[["전국", "서울", "수도권"]].plot(
        figsize=(15, 6), title="exchange rate"
    )
    plt.show()


# 년도별 추이 분석
def year_rate_data_view(df_rates):
    df_rates["등록일"] = (
        df_rates["등록일"].str.replace(".", "").astype("datetime64[ms]")
    )
    df_rates["년"] = df_rates["등록일"].dt.year
    year_in = int(input("검색할 년 입력: "))

    year_df = df_rates.loc[
        df_rates["년"] == year_in, ["등록일", "전국", "서울", "수도권", "번호"]
    ].reset_index(drop=True)
    print(year_df.head(20))

    year_df_chart = year_df.copy()
    year_df_chart = year_df_chart.set_index("등록일")
    year_df_chart[["전국", "서울", "수도권"]].plot(
        figsize=(15, 6), title="exchange rate"
    )
    plt.show()


get_exchange_rate_data()
