#!/bin/bash

cd backend
heroku container:push web --app python-stack-backend
heroku container:release web --app python-stack-backend
cd ..

cd nginx
heroku container:push web --app python-stack
heroku container:release web --app python-stack
cd ..

open https://python-stack.herokuapp.com