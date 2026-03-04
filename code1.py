# import sys

# def main():
#     data = list(map(int, sys.stdin.buffer.read().split()))
#     # Có thể nhập dạng: a0 b0 c0 a1 b1 c1 (có/không kèm chữ)
#     a0, b0, c0, a1, b1, c1 = data[:6]

#     start = a0 * 3600 + b0 * 60 + c0
#     end = a1 * 3600 + b1 * 60 + c1

#     if end < start:
#         end += 24 * 3600  # qua ngày

#     print(end - start)

# if __name__ == "__main__":
#     main()



# import sys

# def main():
#     data = list(map(int, sys.stdin.buffer.read().split()))
#     n = data[0]
#     s = sum(data[1:])  # tổng n-1 số đã nhập
#     total = n * (n + 1) // 2
#     print(total - s)

# if __name__ == "__main__":
#     main()

# n = int(input())   # nhập số thí sinh

# scores = []
# for _ in range(n):
#     scores.append(int(input()))  # nhập từng điểm

# scores.sort(reverse=True)  # sắp xếp giảm dần
# silver = scores[1]         # điểm cao thứ 2

# print("Silver = ", silver)

# t = int(input())

# for _ in range(t):
#     N = int(input())
#     result = []

#     for num in range(22, N):
#         s = str(num)

#         if len(s) % 2 != 0:
#             continue
#         if s != s[::-1]:
#             continue

#         if all(ch in "02468" for ch in s):
#             result.append(s)
        
#     print(" ".join(result))

# import math

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# t = int(input())

# for _ in range(t):
#     a, b = map(int, input().split())
    
#     gcd_value = math.gcd(a, b)          # Ước chung lớn nhất
#     digit_sum = sum(int(d) for d in str(gcd_value))  # Tổng chữ số
    
#     if is_prime(digit_sum):
#         print("YES")
#     else:
#         print("NO")

a, K, N = map(int, input().split())

result = []

max_b = N - a

for b in range(1, max_b + 1):
    if (a + b) % K == 0:
        result.append(str(b))

if result:
    print(" ".join(result))
else:
    print(-1)

