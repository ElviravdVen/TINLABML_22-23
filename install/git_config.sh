#!/usr/bin/env bash

argument_names=("name" "email")
argument_values=("$@")
nr_of_arguments=${#argument_values[@]}

if [ $nr_of_arguments -lt ${#argument_names[@]} ]; then
    printf "USAGE: %s %s\n" "$0" "${argument_names[*]}"
    exit 1;
fi

git config user.name "${argument_values[0]}"
git config user.email "${argument_values[1]}"
git config --list | grep user

git config pull.rebase false