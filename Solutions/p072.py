 
import eulerlib, itertools


def compute():
	totients = eulerlib.list_totients(10**6)
	ans = sum(itertools.islice(totients, 2, None))
	return str(ans)


if __name__ == "__main__":
	print(compute())
