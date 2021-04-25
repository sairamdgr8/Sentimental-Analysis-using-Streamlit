# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 22:13:18 2021

@author: Bunnyyyyyyy
"""

# import the streamlit library
import streamlit as st
from textblob import TextBlob 
from PIL import Image

# give a title to our app
st.title('SAI- Made Sentimental Analysis')

# TAKE WEIGHT INPUT in kgs

st.subheader("Enter your text to verify the tweet")
tweet  = st.text_input(" ", "please type here...")



# compare status value
x=TextBlob(tweet)
sentiment_polarity=x.sentiment.polarity

# check if the button is pressed or not
if(st.button('Submit')):
    
    #result = x.title()
    
    if(sentiment_polarity < 0):
        st.error("The given tweet looks Negative")
    elif(sentiment_polarity ==0):
        st.warning("The given tweet looks Neutral")
    elif(sentiment_polarity > 0 ):
        st.success("The given tweet looks Positive ")
        
st.subheader("Sairamdgr8 -- An Aspiring Full Stack Data Engineer")
image = Image.open('dev - Copy.jpg')
st.image(image, caption='Developed by Sai')
st.text('')
st.subheader('Connect  me... ')
#st.subheader('https://www.linkedin.com/in/sairam-p-l/')
#st.subheader('https://medium.com/@sairamdgr8')
#st.subheader('https://www.facebook.com/bunnydgr8')
"""
[![Linkledn Follow](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sairam-p-l/) https://www.linkedin.com/in/sairam-p-l/
       
[![medium Follow](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@sairamdgr8)  https://medium.com/@sairamdgr8 
        
[![facebook Follow](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/bunnydgr8) https://www.facebook.com/bunnydgr8
        
![Gmail Follow](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white) sairamdgr8@gmail.com
   
"""
        
