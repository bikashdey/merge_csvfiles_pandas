import pandas as pd
from glob import glob


#df1=pd.read_csv('csv_data1.csv')
#df2=pd.read_csv('csv_data2.csv')
#df=pd.concat([df1,df2],ignore_index=True)

# sorting all csv files here
csv_sorted_files=sorted(glob('csvfiles/*.csv', recursive=False))

# read the csv file and store into dataframe....and add on extra colomn(filename) which shows row data comesfrom which csv file  and path... 
df=pd.concat((pd.read_csv(file).assign(filename=file)for file in csv_sorted_files),ignore_index=True)

# rename undefined colomn name here using rename function...
df.rename(
    columns=({ 'Unnamed: 0': 'Id'}), 
    inplace=True,
)
# to create and save new csv file....
try:
    df.to_csv('mergefile.csv',index=False,header=True)
except FileExistsError: 
    print("filename already exists please change merging filename")
    

print(df)