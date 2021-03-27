#!/bin/bash

ready=0
while [ "$ready" != "1" ]
do
    echo "waiting for database";
    psql $DATABASE_URL -c "select 'yes' as DATABASE_IS_READY" > ./backend/init.output
    ready=`grep yes ./backend/init.output | wc -l`
    sleep 1;
done;
echo "database is ready";
rm ./backend/init.output

gunicorn -w 1 -b 0.0.0.0:5000 --reload --reload-engine auto backend:app
