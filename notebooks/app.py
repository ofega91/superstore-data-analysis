import pandas as pd
import streamlit as st

df_usuarios = pd.read_csv("usuarios_api.csv")
st.title("Usuarios de la API")
st.dataframe(df_usuarios)