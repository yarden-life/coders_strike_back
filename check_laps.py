checkpoints = []
lap = 0
current_checkpoint = None


def debug_print(*args):
    print(args, file=sys.stderr)


def check_lap(checkpoint):
    global checkpoints
    global lap
    global current_checkpoint
    if not checkpoint in checkpoints:
        checkpoints.append(checkpoint)
    if checkpoint == checkpoints[0] and not checkpoint == current_checkpoint:
        lap += 1
        debug_print("New lap, #{}".format(lap))
    current_checkpoint = checkpoint
