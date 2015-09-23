import click
from  urlparse import urlparse

def validate_url(ctx,param,site):
    if urlparse(site).scheme:
        return site
    else:
        raise click.BadParameter('Invalid URL to scrape provided, please provide a valid URL.')