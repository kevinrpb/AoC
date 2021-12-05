> [Back Home](/)   &#124;   [Back to 2021](/2021/)

# AoC 2021 - December 1 - Sonar Sweep

> Solutions: [Problem I](#solution)   &#124;   [Problem II](#solution-1)

## Problem I

As the submarine drops below the surface of the ocean, it automatically performs a sonar sweep of the nearby sea floor. On a small screen, the sonar sweep report (your puzzle input) appears: each line is a measurement of the sea floor depth as the sweep looks further and further away from the submarine.

For example, suppose you had the following report:

	199
	200
	208
	210
	200
	207
	240
	269
	260
	263

This report indicates that, scanning outward from the submarine, the sonar sweep found depths of 199, 200, 208, 210, and so on.

The first order of business is to figure out how quickly the depth increases, just so you know what you're dealing with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

To do this, count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:

	199 (N/A - no previous measurement)
	200 (increased)
	208 (increased)
	210 (increased)
	200 (decreased)
	207 (increased)
	240 (increased)
	269 (increased)
	260 (decreased)
	263 (increased)

In this example, there are 7 measurements that are larger than the previous measurement.

**How many measurements are larger than the previous measurement?**

### Solution

> [Source code here](https://github.com/kevinrpb/AoC/blob/main/solutions/y2021/d01/p1.py)

First of all, we'll need a function to read our lines into a list of numbers. This can be done simply in a few lines of code:

```python
lines = []

with open(filepath, 'r') as file: # Open the file to read from it
	# `readline` reads one line (better do it like this for large files)
	# `strip` removes leading/trailing whitespace
	while (line := file.readline().strip()):
		lines.append(int(line)) # We want integer numbers
```

Once we do this, checking which of those lines are greater than the previous one is as easy as iterating over them, comparing, and counting.

<span id="code-snippet-count" />

```python
count = 0

for i in range(1, len(lines)): # Iterate the lines
	if lines[i] > lines[i - 1]: # Compare each line with the previous
		count += 1 # Add one to the count
```

Note that it's important that we start at `1` and not `0`, since the first element doesn't have a previous one!

With the code ready, we can run it and print our results

	There are 2000 measurements
	  -> 1692 are deeper than the previous one

## Problem II

Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.

Instead, consider sums of a three-measurement sliding window. Again considering the above example:

	199  A
	200  A B
	208  A B C
	210    B C D
	200  E   C D
	207  E F   D
	240  E F G
	269    F G H
	260      G H
	263        H

Start by comparing the first and second three-measurement windows. The measurements in the first window are marked A (199, 200, 208); their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618. The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.

In the above example, the sum of each three-measurement window is as follows:

	A: 607 (N/A - no previous sum)
	B: 618 (increased)
	C: 618 (no change)
	D: 617 (decreased)
	E: 647 (increased)
	F: 716 (increased)
	G: 769 (increased)
	H: 792 (increased)

In this example, there are 5 sums that are larger than the previous sum.

Consider sums of a three-measurement sliding window. **How many sums are larger than the previous sum?**

### Solution

> [Source code here](https://github.com/kevinrpb/AoC/blob/main/solutions/y2021/d01/p2.py)

The tricky part here is creating the sliding windows. To do that, however, we just need to iterate the list of lines. That simple!

```python
windows = []

for i in range(2, len(lines)):
	window = lines[i] + lines[i+1] + lines[i+2]
	windows.append(windows)
```

Now, instead of checking the previous item in the list, we want two (2) previous ones. That's why we start the range at `2`. Then we can sum the three elements in the window and add that to our list of windows. Since the sliding window is of size `3`, we will end up with two fewer windows than initial lines.

Once we have the windows, since we end up with a list of numbers, we can use [the same logic as earlier](#code-snippet-count) to check how many of them are deeper than the previous.

	There are 2000 measurements
	  -> 1692 are deeper than the previous one
	There are 1998 measurement windows
	  -> 1724 are deeper than the previous one
