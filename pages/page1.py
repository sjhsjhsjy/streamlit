import streamlit as st
import pandas as pd
name =st.text_input(
    label='이름을 입력하세요',
    placeholder='홍길동'
)

button = st.button("보내기")
if button:
    st.write(':blue[메세지]를 보냈습니다.🎁')

data = pd.DataFrame({
        'number':[10101,10102,10103,10104],
        'name':['kim','iee','choi','park'],
        'score':[85,92,100,70]})
st.download_button(
    label='성적다운로드',
    data=data.to_csv(),
    file_name='sample.csv',
    mime='text/csv'
)
agree= st.checkbox('개인정보수집 동의 하십니가?')
if agree:
    st.write('동의해주셔서 감사합니다. :100:')
mbti = st.radio(
    '당신의 명품브랜드를 좋아하나요?',
    ('네','아니요','선택지 없음'),
    index=2
)

if mbti=='네':
    st.write('당신의 명품브랜드와 콜라보한 제품을 사는 것을 추천합니다.')
elif mbti =='아니요':
    st.write('당신은 기본을 좋아하나요?')
else:
    st.write(':red[선택 하세요 제발]')

options=st.multiselect(
    '당신이 좋아하는 휴대폰 브랜드',
['삼성','애플','lg','중궈','[]'],
['[]']
)
st.write(f'당신의 선택은: :red[{options}]입니다.')

valuses =st.slider(
    '돈:sparkles:',
    30000,5000000,(30000,5000000))
st.write('선택범위:',valuses)

number =st.number_input(
    label='나이를 입력해주세요.',
    min_value=10,
    max_value=100,
    value=30,
    step=1
)
st.write('당신의 나이는: ',number)


st.title('당신이 중요하다 생각한는 휴대폰')


image_path = '4423898.png'
st.image(image_path)

ppt = st.radio(
    '다음중 고르세요',
    ('디자인','가격','성능','기술'),
    index=2
)

if ppt=='디자인':
    st.write('당신이 선택한것은 디자인')
elif ppt =='가격':
    st.write('당신이 선택한것은 가격')
elif ppt =='성능':
    st.write('당신의 선택한것은 성능')
else:
    st.write('당신의 선택한것은 기술')

import streamlit as st


st.balloons()