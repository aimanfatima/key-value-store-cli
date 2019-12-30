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
    response = requests.get('{}/Employee/{}.json'.format(os.getenv('URL'), employee_id))
    if response.json():
        click.echo("\nThe Employee ID is already assigned to someone, use another ID \n")
    else:
        response = requests.put( '{}/Employee/{}.json'.format(os.getenv('URL'), employee_id),json={'name': '{}'.format(name)} )
        click.echo('Employee {} added!'.format(employee_id))
        click.echo(response.json())

@cli.command()
def list_all():
    """
    Views the list of all the Employees
    """
    response = requests.get('{}/Employee.json'.format(os.getenv('URL')))
    click.echo('\nHere\'s a list of all the present Employees : \n\n')
    data = response.json()
    click.echo('\nEmployee id:            Name:\n\n')
    for emp_id in data:
        name = data[emp_id]['name']
        click.echo('{}                      {}'.format(emp_id, name))
    click.echo('\n\n')

@cli.command()
@click.argument('employee_id')
def view(employee_id):
    """
    View single Employee with a particular ID
    """
    response = requests.get('{}/Employee/{}.json'.format(os.getenv('URL'), employee_id))
    if not response.json():
        click.echo("\nThe Employee you are searching dosen't exist !!\n")
    else:
        data = response.json()
        for emp_id in data:
            click.echo('{} : {}'.format(emp_id, data[emp_id]))


@cli.command()
@click.argument('employee_id')
@click.option('--name', '-n', required=True)
def update(employee_id, name):
    """
    Update the info of an employee
    """
    response = requests.get('{}/Employee/{}.json'.format(os.getenv('URL'), employee_id))
    if not response.json():
        click.echo("\nThe Employee you are trying to update dosen't exist, you may add new !!\n")
    else:
        response = requests.patch('{}/Employee/{}.json'.format(os.getenv('URL'), employee_id),json={'name': '{}'.format(name)})
        click.echo('The information is updated !!')
        click.echo(response.json())

@cli.command()
@click.argument('employee_id')
def delete(employee_id):
    """
    Delete contact
    """
    requests.delete('{}/Employee/{}.json'.format(os.getenv('URL'), employee_id))
    click.echo('\nEmployee deleted!\n')