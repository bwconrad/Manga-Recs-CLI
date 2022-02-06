def clean_title(title: str) -> str:
    if title[-1] == "）":
        title = title[: title.rfind("（")]
    if title[-1] == ")":
        title = title[: title.rfind("(")]
    if title[-1] == "】":
        title = title[: title.rfind("【")]
    if "モノクロ版" in title:
        title = title[: title.find("モノクロ版")]
    if "カラー版" in title:
        title = title[: title.find("カラー版")]
    if "完全版" in title:
        title = title[: title.find("完全版")]

    return title
