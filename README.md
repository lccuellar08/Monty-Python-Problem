# Monty Python Problem - Simulation

This repository contains a simple script that runs a simulation of the [Monty Python Problem](https://en.wikipedia.org/wiki/Monty_Hall_problem). A statistical brain teaser that goes as follows:

>Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?

Statistically, one must always choose to switch to the other door, as this will yield a higher probability of winning the car (~66.66%). The script in this repo runs the exact scenario stated in the problem a large number of times and calculates the total Win Rate.

In addition, the win rate increases and eventually converges close to 100% when the total number of doors increases. For example, if there are 10 doors (9 goats, 1 car), after the contestant choses their door, the host will open 8 doors revealing 8 goats, then the contestant has the opportunity to switch their door (raising their win probability to ~90%).

### Results

The script produces the following win rates (1000 simulations for each number of total doors), for different number of total doors:
| Total Doors | Win Rate |
| ----------- | -------- |
| 3 | 67.2% |
| 4 | 77.5% |
| 5 | 79.0% |
| 6 | 82.0% |
| 7 | 85.6% |
| 8 | 88.7% |
| 9 | 90.4% |
| 10 | 88.7% |
| 20 | 94.1% |
| 30 | 96.3% |
| 40 | 97.7% |
| 50 | 98.1% |
| 60 | 98.5% |
| 70 | 98.3% |
| 80 | 98.6% |
| 90 | 99.3% |
| 100 | 99.3% |
| 200 | 99.4% |
| 300 | 99.9% |
| 400 | 99.8% |
| 500 | 99.8% |



### Installing

Download the repository

```
git clone https://github.com/lccuellar08/Monty-Python-Problem.git
```

## Running

Run main.py and pass the total number of simulations you wish to run

Example:
```
python main.py 1000
```