# Data

**Dataset:** [UCI Online News Popularity](https://archive.ics.uci.edu/dataset/332/online+news+popularity)
— 39,644 Mashable articles, 58 content features, target = number of shares.

## One-step download
```bash
curl -L -o data/news.zip "https://archive.ics.uci.edu/static/public/332/online+news+popularity.zip"
unzip data/news.zip -d data/
```
This produces `data/OnlineNewsPopularity/OnlineNewsPopularity.csv`. The notebook does all
target definition (median split) and feature prep.

Raw data is kept out of git via `.gitignore`.
