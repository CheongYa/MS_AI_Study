import streamlit as st
import finance_naver

# 사이드바 화면
st.sidebar.header("로그인")
st.sidebar.text_input("아이디 입력")
user_password = st.sidebar.text_input("패스워드 입력", value="1234", type='password')

# 사이드바에 있는 비밀번호에 1234를 작성 시 나오는 메뉴 선택 생성
if user_password == '1234':
    st.sidebar.header("청야의 포트폴리오")
    opt_data = ['', '환율 조회', '따릉이', '유성우']
    menu = st.sidebar.selectbox("메뉴 선택", opt_data, index=0) # index = opt_data에 있는 것 중 처음에 보일것
    st.sidebar.write("선택한 메뉴: ", menu)

    if menu == '환율 조회':
        st.subheader("환율 조회")
        finance_naver.exchange_main()
    elif menu == '따릉이':
        st.subheader("따릉이 데이터 분석")
        finance_naver.exchange_main()
    elif menu == '유성우':
        st.subheader("유성우 데이터 분석")
        finance_naver.exchange_main()
    else:
        st.subheader("환영합니다!")
        


# 메인 화면
st.subheader("청야의 개발 노트")
