s=input().split(" ")
d={'0':'zero' 
, '1':'one'
, '2':'two'
, '3':'three'
, '4':'four'
, '5':'five'
, '6':'six'
, '7':'seven'
, '8':'eight'
, '9':'nine'
,'10':'ten'
}
for i in s:
    if i.isdigit():
        print(d.get(i),end=" ")
    else:
        print(i,end=" ")