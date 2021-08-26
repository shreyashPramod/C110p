import plotly.figure_factory as ff
import statistics
import random
import csv
import pandas as pd

df=pd.read_csv("data.csv")
data=df["temp"].tolist()
population_mean=statistics.mean(data)
std_deviation=statistics.stdev(data)
print("Population Mean:-",population_mean)
print("Standard Deviation:-",std_deviation)
#fig=ff.create_distplot([data],["temp"],show_hist=False)
#fig.show()

#code to find mean and standard deviation of 100 data points
dataset=[]
for i in range(0,100):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    dataset.append(value)

mean=statistics.mean(dataset)
std_deviation1=statistics.stdev(dataset)
print("mean of sample:-",mean)
print("standard deviastion of sample:-",std_deviation1)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

#function to plot mean on the graph
def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.show()

#function to get mean of 100 data points 1000 times and plot the graph
def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
setup()

def standard_deviation():
    mean_list=[]
    for i in range(0,1000):
        set_of_mean=random_set_of_mean(100)
        mean_list.append(set_of_mean)
    std_deviation=statistics.stdev(mean_list)
    print("standard deviastion of sampling distribution:-",std_deviation)
standard_deviation()
      
