class WeiboPipeline(object):
    def process_item(self, item, spider):
        # 使用save就是把item存入到了数据库
        item.save()
        return item
