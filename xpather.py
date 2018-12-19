from selenium import webdriver
from bs4 import BeautifulSoup
import time

def xpath_soup(element):
    components = []
    child = element if element.name else element.parent
    for parent in child.parents:
        siblings = parent.find_all(child.name, recursive=False)
        components.append(
            child.name
            if siblings == [child] else
            '%s[%d]' % (child.name, 1 + siblings.index(child))
            )
        child = parent
    components.reverse()
    return '/%s' % '/'.join(components)


def reloadSoup(driver: webdriver) -> BeautifulSoup:
    return BeautifulSoup(driver.page_source, features="lxml")


def turnHtmlintoElements(driver:webdriver,soup:BeautifulSoup,tag: str, atri: str, value : str)->[]:
    return list(map(lambda j: driver.find_elements_by_xpath(j),list(map(lambda obj: xpath_soup(obj), soup.find_all(tag, {atri: value})))))


def searchIndex(keys: str, a: [], driver:webdriver,soup:BeautifulSoup):
    search = driver.find_element_by_xpath(xpath_soup(soup.find("input", {"maxlength": "2048"})))
    search.clear()
    search.send_keys(keys)
    time.sleep(1)
    soup = reloadSoup(driver)
    results = soup.find_all("div", {"role": "option"})
    print(results)
    for x in results:
        temp = BeautifulSoup(str(x), features="lxml")
        print(temp.find("b"))
        try:
            a.append(keys + temp.find("b").string)
        except AttributeError:
            print("one down")
