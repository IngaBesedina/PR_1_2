def FibRecursive(n):
	if n <= 1:
		return n
	else:
		return FibRecursive(n-1)+FibRecursive(n-2)

print(FibRecursive(8))

# комментарий
