<img src="https://th.bing.com/th/id/OIP.tZKxFU0lwHLBBNMxk53WfAHaJh?w=169&h=218&c=7&r=0&o=5&dpr=1.6&pid=1.7" alt="Ícone Json" width="200" height="200">

# Site em Flask

Site simples feito com Flask para aprendizado e desenvolvimento de habilidades em Front-End e Back-End.

## Tecnologias Utilizadas

- **Python**: Linguagem principal utilizada no desenvolvimento do site.
- **Flask**: Framework web utilizado para a criação das rotas e lógica do servidor.
- **HTML/CSS**: Para estruturação e estilização das páginas.
- **JavaScript**: Para funcionalidades interativas (se aplicável).
- **MySQL**: Banco de dados utilizado para armazenar informações (ajustar conforme o banco de dados utilizado).
- **Json**: Banco de dados emprovisado utilizado para armazenar informações dentro de arrays.

## Funcionalidades

- Fazer get no mysql e json

## Como Executar o Projeto

### Pré-requisitos

- **Python 3.x**: Certifique-se de ter o Python instalado em sua máquina.
- **Virtualenv** (opcional, mas recomendado): Para criar um ambiente virtual isolado.

### Instalação

1. Clone o repositório para a sua máquina local:

   ```bash
   git clone https://github.com/seu-usuario/flask-com-mysql-e-json.git
   cd flask-com-mysql-e-json

2. (Opcional) Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`

3. Instale as dependências do projeto:
   
   ```bash
   pip install -r requirements.txt

### Configuração

1. Crie um arquivo .env na raiz do projeto e adicione as variáveis de ambiente necessárias (por exemplo, a URL do banco de dados, chave secreta do Flask, etc.).

2. (Opcional) Execute as migrações para configurar o banco de dados:
   
   ```bash
   flask db upgrade

### Executar o Servidor

1. Inicie o servidor Flask:
   
   ```bash
   flask run

2. Acesse o site no navegador:
   
   ```bash
   [flask run](http://127.0.0.1:5000)

### Testes

- Para executar os testes:

   ```bash
   pytest

### Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (git checkout -b feature/nova-feature).
3. Commit suas alterações (git commit -m 'Adiciona nova feature').
4. Envie para o repositório remoto (git push origin feature/nova-feature).
5. Abra um Pull Request.

### Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
