
# Web Scrapping project - Most winning team in NFL history stats

# Importing all required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv


# These lines are no longer necessary due to the Selenium Version
#   path = '\chromedriver'
#   service = Service(path)
#   driver = webdriver.Chrome(service=service, options=options)

# Getting webpage URL and setting up Selenium
url = 'https://www.statmuse.com/nfl/ask/who-is-the-most-winning-team-in-nfl'

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.get(url)

# Creating required variables
set_1 = driver.find_element(By.TAG_NAME, "tbody")
set_2 = set_1.find_elements(By.TAG_NAME, "a")
place = 1
data_dict = {}
data = []

for n in range(1, 21):
    if n % 2 != 0:
        games_played = driver.find_element(By.XPATH, f'//*[@id="container"]/div[2]/div/table/tbody/tr[{place}]/td[3]')
        wins = driver.find_element(By.XPATH, f'//*[@id="container"]/div[2]/div/table/tbody/tr[{place}]/td[4]')
        lose = driver.find_element(By.XPATH, f'//*[@id="container"]/div[2]/div/table/tbody/tr[{place}]/td[5]')
        ties = driver.find_element(By.XPATH, f'//*[@id="container"]/div[2]/div/table/tbody/tr[{place}]/td[6]')
        data_dict = {'Place': place, 'Team': f'{set_2[n].text}', 'GP': games_played.text,  'Wins': wins.text, 'Losses': lose.text, 'Ties': ties.text}
        data.append(data_dict)
        place += 1

fields = ["Place", "Team", "GP", "Wins", "Losses", "Ties"]

with open('NFL_Records.csv', "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()

    for row in data:
        writer.writerow(row)

    print('Complete')

driver.quit()
