
data = []
count = 0

with open('reviews.txt', 'r')as f:
	for line in f:
		data.append(line)
		count += 1000
		if count % 1000 == 0: # %除完餘數等於0
			print(len(data))
print('檔案讀取完了，總共有', len(data),'筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)

print('留言平均是', sum_len/len(data))