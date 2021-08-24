from typing import Union
import requests
from bs4 import BeautifulSoup, FeatureNotFound


def safe_get(url: str) -> requests.Response:
    print(f"Requesting {url}\n")
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url , headers=headers)
    response.raise_for_status()
    return response


def soup_from_url(url: str) -> BeautifulSoup:
    response = safe_get(url)
    return soup_of(response.text)


def soup_of(content : Union[str , bytes]):
    try :
        soup = BeautifulSoup(content, features="lxml")
        return soup
    except FeatureNotFound as e :
        soup = BeautifulSoup(content, features="html.parser")
        return soup


def is_url_root(url: str) -> bool:
    result = True
    if "http" in url:
        try:
            url = url.split("https://")[1]
        except IndexError:
            url = url.split("http://")[1]
        try:
            if not (url.split("/")[1] == ""):
                result = False
        except IndexError as e:
            pass
        return result
    else:
        raise Exception(f"{url} Must be an http/https pattern")


def url_spliter(url: str, root: bool = False) -> list:
    if "http" in url:
        try:
            url = url.split("https://")[1]
        except IndexError:
            url = url.split("http://")[1]
    root = url.split("/")[0]
    children = url.split("/")[1:]

    result = (root, children) if root == True else children

    return result
