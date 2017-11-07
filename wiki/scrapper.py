import os
import os.path
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://lede-project.org/start']

    def parse(self, response):
        if not response.url.startswith('https://lede-project.org/'):
            return
        if '?' in response.url:
            if 'do=edit' in response.url :
                for title in response.css('#wiki__text'):
                    path = response.url[len('https://lede-project.org/'):]
                    path, _, _ = path.partition('?')
                    print('Storing', response.url, 'in', path)
                    dirname = os.path.dirname(path)

                    if dirname:
                        os.makedirs(dirname, exist_ok=True)
                    with open(path + '.txt',mode='wt') as file:
                        file.write(title.root.text)

                    yield {response.request.url: title.root.text}
            else:
                return
        else:
            yield scrapy.Request(response.url+'?do=edit', headers={'Referrer': response.url})
            for next_page in response.css('a'):
                base_url  = next_page.root.base_url
                if not next_page.root.base_url.startswith('https://lede-project.org/'):
                    continue
                if '?' in base_url and 'do=edit' not in base_url:
                    continue
                yield response.follow(next_page, self.parse)


