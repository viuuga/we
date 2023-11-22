import streamlit as st
import sqlite3

st.markdown("""
<style>
.st-emotion-cache-6q9sum.ef3psqc4
{
    visibility: hidden;
}
.st-emotion-cache-ch5dnh.ef3psqc5
{
    visibility: hidden;
}
.st-br.st-bq.st-as.st-at.st-b7.st-b6.st-bs.st-bt.st-bu.st-bv.st-av.st-aw.st-ax.st-ay.st-bj.st-bw.st-bx.st-by.st-bz.st-c0.st-c1.st-c2
{
    visibility: hidden;
}
.st-emotion-cache-cio0dv.ea3mdgi1
{
    visibility: hidden;
}
.st-emotion-cache-4z1n4l.en6cib65
{
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


st.sidebar.success("Вы на первой странице") 
DataBase = sqlite3.connect('nouts.db')

text1 = st.text_area("notebook", key=1, height=100, max_chars=3600)
text_noote = text1
c = DataBase.cursor()
c.execute("""CREATE TABLE note_5 (
    noote text       
)""")
DataBase.commit()

st.text("NONE")
DataBase.close()