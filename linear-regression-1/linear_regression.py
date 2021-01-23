import pandas as pd
import random as rand

ALFA = 0.01
ERRO_D = 0.0001

def main_pt_1(data, MIN, MAX, length):
    teta0 = 0
    teta1 = 1 / 2
    decay_array = []
    
    while True:
        cost = 0
        dcost0 = 0
        dcost1 = 0
        
        for index, (x, y) in data.iterrows():
            cost += ALFA * 1 / (length * 2) * (((teta1 * x + teta0) - y) **2)

            dcost0 += ALFA * 1 / length * ((teta1 * x + teta0) - y)

            dcost1 += ALFA * 1 / length * (((teta1 * x + teta0) - y) * x)
    
        decay_array.append(cost)
        teta0 -= dcost0
        teta1 -= dcost1

        if abs(dcost0) <= ERRO_D and abs(dcost1) <= ERRO_D:
            break

    return teta0, teta1, decay_array

# PARTE 1

data1 = pd.read_csv("data1.txt", names=["pop", "prof"])
data1 = data1.sort_values(by="pop")

graph = data1.plot.scatter(x="pop", y="prof", color='blue')
length = len(data1["pop"])

teta0, teta1, decay_array = main_pt_1(data1, length)
print("teta0: {} teta1: {}".format(teta0, teta1))

hvalues = pd.DataFrame(
    { "pop": data1["pop"], 
      "hprof": [teta1 * x + teta0 for i, (x, y) in data1.iterrows()] })

hvalues.plot.line(x="pop", y="hprof", color="black", label="hypothesis", ax=graph)

pd.DataFrame(
    { "iter": [i for i in range(len(decay_array))],
      "cost": decay_array }).plot.line(x="iter", y="cost")


# PARTE 2

data2 = pd.read_csv("data2.txt", names=["size", "n_rooms", "price"])

mean_size = data2["size"].mean()
mean_n_rooms = data2["n_rooms"].mean()
mean_price = data2["price"].mean()

std_size = data2["size"].std()
std_n_rooms = data2["n_rooms"].std()
std_price = data2["price"].std()

data2["size"] = [(s - mean_size) / std_size for s in data2["size"]]
data2["n_rooms"] = [(s - mean_n_rooms) / std_n_rooms for s in data2["n_rooms"]]
data2["price"] = [(s - mean_price) / std_price for s in data2["price"]]

# print(mean_size, mean_n_rooms, mean_price)
# print(std_size, std_n_rooms, std_price)

# graph = data1.plot.scatter(x="size", y="prof", color='blue')
# length = len(data1["pop"])

teta0, teta1, teta2, decay_array = main(data1, length)
print("teta0: {} teta1: {} teta3: {}".format(teta0, teta1, teta2))

# hvalues = pd.DataFrame(
#     { "pop": data1["pop"], 
#       "hprof": [teta1 * x + teta0 for i, (x, y) in data1.iterrows()] })

# hvalues.plot.line(x="pop", y="hprof", color="black", label="hypothesis", ax=graph)

# pd.DataFrame(
#     { "iter": [i for i in range(len(decay_array))],
#       "cost": decay_array }).plot.line(x="iter", y="cost")