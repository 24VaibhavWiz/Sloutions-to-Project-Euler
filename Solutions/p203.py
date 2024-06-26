
import eulerlib


def compute():
	# Collect unique numbers in Pascal's triangle
	numbers = set(eulerlib.binomial(n, k) for n in range(51) for k in range(n + 1))
	maximum = max(numbers)
	
	# Prepare list of squared primes
	primes = eulerlib.list_primes(eulerlib.sqrt(maximum))
	primessquared = [p * p for p in primes]
	
	def is_squarefree(n):
		for p2 in primessquared:
			if p2 > n:
				break
			if n % p2 == 0:
				return False
		return True
	
	# Sum up the squarefree numbers
	ans = sum(n for n in numbers if is_squarefree(n))
	return str(ans)


if __name__ == "__main__":
	print(compute())
