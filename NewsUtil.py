from newsapi import NewsApiClient
from ConfigLoader import ConfigLoader

class NewsUtil:
    API_KEY = None
    newsapitoken = None 
    keywords = ['bitcoin']

    def __init__(self):
        config_loader = ConfigLoader()
        self.API_KEY = config_loader.getNewsToken()
        self.newsapitoken = NewsApiClient(api_key=API_KEY)

    def getNewsAPIArticlesKeywords(self):
        for word in keywords:
            all_articles = self.newsapitoken.get_everything(q=word,
                                        sources='wired,the-verge',
                                        from_param='2020-01-01',
                                        to='2017-12-12',
                                        language='en',
                                        sort_by='relevancy'
                                        )
    
    def getNewsAPITrending(self):
        return False

    def getCurrentsAPIArticlesKeywords(self):
        return False

    def getKeywordCount(self):
        return False

    def addKeyword(self, keyword):
        self.keywords.append(keyword)

    def removeKeyword(self, keyword):
        prev_count = self.getKeywordCount()
        self.keywords.remove(keyword)
        current_count = count(self.keywords)
        if prev_count == current_count:
            return True
        return False