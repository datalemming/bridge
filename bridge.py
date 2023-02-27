import random

def shuffle(nums):
    for i in range(6):
        random.shuffle(nums)
    return nums

def deal_hands(nums):
    north=nums[0:13]
    north.sort()
    east=nums[13:26]
    east.sort()
    south=nums[26:39]
    south.sort()
    west=nums[39:52]
    west.sort()
    return(north, east, south, west)






cards=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
suits=['S','H','D','C']
pack=[]
for suit in suits:
    for card in cards:
        pack.append(card+suit)
#print(pack)

card_dict={}
card_num=1
for card in pack:
    card_dict[card_num]=card
    card_num=card_num+1
#print(card_dict)

nums=[]
for n in range(1,53):
    nums.append(n)
#print(nums)

for n in range(11):
    shuffle(nums)
    deal_instance=deal_hands(nums)

    #interpret hands
    north_actual=[]
    east_actual=[]
    south_actual=[]
    west_actual=[]

    for c in deal_instance[0]:
        north_actual.append(card_dict[c])
    for c in deal_instance[2]:
        south_actual.append(card_dict[c])
    for c in deal_instance[1]:
        east_actual.append(card_dict[c])
    for c in deal_instance[3]:
        west_actual.append(card_dict[c])

    print('###  HAND  ###')
    print("north: ",north_actual)
    print("east: ",east_actual)
    print("south: ", south_actual)
    print("west: ",west_actual)
    print('===============')
