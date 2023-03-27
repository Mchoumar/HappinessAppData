import pandas as pd


# this function extracts data from the csv file
def extract():
    df = pd.read_csv("happy.csv")
    return df["happiness"], df["gdp"], df["generosity"]


def data_show(x_ax, y_ax):
    happy, gdp, generosity = extract()
    match x_ax:
        case "GDP":
            result_x = gdp
        case "Happiness":
            result_x = happy
        case "Generosity":
            result_x = generosity
    match y_ax:
        case "GDP":
            result_y = gdp
        case "Happiness":
            result_y = happy
        case "Generosity":
            result_y = generosity
    return result_x, result_x


if __name__ == "__main__":
    extract()
