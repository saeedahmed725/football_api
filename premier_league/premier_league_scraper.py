# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
from bs4 import BeautifulSoup
import pandas as pd
import requests as request

def getstandings():
    url = 'https://www.premierleague.com/tables'
    requests = request.get(url)
    soup = BeautifulSoup(requests.content, 'html.parser')
    table = soup.find('table')
    table = soup.find('table')
    headers = []
    for th in table.find_all('th'):
        headers.append(th.get_text(strip=True))
    rows = table.find_all('tr')
    data = []
    for row in rows[1:]:  # Skip header row
        cols = row.find_all('td')
        cols = [col.get_text(strip=True) for col in cols]
        if cols:
            data.append(cols)
    df = pd.DataFrame(data, columns=headers)
    df_cleaned = df.dropna()
    for index, row in df_cleaned.iterrows():
        if index >= 9:
            df_cleaned.at[index, 'PositionPos'] = row['PositionPos'][0:2]  # Update for index >= 9
        else:
            df_cleaned.at[index, 'PositionPos'] = row['PositionPos'][0]    # Update for index < 9
    json_data = df_cleaned.to_json(orient='records', force_ascii=False)
    return json_data


# def getstanding():