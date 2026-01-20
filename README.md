# ns3-rl-congestion-control

This repository implements an RL-based congestion control framework
for ns-3 using three native control parameters:

1. Scheduler Weight Vector
2. AQM Aggressiveness
3. Flow-to-Class Mapping

The goal is live congestion control under delayed rewards,
not traffic prediction.

The code is structured to support:
- Offline learning
- Safe RL experimentation
- Future integration with ns-3 simulations
