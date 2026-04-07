def prepareTea(water, leaves, milk, sugar):
    return f"{water} + {leaves} + {milk} + {sugar} → brewed and served "

def makeTea(tea_type):
    if tea_type == "normal":
        return prepareTea("hot water", "black tea", "milk", "sugar")
    elif tea_type == "special":
        return prepareTea("hot water", "masala tea", "almond milk", "jaggery")
    else:
        return "Please choose 'normal' or 'special' tea."

# Usage
print(makeTea("normal"))
print(makeTea("special"))

# hot water + black tea + milk + sugar → brewed and served 
# hot water + masala tea + almond milk + jaggery → brewed and served 