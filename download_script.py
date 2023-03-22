import requests as req
import os
from dotenv import load_dotenv
load_dotenv()

def download_input_files(year):
    """To download all input files for a given year"""
    for day in range(1,26):
        url = f'https://adventofcode.com/{year}/day/{day}/input'
        cookies = {'session': os.getenv('AOC_SESSION')}
        resp = req.get(url, cookies=cookies)
        with open('./input/D'+str(day).zfill(2)+'.txt', 'wb') as f:
            f.write(resp.content)

if __name__ == '__main__':
    download_input_files(2022)