# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 20:18:52 2023

@author: ansia
"""

import pandas as pd
import matplotlib.pyplot as plt


def readLinePlotData():
  df_Food_Prices = pd.read_excel("Food_Prices_For_Nutrition.xlsx")
  df_Food_Prices_updated = df_Food_Prices.iloc[0:4, :]
  return df_Food_Prices_updated


def readPiePlotData():
  df_Food_Prices = pd.read_excel("Food_Prices_For_Nutrition.xlsx")
  df_Food_Prices_t = pd.DataFrame.transpose(df_Food_Prices)
  df_Food_Prices_updated = df_Food_Prices_t.iloc[[82, 108, 109, 185]]
  header = df_Food_Prices.iloc[0:11, 4].astype(str)
  df_Food_Prices_updated.columns = header
  return df_Food_Prices_updated


def readStackedBarPlotData():
    df_illiterate_population = pd.read_csv("Youth illiterate population.csv")
    return df_illiterate_population


def linePlot(df):
    df_Food_Prices_updated = df
    plt.figure()
    plt.plot(df_Food_Prices_updated['Time'],
             df_Food_Prices_updated["Iran, Islamic Rep. [IRN]"], linestyle='-', label="Iran")
    plt.plot(df_Food_Prices_updated['Time'], df_Food_Prices_updated["Middle East & North Africa [MEA]"],
             linestyle='-.', label="Middle East & North Africa")
    plt.plot(df_Food_Prices_updated['Time'],
             df_Food_Prices_updated["China [CHN]"], label="China")
    plt.plot(df_Food_Prices_updated['Time'], df_Food_Prices_updated["United Kingdom [GBR]"],
             linestyle=':', label="United Kingdom")
    plt.plot(df_Food_Prices_updated['Time'],
             df_Food_Prices_updated["Nigeria [NGA]"], linestyle='--', label="Nigeria")
    plt.ylim(-20, 400)
    plt.xlim(2017, 2020)
    plt.xticks([2017, 2018, 2019, 2020], [2017, 2018, 2019, 2020])
    plt.xlabel("Year")
    plt.ylabel("Population (millions")
    plt.title(
        "Population who cannot afford a healthy diet in past 4 years for different countries")
    plt.legend(loc='upper right')
    plt.savefig('LinePlot.jpg')
    plt.show()
    return


def piePlot(df):
    food_prices = df
    names = ["High income [HIC]", "Low income [LIC] ", "Lower middle income [LMC]",
             "Upper middle income [UMC]"]
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.pie(food_prices['2019.0'], autopct='%1.1f%%', labels=names)
    plt.title("Population who cannot afford a healthy diet (millions) in 2020")
    plt.subplot(2, 1, 2)
    plt.pie(food_prices['2020.0'], autopct='%1.1f%%', labels=names)
    plt.title("Population who cannot afford a healthy diet (millions) in 2019")
    plt.tight_layout()
    plt.savefig("PiePlot.png")
    plt.show()
    return


def stackedBarPlot(df):
    illiterate_population = df
    plt.figure()
    plt.bar(illiterate_population["Time"],
            illiterate_population["Youth illiterate population, 15-24 years, male (number) [UIS.LP.AG15T24.M]"], width=.5, label="Male")
    plt.bar(illiterate_population["Time"], illiterate_population["Youth illiterate population, 15-24 years, female (number) [UIS.LP.AG15T24.F]"],
            bottom=illiterate_population["Youth illiterate population, 15-24 years, male (number) [UIS.LP.AG15T24.M]"], width=.5, label="Female")
    plt.title("Youth illiterate population")
    plt.xlabel("Year")
    plt.ylabel("Population (millions)")
    plt.legend()
    plt.savefig("StackedBarPlot.png")
    plt.show()
    return


if __name__ == "__main__":
    linePlot(readLinePlotData())
    piePlot(readPiePlotData())
    stackedBarPlot(readStackedBarPlotData())
