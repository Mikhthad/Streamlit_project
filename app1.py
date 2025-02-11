import streamlit as st
import joblib
import pandas as pd

model = joblib.load('Canada_PCI.pki')
house = joblib.load('house100.pki')

st.sidebar.title("Prediction apps")
page=st.sidebar.selectbox("pages",options=["Per Capita Income","house"])

if page=="Per Capita Income":
    st.subheader('Per Capita income of canada')
    st.write('this is a simple web app to predict the per capita income of canada')

    year = st.number_input('Enter the year')

    prediction = model.predict([[year]])
    prediction= pd.Series(prediction[0])

    if st.button('predict'):
        st.success(f'The per capita income of canada in the year {year} is {round(prediction[0],2)}')


if page == 'house':
    st.subheader('House price prediction')
    
    sq = st.number_input('Enter Square_feet')
    bd = st.number_input('enter bedrroms')
    age = st.number_input('age')

    predicts = house.predict([[sq,bd,age]])
    pd = pd.Series(predicts[0])
    
    b = st.button('predict')
    if b:
        st.success(f'predicted price of the given data is {pd[0]}')
# st.write(prediction[0])