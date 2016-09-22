
# coding: utf-8

# In[18]:

import ftplib #library for ftp transferences


# In[17]:

#Here we will download a file from CMEMS catalogue http://marine.copernicus.eu/ and to do that you
#should sign-up as user
#Our aimed directory will be instu-observations for the mediterranean basin and, within it, the file 'index_history.txt'

#So we establish first arguments for the FTP function in python ftplib:

host = "medinsitu.hcmr.gr" #aimed organization ie; from CMEMS catalogue ftp: //medinsitu.hcmr.gr/Core/INSITU_MED_TS_REP_OBSERVATIONS_013_041/
user = #your user id within colons
password = # your password id within colons
ftp = ftplib.FTP(host, user, password) #ftp call
ftp.cwd("Core/INSITU_MED_TS_REP_OBSERVATIONS_013_041") #aimed directory

#the idea is copying on a local_file the content of the remote_file within the previous aimed directory
remote_filename = "index_history.txt"

#so first: create a local_file ready to be written
local_filename = remote_filename #same of remote_file but within a new directory called data
local_file = open(local_filename, 'wb') #open for binary writting

#second: we retrieve the content of the remote document and write it to the local
ftp.retrbinary('RETR ' + remote_filename, local_file.write) #mind the blank space in 'RETR '

#third: close file and ftp operation
local_file.close()
ftp.quit()


# In[20]:

#your file is:
import os # python library to interactuate with the underlying operating system that Python is running on
print(os.path.dirname(os.path.abspath(local_filename)))


# In[ ]:

#in case of wanting to download several files you may consider listing the directory contents and iterate all along.
#to do that have a look to ftp.nlst

