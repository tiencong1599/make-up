from utils.config import config_map
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from utils.models import Account

class MongoConnection(object):
    def __init__(self):
        self.config = config_map.get_config()
        self.client = AsyncIOMotorClient(f"mongodb://{self.config['host']}:{self.config['port']}")

    async def init_connection(self):
        await init_beanie(database=self.client.makeupdb, document_models=[Account])

mongo = MongoConnection()
