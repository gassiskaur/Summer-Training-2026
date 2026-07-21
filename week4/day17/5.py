#LAMBDAS

taxes = lambda amount : amount*0.2 + amount*16 + 1 

print (taxes(amount=100))

#Lambdas in lambda 


discounted_price = lambda discount : (lambda price :  price - price*discount/100)

monthly_subscription = discounted_price(discount=10)
yearly_subscription = discounted_price(discount=30)
halfyearly_subscription = discounted_price(discount=20)

print(monthly_subscription(1000))
print(yearly_subscription(1000))
print(halfyearly_subscription(1000))