
n = 100
assert n > 0, f"number greater than 0 expected, got: {n} "

def test_some_primes():
    assert 3 in {num for num in range(2, 50) if not any(num % div==0 for div in range(2, num))}
    
test_some_primes()