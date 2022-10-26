# friendlysolutions_task
Friendly solutions test task

## Start
``docker compose build``  
``docker compose up -d``  
Run inside container:  
``python manage.py migrate``  
## REST API
#### Main endpoint:  
http://localhost:8000/api/v1/image/
#### Import from api (by album cause all images is too much):
``POST``
``{"albumId": <id>}``  
http://localhost:8000/api/v1/image/import_from_api/
#### Import from file
``POST``
``<binary .json file>``  
http://localhost:8000/api/v1/image/import_from_file/

## CLI commands
Put json file in the project root (where example.json file is)  
Run commands inside docker container
#### Import from api (by album cause all images is too much):
``python manage.py import_from_api <albumId>``
#### Import from file
``python manage.py import_from_file ./example.json``

## Notes
1. I used the [ColorThief](https://github.com/lokesh/color-thief) library for determining the dominant color and the hex doesn't exactly match the names of files in the API you provided, but i uploaded some of the images from this API to online tools that do the same thing & they match my hex & not the one in the name of files, so i hope that's ok because the rgb values are almost identical.
2. I made the import from API take ``albumId`` as an argument and download only 50 images, if the task is to download all 1000 images, i can add celery to the project & use an async task for that.
3. Thank you if you read all this! I hope for some feedback on this. I tried to do this as fast as possible, so i think some things can be improved!
