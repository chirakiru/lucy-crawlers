# Scrapy settings for calidadaire project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'air_quality_bot'

SPIDER_MODULES = ['air_quality.spiders']
NEWSPIDER_MODULE = 'air_quality.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'calidadaire (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'air_quality.pipelines.AirQualityPipeline': 300
}