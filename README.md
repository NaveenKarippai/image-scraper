# image-scraper [![Build Status](https://travis-ci.org/nathanIL/image-scraper.svg)](https://travis-ci.org/nathanIL/image-scraper)
Python script to scrap images 

### Developer's guide
```
$ git clone https://github.com/NaveenKarippai/image-scraper
$ cd image-scraper
```

### Information
_Usage:_
```Bash
python scraper.py --help
```
will show:
```Bash
Usage: scraper.py [OPTIONS] COMMAND [ARGS]...

  A site image scraping tool.

Options:
  --help  Show this message and exit.

Commands:
  batch_downloader  Takes a text file and scrapes the image URLs
  site_scrape       Takes a URL and scrapes all the images
```
##### site_scrape
```Bash
# python scraper.py site_scrape --help
Usage: scraper.py site_scrape [OPTIONS]

  Takes a URL and scrapes all the images

Options:
  --site TEXT  The site's URL to scrape images from
  --help       Show this message and exit.
```
##### batch_downloader
```Bash
# python scraper.py batch_downloader --help
Usage: scraper.py batch_downloader [OPTIONS]

  Takes a text file and scrapes the image URLs

Options:
  --file PATH  A text file with URLs of the images to download
  --help       Show this message and exit.

```

### Unit Testing
`$ python -m unittest discover -v tests/`

### Contributing
Please read the ![contributor's guide](https://github.com/NaveenKarippai/image-scraper/blob/master/CONTRIBUTING.md) before a pull request.

### ToDo
Please read the ![ToDo list](https://github.com/NaveenKarippai/image-scraper/blob/master/TODO.md) for tasks you could contribute to.
