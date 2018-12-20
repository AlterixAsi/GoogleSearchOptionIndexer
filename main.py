
import threading
import collections
from xpather import*
from sortedcontainers import SortedDict
from selenium.webdriver.chrome.options import Options

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
            searchIndex(a[self.count+x*3],a,self.driver,BeautifulSoup(self.driver.page_source,features="lxml"))
        print("end of thread")

class quitter (threading.Thread):
    def __init__(self, driver1:webdriver,driver2:webdriver,driver3:webdriver):
        threading.Thread.__init__(self)
        self.driver1 = driver1
        self.driver2 = driver2
        self.driver3 = driver3
    def run(self):
        try:
            self.driver1.quit()
        except Exception:
            print(" ")
        try:
            self.driver2.quit()
        except Exception:
            print(" ")
        try:
            self.driver3.quit()
        except Exception:
            print(" ")


f = open("searches","w+")
#options = webdriver.ChromeOptions()
#options.binary_location = "chromedriver.exe"
#options.add_argument('headless')
options = Options()
options.headless = True
driver1 = webdriver.Chrome(options=options,executable_path=r"chromedriver.exe")
driver2 = webdriver.Chrome(options=options,executable_path=r"chromedriver.exe")
driver3 = webdriver.Chrome(options=options,executable_path=r"chromedriver.exe")
#driver = webdriver.PhantomJS("phantomjs-2.1.1-windows/bin/phantomjs.exe")
driver1.get("https://google.com")
driver2.get("https://google.com")
driver3.get("https://google.com")
soup = reloadSoup(driver1)
a = []
amount = 100
searchIndex("W",a,driver1,soup)
thread1 = thread(driver1,0,a,amount//3)
thread2 = thread(driver2,1,a,amount//3)
thread3 = thread(driver3,2,a,amount//3+(amount - (amount//3)*3))
thread4 = quitter(driver1,driver2,driver3)
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
thread4.start()

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
d = SortedDict(d)
sort = sorted(d.items(), key=lambda kv: kv[1])
sort.reverse()
thread4.join()
print(sort)
for key in sort:
    f.write(str(key)+"\n")






