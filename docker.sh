#!/bin/bash
### COMMANDS
# <empty> - join to a container
#
# --prod - for a production assembly
###

name=skymix
args=("$@")

# Check key in arguments
has_key() {
  for arg in "${args[@]}"; do
    if [[ $arg == $1 ]]; then return 0; fi
  done
  return 1
}

# Set prod or dev mode
has_key "--prod" && mode='prod' || mode='dev'

# Set name prefix
prefix="$mode"_"$name"

docker exec -it "$prefix" /bin/sh