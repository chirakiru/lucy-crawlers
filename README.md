## lucy-crawlers

lucy's web crawler and web scraper.

[lucy](https://github.com/chirakiru/lucy "Code repository") is a tool to visualize in a friendly way truthful information about the status of quality air.

## Installation

Ubuntu 14.04.1 LTS (Trusty Tahr):

Scrapy:

```bash
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 627220E7
echo 'deb http://archive.scrapy.org/ubuntu scrapy main' | sudo tee /etc/apt/sources.list.d/scrapy.list
sudo apt-get update && sudo apt-get install scrapy-0.24
```

## Usage

```bash
scrapy crawl pollutants
```

Also, you can check [scrapy's documentation](http://doc.scrapy.org/en/latest/index.html).
