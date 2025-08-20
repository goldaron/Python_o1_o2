#Ohjelma joka kertoo Fahrenheit-asteista onko kuuma vai kylmä

fahrenheit_str = input("Anna lämpötila Fahrenheit-asteina: ")
fahrenheit = float(fahrenheit_str)
celsius = (fahrenheit - 32)*5/9
if celsius < 22
    print(f"Lämpötila Celsius-asteina {celsius}, on aika kylmä")
    else print(f"Lämpötila Celsius-asteina: {celsius}, on aika lämmin.")