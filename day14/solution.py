from dataclasses import dataclass
import os
import re
import time


@dataclass
class Robot:
    x: int
    y: int
    v_x: int
    v_y: int


def safety_factor(robots: list[Robot], width: int, height: int) -> int:
    top_left = sum(
        1
        for robot in robots
        if robot.x < (width - 1) / 2 and robot.y < (height - 1) / 2
    )
    top_right = sum(
        1
        for robot in robots
        if robot.x > (width - 1) / 2 and robot.y < (height - 1) / 2
    )
    bottom_left = sum(
        1
        for robot in robots
        if robot.x < (width - 1) / 2 and robot.y > (height - 1) / 2
    )
    bottom_right = sum(
        1
        for robot in robots
        if robot.x > (width - 1) / 2 and robot.y > (height - 1) / 2
    )
    return top_left * top_right * bottom_left * bottom_right


def move(robots: list[Robot], width: int, height: int, seconds: int) -> list[Robot]:
    result = []
    for robot in robots:
        result.append(
            Robot(
                (robot.x + seconds * robot.v_x) % width,
                (robot.y + seconds * robot.v_y) % height,
                robot.v_x,
                robot.v_y,
            )
        )
    return result


def process_part1(content: str, width: int, height: int) -> int:
    robots = []
    for line in content.split("\n"):
        nums = map(int, re.findall("-?\d+", line))
        robots.append(Robot(*nums))
    return safety_factor(move(robots, width, height, 100), width, height)


def print_robots(robots: list[Robot], width: int, height: int) -> str:
    result = ""
    for y in range(height):
        for x in range(width):
            num_of_robots = sum(1 for robot in robots if robot.x == x and robot.y == y)
            result += str(num_of_robots) if num_of_robots else "."
        result += "\n"
    return result


def process_part2(content: str, width: int, height: int) -> None:
    robots = []
    seconds = 7858
    for line in content.split("\n"):
        nums = map(int, re.findall("-?\d+", line))
        robots.append(Robot(*nums))
    print(f"The tree is at second: {seconds}")
    print(print_robots(move(robots, width, height, seconds), width, height))


if __name__ == "__main__":
    with open("input.txt") as file:
        content = file.read().strip()

    result1 = process_part1(content, width=101, height=103)
    print(f"The safety factor is: {result1}")
    process_part2(content, width=101, height=103)
