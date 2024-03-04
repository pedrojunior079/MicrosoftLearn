print("Ola, Contosville!");

# Associe a variável cidade ao valor "Contosville"
town = "Contosville";

# Imprima uma mensagem sobre o local secreto
print("A cidade que procuro é " + town);

# Definir uma função para citar uma frase
def chant(phrase):
    # Cole trés cópias juntas e imprima como uma mensagem
  print(phrase + phrase + phrase);

# Use a função de citação na frase "Contosville"
chant("Contosville!");  

def lasso_letter( letter, shift_amount ):
    letter_code = ord(letter.lower())
    decoded_letter_code = letter_code + shift_amount
    decoded_letter = chr(decoded_letter_code)
    return decoded_letter

print(lasso_letter('N', 13))


