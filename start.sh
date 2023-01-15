#!/bin/bash
tmux new-session -d -s my_session 'source venv/bin/activate && celery -A traffic_disruptor beat'
tmux new-session -d -s my_session 'source venv/bin/activate && celery -A traffic_disruptor worker -B'
