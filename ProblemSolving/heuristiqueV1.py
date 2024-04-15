from __future__ import annotations
import random
from typing import Optional, List, Tuple
import time


class Reverter:
    """This class represents an array to be sorted. It formally encodes the states of the problem.
    """
    
    def __init__(self, size: int, init: bool = True) -> None:
        """Initializes the Reverter object."""
        if init:
            self.size = size
            self.initial_array = list(range(1, size + 1))
            random.shuffle(self.initial_array)
            self.table = self.initial_array[:]
            self.objective_array = sorted(self.initial_array)
            self.hash()
            self.parent = None
        else:
            self.table = []
            self.initial_array = []
            self.objective_array = []
            self.size = 0
    
    def __str__(self) -> str:
        """Returns a string representation of the object Reverter."""
        return str(self.table)

    def hash(self):
        """Computes a hash code of the array."""
        self.__hash__ = hash(tuple(self.table))

    def __eq__(self, other: Reverter) -> bool:
        """Tests whether the current object is equal to another object (Reverter)."""
        return self.__hash__ == other.__hash__
    
    def is_the_goal(self) -> bool:
        """Tests whether the table is sorted."""
        return self.heuristic() == 0

    
    def clone(self) -> Reverter:
        """Creates a copy of the current object."""
        res = Reverter(self.size, init=False)
        res.table = [*self.table]
        res.parent = self
        return res
    
    def actions(self) -> List[Reverter]:
        """Builds a list of possible actions."""
        res = []
        sz = len(self.table)
        for i in range(sz):
            r = self.clone()
            v = self.table[i:]
            v.reverse()
            r.table = self.table[:i] + v
            r.hash()
            res.append(r)
        return res

    def heuristic(self) -> int:
        """Heuristic function h: Calculates the sum of the number of elements greater than it to the left 
        and the number of elements smaller than it to the right."""
        cost = 0
        for i in range(len(self.table)):
            for j in range(i):
                if self.table[j] > self.table[i]:
                    cost += 1
            for j in range(i + 1, len(self.table)):
                if self.table[j] < self.table[i]:
                    cost += 1
        return cost

    def solveAStar(self) -> Optional[Reverter]:
        """Implements A* search to find the sorted table."""
        start_time = time.time()
        
        visited = set()
        states_visited = 0
        current_state = self
        visited.add(current_state.__hash__)
        
        while not current_state.is_the_goal():
            states_visited += 1
            print(f"Current State: {current_state}, Heuristic Value: {current_state.heuristic()}")
            actions = current_state.actions()
            next_states: List[Tuple[Reverter, int]] = []
            for action in actions:
                if action.__hash__ not in visited:
                    cost = action.heuristic()
                    next_states.append((action, cost))
            if not next_states:
                return None
            next_states.sort(key=lambda x: x[1])
            current_state, heuristic_value = next_states[0]
            visited.add(current_state.__hash__)
        
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"Time taken by A* Search: {time_taken:.6f} seconds")
        print(f"States visited by A* Search: {states_visited}")
        
        # Output the sorted array along with the heuristic value
        print(f"Sorted array found: {current_state}, Heuristic Value: {current_state.heuristic()}")
        
        return current_state



size = 5# Adjust array size as needed
rev = Reverter(size, True)
sorted_array = rev.solveAStar()
if sorted_array:
    print("Sorted array found:")
    print(sorted_array)
else:
    print("No solution found.")
