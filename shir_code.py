import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class Location:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @property
    def coordinate(self):
        return self.x, self.y


def get_distance(source_location: Location, dest_location: Location):
    point1 = source_location.coordinate
    point2 = dest_location.coordinate
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(point1, point2)]))


class Checkpoint(Location):
    def __init__(self, x, y, distance, angle):
        super(Checkpoint, self).__init__(x, y)
        self.distance = distance
        self.angle = angle


class SensorData:
    def __init__(self, my_location: Location,
                 next_checkpoint: Checkpoint,
                 opponent_location: Location):
        """Data received from sensors."""
        self.my_location = my_location
        self.next_checkpoint = next_checkpoint
        self.opponent_location = opponent_location

    def get_angle(self):
        return abs(self.next_checkpoint.angle)

    def get_distance(self):
        return self.next_checkpoint.distance


def read_sensors() -> SensorData:
    """Reads the sensors data."""
    x, y, next_checkpoint_x, next_checkpoint_y, dist, angle = [int(i) for i in
                                                               input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
    my_location = Location(x, y)
    next_checkpoint = Checkpoint(next_checkpoint_x, next_checkpoint_y, dist,
                                 angle)
    opponent_location = Location(opponent_x, opponent_y)
    return SensorData(my_location=my_location,
                      next_checkpoint=next_checkpoint,
                      opponent_location=opponent_location)


def get_thrust(sensor_data: SensorData) -> int:
    thrust = 100
    if sensor_data.get_angle() < 1 and sensor_data.get_distance() < 600:
        thrust = 10
    elif sensor_data.get_angle() > 90:
        thrust = 0
    return thrust


def get_next_aim(sensor_data):
    return sensor_data.next_checkpoint.coordinate


def main():
    while True:
        sensor_data = read_sensors()
        thrust = get_thrust(sensor_data)
        next_x, next_y = get_next_aim(sensor_data)
        print(f"{next_x} {next_y} {thrust}")


if __name__ == '__main__':
    main()