import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")

# input for the x-axis and y-axis
x_axis = st.selectbox("Select the data for the X-axis",
             ("GDP", "Happiness", "Generosity"))
y_axis = st.selectbox("Select the data for the Y-axis",
             ("GDP", "Happiness", "Generosity"))

st.subheader(f"{x_axis} and {y_axis}")


# this function extracts data from the csv file
def extract():
    df = pd.read_csv("happy.csv")
    return df["happiness"], df["gdp"], df["generosity"]


happy, gdp, generosity = extract()
match x_axis:
    case "GDP":
        result_x = gdp
    case "Happiness":
        result_x = happy
    case "Generosity":
        result_x = generosity
match y_axis:
    case "GDP":
        result_y = gdp
    case "Happiness":
        result_y = happy
    case "Generosity":
        result_y = generosity


# displays the graph
figure = px.scatter(x=result_x, y=result_y,
                 labels={"x": f"{x_axis}", "y": f"{y_axis}"})
st.plotly_chart(figure)