import datetime
import os
import platform
import time
import subprocess


try:
    import requests
except ImportError:
    print("!!Required Modules are missing!!\nPlease refer README.md\nor run pip install -r requirements.txt")
    exit()


class SlotChecker:
    def __init__(self):
        self.DISTRICT_IDS = [(395, "Mumbai"), (392, "Thane")]
        self.NUM_WEEKS = 5
        self.DATES = []
        self.URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}"
        self.WRITE_TO_FILE = True
        self.ALARM = True
        self.FILE_NAME = "vaccine.txt"
        self.MIN_AGE = [18,45]
        self.MIN_CAPACITY = 0
        self.OPEN_PAGE = True
        self.COWIN_PORTAL ="https://selfregistration.cowin.gov.in/"

        now = datetime.datetime.now()
        for i in range(5):
            target_time = now + datetime.timedelta(days=7 * i)
            self.DATES.append(target_time.strftime("%d-%m-%Y"))

    def check_free_slots(self, data):
        free_slots = []
        centers = data['centers']
        for center in centers:
            for session in center['sessions']:
                for min_age in self.MIN_AGE:
                    if session['min_age_limit'] == min_age and session['available_capacity'] > self.MIN_CAPACITY:
                        print(
                            "{}-{}-{}-{}-{}-{}-{}".format(session['min_age_limit'],session['available_capacity'], center['district_name'], session['date'],
                                                            center['fee_type'], session['vaccine'], center['name']).expandtabs(20))
                        free_slots.append(
                            "{}\t{}\t{}\t{}\t{}\t{}\t{}".format(session['min_age_limit'],session['available_capacity'], center['district_name'], session['date'],
                                                            center['fee_type'], session['vaccine'], center['name']).expandtabs(20))
        return free_slots

    def write_to_file(self, slots):
        slot_head=["{}\t{}\t{}\t{}\t{}\t{}\t{}".format("Age","Available Slots","District","Date",
                                                        "Fees Type","Vaccine","Centre Name").expandtabs(20)]
        f = open(self.FILE_NAME, "a")
        f.write('{}\n'.format(datetime.datetime.now()))
        f.write('\n'.join(slot_head))
        f.write('\n')
        data = '\n'.join(slots)
        f.write(data)
        f.write('\n\n')
        f.close()

    def run(self):
        slots = []
        for min_age in self.MIN_AGE:
            print("Checking for Age: {}".format(min_age))
            for district_id in self.DISTRICT_IDS:
                for date in self.DATES:
                    resp = requests.get(self.URL.format(district_id[0], date), headers={
                        "accept": "application/json",
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
                    })
                    if resp.status_code != 200:
                        print(resp.status_code)
                        continue
                    free_slots = self.check_free_slots(resp.json())
                    if free_slots:
                        slots.extend(free_slots)
                    else:
                        print("No free slots found on {} for {}".format(date, district_id[1]))
                        # print("Failed to fetch slots on {} for {}".format(date, district_id[1]))

        if slots:
            if self.WRITE_TO_FILE:
                self.write_to_file(slots)
                os.startfile(self.FILE_NAME)
                
            if self.ALARM:
                if platform.system() == 'Darwin':
                    os.system("afplay " + 'alarm.wav')
                elif platform.system() == 'Linux':
                    subprocess.call(["aplay", "alarm.wav"])
                #elif platform.system() == 'Windows':               #Choice between Beeping or playing the wav file
                #    os.startfile("alarm.wav")
                elif platform.system() == 'Windows':
                    import winsound
                    duration = [200,500,200,500,200,500,200,500]  # milliseconds
                    freq = 440  # Hz
                    for x in duration:      #more like alarm compared to a static beep
                        winsound.Beep(freq, x)

            if self.OPEN_PAGE:
                print("\n\n\nOpening {}".format(self.COWIN_PORTAL))
                time.sleep(5)
                if platform.system()=='Windows':
                    os.startfile(self.COWIN_PORTAL)
                elif platform.system()=='darwin':
                    subprocess.Popen(['open', self.COWIN_PORTAL])
                else:
                    try:
                        subprocess.Popen(['xdg-open', self.COWIN_PORTAL])
                    except OSError:
                        import webbrowser
                        webbrowser.open(self.COWIN_PORTAL)


if __name__ == '__main__':
    sc = SlotChecker()
    sc.run()
