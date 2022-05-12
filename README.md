# pybay
Matches your Discogs wantlist against current ebay listings

## Setup
- Install `pip3` dependencies: `discogs_client`, `python dot-env`, `requests`, `pandas`, `bs4`
- Make sure your [wantlist](https://www.discogs.com/settings/privacy) is `public`
- Create a Personal Access Token at [Discogs](https://www.discogs.com/settings/developers)
- Create a `.env` file and use the following format

```
TOKEN=YOUR_TOKEN_HERE
USERNAME=YOUR_USERNAME
```

## How to use
- Run `discogs.py` to save your wantlist to disk
- Run `scraper.py` to search ebay for listings
- Open `output.csv` to view your table

## Example output
