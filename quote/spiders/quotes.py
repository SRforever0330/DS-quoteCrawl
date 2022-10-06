import scrapy
from scrapy import Selector, Request

from quote.items import QuoteItem

"""
    Quotes爬虫
"""


class QuotesSpider(scrapy.Spider):

    # 爬虫的名称
    name = 'quotes'
    # 爬虫的域名
    allowed_domains = ['quotes.toscrape.com']

    # 源码是由启动页面然后获取到下一页面到url，再获取新的请求，更好的方法。一开始就构建好10个请求，直接交给引擎，再由引擎交给调度器
    def start_requests(self):
        for page in range(1, 11):
            yield Request(url=f'http://quotes.toscrape.com/page/{page}/')

    # 钩子方法/回调方法
    def parse(self, response, **kwargs):
        for each in response.xpath('//div[@class="quote"]'):
            item = QuoteItem()
            # 名人名言文本
            item['text'] = each.xpath('./span/text()').extract()[0]
            # 作者
            item['author'] = each.xpath('.//small/text()').extract()[0]
            detail_url = "http://quotes.toscrape.com" + each.xpath('.//a/@href').extract()[0]
            tagList = each.xpath('.//a[@class="tag"]/text()').extract()
            # 标签
            item['tags'] = '/'.join(tagList)
            # dont_filter = true是不过滤重复的url
            yield Request(url=detail_url, callback=self.parse_detail,  cb_kwargs={'item': item}, dont_filter=True)  # 回调函数和这个不一样，需要另外创建

    '''
    异步处理请求，也就是说Scrapy发送请求之后，不会等待这个请求的响应（也就是不会阻塞），
    而是可以同时发送其他请求或者做别的事情。而我们知道服务器对于请求的响应是由很多方面的因素影响的，
    如猫之良品所说的网络速度、解析速度、资源抢占等等，其响应的顺序是难以预测的。
    '''
    def parse_detail(self, response, **kwargs):
        item = kwargs['item']
        item['author_born_date'] = response.xpath('//span[@class="author-born-date"]/text()').extract()[0]
        item['author_born_location'] = response.xpath('//span[@class="author-born-location"]/text()').extract()[0]
        item['author_description'] = response.xpath('//div[@class="author-description"]/text()').extract()[0]
        yield item
