import logging
from constants import logfile

#now we will Create and configure logger 
logging.basicConfig(filename=logfile, 
					format='%(asctime)s %(message)s', 
					filemode='a')

#Let us Create an object 
logger=logging.getLogger() 

#Now we are going to Set the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 

#some messages to test
#logger.debug("This is just a harmless debug message") 
#logger.info("This is just an information for you") 
#logger.warning("OOPS!!!Its a Warning") 
#logger.error("Have you try to divide a number by zero") 
#logger.critical("The Internet is not working....") 

# create the log file if does not exist
try:
    f = open(logfile,'r')
    print("Log file Exists")
except IOError:
    f = open(logfile, 'w+')
    print("Log File Created ...")