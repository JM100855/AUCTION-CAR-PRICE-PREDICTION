import streamlit as st
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
from PIL import Image
import pandas as pd
import time
import matplotlib.pyplot as plt

pkl = open("random_forest_regression_model.pkl","rb")
random_forest_regression_model=pickle.load(pkl)

def Home():
    return render_template('This is WEB APP')


standard_to = StandardScaler()
def predicting(Present_Price,Kms_Driven,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual):
    prediction=random_forest_regression_model.predict([[Present_Price,Kms_Driven,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
    output=round(prediction[0],2)
    return output


def main():
    st.title("Auction Car Price Predictions")
    
    image = Image.open('mainpic.jpg')
    st.image(image, use_column_width=True)

    

    st.subheader("Whats Your Car's Age?")
    Year = st.slider("",min_value = 0,max_value=20,value = 5,step = 1)
    st.subheader("How much does it cost first hand?")
    Present_Price = st.text_input("","Type Here")
    

    st.subheader("Kilometers driven so far?")
    Kms_Driven = st.text_input("","Enter Here")
    

    st.subheader("Number of owners until now??")
    Owner = st.selectbox("",range(1,4),0)
    # st.write(Owner)
    st.subheader("What type of fuel does it run on?")
    fual = ("Petrol","Diesel", "CNG")
    fual_type = st.radio("", fual)
    if fual_type == "Petrol":
        Fuel_Type_Petrol = 1
        Fuel_Type_Diesel = 0
    elif fual_type == "Diesel":
        Fuel_Type_Petrol = 0
        Fuel_Type_Diesel = 1
    else:
        Fuel_Type_Petrol = 0
        Fuel_Type_Diesel = 0

    # st.write(Fuel_Type_Petrol)
    # st.write(Fuel_Type_Diesel)

    # Fuel_Type_Diesel = st.selectbox("Fual type is Diesel(Yes=1/No=0)",range(3),0)
    # Fuel_Type_Petrol = st.selectbox("Fual type is Petrol(Yes=1/No=0)",range(3))
    # Seller_Type_Individual = st.text_input("Are you a Dealer(0) or Individual(1)","Type Here")
    seller = ("Dealer", "Indivisual")

    # options = list(range(len(display)))
    st.subheader("Which are you, a Dealer or an Individual")

    Seller_Type_Individual = st.radio("",seller)
    if Seller_Type_Individual == "Indivisual":
         Seller_Type_Individual = 1
    else:
        Seller_Type_Individual = 0

    # st.write(Seller_Type_Individual)
    # Transmission_Mannual = st.text_input("Transmission Type(Manual=1/Automatic=0)","Type Here")
    # if Transmission_Mannual == Manual:
    #     Transmission_Mannual = 1
    # else:
    #     Transmission_Mannual = 0
    
    display = ("Automatic", "Manual")

    # options = list(range(len(display)))
    st.subheader("What is your car's transmission type?")

    Transmission_Mannual = st.radio("",display)
    if Transmission_Mannual == "Manual":
         Transmission_Mannual = 1
    else:
        Transmission_Mannual = 0

    # st.write(Transmission_Mannual)

    result=""
    if st.button("PREDICT"):
        
        if Present_Price == "Type Here":
            st.error("this is an error")
            st.text("Enter Showroom Price")

        if Kms_Driven == "Enter Here":
            st.text("Enter how many Kms drived")

        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete +1)
        result=predicting(Present_Price,Kms_Driven,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual)

    
    st.success('Selling Price of your Car : {} L'.format(result))
       
    st.balloons()

nav = st.sidebar.radio("Navigate",["Home", "Data"])
if nav == "Home":
    if __name__=="__main__":
        main()
    

if nav == "Data":
    st.title("Vehicle Dataset")
    st.subheader("I have taken a different data set from online")
    data = pd.read_csv("car data.csv")
    if st.checkbox("Show Table"):
        st.table(data)
    
    plt.show()
