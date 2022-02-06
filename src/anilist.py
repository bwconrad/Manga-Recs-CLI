import re
from typing import Any

import requests


def get_anilist_data(title: str):
    query = """
    query ($search: String) {
      Media (search: $search, type: MANGA) { 
        status
        volumes
        chapters
        title {
            romaji
            native
        }
        siteUrl
      }
    }
    """

    url = "https://graphql.anilist.co"
    variables = {"search": title}

    # Make the HTTP Api request
    response = requests.post(url, json={"query": query, "variables": variables}).json()

    if "errors" in response.keys():
        return None, None, None, None, None
    else:
        data = response["data"]["Media"]
        return (
            data["title"]["romaji"],
            data["status"],
            data["volumes"],
            data["chapters"],
            data["siteUrl"],
        )


def search_anilist_title(search: str) -> tuple[Any, Any]:
    query = """
    query ($search: String) { 
      Media (search: $search, type: MANGA) {
        title {
            romaji
            native
        }
      }
    }
    """

    url = "https://graphql.anilist.co"
    variables = {"search": search}

    # Make the HTTP Api request
    response = requests.post(url, json={"query": query, "variables": variables}).json()

    if "errors" in response.keys():
        return -1, -1
    else:
        return (
            response["data"]["Media"]["title"]["native"],
            response["data"]["Media"]["title"]["romaji"],
        )


def search_anilist_id(url: str) -> tuple[Any, Any]:
    idxs = [m.start() for m in re.finditer(r"/", url)]
    id = url[idxs[3] + 1 : idxs[4]]

    # Here we define our query as a multi-line string
    query = """
    query ($id: Int) { 
      Media (id: $id, type: MANGA) {
        title {
            romaji
            native
        }
      }
    }
    """

    url = "https://graphql.anilist.co"
    variables = {"id": id}

    # Make the HTTP Api request
    response = requests.post(url, json={"query": query, "variables": variables}).json()

    if "errors" in response.keys():
        return -1, -1
    else:
        return (
            response["data"]["Media"]["title"]["native"],
            response["data"]["Media"]["title"]["romaji"],
        )
