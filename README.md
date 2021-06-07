# poll-generator

## O que é

Este é o backend funcional de um app de criação de enquetes públicas. Ele fornece os seguintes endpoints:

- Endpoint REST para cadastros e edição de enquetes, e registro de votos.
- Endpoint Websocket para acompanhar os resultados em tempo real.

## O que usa

Para desenvolver este projeto, utilizei a seguinte stack:
- [Django](https://www.djangoproject.com/) como base
- [Django Rest Framework](https://www.django-rest-framework.org/) para agilizar funcionalidades do endpoint da API REST
- [Django Channels](https://channels.readthedocs.io/en/stable/) para extender o Django e fazer com que ele suporte conexões websockets

Também utilizei uma imagem docker do Redis em ambiente de desenvolvimento.

O projeto atualmente está hospedado e funcional no [Heroku](https://www.heroku.com/).

## Features

- Permite cadastrar enquetes com título, descrição, e N opções de voto
- Permite encerrar uma enquete ativa
- Permite reabrir uma enquete encerrada
- Permite excluir uma enquete criada
- Permite receber votos nas enquetes ativas
- Faz o controle para que cada usuário vote somente uma vez em cada enquete, através de um código único gerado e armazenado nos cookies
- Permite vizualizar e acompanhar os resultados das votações em tempo real
