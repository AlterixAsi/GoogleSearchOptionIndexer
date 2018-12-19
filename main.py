
import threading
import collections
from xpather import*
from sortedcontainers import SortedDict

class thread (threading.Thread):
    def __init__(self, driver:webdriver, start:int, a:[], end:int):
        threading.Thread.__init__(self)
        self.count = start
        self.a = a
        self.end = end
        self.driver = driver
    def run(self):
        print("started Thread")
        for x in range (0,self.end):
            searchIndex(a[self.count+x*2],a,self.driver,BeautifulSoup(self.driver.page_source))
        print("end of thread")

f = open("searches","w+")
# options = webdriver.ChromeOptions()
# options.binary_location = "chromedriver.exe"
# options.add_argument('headless')
driver1 = webdriver.Chrome("chromedriver.exe")
driver2 = webdriver.Edge("MicrosoftWebDriver2.exe")
#driver = webdriver.PhantomJS("phantomjs-2.1.1-windows/bin/phantomjs.exe")
driver1.get("https://google.com")
driver2.get("https://google.com")
soup = reloadSoup(driver1)
a = []
amount = 200
searchIndex("What",a,driver1,soup)
thread1 = thread(driver1,0,a,amount//2)
thread2 = thread(driver2,1,a,amount//2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
# for x in range(0,25):
#     try:
#
#     except Exception:
#         print("end")
#     #searchIndex(a[x],a,driver,soup)
print(len(a))
b = set(a)
print(len(b))
d = collections.Counter(a)
print(d)
d = SortedDict(d)
for key,value in d.items():
    f.write(key+" "+str(value)+"\n")

try:
    driver1.quit()
except Exception:
    print(" ")
try:
    driver2.quit()
except Exception:
    print(" ")




