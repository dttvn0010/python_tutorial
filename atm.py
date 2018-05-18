tientralai = input('Số tiền cần trả lại (nghìn đồng) :')
tientralai = int(tientralai)

soto50k = tientralai // 50
tientralai %= 50

soto20k = tientralai // 20
tientralai %= 20

soto5k = tientralai // 5

print('Số tờ tiền 50k : ', soto50k)
print('Số tờ tiền 20k : ', soto20k)
print('Số tờ tiền 5k : ', soto5k)
