num_casos = int(input())
words = []
def count(word):
	chars = dict.fromkeys(set(word),0)
	for char in word:
		if chars.get(char) is not None:
			chars[char]+=1
	highest = max(chars.values())
	v = [k for k, v in chars.items() if v == highest]
	return sorted(v)
for k in range(num_casos):
	word = input()
	words.append(''.join(count(word.lower().strip().replace(" ",""))))
for k in words:
	print(k)