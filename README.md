# Análise de Sentimento

Este é um projeto de análise de sentimento utilizando técnicas de Machine Learning, implementado como uma API usando o framework FastAPI. O objetivo é fornecer uma maneira simples de determinar o sentimento associado a um determinado texto ou imagem.

## Requisitos

Certifique-se de ter o Docker instalado em sua máquina antes de continuar.

## Instalação

1. Clone este repositório para o seu ambiente local:

   ```bash
   git clone https://github.com/BieL-Lopes/desafio-ML.git
   ```

2. Navegue até o diretório do projeto e builda com o Docker:

   ```bash
   cd nome-do-repositorio
   docker build -t analise-sentimento .
   ```

## Uso

1. Após construir a imagem Docker, você pode executar o aplicativo em um contêiner. Certifique-se de mapear a porta corretamente para acessar o aplicativo:

   ```bash
   docker run -p 8000:8000 analise-sentimento
   ```

2. A documentação estará disponível em: http://localhost:8000/docs, fornecido por Swagger UI.

## Endpoint

POST http://localhost:8000/analise

Parâmetros:

- "text" (texto a ser analisado)
- "img" (imagem a ser analisada)


Este endpoint permite enviar um texto ou uma imagem de texto para análise de sentimento. Você pode usar ferramentas como curl ou Postman para fazer solicitações POST.

## Exemplo

- Análise de texto:
   POST /analise

   text=Python é muito bom.

- Análise de imagem:
   POST /analise

   Content-Type: multipart/form-data;
   Accept: application/json

   --boundary
   Content-Disposition: form-data; name="img"; filename="imagem.jpg"
   Content-Type: image/jpeg

   ...conteúdo binário da imagem...
   --boundary--

- Caso precise, na pasta app/example contém alguns exemplos de imagens para teste.

