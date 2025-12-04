package main

import (
	"os"
	"strings"
)

type Point struct {
	R, C int
}

func Part2() int {
	data, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}

	lines := strings.Split(strings.TrimSpace(string(data)), "\n")
	h := len(lines)

	// convert to [][]byte for easy mutability
	grid := make([][]byte, h)
	for i := 0; i < h; i++ {
		grid[i] = []byte(lines[i])
	}

	totalRemoved := 0

	for {
		acc := accessible(grid)
		if len(acc) == 0 {
			break
		}

		for _, p := range acc {
			grid[p.R][p.C] = '.' // remove the roll
		}

		totalRemoved += len(acc)
	}

	return totalRemoved
}

// helper to find accessible rolls
func accessible(grid [][]byte) []Point {
	dirs := [][2]int{
		{-1, -1}, {-1, 0}, {-1, 1},
		{0, -1}, {0, 1},
		{1, -1}, {1, 0}, {1, 1},
	}

	h := len(grid)
	w := len(grid[0])
	var acc []Point

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
				acc = append(acc, Point{r, c})
			}
		}
	}

	return acc
}
