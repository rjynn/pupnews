import json

class ConfigLoader:
    FILENAME = "bot_config.json"

    configloader = None
    bot_token = None
    news_token = None
    news_channel = None
    currents_token = None

    def __init__(self):
        if self.configloader == None:
            with open(self.FILENAME) as json_data_file:
                data = json.load(json_data_file)

        self.bot_token = data['bot_auth']['token']
        self.news_token = data['other']['news_api_key']
        self.news_channel = data['other']['stock_channel_id']
        self.currents_token = data['other']['currents_api']

    def getBotToken(self):
        return self.bot_token

    def getNewsAPIToken(self):
        return self.news_token
    
    def getNewsDiscordChannel(self):
        return self.news_channel

    def getCurrentsAPIToken(self):
        return self.currents_token


        