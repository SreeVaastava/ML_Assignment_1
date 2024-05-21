L1=[int(num) for num in input().split(" ")]
Lb_to_Kg=[]
for i in L1:
    Lb_to_Kg.append(round(i/2.205,2))
print("Values are:",Lb_to_Kg)