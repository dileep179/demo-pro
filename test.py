import pandas as pd
import json
import time
import DbUtil

# this is about database connection
dbconnect = DbUtil.getDbConnection()
c = dbconnect.cursor()
c.execute('IF EXISTS(SELECT	* FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = "loan_data")')

