# Guia de Uso do Poetry

O **Poetry** é uma ferramenta para gerenciamento de dependências e empacotamento de projetos Python.

## 1. Instalar o Poetry

Se você ainda não tem o Poetry instalado, use o comando abaixo:

#### Para sistemas Linux/macOS:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

## 2. Inicializar um Novo Projeto com Poetry

Crie um novo projeto com o Poetry usando o comando:

```bash
poetry new nome-do-projeto
```

Isso criará uma estrutura básica de diretórios para o seu projeto, incluindo o arquivo pyproject.toml.

## 3. Adicionar Dependências

Para adicionar dependências ao seu projeto (como requests, numpy, etc.), use o comando poetry add:

```bash
poetry add requests
```

Para adicionar uma dependência com uma versão específica:

```bash
poetry add requests@2.25.0
```

Para adicionar dependências de desenvolvimento (ex: pytest para testes):

```bash
poetry add --dev pytest
```

## 4. Instalar as Dependências do Projeto

Para instalar as dependências definidas no arquivo pyproject.toml, execute:

```bash
poetry install
```

Isso instalará todas as dependências no ambiente virtual gerenciado pelo Poetry.

## 5. Usar um Ambiente Virtual com Poetry

O Poetry cria automaticamente um ambiente virtual para o projeto. Para ativá-lo, execute:

```bash
poetry shell
```

Isso ativa o ambiente virtual e permite executar comandos Python diretamente nele.

## 6. Executar Scripts ou Comandos no Ambiente Virtual

Se não quiser ativar o ambiente virtual manualmente, você pode executar comandos diretamente com o Poetry, assim:

```bash
poetry run python seu_script.py
```

Ou para executar testes, por exemplo:

```bash
poetry run pytest
```

## 7. Gerenciar Dependências de Produção e Desenvolvimento

O Poetry organiza as dependências em duas categorias:

Dependências de produção: Bibliotecas necessárias para o funcionamento normal do projeto.
Dependências de desenvolvimento: Bibliotecas necessárias apenas para desenvolvimento, como ferramentas de testes ou linters.
Adicione dependências de produção assim:

bash
Copy code
poetry add nome-da-dependencia
Adicione dependências de desenvolvimento assim:

bash
Copy code
poetry add --dev nome-da-dependencia

## 8. Atualizar Dependências

Para atualizar todas as dependências do projeto para as versões mais recentes permitidas pelas restrições de versão no pyproject.toml, use:

bash
Copy code
poetry update
Para atualizar uma dependência específica:

bash
Copy code
poetry update nome-da-dependencia

## 9. Gerar o Arquivo pyproject.toml

O pyproject.toml é o arquivo onde o Poetry gerencia as dependências e configurações do projeto. Sempre que você adicionar ou atualizar dependências, o arquivo será atualizado automaticamente.

## 10. Empacotar o Projeto para Distribuição

Para empacotar o projeto para distribuição (por exemplo, para o PyPI), execute:

bash
Copy code
poetry build
Isso criará os pacotes no formato .tar.gz ou .whl na pasta dist/.

## 11. Publicar o Pacote no PyPI

Após gerar o pacote, você pode publicá-lo no PyPI com:

bash
Copy code
poetry publish --build
Este comando enviará o pacote para o PyPI. Você precisará configurar suas credenciais do PyPI