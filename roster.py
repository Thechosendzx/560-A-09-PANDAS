#https://goheels.com/sports/mens-basketball/roster
import pandas as pd


player = {"last name":["bacot","davis","cadeau"],
          "first name": ["armando","rj","elliot"],
          "height":[83,72,73],
          "weight":[240,180,180]}
data= pd.DataFrame(player)

data["bmi"]=(data["weight"]/2.205)/((data["height"]/39.7)**2)
print(data)

data.to_csv("bmi.csv")
