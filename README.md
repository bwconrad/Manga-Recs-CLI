# Manga Recs CLI
Get manga recommendations based on a series through the command line.

## Installation
- Install Python ≥3.10 and Firefox (for Selenium web scraping).
- Run `pip install -r requirements.txt`.

## Usage
```
usage: manga-recs.py [-h] [-n N] [-r] query

positional arguments:
  query       title, AniList url or BookWalker url of work to get recommendations based on

options:
  -h, --help  show this help message and exit
  -n N        maximum number of recommendations to return (default=3)
  -r          Randomize the recommendations order
```

## Examples
```
>> python manga-recs.py "Tensei Shitara Slime Datta Ken" -r 

Setting up...
Getting recommendations for Tensei Shitara Slime Datta Ken (「転生したらスライムだった件～魔物の国の歩き方～」シリーズ)...
1) Tensei Shitara Ken Deshita (転生したら剣でした) - RELEASING
         - https://anilist.co/manga/98014
         - https://bookwalker.jp/defe46422c-7fc3-4f6d-a014-bb5a80d6009a/
2) Tondemo Skill de Isekai Hourou Meshi (とんでもスキルで異世界放浪メシ) - RELEASING
         - https://anilist.co/manga/99049
         - https://bookwalker.jp/def9d0f7c0-7868-4c8a-ae7c-6e8b30936826/
3) Mushoku Tensei: Isekai Ittara Honki Dasu (無職転生 ～異世界行ったら本気だす～) - RELEASING
         - https://anilist.co/manga/85470
         - https://bookwalker.jp/de664bd695-8b62-4319-84dc-b4440479b0ae/
```
```
>> python manga-recs.py "Smile Down the Runway"

Setting up...
Getting recommendations for Runway de Waratte (ランウェイで笑って)...
1) Hitman (ヒットマン) - FINISHED, 13 volumes, 127 chapters
         - https://anilist.co/manga/102903
         - https://bookwalker.jp/de9d46f635-3637-483c-8cb3-0b30a2bb04f7/
2) Watashi no Shounen (私の少年) - FINISHED, 9 volumes, 43 chapters
         - https://anilist.co/manga/98858
         - https://bookwalker.jp/de395d7b8e-37c8-4cc8-9170-c02e2be77d71/
3) Kishuku Gakkou no Juliet (寄宿学校のジュリエット) - FINISHED, 1 chapters
         - https://anilist.co/manga/97927
         - https://bookwalker.jp/dee87d2c82-b8de-4794-8ec7-d3b06d94540d/
```

```
>> python manga-recs.py "絢爛たるグランドセーヌ" -n 5 -r

Setting up...
Getting recommendations for Kenrantaru Grande Scène (絢爛たるグランドセーヌ)...
1) Erzsebet (エルジェーベト) - FINISHED, 3 volumes, 18 chapters
         - https://anilist.co/manga/115828
         - https://bookwalker.jp/de7e9db068-b04a-4d96-b170-1568574ee01e/
2) Eisei Otome no Tatakai Kata (永世乙女の戦い方) - RELEASING
         - https://anilist.co/manga/113257
         - https://bookwalker.jp/de8050be4b-70ca-412f-a2d0-8bd75d72bcb5/
3) Hitohake no Niji (ひとはけの虹) - FINISHED, 3 volumes, 18 chapters
         - https://anilist.co/manga/116412
         - https://bookwalker.jp/de9b4902ea-c458-4822-8902-3e48afd63e28/
4) Arte (アルテ) - RELEASING
         - https://anilist.co/manga/87466
         - https://bookwalker.jp/de48eaf344-e985-4e30-88e8-9297c401364e/
5) Hibiki: Shousetsuka ni Naru Houhou (響～小説家になる方法～) - FINISHED, 13 volumes, 119 chapters
         - https://anilist.co/manga/99040
         - https://bookwalker.jp/de0126fd73-4976-4d84-a28c-33a40e4108df/
```

```
>> python manga-recs.py https://anilist.co/manga/97418/Asobi-Asobase/

Setting up...
Getting recommendations for Asobi Asobase (あそびあそばせ)...
1) Hinamatsuri (ヒナまつり) - FINISHED, 19 volumes, 132 chapters
         - https://anilist.co/manga/66413
         - https://bookwalker.jp/de8335aa19-e942-4d8c-85b0-1f111f3766f8/
2) Ueno-san wa Bukiyou (上野さんは不器用) - RELEASING
         - https://anilist.co/manga/86739
         - https://bookwalker.jp/de6bd63ab5-2451-4d0d-80f4-c9745244f800/
3) Little Chaos (りとる・けいおす ) - FINISHED, 2 volumes, 35 chapters
         - https://anilist.co/manga/96134
         - https://bookwalker.jp/deba35e069-a5dc-48e1-9afb-13560b71dafe/
```


## Tips
- Recommendations can only be retrieved for works available on BookWalker.
- If you are having issues searching for a series try to use the exact spelling found on AniList or the native spelling used on BookWalker.
    - If a work is not on AniList then only searching the native name (in kanji) will work.
- Title discrepancies between BookWalker and AniList may result in inaccuracies in the output or failing to retrieve recommendations.
    - If the output or AniList page appears incorrect check the BookWalker url for the correct recommendation.
- Recommendations are based off recent customer data on BookWalker which often results in currently popular series (ex. currently airing) to have mediocre results. 
