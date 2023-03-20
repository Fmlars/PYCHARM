def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(33))





jonna = ["Magnus","Fredrik"]

jonna.append("Lars")
print(jonna)
print(len(jonna))
jonna.remove(jonna[1])
print(jonna)
print(len(jonna))