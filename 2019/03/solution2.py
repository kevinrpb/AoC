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
	points = {}

	x, y = 0, 0

	sum_n = 0

	for instruction in path:
		d = instruction[0]
		n = int(instruction[1:])

		dx = DIR[d][0]
		dy = DIR[d][1]

		for _ in range(n):
			x = x + dx
			y = y + dy

			sum_n = sum_n + 1

			points[(x, y)] = sum_n

	return points

paths = read_paths("input.txt")

pa = get_points(paths[0])
pb = get_points(paths[1])

intersections = set(pa.keys()) & set(pb.keys())

distances = [pa[i] + pb[i] for i in intersections]

min_distance = min(distances)

print("Min distance is {}".format(min_distance))
