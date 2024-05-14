# https://codechick.io/challenges/44

def frames(minutes, fps):
    seconds = 60
    fps_per_min = fps * seconds
    total_fps = fps_per_min * minutes

    return total_fps

print(frames(1, 1))
print(frames(10, 1))
print(frames(10, 25))
