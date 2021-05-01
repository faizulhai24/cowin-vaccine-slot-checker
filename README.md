# cowin-vaccine-slot-checker
This is a Python script which will help you to know when a slot is available on Cowin website.

**This script has been tested with Python version 3.6, 3.8. In case you want to run it with Python 2.7, some changes might be required.**

## Features:
1. Find any open slots and print it in the terminal and optionally write to a file
2. (Optional) Run the script as a cron job (Linux/MacOS) which will periodically check for the slots.
3. (Optional) Run the script as a cron job (Linux/MacOS), you can get an alert whenever a slot frees up.

The main code is the file [slot_checker.py](https://github.com/faizulhai24/cowin-vaccine-slot-checker/blob/main/slot_checker.py)

## Configurations:
Explanation for all the configuration that can be found in [slot_checker.py](https://github.com/faizulhai24/cowin-vaccine-slot-checker/blob/main/slot_checker.py)

Config                                |           Info
--------------------------------------| ----------------------------------
DISTRICT_IDS                          | This is the list of districts to check for free slot. You can get your district id in [district_ids_list](https://github.com/faizulhai24/cowin-vaccine-slot-checker/blob/main/district_id_list.py) E.g. [(294, "BBMP"), (265, "Bengaluru Urban")] will find slots in BBMP and Bengaluru Urban districts. Change this id and name to your district. 
WRITE_TO_FILE                         | Optional. Write the free slots to a file. Default: True
FILE_NAME                             | Optional. File to which to write the open slots to. Default: "vaccine.txt"
ALARM                                 | Optional. This will ring an alarm when free slots are found. Default: True
DATE_INTERVAL                         | The default interval in which the slot will be queried is the next 5 weeks starting today.   

## Steps to run:
1. Clone the repository
2. Run ```pip install requests```
3. Change the above defined configurations in [slot_checker.py](https://github.com/faizulhai24/cowin-vaccine-slot-checker/blob/main/slot_checker.py) 
4. Run the script using ```python3 slot_checker.py```

## Steps to run a cron job periodically (Linux/MacOS):

There is a cron helper script [slot_script.sh](https://github.com/faizulhai24/cowin-vaccine-slot-checker/blob/main/cron_script.sh) in the repo

1. Go to the terminal and run ```crontab -e```
2. Add this line `````*/10 * * * *  <PATH_TO_THE_REPO>/cron_script.sh`````
3. You can change the periodicity. Just a regular cron expression. The above one will execute every 10 minutes.
3. (Optional) If you want to disable the terminal mail for every cron job run add ```MAILTO="""``` above the previous command.