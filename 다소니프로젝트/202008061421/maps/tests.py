from django.test import TestCase
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus

url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : 'oe0CR6Hcs0OktQ3xDGozMrKU%2BUPTxUAi%2Fl0ZwWQQ2%2FLpiNXU5JgfiGAC6ek7LOR5bueVBXcj%2Bqhazy3E4E4sWw%3D%3D(UTF-8)', quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', quote_plus('dataType') : 'XML', quote_plus('base_date') : '20151201', quote_plus('base_time') : '0600', quote_plus('nx') : '18', quote_plus('ny') : '1' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)