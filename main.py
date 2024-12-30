import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>Welcome! To The Portfolio</h1>", unsafe_allow_html=True)

s1, s2 = st.columns(2)

s1.image("images/photo.png")
s2.title("ADIL ALI")
content = '''I'm a Python Developer and a Data Scientist with a passion for learning and teaching. You are a Python Developer and Data Scientist with a strong passion for learning and teaching. Your expertise lies in developing robust Python applications and leveraging data science techniques to extract meaningful insights from complex datasets. You have a solid understanding of various Python frameworks and libraries, which allows you to build efficient and scalable solutions. Your portfolio showcases a range of projects that highlight your ability to solve real-world problems using Python.'''
s2.info(content)

st.write("Below you can find some of the Apps I have built in Python. Feel free to contact me.")

data = pd.read_csv("data.csv", sep=";")
# print(data)
# print(len(data))

length = int(len(data)/2)
print(length)

s3, s4, s5 = st.columns([1.5,0.4,1.5])

with s3:
    for i, d in data[:length].iterrows():
        st.header(d["title"])
        st.write(d['description'])
        st.image(f"images/{d['image']}")
        st.write(f"[Source Code]({d['url']})")

with s5:
    for index, data in data[length:].iterrows():
        st.header(data["title"])
        st.write(data['description'])
        st.image(f"images/{data['image']}")
        st.write(f"[Source Code]({data['url']})")

