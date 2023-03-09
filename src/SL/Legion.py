from SL import Spider
# start
import threading

# info 军团信息
# spiders 爬虫信息 每个信息格式为 {
# 'info': {这个字典为爬虫的信息},
# 'tasks': [这个列表是爬虫获取任务的列表]
# 'results' : [这个列表是爬虫存放结果的列表]
# }
class Legion:
    def __init__(self,
                 info = {'name':'sl'}):
        self.info = info
        self.log = []
        self.tasks = []
        self.results = []

        # 根据信息生成爬虫
        self.generateSpiders()

    def generateSpiders(self):
        pass
       
    # 开始任务
    def start(self):
        pass

    # 结束任务
    def stop(self):
        pass
