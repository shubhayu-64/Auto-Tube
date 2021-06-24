from instalooter.looters import ProfileLooter
import datetime
from datetime import datetime, timedelta
import dateutil.relativedelta
import config


class scrapeVideos:
    def __init__(self, uname, location):
        self.username = uname
        self.location = location
        self.looter = ProfileLooter(
            self.username, template="{username}_{datetime}")
        self.login()
        self.download()

    def login(self):
        if not self.looter.logged_in():
            self.looter.login(config.insta_uname, config.insta_passwd)

    def logout(self):
        self.looter.logout()

    def download(self):
        self.looter.download_videos(
            self.location, new_only=True, timeframe=[datetime.now(), datetime.now() - timedelta(hours=24)])
