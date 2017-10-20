import ftplib
import schedule
import datetime
import json
import pandas as pd
import sqlite3
#import mysql.connector
import smtplib
from email.message import EmailMessage
from sqlalchemy import create_engine

#we connect to the FTP server
def connect():
        ftp = ftplib.FTP("someserver.se")
        ftp.login("someusername", "somepassword")
        print("OK: Connection to server established.")
        return(ftp)


#we retrieve a list of all files/directories in root
#we check which ones are new (could be none, 1 or more than 1)
def check_file(ftp):

    #get directory/file names from server
    file_names = ftp.nlst()

    #we upload our record of file names from the past
    try:
        with open('raw_data/historical_file_names.json', "r") as historical_json:
            historical = json.load(historical_json)
    except:
        historical = ["zero-history-file"]

    #we select files which are not in our historical recors and which are in csv format
    target_files = []
    for files in file_names:
        if files not in historical and files[-3:]=="csv":
            target_files.append(files)
    if len(target_files) == 0:
        print("We checked, there was no new file.")
    global new_historical
    new_historical = historical + target_files

    #we return a list of target files' names
    return(target_files)
    
#we download the file in the original format
def get_file(ftp, target_files):
    for filename in target_files:
        #show content in root directory (if automated, we will skip this)
        print("Files in root: ")
        files = ftp.dir()
        print(files)
        
        #retrieve file and save it to path
        ftp.retrbinary("RETR " + filename ,open("raw_data/" + filename, 'wb').write)
        print("OK: file downloaded.")
        ftp.quit()

#we add year column in given format and convert non-ASCII characters 
def clean_convert():
    for filename in target_files:
        df = pd.read_csv("raw_data/" + filename, delimiter=";", encoding='ISO-8859-1')
        #we strip day and month form the filename
        raw_date = [filename.split(" ")[-2:][0], filename.split(" ")[-2:][1].split(".")[0]]
        #we create a dictionary for months
        months_dict = {"jan":"01", "feb": "02", "mar": "03", "apr": "04" , "may": "05", "jun": "06", "jul": "07", "aug": "08", "sep": "09", "oct": "10", "nov": "11", "dec": "12"}
        #we retrieve the year from current year
        date = str(datetime.date.today().year) + "-" + months_dict[raw_date[0]] + "-" + raw_date[1]
        #we remove non-ASCII characters from Region
        df["Region"] = df["Region"].map(lambda string: string.replace("ä","a").replace("Ä","A").replace("å","a").replace("ö","o").replace("Ö","O").replace("Å","A"))
        #we remove non-ACII characters from column headers
        df.rename(columns=lambda string: string.replace("ä","a").replace("Ä","A").replace("å","a").replace("ö","o").replace("Ö","O").replace("Å","A"), inplace=True)
        #we assign the value date to a new column "Date" within the dataframe
        df["Date"]= date   
        #we save the new framework to file
        df.to_csv("clean_data/" + filename,sep = ',', index=False)
        print("OK: dataframe clean.")

#we append the new dataframe object to a table within a SQLite database
def to_sql():  
    for filename in target_files:  

        #we upload the dataframe
        df=pd.read_csv("clean_data/" + filename)
        
        #we connect to SQLite
        conn = sqlite3.connect("databases/less_friction_database.db")

        #we append to table if exists, create table otherwise 
        try:
            df.to_sql("customer1_data", conn, if_exists= "append" , index=False)
        except:
            df.to_sql("customer1_data", conn, if_exists= "replace" , index=False)
        #we fetch all lines in the new table
        s = pd.read_sql_query("SELECT * FROM customer1_data;", conn)
        #FOR THE USER: uncomment the folling line to see table
        #print(s)
        print("OK: SQL database updated.")
        
        #we create an sql dump for the file
        with open('databases/less_friction_dump.sql', 'w') as f:
            for line in conn.iterdump():
                f.write('%s\n' % line)
        conn.commit()
        conn.close()
        #if all went well, we add the file name to historical, so it won't be downloaded again next time
        with open('raw_data/historical_file_names.json', "w") as historical_json:
            json.dump(new_historical, historical_json)

#we repeat the previous step for a MySQL database
def to_mysql():
    engine = create_engine('mysql+mysqldb://user:password@localhost/less_friction_mydatabase', echo=False)
    df=pd.read_csv("clean_data/" + filename)
    try:
        df.to_sql(name="customer1_data", con=engine, schema=None, if_exists='append', index=False)
    except: 
        df.to_sql(name="customer1_data", con=engine, schema=None, if_exists='replace', index=False)
#we send an email of warning to a target user in case an error occurred (faulty server, etc...)
def send_warning(text):
    
    msg = EmailMessage()
    msg.set_content(text)

    sender = 'someone.somehow@gmail.com'
    password = 'mypassword'
    receiver = 'something.somewhere@gmail.com'

    msg['Subject'] = "WARNING: database could not downloaded."
    msg['From'] = sender
    msg['To'] = receiver

    # Send the message via gmail server
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login(sender, password)
    s.sendmail(sender, receiver, msg.as_string())
    s.quit()

#we create a lever for ll jobs above so that we can execute them at once
def do_all():
    try:
        ftp = connect()
        global target_files
        target_files = check_file(ftp)
        get_file(ftp,target_files)
        clean_convert()
        to_sql()
        #we comment the create mysql database function as it reauires autentication to local server
        #to_mysql()

    #in case something went wrong, we send an error message to a target user
    except Exception as e:
        warning_text = "There was an error:" + str(e)
        print("An error occurred:", warning_text)
        try:
            send_warning(warning_text)
            print("A warning message was sent.")
        except:
            print("A warning message could not be sent.")

if __name__ == "__main__":
        #we schedule all jobs for each Monday morning at 9:00am
        schedule.every().wednesday.at("14:49").do(do_all)        

        #we run the pending jobs
        while True:
            schedule.run_pending()



