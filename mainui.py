import streamlit as st
import pandas as pd
button = st.button("보내기")
if button:
    st.write(':blue[메세지]를 보냈습니다.🎁')
import streamlit as st
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
    '당신의 바보 입니까?',
    ('니거','바보','선택지 없음','istj'),
    index=2
)

if mbti=='니거':
    st.write('당신의 :blue[니거]이시네요')
elif mbti =='바보':
    st.write('당신의 :green[바보]이시네요')
elif mbti =='istj':
    st.write('당신의 :orange[병신]으으으으ㅡ으으으ㅡ으으ㅡㅡ')
else:
    st.write('당신의 :red[당신은 천재 알고싶네요]이시네요')

options=st.multiselect(
    '당신이 좋아하는 과일?',
['망고','오렌지','사과','바나나'],
['망고']
)
st.write(f'당신의 선택은: :red[{options}]입니다.')

valuses =st.slider(
    '키:sparkles:',
    140.0,190.0,(165.0,175.0))
st.write('선택범위:',valuses)

name =st.text_input(
    label='이름을 입력하세요',
    placeholder='홍길동'
)
t =st.text_input(
    label='여행지리',
    placeholder='여행기간'
)
st.write(f'{name}이 선택한 여행지는 :violet[{t}]')

number =st.number_input(
    label='나이를 입력해주세요.',
    min_value=10,
    max_value=100,
    value=30,
    step=5
)
st.write('당신의 나이는: ',number)

path = '인구.csv'
data1 =pd.read_csv(path, encoding='cp949')
print(data1)
st.dataframe(data1, use_container_width=True)

fig3, ax = plt.subplots()
plt.title("출생아수 추이")
ax.bar(data1['시점'], data1['출생아수(명)'])
plt.xlabel("연도")
plt.ylabel("출생아수(단위: 명)")
for i, txt in enumerate(data1['출생아수(명)']):
    ax.text(data1['시점'][i], txt, str (txt), ha= 'center', va='bottom')
ax.set_ylim(200000, 500000)
st.pyplot(fig3)

fig4, ax = plt.subplots()
plt.title("출생아수 추이")
ax.plot(data1['시점'], data1['출생아수(명)'], color="#DF013A", marker="*", linestyle='dotted')
plt.xlabel("연도")
plt.ylabel("출생아수(단위: 명)")

for i, txt in enumerate(data1['출생아수(명)']):
    ax.text(data1['시점'][i], txt, str (txt), ha= 'center', va='bottom')
ax.set_ylim(200000, 500000)
st.pyplot(fig4)

st.title('대구고등학교홈페이지 ')
st.title("('.')")
st.header('학교소개💋')
st.subheader('교육활동💕')
st.caption('학급마당🐱‍💻')
sample_code = '''
def function():
print('fuct')
'''
st.code(sample_code, language="python")
st.text('기본 텍스트')
st.markdown('streamlit은 **마크다운 문법을 지원**합니다.')
st.markdown("텍스트의 색상을 :green[초록색]으로,그리고 **:blue[파란색]** 볼트체로 설정할수있습니다.")
