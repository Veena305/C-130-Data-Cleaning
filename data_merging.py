import csv
import pandas as pd

file1 = 'final_1.csv'
file2 = 'final_2.csv'

data_1 = []
data_2 = []
with open(file1,'r',encoding='utf8') as f:
    csv_reader =csv.reader(f) 
    for i in csv_reader:
        data_1.append(i)
        
with open(file2,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        data_2.append(i)

h1 = data_1[0]
h2 = data_2[0]

p_data_1 = data_1[1:]
p_data_2 = data_2[1:]

h = h1+h2

p_d =[]

for i in p_data_1:
    p_d.append(i)
for j in p_data_2:
    p_d.append(j)
with open("final_3.csv",'w',encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   
    csvwriter.writerows(p_d)
    
df = pd.read_csv('final_3.csv')
df.tail(8)