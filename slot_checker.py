import time

import requests
from pygame import mixer


class SlotChecker:
    def __init__(self):
        self.DISTRICT_IDS = [(294, "BBMP"), (265, "Bengaluru Urban")]
        self.DATES = ["01-05-2021", "08-05-2021", "15-05-2021", "22-05-2021", "29-05-2012"]
        self.URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id={}&date={}"
        self.EXCLUDED_HOSPITALS = ["H K HOSPITAL C1", "Newbagalur Layout UPHC C 1"]
        self.FILE_NAME = "vaccine.txt"

    def check_free_slots(self, data):
        free_slots = []
        centers = data['centers']
        for center in centers:
            for session in center['sessions']:
                if session['min_age_limit'] == 18 and session['available_capacity'] > 10 and center[
                    'name'] not in self.EXCLUDED_HOSPITALS:
                    free_slots.append("{} - {} - {}".format(center['name'], center['district_name'], session['date']))
        return free_slots

    def write_to_file(self, slots):
        print(slots)
        f = open(self.FILE_NAME, "a")
        data = '\n'.join(slots)
        f.write(data)
        f.write('\n')
        f.close()

    def run(self):
        slots = []
        for district_id in self.DISTRICT_IDS:
            for date in self.DATES:
                resp = requests.get(self.URL.format(self.DISTRICT_IDS[0][0], self.DATES[0]))
                free_slots = self.check_free_slots(resp.json())
                if free_slots:
                    slots.extend(free_slots)
                else:
                    print("No free slot found on {}".format(date))

        if slots:
            self.write_to_file(slots)
            mixer.init()
            mixer.music.load('./alarm.mp3')
            mixer.music.play()
            time.sleep(5)


if __name__ == '__main__':
    sc = SlotChecker()
    sc.run()
