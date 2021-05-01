import time

import requests
from pygame import mixer


class SlotChecker:
    def __init__(self):
        self.DISTRICT_IDS = [(294, "BBMP"), (265, "Bengaluru Urban")]
        self.DATES = ["02-05-2021", "09-05-2021", "16-05-2021", "23-05-2021", "30-05-2012"]
        self.URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id={}&date={}"
        self.WRITE_TO_FILE = True
        self.ALARM = True
        self.FILE_NAME = "vaccine.txt"

    def check_free_slots(self, data):
        free_slots = []
        centers = data['centers']
        for center in centers:
            for session in center['sessions']:
                if session['min_age_limit'] == 18 and session['available_capacity'] > 0:
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
                resp = requests.get(self.URL.format(district_id[0], date))
                if resp.status_code != 200:
                    continue
                free_slots = self.check_free_slots(resp.json())
                if free_slots:
                    slots.extend(free_slots)
                else:
                    print("No free slot found on {}".format(date))

        if slots:
            if self.WRITE_TO_FILE:
                self.write_to_file(slots)
            if self.ALARM:
                mixer.init()
                mixer.music.load('./alarm.mp3')
                mixer.music.play()
                time.sleep(5)


if __name__ == '__main__':
    sc = SlotChecker()
    sc.run()
