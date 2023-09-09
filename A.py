import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc, font_manager

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