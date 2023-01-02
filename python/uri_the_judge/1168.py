n = int(input())

nums = {
	'1':2,
	'2':5,
	'3':5,
	'4':4,
	'5':5,
	'6':6,
	'7':3,
	'8':7,
	'9':6,
	'0':6
}
qtd_led = []
for i in range(n):
	number = input()
	qtd = 0
	for k in number:
		qtd += nums[k]
	qtd_led.append(qtd)
for k in qtd_led:
	print(str(k) + " leds")
