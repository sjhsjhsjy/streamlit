import streamlit as st
st.title('새탭만들기!')

image_path = 'qqq.jpg'
st.image(image_path)

ppt = st.radio(
    '위 사람의 이름은?',
    ('이서','레이','안유진','장원영'),
    index=2
)

if ppt=='이서':
    st.write('당신의 :blue[틀니]시네요')
elif ppt =='레이':
    st.write('당신의 :green[틀니]시네요')
elif ppt =='안유진':
    st.write('당신의 :orange[틀니]으으으으ㅡ으으으ㅡ으으ㅡㅡ')
else:
    st.write('당신의 :red[정답]이시네요')

import streamlit as st

st.balloons()