name=input("enter your name: ")
gender=input("enter your xender: ")
age=int(input("enter your age: "))
product=input("enter the product: ")
gram=int(input("enter the product weight in gram: "))

current_price=11633
print("---------------------")
total=current_price*gram
print(f"total price is: {total}")
print("---------------------")

makingcharge=gram*845
print(f"making charge (1gram) is: {makingcharge}")
print("----------------------")

total_amount=total+makingcharge
print(f"total amount: {total_amount}")
print("---------------------------")

if gender == "m":
    if age >= 65:
        if total >= 200000 and total <= 300000:
            print("discount is 20%")
            discount=total*25/100
            final=total-discount
            print(f"final price is{total}-{discount} ={final}")
        elif total > 300000 and total <= 500000:
            print("discount is 30%")
            discount=total*30/100
            final=total-discount
            print(f"final price is{total}-{discount} ={final}")
        elif total > 500000:
            print("discount is 35%")
            discount=total*35/100
            final=total-discount
            print(f"final price is{total}-{discount} ={final}")
    else:
        if total >= 200000 and total <= 300000:
            print("discount is 10%")
            discount=total*10/100
            final=total-discount
            print(f"final price is{total}-{discount} ={final}")
        elif total > 300000 and total <= 500000:
            print("discount is 20%")
            discount=total*20/100
            final=total-discount
            print(f"final price is{total}-{discount} ={final}")
        elif total > 500000:
            print("discount is 25%")
            discount=total*25/100
            final=total-discount
            print(f"final price is{total}-{discount} ={final}")


elif gender == "f" :
    if age >= 65:
        if total >= 200000 and total <= 300000:
            print("discount is 20%")
            discount=total*25/100
            final=total-discount
            print(f"final price is{total}-{discount} ={final}")
        elif total > 300000 and total <= 500000:
            print("discount is 35%")
            discount=total*35/100
            final=total-discount
            print(f"final price is{total}-{discount} ={final}")
        elif total > 500000:
            print("discount is 40%")
            discount=total*40/100
            final=total-discount
            print(f"final price is{total}-{discount} ={final}")
    else:
        if total >= 200000 and total <= 300000:
            print("discount is 15%")
            discount=total*15/100
            final=total-discount
            print(f"final price is{total}-{discount} ={final}")
        elif total > 300000 and total <= 500000:
            print("discount is 25%")
            discount=total*25/100
            final=total-discount
            print(f"final price is{total}-{discount} ={final}")
        elif total > 500000:
            print("discount is 30%")
            discount=total*30/100
            final=total-discount
            print(f"final price is{total}-{discount} ={final}")

else:
    print("\n Invalid gender! Please enter M or F only.")



       
     
    

