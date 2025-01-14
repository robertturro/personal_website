# Stage 1:Build Frontend
FROM node:18 as build-stage

WORKDIR /code

COPY ./frontend/ /code/frontend

WORKDIR /code/frontend

# Installing packages
RUN npm install

#Building the frontend
RUN npm run build

#Stage 2:Build Backend
FROM python:3.12.3 

#Set Environment Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

# Copy Django Project to the container
COPY ./backend/ /code/backend/

#Install the required packages
RUN pip install -r ./backend/requirements.txt

#Copy the frontend build to the Django project
COPY --from=build-stage ./code/frontend/build /code/backend/static/
COPY --from=build-stage ./code/frontend/build/static /code/backend/static/
COPY --from=build-stage ./code/frontend/index.html /code/backend/backend/templates/index.html

#Run Django Migration Command
RUN python ./backend/manage.py migrate

#Run Django Collectstatic Command
RUN python ./backend/manage.py collectstatic --no-input

#Expose the port
EXPOSE 80

WORKDIR /code/backend

#Run the Django Server
CMD ["gunicorn", "backend.wsgi.application", "--bind", "0.0.0.0:8000"]

