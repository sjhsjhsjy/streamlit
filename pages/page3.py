import streamlit as st
import datetime
name =st.text_input(
    label='이름을 입력하세요',
    placeholder='홍길동'
)
t =st.text_input(
    label='여행지',
    placeholder='여행기간'
)
g =st.text_input(
    label='여행기간',
    placeholder='몇일'
)

st.write(f'{name}이 선택한 여행지는 :violet[{t}] 여행기간은{g}입니다')

st.title(f':red[{name}]님의주식')

st.metric(label="온도", value="10℃", delta="1.2℃")
st.metric(label='삼성전자', value="61,100원", delta="-1200원")

col1, col2 , col3 = st.columns(3)
col1.metric(label="달러use", value="1,228원", delta="-12.00원")
col2.metric(label="일본JYP", value="958.63원", delta="-7.44원")
col3.metric(label="유럽연합", value="1,335.82원", delta="11.44원")

st.write("지금현재시각:", datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))


