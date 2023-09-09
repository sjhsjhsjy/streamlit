import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc, font_manager
import numpy as np
import os
import matplotlib.font_manager as fm
data = pd.DataFrame({
    '이름': ['아이폰14p','아이폰14pm','ipad m2','s23u','s23+','s7+tab'],
    '싱글코어':[2518,2517,2489,1878,1870,1202],
    '멀티코어': [6379,6359,9404,4972,4958,3042]
})
st.dataframe(data, use_container_width=True)


font_dirs = [os.getcwd() + '/customFonts']
font_files = fm.findSystemFonts(fontpaths=font_dirs)

for font_file in font_files:
    fm.fontManager.addfont(font_file)
fm._load_fontmanager(try_read_cache=False)

plt.rc('font', family='NanumGothic')
fig1,  ax = plt.subplots()
plt.title("스마트폰 싱글코어 성능")

ax.bar(data['이름'],data['싱글코어'])
for p in ax.patches:
    ax.annotate(format(p.get_height(),'.1f'),
    (p.get_x() + p.get_width() / 2., p.get_height()),
    ha = 'center' , va ='center',
    xytext = (0,10),
    textcoords= 'offset points')
ax.set_ylim(0,3000)
st.pyplot(fig1)

fig2,  ax = plt.subplots()
plt.title("스마트폰 멀티코어 성능")
ax.bar(data['이름'],data['멀티코어'])
for p in ax.patches:
    ax.annotate(format(p.get_height(),'.1f'),
    (p.get_x() + p.get_width() / 2., p.get_height()),
    ha = 'center' , va ='center',
    xytext = (0,10),
    textcoords= 'offset points')
ax.set_ylim(0,11000)
st.pyplot(fig2)

