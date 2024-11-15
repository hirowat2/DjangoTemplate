import click
import requests
from decouple import config


REPO_OWNER = config('REPO_OWNER')
REPO_NAME = config('REPO_NAME')
TOKEN = config('TOKEN')

@click.command()
@click.option('--title', prompt='Title', help='Digite o título.')
@click.option('--body', prompt='Description', help='Digite a descrição.')
@click.option('--labels', prompt='Labels', help='Digite as labels, separadas por vírgula.')

def make_github_issue(title, body, labels):
    # Formata as labels, caso o usuário tenha fornecido múltiplas
    labels = labels.split(',')

    # Define a URL da API do GitHub
    url = 'https://api.github.com/repos/{owner}/{repo}/issues'.format(
        owner=REPO_OWNER, repo=REPO_NAME)

    # Cabeçalhos da requisição
    headers = {
        'Authorization': f"token {TOKEN}"
    }

    # Criação do objeto de issue
    issue = {
        'title': title,
        'body': body,
        'labels': labels
    }

    # Faz a requisição para criar a issue no GitHub
    req = requests.post(url, json=issue, headers=headers)

    if req.status_code == 201:
        print(f'Successfully created Issue "{title}"')
        number = req.json()['number']
        description = req.json()['body']
        print(f'Issue number: {number}\nIssue description: {description}')

        # Grava a issue no arquivo
        filename = '/home/hiro/Documentos/tarefas.txt'
        write_file(filename, number, title, description, labels)
    else:
        print(f'Could not create Issue "{title}"')
        print('Response:', req.content)


def write_file(filename, number, title, description, labels):
    labels = ', '.join(labels).strip()
    with open(filename, 'a') as file:
        file.write(f'\n---\n\n')
        file.write(f'[] {number} - {title}\n')
        file.write(f'    {labels}\n\n')

        if description:
            file.write(f'    {description}\n\n')

        file.write(f"    make lint; g add . ; g co -m'{title}. close#{number}'; g push\n")


if __name__ == '__main__':
    make_github_issue()
