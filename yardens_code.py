import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def debug_print(*args):
    print(args, file=sys.stderr)


def print_instructions(x, y, thrust):
    print(str(x) + " " + str(y) + " " + str(thrust))
    

def is_new_lap(checkpoints, prev_checkpoint, checkpoint):
    if not checkpoint in checkpoints:
        checkpoints.append(checkpoint)
    return checkpoint == checkpoints[0] and checkpoint != prev_checkpoint
    
def calculate_thrust(angle, can_boost):
    if angle > 90 or angle < -90:
        thrust = 0
    elif 0 == angle and can_boost:
        thrust = "BOOST"
    else:
        thrust = 100
    return thrust
        
            
def main():
    can_boost = True
    checkpoints = []
    lap = 0
    prev_checkpoint = None
    
    # game loop
    while True:
        x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
        checkpoint = (next_checkpoint_x, next_checkpoint_y)
        
        if is_new_lap(checkpoints, prev_checkpoint, checkpoint):
            lap += 1
            debug_print("New lap #{}".format(lap))
        
        opponent_x, opponent_y = [int(i) for i in input().split()]
        
        thrust = calculate_thrust(next_checkpoint_angle, can_boost)
        if "BOOST" == thrust:
            can_boost = False
    
        # You have to output the target position
        # followed by the power (0 <= thrust <= 100)
        # i.e.: "x y thrust"
        print_instructions(next_checkpoint_x, next_checkpoint_y, thrust)
        prev_checkpoint = checkpoint
        
if __name__ == "__main__":
    main()
