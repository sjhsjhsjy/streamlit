import streamlit as st
import pandas as pd

st.title('streamlit dataframe')
dataframe = pd.DataFrame({
    'fist column':[ 1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})
st.dataframe(dataframe, use_container_width=False)
st.table(dataframe)

st.metric(label="온도", value="10℃", delta="1.2℃")
st.metric(label='삼성전자', value="61,100원", delta="-1200원")

col1, col2 , col3 = st.columns(3)
col1.metric(label="달러use", value="1,228원", delta="-12.00원")
col2.metric(label="일본JYP", value="958.63원", delta="-7.44원")
col3.metric(label="유럽연합", value="1,335.82원", delta="11.44원")