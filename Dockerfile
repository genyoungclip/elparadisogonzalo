FROM node:22 AS frontend

WORKDIR /frontend

COPY frontend/package*.json ./

RUN npm install

COPY frontend .

RUN npm run build



FROM python:3.12-slim

WORKDIR /app

COPY . .

COPY --from=frontend /frontend/dist src/elparadisogonzalo/static

RUN pip install .

EXPOSE 8000

CMD ["elparadisogonzalo"]
