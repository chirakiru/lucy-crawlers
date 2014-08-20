## Lucy Crawlers
> Lucy's web crawler and web scraper.

[Lucy](https://github.com/chirakiru/lucy "Code repository") is a tool to visualize in a friendly way truthful information about the status of air pollution.

## Installation

### Ubuntu 14.04.1 LTS (Trusty Tahr):
Commands to install [Scrapy](http://doc.scrapy.org):

```bash
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 627220E7
$ echo 'deb http://archive.scrapy.org/ubuntu scrapy main' | sudo tee /etc/apt/sources.list.d/scrapy.list
$ sudo apt-get update && sudo apt-get install scrapy-0.24
```

### OS X
Install [pip](https://pip.pypa.io/en/latest/):

```bash
$ sudo easy_install pip
```

And then, install Scrapy

```bash
$ sudo pip install scrapy
```

## Usage

```bash
$ scrapy crawl pollutants
```

Also, you can check [scrapy's documentation](http://doc.scrapy.org/en/latest/index.html).
