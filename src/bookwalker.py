from random import shuffle

from bs4 import BeautifulSoup
from selenium import webdriver

from .anilist import get_anilist_data
from .utils import clean_title


def search(query: str, driver: webdriver.Firefox):
    """
    Search query on bookwalker and return url to match page
    """
    url = f"https://bookwalker.jp/category/2/?word={query}&order=score&qcat=2&qpri_min=1&qpri_max="

    # Load page html
    driver.get(url)
    soup = BeautifulSoup(
        driver.page_source,
        "lxml",
    )

    entry = soup.find(class_="m-book-item")

    if entry is not None:
        title = entry.find(class_="m-book-item__title").text.strip()
        title = clean_title(title)

        if query in title:
            return entry.find(class_="a-icon-btn--text")["href"]
        else:
            return -1
    else:
        return -1


def get_recs(
    url: str, driver: webdriver.Firefox, n: int = 3, r: bool = False, romaji: str = None
) -> dict:
    """
    Return the cover image and title of recommended series
    """
    # Load page html
    driver.get(url)
    soup = BeautifulSoup(
        driver.page_source,
        "lxml",
    )

    # Get info for queried series
    query_title = get_data(soup)

    if romaji:
        print(f"Getting recommendations for {romaji} ({query_title})...")
    else:
        print(f"Getting recommendations for {query_title}...")

    # Get urls of recs
    data_dict = {
        "title": [],
        "url": [],
        "romaji": [],
        "status": [],
        "volumes": [],
        "chapters": [],
        "al_url": [],
    }
    all_fields = soup.find(class_="m-simple-shelf__list swiper-wrapper").find_all(
        class_="m-book-item__title"
    )
    data_dict["url"] = [x.a["href"] for x in all_fields]

    # Get data for each rec
    if r:
        shuffle(data_dict["url"])
    for i, url in enumerate(data_dict["url"]):
        if i == n:
            break

        # Get series data
        title = get_series_data(url, driver)
        romaji, status, volumes, chapters, al_url = get_anilist_data(title)

        # Append data
        data_dict["title"].append(title)
        data_dict["romaji"].append(romaji)
        data_dict["status"].append(status)
        data_dict["volumes"].append(volumes)
        data_dict["chapters"].append(chapters)
        data_dict["al_url"].append(al_url)

    return data_dict


def get_series_data(url: str, driver: webdriver.Firefox) -> str:
    """
    Get the title and cover image of a series
    """
    # Grab page for series
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "lxml")

    # Get info
    title = get_data(soup)
    title = clean_title(title)

    return title


def get_data(html: BeautifulSoup) -> str:
    # Extract series title
    title = html.find(id="information-section").find("dd").text
    title = clean_title(title)
    return title
