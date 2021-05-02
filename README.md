# cowin-vaccine-slot-checker
This is a Python script which will help you to know when a slot is available on Cowin website.

**This script has been tested with Python version 3.6, 3.8 on Linux/MacOs. In case you want to run it with Python 2.7 or Windows, some changes might be required.**

## Features:
1. Find any open slots and print it in the terminal and optionally write to a file
2. (Optional) Run the script as a cron job (Linux/MacOS) which will periodically check for the slots.
3. (Optional) Run the script as a cron job (Linux/MacOS), you can get an alert whenever a slot frees up.

The main code is in the file [slot_checker.py](https://github.com/faizulhai24/cowin-vaccine-slot-checker/blob/main/slot_checker.py). Rest everything is optional in case you want to run it as a cron job.

## Configurations:
Explanation for all the configuration that can be found in [slot_checker.py](https://github.com/faizulhai24/cowin-vaccine-slot-checker/blob/main/slot_checker.py)

Config                                |           Info
--------------------------------------| ----------------------------------
DISTRICT_IDS                          | This is the list of districts to check for free slot. You can get your district id in [DISTRICT_LISTS](https://github.com/faizulhai24/cowin-vaccine-slot-checker/blob/main/DISTRICT_LISTS.md). Example. [(294, "BBMP"), (265, "Bengaluru Urban")] will find slots in BBMP and Bengaluru Urban districts. Change this id and name to your district. 
WRITE_TO_FILE                         | Optional. Write the free slots to a file. Default: True
FILE_NAME                             | Optional. File to which to write the open slots to. Default: "vaccine.txt"
ALARM                                 | Optional. This will ring an alarm when free slots are found. Default: True
NUM_WEEKS                             | No of weeks starting today to check the slots in. Default: 5
MIN_AGE                               | Minimum age limit. Default: 18. Can be changed to 45 for senior people.   


## Steps to run:
1. Clone the repository
2. Run ```pip install -r requirements.txt```
3. Change the above defined configurations in [slot_checker.py](https://github.com/faizulhai24/cowin-vaccine-slot-checker/blob/main/slot_checker.py) 
4. Run the script using ```python3 slot_checker.py```

## Steps to run a cron job periodically (Linux/MacOS):

Cron job are periodic jobs that will run silently in the background automatically.
There is a cron helper script [slot_script.sh](https://github.com/faizulhai24/cowin-vaccine-slot-checker/blob/main/cron_script.sh) in the repo, however you might have to make some changes to cron_script according to your environment.

1. Go to the terminal and run ```crontab -e```
2. Add this line `````*/10 * * * *  <PATH_TO_THE_REPO>/cron_script.sh`````
3. You can change the periodicity. Just a regular cron expression. The above one will execute every 10 minutes.
3. (Optional) If you want to disable the terminal mail for every cron job run add ```MAILTO="""``` above the previous command.

>Note: There is ```MIN_CAPACITY``` config in the main file. Change it to maybe ```5```, so that your laptop does not keep alerting you when a single slot opens up because most likely it is going to filled by the time you sign in onto the portal.
>
>Note: To check if this cron is running properly, you can check if the file with FILE_NAME got created. Another way is to check terminal mail. The terminal is going to create a mail for every time the cron runs. To check, go to terminal and run ```mail```.  