# poll-generator

[![Python](https://img.shields.io/badge/python-%2314354C.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-%23092E20.svg?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=flat&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org/)
[![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=flat&logo=heroku&logoColor=white)](https://www.heroku.com)
[![Insomnia](https://img.shields.io/badge/Insomnia-black?style=flat&logo=insomnia&logoColor=5849BE)](https://insomnia.rest/)

## O que é

Este é o backend funcional de um app de criação de enquetes públicas. Ele fornece os seguintes endpoints:

- Endpoint REST para cadastros e edição de enquetes, e registro de votos.
- Endpoint Websocket para acompanhar os resultados em tempo real.

## O que usa

Para desenvolver este projeto, utilizei a seguinte stack:
- [Django](https://www.djangoproject.com/) como base
- [Django Rest Framework](https://www.django-rest-framework.org/) para agilizar funcionalidades do endpoint da API REST
- [Django Channels](https://channels.readthedocs.io/en/stable/) para extender o Django e fazer com que ele suporte conexões websockets
- [Django Rest Framework Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) para autenticação

Também utilizei uma imagem docker do Redis em ambiente de desenvolvimento.

O projeto atualmente está hospedado e funcional no [Heroku](https://www.heroku.com/).

## Features

- Permite cadastrar enquetes com título, descrição, e N opções de voto
- Permite encerrar uma enquete ativa
- Permite reabrir uma enquete encerrada
- Permite excluir uma enquete criada
- Sistema de login e token para ações de criação e edição de enquetes
- Permite receber votos nas enquetes ativas
- Faz o controle para que cada usuário vote somente uma vez em cada enquete, através de um código único gerado e armazenado nos cookies
- Permite vizualizar e acompanhar os resultados das votações em tempo real
