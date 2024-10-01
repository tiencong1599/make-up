import asyncio

from utils.models import Account

class MyHandler:

    async def async_get(self, data):

        account = await Account.find_one({"username": data["username"]})
        if account:
            if account.password == data["password"]:
                return True
        return False

    def login(self, data):
        task = asyncio.get_event_loop().run_until_complete(self.async_get(data))
        return task