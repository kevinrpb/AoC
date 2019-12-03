#! /usr/bin/env python3

def read_paths(filename: str):
	lines = open(filename).read().split("\n")[:-1]

	paths = [[item.strip() for item in line.split(",")] for line in lines]

	return paths

DIR = {
	"L": (-1, 0),
	"R": (1, 0),
	"U": (0, 1),
	"D": (0, -1)
}

def get_points(path: list):
	points = []

	x, y = 0, 0

	for instruction in path:
		d = instruction[0]
		n = int(instruction[1:])

		dx = DIR[d][0]
		dy = DIR[d][1]

		for _ in range(n):
			x = x + dx
			y = y + dy

			points.append((x, y))

	return points

def manhattan(point: tuple):
	return sum([abs(c) for c in point])

paths = read_paths("input.txt")

points = [set(get_points(path)) for path in paths]

intersections = points[0].intersection(*points[1:])

distances = [manhattan(point) for point in intersections]

min_distance = min(distances)

print("Min distance is {}".format(min_distance))
