# merge_csvfiles_pandas
This is simple project based on python pandas.
This project regarding merging csv files into one single csv file.
NOTE: I have used virtual env Name:venv but you have to create new Virtualenv(use command) : 1) pip install virtualenv 2) virtualenv <name of env>
      
      Then activate the virtualenv (use command) : (.\<name of env>\scripts\activate)
      For all dependencies  please see the requirements.txt.
      To install all dependencies from requirements (use command): pip install -r requirements.txt
      After that you can run this py file (use command) : python mergecsv.py



Note: If you find the error of permission denied by (mergefile.csv).
      please change the filename eg:- line 22 (df.to_csv('newfile.csv',index=False,header=True)
