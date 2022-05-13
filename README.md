# pybay
Matches your Discogs wantlist against current ebay listings

## Setup
- Run `pip3 install -r requirements.txt` to install dependencies
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

## Notes
To avoid getting IP blacklisted by Ebay, I've restricted the wantlist to 50 items, but you can change `DISCOGS_PAGE_NUMBER = 1` to a different page and run the script again.

## Example output
![Output](https://raw.githubusercontent.com/cailborg/pybay/main/output.png)