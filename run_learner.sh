#!/bin/bash
tmux send-keys -t learner 'conda activate RL' Enter 'CUDA_VISIBLE_DEVICES=1 LEARNER_IP="202.38.64.174" REPLAY_IP="202.38.64.174" N_ACTORS=8 REGISTERACTORPORT="8079" SENDBATCHPRIORIPORT="8080" UPDATEPRIORIPORT="8081" SAMPLEDATAPORT="8082" PARAMETERPORT="8083" python learner.py --cuda' Enter