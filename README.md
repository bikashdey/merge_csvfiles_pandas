# merge_csvfiles_pandas
This is simple project based on python pandas.
This project regarding merging csv files into one single csv file.
I have used virtual env Name:venv 
at the first activate the virtualenv (use command) : (.\venv\scripts\activate)
after that you can run this py file (use command) : python mergecsv.py

For all dependencies  please see the requirements.txt.
To install all dependencies from requirements (use command): pip install -r requirements.txt

Note: If you find the error of permission denied by (mergefile.csv).
      please change the filename eg:- line 22 (df.to_csv('newfile.csv',index=False,header=True)
