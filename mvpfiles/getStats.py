from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
from basketball_reference_scraper.seasons import get_schedule, get_standings

import pandas as pd
from bs4 import BeautifulSoup
import requests
import os

# Output all player season totals from each season into a csv file stored in statsBySeason folder 
"""
for i in range(2017, 2024):
    source = requests.get(f"https://www.basketball-reference.com/awards/awards_{i+1}.html").text
    soup = BeautifulSoup(source, 'html.parser')
    print("working", i)
    table = soup.find('table', attrs={'id':'mvp'})
    df = pd.read_html(str(table))[0]
    df.to_csv(f"./trainData/{i+1}mvpVotes.csv")


for i in range(2013, 2024):
    source = requests.get(f"https://www.basketball-reference.com/leagues/NBA_{i+1}_per_game.html").text
    soup = BeautifulSoup(source, 'html.parser')
    table2 = soup.find('table', attrs={'id': 'per_game_stats'})
    df2 = pd.read_html(str(table2))[0]
    df2.to_csv(f"./pgstats/{i+1}perGameStats.csv")
"""

for i in range(2013, 2024):
    source = requests.get(f"https://www.basketball-reference.com/leagues/NBA_{i+1}_advanced.html").text
    soup = BeautifulSoup(source, 'html.parser')
    table2 = soup.find('table', attrs={'id': 'advanced_stats'})
    df2 = pd.read_html(str(table2))[0]
    df2 = df2[['Player', 'WS', 'WS/48']]
    df2.to_csv(f"/Users/suvanamruth/Documents/MVPprediction/mvpfiles/winShares/{i+1}winShares.csv")
