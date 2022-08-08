from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = Options()
chrome_options.add_argument("--headless")

# driver = webdriver.Chrome("chromedriver.exe", options = chrome_options)

driver = webdriver.Chrome("chromedriver.exe")

twitter_url = 'https://twitter.com/RajadoresFutbol'
driver.implicitly_wait(10)
driver.get(twitter_url)

tweets_element = driver.find_element(By.CSS_SELECTOR, '.css-901oao.css-1hf3ou5.r-14j79pv.r-37j5jr.r-n6v787.r-16dba41.r-1cwl3u0.r-bcqeeo.r-qvutc0')

print(tweets_element.text)

# options_list = nav_element.find_element(By.CSS_SELECTOR, ".css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-tzz3ar.r-1pi2tsx.r-lltvgl.r-buy8e9.r-mfh4gg.r-2eszeu.r-hbs49y")

# click_options = options_list.find_elements(By.CSS_SELECTOR, ".css-1dbjc4n.r-16y2uox.r-6b64d0.r-cpa5s6")

# click_url = click_options[0].find_element(By.TAG_NAME, "a")

# ActionChains(driver).click(click_url).perform()

# tweets_element = driver.find_element(By.CSS_SELECTOR,'.css-901oao.r-14j79pv.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-6gpygo.r-1x0uki6.r-bcqeeo.r-ymttw5.r-qvutc0')



# print(len(tweets_elements))


print("finished")
driver.close()