import os

home_url = "https://www.coverfox.com/"
browsers = ['chrome', 'firefox', 'edge']
implicit_timeout = 10
explicit_timeout = 10
abs_path = os.path.abspath(path=os.curdir)
chrome_driver_path = (abs_path + "\coverfox\\bin\chromedriver.exe")
print(chrome_driver_path)
