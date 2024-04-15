from __future__ import annotations  #it allows us to use the name of a class that has not been defined yet in type annotations (making forward references possible without causing errors.)

import random  #shuffle arrays.
from typing import Optional, List, Deque  #importing types (Deque = variable should be a double-ended queue)
from collections import deque  #importing deque for implementing a queue
import time  #Measure the execution time

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
        if init: #checks if the init parameter is True
            self.size = size  #setting the size of the array.
            self.initial_array = list(range(1, size + 1))  #creating a sorted array from number 1 to size
            random.shuffle(self.initial_array)  #shuffling the array to make it unsorted
            self.table = self.initial_array[:]  #creating a copy the shuffled array and assign it to table 
            self.objective_array = sorted(self.initial_array)  #creating a sorted version of the array for comparison
            self.hash()  #generating a hash for the array (represents the current state of the sorting problem)
            self.parent = None  #parent att as None.
        else:
            self.table = []  #all 3 initialize empty arrays and set the size to 0 if init is False
            self.initial_array = [] 
            self.objective_array = []  
            self.size = 0  #initializing size as 0.
    
    def __str__(self) -> str:
        """Returns a string representation of the object Reverter.

        Returns:
            str: The string representation.
        """
        return str(self.table)  #returning the array as a string

    def hash(self):
        """Computes a hashcode of the array. Since it is not possible to hash a list, this one is first
        converted to a tuple.
        """
        self.__hash__ = hash(tuple(self.table))  #converting the array to a tuple and hashing it

    def __eq__(self, other: Reverter) -> bool:
        """Tests whether the current object if equals to another object (Reverter). The comparison is made by comparing the hashcodes.

        Args:
            other (Reverter): Another Reverter object to compare with.

        Returns:
            bool: True if self==other, else it is False.
        """
        return self.__hash__ == other.__hash__  #Comparing the hash-codes of two objects
    
    def is_the_goal(self) -> bool :
        """Tests whether the table is already sorted (so that the search is stopped).

        Returns:
            bool: True if the table is sorted, else it is False.
        """
        for i in range(1, len(self.table)):  #iterating through the array
            if self.table[i - 1] > self.table[i]:  #checking if the array is sorted (self.table[i]) is smaller than the previous element (self.table[i - 1]). != because a smaller element appears after a larger one)
                return False  
        return True 
    
    def clone(self) -> Reverter:
        """Creates a copy of the current object.

        Returns:
            Reverter: The copy to be created.
        """
        res = Reverter(self.size, init=False)  #creating a new Reverter object (same size as the current object but initializes it with an empty array)
        res.table = [*self.table]  #copying content of the current array to the new object
        res.parent = self  #setting the parent of the new object (tracking the parent-child relationships between different states during the search process)
        return res  #returning the new object
    
    def actions(self) -> List[Reverter]:
        """Builds a list of possible actions. The returned list contains a set of tables depending on possible
        reverting of the current table.

        Returns:
            List[Reverter]: The list of tables obtained after applying the possible reverting.
        """
        res = []  #initializing an empty list to store (the possible actions)
        sz = len(self.table)  #getting the size of the array (determine the range of indices to iterate over)
        for i in range(sz):  #iterating through the array (consider each element as a potential pivot for the reversing operation)
            r = self.clone()  #cloning the current object
            v = self.table[i:]  #slicing the array (sublist)
            v.reverse()  #reversing the sliced array
            r.table = self.table[:i] + v  #updating the array with the reversed slice
            r.hash()  #generating a hash for the new array
            res.append(r)  #appending the new array to the result list
        return res  #(possible actions)

    def solveBreadth(self) -> Optional[Reverter]:
        """Implements breadth first search to find the sorted table.

        Returns:
            Optional[Reverter]: The sorted table if found, None otherwise.
        """
        start_time = time.time()   #Recording(the start time)
        
        queue: Deque[Reverter] = deque()  #initializing a deque for the queue (data struct to use as a queue for storing states to be explored)
        visited: set[int] = set()  #initializing a set to store visited states (to keep track)
        states_visited = 0  #initializing a counter for visited states
        
        queue.append(self)  #adding the initial state to the queue (we keep track of the states we need to explore 'Let's start exploring the problem from this particular configuration')
        visited.add(self.__hash__)  #adding the hash of the initial state to visited set
        
        while queue:  #Looping until the queue is empty
            current_state = queue.popleft()  #Dequeuing the current state (to explore more actions)
            states_visited += 1  #incrementing the counter for visited states
            
            if current_state.is_the_goal():  #Checking if the current state is the goal
                end_time = time.time()  #recording the end time
                time_taken = end_time - start_time  #Calculating the taken time
                print(f"Time taken by Breadth First Search: {time_taken:.6f} seconds")  
                print(f"States visited by Breadth First Search: {states_visited}")  
                return current_state  
            
            for action in current_state.actions():  #looping through possible actions
                if action.__hash__ not in visited:  #checking if the action has not been visited
                    queue.append(action)  #enqueuing the action to explore
                    visited.add(action.__hash__)  #adding the hash of the action to visited set
        
        end_time = time.time()  
        time_taken = end_time - start_time  
        print(f"Time taken by Breadth First Search: {time_taken:.6f} seconds") 
        print(f"States visited by Breadth First Search: {states_visited}")  
        return None  


size = 8  
rev = Reverter(size, True)  # an instance of Reverter class with size and init parameter
sorted_array = rev.solveBreadth()  #applying BFS
if sorted_array:  
    print("Sorted array found:")  
    print(sorted_array)  
else:  
    print("No solution found.")  

#first part for search process, while the second part explores the problem space using BFS until a goal state is found or all states have been visited.