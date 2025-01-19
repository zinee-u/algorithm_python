n = int(input())

card = [list(map(int, input().split())) for _ in range(2*n)]
# print(card[9])
# print(card_a)
# print(card_b)

for round in range(0, 2*n, 2):
	dic_a, dic_b = {1:0, 2:0, 3:0, 4:0}, {1:0, 2:0, 3:0, 4:0}
	# card_a[round] = sorted(card_a[round], reverse=True)
	# # print(card_a[round])
	# card_b[round] = sorted(card_b[round], reverse=True)
	# # print(card_b[round])

	len_a = card[round][0]
	for idx in range(1, len_a+1):
		for i in range(1, 5):
			if card[round][idx] == i:
				dic_a[i] += 1
	# print(dic_a)

	len_b = card[round+1][0]
	for idx in range(1, len_b+1):
		for i in range(1, 5):
			if card[round+1][idx] == i:
				dic_b[i] += 1
	# print(dic_b)
	
	for num in range(4, 0, -1):
		# print(dic_a[num], dic_b[num], num)
		if dic_a[num] > dic_b[num]:
			print('A')
			break
		elif dic_a[num] < dic_b[num]:
			print('B')
			break
	else:
		print('D')
	
	