import hashlib
import os.path
from abc import abstractmethod, ABC
from requests import get


class Request(ABC):
    @abstractmethod
    def run(self, url: str) -> str:
        pass


class GetRequest(Request):

    def run(self, url: str) -> str:
        return get(url).text


def url_hash(url: str):
    return f'{hashlib.sha256(url.encode("utf-8")).hexdigest()}'


def get_cached(url: str) -> str:
    with open(f'cache/{url_hash(url)}') as fp:
        return fp.read()


class CachedGetRequest(Request):
    req = GetRequest()

    def run(self, url: str) -> str:
        os.makedirs('cache/', exist_ok=True)

        try:
            with open(f'cache/{url_hash(url)}', mode='x') as fp:
                fp.write(self.req.run(url))
                fp.flush()
        except FileExistsError:
            print('cache hit')
            pass  # means the file is cached, which is fine

        return get_cached(url)


if __name__ == '__main__':
    req = CachedGetRequest()
    while True:
        url = input('Write a URL to be fetched:')
        print(req.run(url))
