#!/bin/sh

ENV=$1


if [ "$ENV" = "" ]; then
	echo "ENV arg is required (DEV, PROD)"
elif [ "$ENV" = "DEV" ]; then
	. src/env.sh
	echo "Environment export done!!"
	echo "Running development server..."
	python -m src.app
elif [ "$ENV" = "PROD" ]; then
	echo "Running production server..."
	gunicorn --bind 0.0.0.0:8000 src.app:app
else
	echo "$ENV not supported. Use one of (DEV, PROD)"
fi
