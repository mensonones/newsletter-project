## API de Newsletter Simples com Python e Django

**Descrição:**

Este projeto é uma API RESTful simples para gerenciar newsletters em Python e Django.

**Funcionalidades:**

* Cadastro de assinantes
* Criação de newsletters
* Envio de newsletters

**Tecnologias:**

* Python
* Django
* Django REST Framework
* Celery (opcional)
* RabbitMQ (opcional)

**Instalação:**

1. Clone o repositório:

```
git clone https://github.com/mensonones/newsletterProject.git
```

2. Crie um ambiente virtual e instale as dependências:

```
python -m venv venv
pip install -r requirements.txt
```

3. Configure o banco de dados:

```
cp .env.example .env
```

Edite o arquivo `.env` e configure as variáveis de ambiente do banco de dados.

4. Crie as migrations e migre o banco de dados:

```
python manage.py makemigrations
python manage.py migrate
```

5. Inicie o servidor de desenvolvimento:

```
python manage.py runserver
```

**Uso:**

* Cadastro de assinantes:

```
POST /api/subscribers/
```

Body:

```json
{
  "email": "seuemail@exemplo.com"
}
```

* Criação de newsletter:

```
POST /api/newsletters/
```

Body:

```json
{
  "subject": "Assunto da newsletter",
  "body": "Conteúdo da newsletter",
}
```

**Contribuições:**

Sinta-se à vontade para contribuir com o projeto. Para mais informações, consulte o arquivo `CONTRIBUTING.md`.

**Licença:**

Este projeto é licenciado sob a licença MIT.

**Observações:**

* Este projeto é um exemplo simples. Adapte-o às suas necessidades específicas.
* Utilize bibliotecas de email para enviar as newsletters (e.g., `django-sendgrid`).

**Recursos adicionais:**

* Documentação do Django: [https://www.djangoproject.com/](https://www.djangoproject.com/)
* Documentação do Django REST Framework: [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)
* Documentação do Celery: [https://docs.celeryq.dev/en/stable/]([https://www.medicalnewstoday.com/articles/270678](https://docs.celeryq.dev/en/stable/))
* Documentação do RabbitMQ: [https://www.rabbitmq.com/](https://www.rabbitmq.com/)
