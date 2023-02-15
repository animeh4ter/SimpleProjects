from view import UserInterface
from model import RaidModel


class Controller:
    def __init__(self):
        self.raid_model = RaidModel()
        self.interface = UserInterface()

    def run(self):
        answer = None
        while answer != "q":
            answer = self.interface.wait4answer()
            self.check_ans(answer)

    def check_ans(self, ans):
        if ans == "1":
            raid = self.interface.add_raid()
            self.raid_model.add_raid(raid)
        elif ans == "2":
            raids = self.raid_model.get_all_raids()
            self.interface.show_all_raids(raids)
        elif ans == "3":
            raid_time = self.interface.get_raid_time()
            try:
                raid = self.raid_model.get_single_raid(raid_time)
            except KeyError:
                self.interface.show_incorrect_raid_time_error(raid_time)
            else:
                self.interface.show_certain_raid(raid)
        elif ans == "4":
            raid_time = self.interface.get_raid_time()
            try:
                raid = self.raid_model.del_raid(raid_time)
            except KeyError:
                self.interface.show_incorrect_raid_time_error(raid_time)
            else:
                self.interface.del_raid(raid)
        elif ans == "5":
            income = self.raid_model.get_income()
            self.interface.show_income(income)
        elif ans == "q":
            self.raid_model.save_data()
        else:
            self.interface.show_incorrect_answer()
