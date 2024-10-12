var = input("Digite algo: ")
print(type("\n"+var))

print(f"É numérico? {var.isnumeric()}",  f"\nÉ Alfabético? {var.isalpha()}" )
print("É só espaço? ", var.isspace())
print(f"É alfanumérico? {var.isalnum()}")