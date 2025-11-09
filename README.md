# encurtador-links-microservices
#Encurtador de links com Microsserviços (Django + flask + Nginx + Docker)

Este projeto é um encurtador de links desenvolvido com arquitetura de microsserviços, utilizando Django REST Framework, Flask e Nginx para orquestração via Docker Compose.

| Serviço              | Framework    | Função                                       |
| -------------------- | ------------ | -------------------------------------------- |
| **servico-auth**     | Django + DRF | Gerencia autenticação, registro e tokens JWT |
| **servico-links**    | Django + DRF | Cria e gerencia links curtos                 |
| **servico-redirect** | Flask        | Faz o redirecionamento rápido das URLs       |
| **gateway**          | Nginx        | Roteia o tráfego para os serviços corretos   |

🚀 Tecnologias Utilizadas

Python 3.12+

Django REST Framework

Flask

Docker & Docker Compose

Nginx

JWT (JSON Web Token)

# Clonar o repositório
git clone https://github.com/SEU-USUARIO/encurtador-links-microservices.git
cd encurtador-links-microservices

# Subir os containers
docker-compose up --build
