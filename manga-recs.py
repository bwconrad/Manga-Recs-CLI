import argparse
import warnings

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from src.anilist import search_anilist_id, search_anilist_title
from src.bookwalker import get_recs, search

warnings.filterwarnings("ignore", category=DeprecationWarning)


def main(query: str, n: int = 3, r: bool = False) -> None:
    # Load scrapper
    print("Setting up...")
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, service_log_path="/dev/null")

    # If query is a title then get the bookwalker url
    if query.startswith("https://bookwalker.jp"):
        al_title = None
        query_url = query
    elif query.startswith("https://anilist.co"):
        al_title, romaji = search_anilist_id(query)
        query_url = search(al_title, driver)
    else:
        # Get native name from AL
        al_title, romaji = search_anilist_title(query)

        if al_title == -1:
            # If search failed then try query on BW
            query_url = search(query, driver)
        else:
            query_url = search(al_title, driver)

    # Stop if search failed
    if query_url == -1:
        print(f"Cannot find any results for {query}.")
        return

    # Get recommendations
    results = get_recs(query_url, driver, n, r, romaji)

    # Print results
    for i, (title, url, status, romaji, volumes, chapters, al_url) in enumerate(
        zip(
            results["title"],
            results["url"],
            results["status"],
            results["romaji"],
            results["volumes"],
            results["chapters"],
            results["al_url"],
        )
    ):

        if status == None:
            print(f"{i+1}) {title}\n\t- {url}")
        else:
            string = f"{i+1}) {romaji} ({title}) - {status}"
            if volumes:
                string += f", {volumes} volumes"
            if chapters:
                string += f", {chapters} chapters"
            string += f"\n\t - {al_url}\n\t - {url}"
            print(string)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "query",
        type=str,
        help="title, AniList url or BookWalker url of work to get recommendations based on",
    )
    parser.add_argument(
        "-n",
        type=int,
        default=3,
        help="maximum number of recommendations to return (default=3)",
    )
    parser.add_argument(
        "-r",
        action="store_true",
        help="Randomize the recommendations order",
    )

    args = parser.parse_args()

    main(query=args.query, n=args.n, r=args.r)
