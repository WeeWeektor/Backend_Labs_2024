# Backend_Labs_2024
### Технології розробки серверного програмного забезпечення 2024

## Опис
Цей проект є простим Flask-додатком, що містить `healthcheck` ендпоінт, який повертає HTTP статус 200 разом із поточною датою та статусом сервісу. Проект також містить налаштування для Docker та Docker-Compose, що дозволяє легко запускати та тестувати додаток у контейнері.

## Інструкції по встановленню та запуску

### Локальний запуск
1. **Клонуйте репозиторій**:
   ```bash
   git clone https://github.com/WeeWeektor/Backend_Labs_2024.git

2. **Перейдіть у директорію проекту**:
   ```bash
   cd <project-directory>

3. **Створіть віртуальне середовище та активуйте його**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   
4. **Встановіть залежності**:
   ```bash
   pip install -r requirements.txt

5. **Запустіть додаток**:
   ```bash
   flask --app views.py run --host 0.0.0.0 --port 8080

6. **Перевірте ендпоінт /healthcheck: Відкрийте браузер або надішліть запит до**:
   ```bash
   http://127.0.0.1:8080/healthcheck


### Запуск за допомогою Docker
1. **Зібрати Docker-образ**:
   ```bash
   docker build . -t labs_backend:latest

2. **Запустити контейнер**:
   ```bash
   docker run -it --rm --network=host -e PORT=8080 labs_backend:latest

3. **Перевірте ендпоінт /healthcheck: Відкрийте браузер або надішліть запит до**:
   ```bash
   http://127.0.0.1:8080/healthcheck


### Запуск за допомогою Docker-Compose
1. **Запустіть команду для збілду та запуску контейнерів**:
   ```bash
   docker-compose up --build

2. **Перевірте ендпоінт /healthcheck: Відкрийте браузер або надішліть запит до**:
   ```bash
   http://127.0.0.1:8080/healthcheck


### Деплой на Render.com
1. Зареєструйтесь на render.com.
2. Створіть новий Web Service, підключивши свій репозиторій.
3. Після завершення деплою, ваш додаток буде доступний за вказаною адресою.