import sys
import random
import pprint
from enum import Enum

class Prize(Enum):
	GOAT = 1
	CAR = 2

class Door():
	def __init__(self, prize: Prize):
		self.prize = prize
		self.closed = True

	def open(self):
		if(self.closed):
			self.closed = False
			return self.prize

class GameSim():
	def __init__(self, num_doors = 3):
		self.doors: List[Door] = []
		self.num_doors = num_doors

		self.doors.append(Door(Prize.CAR))
		for i in range(1, num_doors):
			self.doors.append(Door(Prize.GOAT))

		random.shuffle(self.doors)

	def choose_random_door(self):
		door_num = random.randint(0, self.num_doors - 1)
		return door_num

	def open_goat_doors(self, chosen_door):
		doors_opened = 0
		total_doors_to_open = self.num_doors - 2
		for i in range(0, self.num_doors):
			if(doors_opened < total_doors_to_open):
				if(self.doors[i].prize is not Prize.CAR and i != chosen_door):
					prize = self.doors[i].open()
					doors_opened += 1

	def print_closed_doors(self):
		for i in range(0, self.num_doors):
			print(f"Door {i} is closed")

	def switch_doors(self, chosen_door):
		new_door_num = 0
		for i in range(0, self.num_doors):
			if(self.doors[i].closed and i != chosen_door):
				new_door_num = i
		return new_door_num

	def is_winner(self, chosen_door):
		prize = self.doors[chosen_door].open()
		return prize is Prize.CAR

	def print_doors(self):
		for i in range(0, self.num_doors):
			print(f"Door {i} is {self.doors[i].prize}")


def run_simulation(switch_doors = True, num_doors = 3):
	sim = GameSim(num_doors)
	chosen_door = sim.choose_random_door()
	sim.open_goat_doors(chosen_door)
	if(switch_doors):
		chosen_door = sim.switch_doors(chosen_door)
	return sim.is_winner(chosen_door)

def get_win_rate(num_simulations, num_doors):
	wins = 0.0

	for i in range(0, num_simulations):
		if(run_simulation(True, num_doors)):
			wins += 1.0

	win_rate = wins/num_simulations
	return(win_rate)

def growing_win_rate(num_simulations, final_num_doors):
	num_doors = 3
	win_rates = dict()
	while(num_doors <= final_num_doors):
		win_rates[num_doors] = get_win_rate(num_simulations, num_doors)

		if(num_doors < 10):
			num_doors += 1
		elif(num_doors < 100):
			num_doors += 10
		else:
			num_doors += 100

	pprint.pprint(win_rates)


def main(num_simulations = 1000):
	growing_win_rate(num_simulations, 100)
	# win_rate = get_win_rate(num_simulations, 3)
	# print("Win rate: {0:.2%}".format(win_rate))

if __name__ == "__main__":
	num_simulations = int(sys.argv[1])
	main(num_simulations)