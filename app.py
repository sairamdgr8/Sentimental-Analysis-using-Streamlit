# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 22:13:18 2021

@author: Bunnyyyyyyy
"""

# import the streamlit library
import streamlit as st
from textblob import TextBlob 

# give a title to our app
st.title('SAI- Made Sentimental Analysis')

# TAKE WEIGHT INPUT in kgs
tweet  = st.text_input("Enter Your text to verify the tweet", "please type here...")



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
        
        