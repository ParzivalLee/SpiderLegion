import threading

class Legion:
    def __init__(self,
                 info = {'name':'legion'},
                 spiders=[]):
        self.info = info
        self.spiders = spiders

        # 根据信息生成爬虫
        self.generateSpiders()
       
    # 生成爬虫
    def generateSpiders(self):
        for i in self.spiders:
            i['spider'] = Spider(info=i['info'],
                                 tasks=i['tasks'],
                                 results=i['results'])

    # 开始任务
    def start(self):
        # 根据信息生成线程
        for i in self.spiders:
            for j in range(i['threadNumber']):
                threading.Thread(target=i['spider'].start).start()

    # 结束任务
    def stop(self):
        for i in self.spiders:
            i['spider'].stop()


class Genarator:
    def __init__(self):
        pass

    # 生成任务
    def generateTask(function, params):
        return { 'function':function, 'params':params }

import time
import threading

"""
tasks中应包含'function'键,其值为任务执行的函数
其返回值将作为结果被添加到结果列表中
以及'params'键，其值为任务执行函数所需的参数
"""

class Spider:
    def __init__(self,
                 info = {'name':'spider'},
                 tasks=[],
                 results=[],
                 restTime=1):
        self.info = info
        self.tasks = tasks
        self.results = results
        self.restTime = restTime
        self.isActive = False

    # 开始执行任务
    def start(self):
        self.isActive = True
        while self.isActive:
            if self.tasks:
                # 如果任务列表不为空
                task = self.tasks.pop(0)
                # 从任务列表里获取函数和参数
                # 执行任务后将结果添加到结果列表
                self.results.append(task['function'](task['params']))
                time.sleep(self.restTime)
            else:
                time.sleep(3)
                continue

    # 停止任务
    def stop(self):
        self.isActive = False

