from template import AbstractSimulation


class Rule90(AbstractSimulation):
    def __init__(self, number_steps, size):
        super().__init__(number_steps)
        self.size = size
        self.time = 0

    def initialize_sim(self):
        self.arr = [0] * self.size

    def run_one_step(self):
        self.time += 1
        arr_hold = [None] * self.size
        for i in range(self.size):
            if i == 0 or i == self.size - 1:
                arr_hold[i] = 1
            else:
                if self.arr[i - 1] == self.arr[i + 1]:
                    arr_hold[i] = 0
                else:
                    arr_hold[i] = 1
        self.arr = arr_hold

    def print_sim_state(self):
        print(f"At time {str(self.time):2s} the current state is {self.arr}")


rule90 = Rule90(number_steps=5, size=3)
rule90.run()
