from __future__ import annotations
import random
from typing import Optional, List, Deque
from collections import deque
import time


class Reverter:
    """This class represents an array to be sorted. It formally encodes the states of the problem.
    """
    
    def __init__(self, size: int, init: bool = True) -> None:
        """The class only sorts an array containing numbers 1..size. The constructor shuffles the array
        in order to create an unsorted array.

        Args:
            size (int): the size of the array
            init (bool, optional): if True, the array is initialized with value 1..size, then shuffled, else, the array
            remains empty (it is used to clone the array). Defaults to True.
        """
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
        """Returns a string representation of the object Reverter.

        Returns:
            str: The string representation.
        """
        return str(self.table)

    def hash(self):
        """Computes a hashcode of the array. Since it is not possible to hash a list, this one is first
        converted to a tuple.
        """
        self.__hash__ = hash(tuple(self.table))

    def __eq__(self, other: Reverter) -> bool:
        """Tests whether the current object if equals to another object (Reverter). The comparison is made by comparing the hashcodes.

        Args:
            other (Reverter): Another Reverter object to compare with.

        Returns:
            bool: True if self==other, else it is False.
        """
        return self.__hash__ == other.__hash__
    
    def is_the_goal(self) -> bool :
        """Tests whether the table is already sorted (so that the search is stopped).

        Returns:
            bool: True if the table is sorted, else it is False.
        """
        for i in range(1, len(self.table)):
            if self.table[i - 1] > self.table[i]:
                return False
        return True
    
    def clone(self) -> Reverter:
        """Creates a copy of the current object.

        Returns:
            Reverter: The copy to be created.
        """
        res = Reverter(self.size, init=False)
        res.table = [*self.table]
        res.parent = self
        return res
    
    def actions(self) -> List[Reverter]:
        """Builds a list of possible actions. The returned list contains a set of tables depending on possible
        reverting of the current table.

        Returns:
            List[Reverter]: The list of tables obtained after applying the possible reverting.
        """
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

    def solveRandom(self) -> Optional[Reverter]:
        """Implements random search to find the sorted table.

        Returns:
            Optional[Reverter]: The sorted table if found, None otherwise.
        """
        start_time = time.time()
        
        visited: set[int] = set()
        states_visited = 0
        
        current_state = self
        visited.add(current_state.__hash__)
        
        while not current_state.is_the_goal():
            states_visited += 1
            actions = current_state.actions()
            action = random.choice(actions)
            if action.__hash__ not in visited:
                current_state = action
                visited.add(current_state.__hash__)
            else:
                # If the action leads to a visited state, choose another action randomly
                continue
        
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"Time taken by Random Search: {time_taken:.6f} seconds")
        print(f"States visited by Random Search: {states_visited}")
        
        return current_state


size = 5  # Adjust array size as needed
rev = Reverter(size, True)
sorted_array = rev.solveRandom()
if sorted_array:
    print("Sorted array found:")
    print(sorted_array)
else:
    print("No solution found.")
