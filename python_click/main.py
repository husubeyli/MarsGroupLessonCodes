import click
import os


@click.command()
@click.option('-p', '--project', required=True, help='This is for set project name')
@click.option('-b', '--bootstrap', prompt="Bootstrap elave edilsinmi? Y/N", type=bool)
def create_project(project, bootstrap):
    project_path = os.getcwd()
    if not os.path.isdir(project):
        os.mkdir(project)
    os.system(f'cp -R project_internal/* {project_path}/{project}')
    if not bootstrap:
        with open(f'{project_path}/{project}/index.html', 'r') as f:
            lines = f.readlines()
        del lines[7]
        with open(f'{project_path}/{project}/index.html', 'w') as f:
            for line in lines:
                f.write(line)

    
if __name__ == '__main__':
    create_project()