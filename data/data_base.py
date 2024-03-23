import asyncio
import json
import time
from datetime import datetime, timedelta

manager = asyncio.Lock()


class Users:
    def __init__(self,
                 user_id: str | int,
                 bot_name: str):
        self.user_id = str(user_id)
        self.file_name = bot_name + ".json"

    async def read_data(self):
        async with manager:
            with open(f"data/users_data/{self.file_name}", "r", encoding="utf-8") as users:
                self.users = json.load(users)
                if self.users.get("users") is None:
                    self.users["users"] = {}
                if self.users.get("statistic") is None:
                    self.users["statistic"] = {
                        "started": 0,
                        "finished": 0
                    }

    async def add_user(self):
        time_now = time.time()
        if self.users.get("users").get(self.user_id) is None:
            self.users["statistic"]["started"] += 1
        elif self.users.get("users").get(self.user_id).get("complete_questions"):
            self.users["statistic"]["finished"] -= 1
        self.users["users"][self.user_id] = {
            "start_time": time_now,
            "start_bot": True,
            "complete_questions": False
        }
        await self.save_data()

    async def user_in_base(self):
        return self.users.get("users").get(self.user_id)

    async def edit_completion(self):
        self.users["users"][self.user_id]["complete_questions"] = True
        self.users["statistic"]["finished"] += 1
        await self.save_data()

    async def get_bot_users(self):
        return [user_id for user_id in self.users.get("users").keys()]

    async def get_day_statistic(self):
        number_start = 0
        number_finish = 0
        current_datetime = datetime.utcfromtimestamp(time.time())
        for user in self.users.get("users").keys():
            if (current_datetime - datetime.utcfromtimestamp(self.users.get("users").get(user).get("start_time"))
                    <= timedelta(days=1)):
                number_start += 1
                if self.users.get("users").get(user).get("complete_questions"):
                    number_finish += 1
        return [number_start, number_finish]

    async def get_month_statistic(self):
        number_start = 0
        number_finish = 0
        current_datetime = datetime.utcfromtimestamp(time.time())
        for user in self.users.get("users").keys():
            if (current_datetime - datetime.utcfromtimestamp(self.users.get("users").get(user).get("start_time"))
                    <= timedelta(days=30)):
                number_start += 1
                if self.users.get("users").get(user).get("complete_questions"):
                    number_finish += 1
        return [number_start, number_finish]

    async def get_all_statistic(self):
        return [self.users.get("statistic").get("started"), self.users.get("statistic").get("finished")]

    async def save_data(self):
        async with manager:
            with open(f"data/users_data/{self.file_name}",
                      "w", encoding="utf-8") as users:
                json.dump(self.users, users, indent=2)