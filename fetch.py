import requests
import sys


def get_cookie() -> str:
    with open('.sessions') as f:
        return f.readline().strip().split('=', 1)[1]

def download_input(session_cookie, year: int = 2023, day: int = 1):
    response = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies={'session': session_cookie})
    response.raise_for_status()

    with open(f'Day{day:02}/input.txt', 'w') as f:
        f.write(response.text)

def main():
    year = int(sys.argv[1])
    day = int(sys.argv[2])
    session_cookie = get_cookie()

    download_input(session_cookie, year, day)

if __name__ == '__main__':
    main()
