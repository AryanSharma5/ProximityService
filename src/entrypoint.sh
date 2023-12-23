#!/bin/sh

# List your all env export cmds in below file
. src/env.sh

flask --app src.app run --reload