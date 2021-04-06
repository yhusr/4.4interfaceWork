import requests
import json


class HandleRequest:
    def __init__(self):
        self.session = requests.session()

    def common_headers(self, header):
        self.session.headers.update(header)

    def send(self, url, method='post', data=None, isJson=True, *args, **kwargs):
        if isinstance(data, str):
            try:
                '''
                json的str形式的对象 转换为
                python对象，即为dict对象
                '''
                data = json.loads(data)
            except NameError as e:
                data = eval(data)
                print(e)
        method = method.lower()
        if method == 'get':
            result = self.session.request(method=method, url=url, params=data, *args, **kwargs)
        elif method in ('post', 'put', 'patch', 'delete'):
            if isJson:
                result = self.session.request(method=method, url=url, json=data, *args, **kwargs)
            else:
                result = self.session.request(method=method, url=url, data=data, *args, **kwargs)
        else:
            return f'此方法{method}不存在'
        return result

    def close(self):
        self.session.close()


if __name__ == '__main__':
    hr = HandleRequest()
    result = hr.send('https://www.baidu.com')
    result.encoding='utf-8'
    print(result.text)