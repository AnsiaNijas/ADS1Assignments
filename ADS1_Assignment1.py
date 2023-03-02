# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 20:18:52 2023

@author: ansia
"""

import pandas as pd
import matplotlib.pyplot as plt


def readLinePlotData() :
  df_Food_Prices = pd.read_excel("Food_Prices_For_Nutrition.xlsx")
  df_Food_Prices_updated=df_Food_Prices.iloc[0:4,:]
  return df_Food_Prices_updated    
    
    
    
def linePlot(df) :
    df_Food_Prices_updated=df
    plt.figure()
    plt.plot(df_Food_Prices_updated['Time'], df_Food_Prices_updated["Iran, Islamic Rep. [IRN]"], linestyle='-', label="Iran")
    plt.plot(df_Food_Prices_updated['Time'], df_Food_Prices_updated["Middle East & North Africa [MEA]"],linestyle='-.', label="Middle East & North Africa")
    plt.plot(df_Food_Prices_updated['Time'], df_Food_Prices_updated["China [CHN]"], label="China")
    plt.plot(df_Food_Prices_updated['Time'], df_Food_Prices_updated["United Kingdom [GBR]"],linestyle=':', label="United Kingdom")
    plt.plot(df_Food_Prices_updated['Time'], df_Food_Prices_updated["Nigeria [NGA]"],linestyle='--', label="Nigeria")
    
    plt.ylim(-20,400)
    plt.xlim(2017,2020)
    plt.xticks([2017,2018,2019,2020],[2017,2018,2019,2020])
    plt.xlabel("Year")
    plt.ylabel("Number of People (millions")
    plt.title("Millions of people unable to afford a healthy diet")
    plt.legend(loc='upper right')
    plt.savefig('LinePlot.jpg')
    plt.show()
    return
   
    
   

if __name__== "__main__" :
    linePlot(readLinePlotData())





