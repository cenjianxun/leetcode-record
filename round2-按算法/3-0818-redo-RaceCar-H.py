'''
818. Race Car

Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions. Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):

When you get an instruction 'A', your car does the following:
position += speed
speed *= 2
When you get an instruction 'R', your car does the following:
If your speed is positive then speed = -1
otherwise speed = 1
Your position stays the same.
For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3, and your speed goes to 1 --> 2 --> 4 --> -1.

Given a target position target, return the length of the shortest sequence of instructions to get there.
'''

'''
没懂为什么要*2
'''
def racecar(self, target: int) -> int:
    pos, speed = 0, 1
    step = 0
    stack = [(pos, speed)]
    visited = {(pos, speed)}
    while stack:
        temp = []
        for pos, speed in stack:
            if pos == target:
                return step
            if  pos < target * 2 and  pos > target * -1:
                for p, s in self.helper(pos, speed, target):
                    if (p, s) not in visited :
                        visited.add((p, s))
                        temp.append((p, s))
        step = step + 1
        stack = temp
    return -1
    
def helper(self, pos, speed, target):
    res = []
    # if (target - pos) * speed < 0:
    p, s = pos, -1 if speed > 0 else 1
    res.append((p, s))
    # if (target - pos) * speed > 0:
    p, s = pos + speed, speed * 2
    res.append((p, s))
    return res