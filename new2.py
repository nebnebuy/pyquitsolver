import random

def estimate_pi(n):
    inside_circle = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x*x + y*y <= 1:
            inside_circle += 1
            
    pi_estimate = 4*inside_circle/n
    return pi_estimate

# 使用10^6个点来估计圆周率
pi = estimate_pi(10**6)
print(f"圆周率的估计值为: {pi:.2f}")
