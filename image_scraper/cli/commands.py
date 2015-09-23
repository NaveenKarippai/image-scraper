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
@click.option('--site', help="The site's URL to scrape images from", type=str, callback=validate_url)
def site_scrape(site):
    """
    Takes a URL and scrapes all the images
    """
    click.echo(" - About to scrape images from: {0}".format(site))
    scrap_images = ImageScrapy(site)
    dirName = scrap_images.filePath()
    img_list = scrap_images.parseImgLinks()
    click.echo("   Found {0} images on {1} . please wait while scraping".format(len(img_list),site))
    scrap_images.downloadImages(dirName, img_list)


@cli.command()
@click.option('--file', help="A text file with URLs of the images to download", type=click.Path(exists=True,dir_okay=False,resolve_path=True))
def batch_downloader(file):
    """
    Takes a text file and scrapes the image URLs
    """
    images = ImagesDownload(fileName = file)
    dirName, imageBookPath = images.filePath()
    imageBookData = images.readFile(imageBookPath)
    images.downloadImages(dirName, imageBookData)