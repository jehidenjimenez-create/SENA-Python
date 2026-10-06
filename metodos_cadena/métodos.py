#Un método es una función que llamas sobre un valor. 
# Para llamar a un método de cadena, escribe la cadena o el nombre de su variable
# seguido de un punto y la llamada al método

print("=" * 50)
#upper(): Devuelve una nueva cadena con todos los caracteres convertidos a mayúsculas.

my_str = 'hello world'

uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD

#lower(): Devuelve una nueva cadena con todos los caracteres convertidos a minúsculas

my_str = 'Hello World'

lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world

#strip(): Devuelve una nueva cadena con los caracteres especificados de inicio y final eliminados.
# Si no se pasa ningún argumento, elimina los espacios en blanco de inicio y final.

my_str = '  hello world  '

trimmed_my_str = my_str.strip()
print(trimmed_my_str)  # "hello world"
