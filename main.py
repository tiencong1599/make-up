import asyncio
import sys

from PyQt5.QtWidgets import QApplication
from resource.main import MainWindow
from utils.database import mongo


async def main():
    await mongo.init_connection()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
    sys.exit()