class RingBuffer:
    def __init__(self, capacity):
        self.overwriteIndex = 0
        self.capacity = capacity
        self.elements = []


    def append(self, item):
        # Check if the length of self.elements is less than the cap, if so, just append the item to elements
        if len(self.elements) < self.capacity:
            self.elements.append(item)
            
        # If the elements list is full, we have to select the indice we want to overwrite based on the overwriteIndex and then increase the Index 
        # counter by 1.
        else:
            self.elements[self.overwriteIndex] = item
            self.overwriteIndex += 1
        

        # We have to check if the index we are overwriting is out of bounds, if it is, reset the index back to 0. 
        if self.overwriteIndex == self.capacity :
            self.overwriteIndex = 0



    # Just return the list of elements
    def get(self):
        return self.elements