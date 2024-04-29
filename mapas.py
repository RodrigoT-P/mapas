import streamlit as st
import pandas as pd
import numpy as np

map_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [20.635898057239174, -100.3527739587572],
   columns=['lat', 'lon'])

st.dataframe(map_data)
st.map(map_data)
