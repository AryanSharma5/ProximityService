#!/bin/sh

ENV=$1

if [ "$ENV" = "DEV" ]; then
	# List your all dev env export cmds in below file
	. src/env.sh
	echo "Environment exports done!!"
fi

python -m src.app