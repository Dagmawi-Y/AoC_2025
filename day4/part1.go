package main

import (
	"os"
	"strings"
)

func Part1() int {
	data, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}

	lines := strings.Split(strings.TrimSpace(string(data)), "\n")
	h := len(lines)
	w := len(lines[0])

	// convert to [][]byte for fast access
	grid := make([][]byte, h)
	for i := 0; i < h; i++ {
		grid[i] = []byte(lines[i])
	}

	dirs := [][2]int{
		{-1, -1}, {-1, 0}, {-1, 1},
		{0, -1}, {0, 1},
		{1, -1}, {1, 0}, {1, 1},
	}

	count := 0

	for r := 0; r < h; r++ {
		for c := 0; c < w; c++ {
			if grid[r][c] != '@' {
				continue
			}

			neighbors := 0
			for _, d := range dirs {
				nr, nc := r+d[0], c+d[1]
				if nr < 0 || nr >= h || nc < 0 || nc >= w {
					continue
				}
				if grid[nr][nc] == '@' {
					neighbors++
				}
			}

			if neighbors < 4 {
				count++
			}
		}
	}

	return count
}
