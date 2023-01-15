#!/bin/bash
source venv/bin/activate
pip install -r requirements.txt
tmux new-session -d -s session_beat 'source venv/bin/activate && celery -A traffic_disruptor beat'
tmux new-session -d -s session_worker 'source venv/bin/activate && celery -A traffic_disruptor worker -B'
