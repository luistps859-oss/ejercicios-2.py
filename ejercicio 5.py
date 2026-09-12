contraseña = input("Ingrese su contraseña: ")

tiene_mayuscula = False
tiene_minuscula = False
tiene_numero = False
tiene_especial = False

caracteres_especiales = "!@#$%^&*()"

for caracter in contraseña:
    if caracter.isupper():
        tiene_mayuscula = True
    elif caracter.islower():
        tiene_minuscula = True
    elif caracter.isdigit():
        tiene_numero = True
    elif caracter in caracteres_especiales:
        tiene_especial = True

if len(contraseña) >= 8 and tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial:
    print("¡Contraseña válida!")
else:
    print("Contraseña inválida. Debe tener al menos 8 caracteres, una mayúscula, una minúscula, un número y un carácter especial.")