import os
import pickle


class Raid:
    def __init__(self, location: str, status: str, time: str, bud_changes: int):
        self.location = location
        self.status = status
        self.time = time
        self.bud_changes = bud_changes

    def __str__(self):
        return f"Raid on {self.location} at {self.time} ({self.status})"


class RaidModel:
    def __init__(self):
        self.data = 'raids_data.txt'
        self.raids = self.load_data()

    def add_raid(self, raid_dict):
        raid = Raid(*raid_dict.values())
        self.raids[raid.time] = raid

    def get_all_raids(self):
        return self.raids.values()

    def get_income(self):
        raids = self.get_all_raids()
        income = 0
        for raid in raids:
            income += int(raid.__dict__['bud_changes'])
        inc2 = str(income) + " rub"
        return inc2

    def get_single_raid(self, time):
        raid = self.raids[time]
        raid_dict = {"Time": raid.time,
                     "Location": raid.location,
                     "Status": raid.status,
                     "Changes": raid.bud_changes
                     }
        return raid_dict

    def del_raid(self, raid_time):
        return self.raids.pop(raid_time)

    def load_data(self):
        if os.path.exists(self.data):
            with open(self.data, 'rb') as file:
                return pickle.load(file)
        else:
            return dict()

    def save_data(self):
        with open(self.data, 'wb') as file:
            pickle.dump(self.raids, file)
