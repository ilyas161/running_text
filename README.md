# running_text

<h2>Version 1.0</h2>

<h2>What is it?</h2>

This application consist of Django project, that take get request on address http://localhost:8000/textrun/video with param (for example: http://localhost:8000/textrun/video?text=lion )
and response video with this param, that running. App also hold requests in db, you can see it on address http://localhost:8000/textrun/texts
<h2>How to run the program?</h2>

You need docker engine and docker compose. Then you have to use "cd path" in terminal, it is path to repository. After do this command.

```
docker compose up -d
```