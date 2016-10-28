import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('-c', '--count', default=1, help='Number of greetings.')
def meow(count):
    click.echo('Synching %s' % count)
