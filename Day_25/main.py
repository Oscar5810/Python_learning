# # import csv
#
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #         # print(row)
# #     print(temperatures)
#
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
# sum = 0
# avg = 0
# temp_list = data["temp"].to_list()
# # for temp in temp_list:
# #     sum += temp
# # avg = sum / len(temp_list)
# # print(temp_list)
# # print(data["temp"].mean())
# # print(data["temp"].max())
#
# # Get data in Row
# print(data[data.temp == data["temp"].max()])
#
#
# # Create a dataFrame from Scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76,56,65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")