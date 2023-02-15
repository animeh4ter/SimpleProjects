def add_title(title: str):
    def deco(method):
        def wrapper(self, *args):
            print(title.center(50, "="))
            return method(self, *args)
        return wrapper
    return deco


class UserInterface:
    @add_title(" Actions list ")
    def wait4answer(self):
        print("""1. Add new raid 
2. View all raids
3. View certain raid
4. Delete certain raid
5. View raids income
q. Quit program""")
        user_ans = input("Choose action: ")
        return user_ans

    @add_title(" Creating raid ")
    def add_raid(self):
        raid_dict = {"location": None,
                     "status": None,
                     "time": None,
                     "changes": None
                     }
        for key in raid_dict:
            raid_dict[key] = input(f"Type {key}: ")
        return raid_dict

    @add_title(" All raids ")
    def show_all_raids(self, raids):
        for ind, raid in enumerate(raids, 1):
            print(f'{ind}. {raid}')

    @add_title(" Finding certain raid ")
    def get_raid_time(self):
        raid_time = input("Type time when raid ended: ")
        return raid_time

    @add_title(" Raid ")
    def show_certain_raid(self, raid):
        for key in raid:
            print(f"{key} - {raid[key]}")

    @add_title(" Error ")
    def show_incorrect_raid_time_error(self, raid_time):
        print(f"There is no raid in time {raid_time}")

    @add_title(" Deleting raid ")
    def del_raid(self, raid):
        print(f"{raid} deleted")

    @add_title(" Income ")
    def show_income(self, income):
        print(f"Income from all saved raids: {income}")

    @add_title(" Error ")
    def show_incorrect_answer(self):
        print("Type only 'q' or digits from actions list")
