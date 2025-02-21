def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
        return ''.join(f"({str(x)}**{factors.count(x)})" if factors.count(x) > 1 else f"({str(x)})" for x in sorted(set(factors)))