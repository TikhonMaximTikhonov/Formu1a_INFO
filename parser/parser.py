from bs4 import BeautifulSoup
import requests

from database.database import DataBase

data_base = DataBase("../database/database.db")


def parse_season(url: str):
    engin = BeautifulSoup(
        requests.get(
            url,
            headers={'User-Agent': 'Mozilla/5.0'}
        ).text, "lxml"
    )

    season = int(engin.find(
        "div",
        {"class": "entity-header__title-name"}
    ).text.strip().split()[1])

    print(str(engin.findAll(
        "td",
        {"class": "tournament-calendar__name"}
    )).count("Гонка"))

    engin.find()

    for race in engin.findAll(
            "td",
            {"class": "tournament-calendar__name"}
    ):
        parse_race(race.findNext("a")["href"])
        # if race.text.strip().startswith("Тесты"):
        #     print(f"Тесты: {race.text.strip().replace('Тесты ', '')}")
        # elif race.text.split(". ")[1].startswith("Гонка"):
        #     print(f"{race.text.strip().split(". ")[0]}: Гонка")
        # else:
        #     print(f"{race.text.strip().split(". ")[0]}: {race.text.strip().split(". ")[1]}")

    return str(data_base.check_season(season))
    # data_base.save_seasons(season)


def parse_race(href: str):
    engin = BeautifulSoup(
        requests.get(
            "https://www.championat.com" + href,
            headers={'User-Agent': 'Mozilla/5.0'}
        ).text, "lxml"
    )

    if engin.find("div", {"class": "match-info__status"}).text.strip() == "Окончено":
        print("OK")
    else:
        print("NOT OK")


if __name__ == "__main__":
    parse_season("https://www.championat.com/auto/_f1/tournament/834/calendar/")
