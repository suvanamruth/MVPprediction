from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
from basketball_reference_scraper.seasons import get_schedule, get_standings

import pandas as pd
from bs4 import BeautifulSoup
import requests
import os

# Output all player season totals from each season into a csv file stored in statsBySeason folder 
"""
print("Writing player season totals for each season to CSV file")
for i in range(1987, 2024):
    file_path = "./statsBySeason/" + str(i) + "_" + str(i+1) + "_player_season_totals.csv"
    client.players_season_totals(season_end_year=i+1, output_type=OutputType.CSV, output_file_path=file_path)
"""

for i in range(2017, 2024):
    source = requests.get(f"https://www.basketball-reference.com/awards/awards_{i+1}.html").text
    soup = BeautifulSoup(source, 'html.parser')
    print("working", i)
    table = soup.find('table', attrs={'id':'mvp'})
    df = pd.read_html(str(table))[0]
    df.to_csv(f"./trainData/{i+1}mvpVotes.csv")

