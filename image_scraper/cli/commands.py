import click
from image_scraper import ImageScrapy, ImagesDownload
from image_scraper.cli.validators import validate_url

@click.group()
def cli():
    """
    A site image scraping tool.
    """
    pass


@cli.command()
@click.option('--site', help="The site's URL to scrape images from.", type=str, callback=validate_url)
@click.option('--depth',help="Recursively scrape up to this depth (HTML tree depth), defaults to 1.",type=int)
def site_scrape(site,depth=1):
    """
    Takes a URL and scrapes all the images
    """
    click.echo(" - About to scrape images from: {0}".format(site))
    scrap_images = ImageScrapy(site)
    dirName = scrap_images.filePath()
    img_list = scrap_images.parseImgLinks(depth)
    if len(img_list):
        click.echo("   Scraping collected images:")
        scrap_images.downloadImages(dirName, img_list)
    else:
        click.echo("   Images not found on this page")



@cli.command()
@click.option('--file', help="A text file with URLs of the images to download.", type=click.Path(exists=True,dir_okay=False,resolve_path=True))
def batch_downloader(file):
    """
    Takes a text file and scrapes the image URLs
    """
    images = ImagesDownload(fileName = file)
    dirName, imageBookPath = images.filePath()
    imageBookData = images.readFile(imageBookPath)
    images.downloadImages(dirName, imageBookData)