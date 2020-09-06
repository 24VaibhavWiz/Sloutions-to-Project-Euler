

def compute():
	TILES = 10**6
	ans = 0
	for n in range(3, TILES // 4 + 2):  # Outer square length
		for k in range(n - 2, 0, -2):  # Inner square length
			if n * n - k * k > TILES:
				break
			ans += 1
	return str(ans)


if __name__ == "__main__":
	print(compute())
