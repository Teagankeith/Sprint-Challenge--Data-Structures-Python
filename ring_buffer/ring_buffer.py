class RingBuffer:
    def __init__(self, capacity):
        self.overwrite = 0
        self.capacity = capacity
        self.elements = []

    def append(self, item):
        # As long as the list of elements is less than the capacity (how many elements we can hold) go ahead and append the item to the list
        if len(self.elements) < self.capacity:
            self.elements.append(item)
        
        # If we have met our capacity, we need to start overwriting items, so whatever idex our overwrite is at we overwrite that
        # indici in elements, and then increase the overwrite so we continue to interate through the whole list
        else:
            self.elements[self.overwrite] = item
            self.overwrite += 1
        # If our overwrite goes out of bounds - larger than our capacity - we need to reset the overwrite back to 0
        if self.overwrite >= self.capacity:
            self.overwrite = 0

    def get(self):
        return self.elements