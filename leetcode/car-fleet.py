class Solution(object):
    def carFleet(self, target, position, speed):
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        # go through it in rev. sorted order
        for p, s in sorted(pair)[::-1]:
            stack.append(float(target - p) / s) # add the time that this car fleet will arrive at the destination
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)