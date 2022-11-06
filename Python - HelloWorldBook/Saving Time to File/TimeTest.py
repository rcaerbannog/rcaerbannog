import time,datetime,os,pickle

some_time = datetime.datetime.now()

#Store time of program exit in a pickled file for next time
first_time = True
if os.path.isfile("last_run.pkl"):
    first_time = False
    with open("last_run.pkl", 'rb') as last_run:
        prev_time = pickle.load(last_run)
        print ("The last time this program was run was " + str(prev_time))
    
with open("last_run.pkl", 'wb') as last_run:
    pickle.dump(some_time, last_run)
    print ("Saved current run time of " + str(some_time) + " to file.")

if first_time:
    print ("Created new pickle file, as this is the first run of the program.")
