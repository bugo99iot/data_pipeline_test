# data_pipeline_test
We build an automated data pipeline which retrieves new files from a FTP server, cleans them and appends the result to a MySQL/SQLite database. 

# Summary
   * Step 1
      Set target time (every Monday 9:00am), read file names from remote server, filter new ones, download new ones in "raw_data".

   * Step 2
      Fetch date from file name and datetime, add date column to raw dataframe, convert non-ASCII characters,
      save clean dataframe to "clean_data".

   * Step 3
      Fetch clean dataframe, append it to 'customer1_data' table within 'less_friction_database.db', create SQLite dump 'less_friction_dump.sql' and MySQL dump 'less_friction_mydump.sql', send an email of warning to a target user in case of failure.

# Installation
To get the code running:
   * Install Python 3
   * Install all required packages listed in 'data_pipe.py'
   
# License
Released under version 2.0 of the [Apache License].

[Apache license]: http://www.apache.org/licenses/LICENSE-2.0
