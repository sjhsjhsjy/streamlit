import streamlit as st
import random
import datetime
name =st.text_input(
    label='이름을 입력하세요',
    placeholder='홍길동'
)

st.title(f':red[{name}]님의로또')
button=st.button('1등은 나의것!')

if button:
    for i in range(1,6):
        roto = set()
        while len(roto)< 6:
            number = random.randint(1,100)
            roto.add(number)
        roto = list(roto)
        roto.sort()
        st.subheader(f'{i}, 행운의 번호: :green[{roto}]')
    st.write("로또번호가 생성된시각:", datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
st.balloons()
