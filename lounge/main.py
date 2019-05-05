import click
import sys
import time

@click.group()
def main():
    pass


@main.group()
def recipe():
    pass


@recipe.command()
def list():
    print('Listing available recipes')


@recipe.command()
def run(add):
	print('Package a new recipe')


@recipe.command()
@click.argument('project', required=False)
def run(project):
	print(f'A project is being cooked for you to start contributing.',
		   'Thank you for all the great code you bring into the system'
		 )
    # myproj = ProjectManager(project)
    # myrecipe = RecipeManager(**myproj.json_data)
    # RecipeExecutor(myrecipe)

"""
def prompter(questions):
    for key, question in questions.items():
        yield key, click.prompt(click.style(question, fg='green'))
"""

"""
if not project:
    questions = dict(
        url='Git URL',
        os="Operating System (mac, windows, linux)",
        recipe_name="What is the recipe file name"
    )
    result = {key:answer for key, answer in prompter(questions)}
"""