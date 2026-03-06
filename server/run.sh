#!/bin/bash

set -e

COMMAND=$1

case "$COMMAND" in
  dev)
    python manage.py runserver
    ;;

  migrate)
    APP=$2
    NUMBER=$3
    python manage.py makemigrations
    if [ -n "$APP" ] && [ -n "$NUMBER" ]; then
      python manage.py migrate "$APP" "$NUMBER"
    else
      python manage.py migrate
    fi
    ;;

  setup)
    python manage.py setup
    ;;

  *)
    echo "Usage: ./run.sh <command>"
    echo ""
    echo "Commands:"
    echo "  dev                        Start the development server"
    echo "  migrate [app] [number]     Run makemigrations + migrate"
    echo "                             Optionally target a specific migration"
    echo "  setup                      Create superuser + default organization (admin@localhost.com / p)"
    exit 1
    ;;
esac
