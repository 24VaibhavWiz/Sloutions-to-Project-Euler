
def compute():
	ans = max(sum(int(c) for c in str(a**b))
		for a in range(100) for b in range(100))
	return str(ans)


if __name__ == "__main__":
	print(compute())
