class TemperatureConverter:
    def celsius_to_fahrenheit(celsius):    
        return (celsius * 9 / 5) + 32

    def fahrenheit_to_celsius(fahrenheit): 
        return (fahrenheit - 32) * 5 / 9


fahrenheit = TemperatureConverter.celsius_to_fahrenheit(25)
print(f"25°C is {fahrenheit}°F.")


celsius = TemperatureConverter.fahrenheit_to_celsius(77)
print(f"77°F is {celsius}°C.")
