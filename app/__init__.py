import click
import os
import requests

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo("\nWelcome to the Key-Value-Store-CLI app !!\n")
        click.echo("\nTo see all the commands options, run employee --help\n")


@cli.command()
@click.argument('employee_id')
@click.option('--name', '-n', required=True)
def add(employee_id, name):
    """
    Add a new Employee
    """
    response = requests.put( '{}/Employee/{}.json'.format(os.getenv('URL'), employee_id),json={'name': '{}'.format(name)} )
    click.echo('Employee {} added!'.format(employee_id))
    click.echo(response.json())