# import module
import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("Hi there, Hello")

#headers
st.header("This is a header")

#markdown
st.markdown("### This is a markdown header")



#text
text = st.text_input("This is a text input")

col1, col2 = st.columns(2)

with col1:
    st.write("This is column 1")
    #slider
    slide = st.slider("This is a slider", min_value=0, max_value=100)
    #writing
    

with col2:
    st.write("the value of this red[slider] is at ", slide)

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))


st.subheader("st.area_chart_random")
st.area_chart(data=df, x=None, y=None, x_label=None, y_label=None, color=None, stack=None, width=None, height=None, use_container_width=True)

with st.sidebar:
    st.header("this is a sidebar")
    st.write("this was my first time developing this, kinda fun actually")
