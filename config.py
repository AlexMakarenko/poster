from sys import platform
import os
import logging

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#   chromedriver settings
if platform.lower() == 'darwin':
    CHROMEDRIVER = BASE_DIR + "/chromedrivers/chromedriver_mac"
elif platform.lower() == 'linux':
    CHROMEDRIVER = BASE_DIR + "/chromedrivers/chromedriver_linux"
else:
    CHROMEDRIVER = BASE_DIR + "\\chromedrivers\\chromedriver.exe"

#   logging settings
log_level = logging.INFO
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=log_level)
log = logging


#   project settings
HEADLESS = False
HOME_PAGE = 'https://joinposter.com/'
DEF_WAIT_TIME = 20
DEF_PASSWORD = "Makarenko1"



