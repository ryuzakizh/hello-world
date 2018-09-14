n = int(raw_input())
integer_list = map(int, raw_input().split())
my = tuple(integer_list)
print(hash(my))
