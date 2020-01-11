#!/bin/bash
tmux send-keys -t actor0 'conda activate RL' Enter 'CUDA_VISIBLE_DEVICES="" REPLAY_IP="202.38.64.174" LEARNER_IP="202.38.64.174" ACTOR_IP="202.38.64.174" ACTOR_ID=4 N_ACTORS=8 REGISTERACTORPORT="8079" SENDBATCHPRIORIPORT="8080" UPDATEPRIORIPORT="8081" SAMPLEDATAPORT="8082" SAMPLEDATAPORTRPLAY="9091" PARAMETERPORT="8083" python actor.py' Enter
tmux send-keys -t actor1 'conda activate RL' Enter 'CUDA_VISIBLE_DEVICES="" REPLAY_IP="202.38.64.174" LEARNER_IP="202.38.64.174" ACTOR_IP="202.38.64.174" ACTOR_ID=5 N_ACTORS=8 REGISTERACTORPORT="8079" SENDBATCHPRIORIPORT="8080" UPDATEPRIORIPORT="8081" SAMPLEDATAPORT="8082" SAMPLEDATAPORTRPLAY="9092" PARAMETERPORT="8083" python actor.py' Enter
tmux send-keys -t actor2 'conda activate RL' Enter 'CUDA_VISIBLE_DEVICES="" REPLAY_IP="202.38.64.174" LEARNER_IP="202.38.64.174" ACTOR_IP="202.38.64.174" ACTOR_ID=6 N_ACTORS=8 REGISTERACTORPORT="8079" SENDBATCHPRIORIPORT="8080" UPDATEPRIORIPORT="8081" SAMPLEDATAPORT="8082" SAMPLEDATAPORTRPLAY="9093" PARAMETERPORT="8083" python actor.py' Enter
tmux send-keys -t actor3 'conda activate RL' Enter 'CUDA_VISIBLE_DEVICES="" REPLAY_IP="202.38.64.174" LEARNER_IP="202.38.64.174" ACTOR_IP="202.38.64.174" ACTOR_ID=7 N_ACTORS=8 REGISTERACTORPORT="8079" SENDBATCHPRIORIPORT="8080" UPDATEPRIORIPORT="8081" SAMPLEDATAPORT="8082" SAMPLEDATAPORTRPLAY="9094" PARAMETERPORT="8083" python actor.py' Enter