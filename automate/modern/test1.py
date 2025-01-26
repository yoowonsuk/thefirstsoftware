import streamlit as st
import pandas

data = {
        'Series_1':[1,3,4,5,6],
        'Series_2':[10,30,40,100,25]
}

df = pandas.DataFrame(data)

st.title('Our First Streamlit App')
st.subheader('Introducing Streamlit in Automate Everything with Python')
st.write('''This is our first Web App.
        Enjoy it!
        ''')
st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider = st.slider('Celsius')
st.write(myslider, 'in Fahrenheit is', myslider * 9/5 + 32)

#streamlit run main.py
#create .replit => run="streamlit run main.py"  otherwise python main.py
#if you want deploy publicly, github -> version control in replit ->  share.streamlit.io -> continue with github -> New app from existing repo
