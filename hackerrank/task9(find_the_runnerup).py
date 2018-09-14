n = int(raw_input())
arr = map(int, raw_input().split())
maxim = None
for i in arr:
    if maxim is None or maxim<=i:
        if i!=max(arr):
            maxim = i
print(maxim)
