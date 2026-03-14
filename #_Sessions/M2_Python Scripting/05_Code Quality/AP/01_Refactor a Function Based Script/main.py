#calculate total
def tot(p,l):return p*l

#discount
def discount_calculator(t):
    return t-(t*.1)

#main
def input_validation():
    print("Total: ",discount_calculator(tot(20,5)))
