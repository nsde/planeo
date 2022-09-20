import os
import webuntis

from dotenv import load_dotenv

load_dotenv()
env = os.getenv

untis = webuntis.Session(
    username=env('USERNAME'),
    password=env('PASSWORD'),
    server=f"https://ajax.webuntis.com",
    school=env('SCHOOL'),
    useragent='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
)
untis.login()
