import streamlit as st
import pandas as pd
import numpy as np

st.title('To divide two numbers')

a = st.number_input("A")

b = st.number_input("B")

if(b==0):
    st.write('Cannot divide by zero')
else:
    st.write(a/b)