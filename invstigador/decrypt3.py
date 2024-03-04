three_two = 3 % 2;
eleven_four = 11 % 4;
five_ten = 5 % 10;

print(three_two);
print(eleven_four);
print(five_ten);

# Defina uma função para encontrar a verdade deslocando a letra pelo valor especificado
def lasso_letter( letter, shift_amount ):
    # Invoque a função ord para traduzir a letra em seu código ASCII 
    # Salve o código na variável letter_code
    letter_code = ord(letter.lower())
    
    # A representação do número ASCII da letra minúscula 'a'
    a_ascii = ord('a')

    # O número de letras do alfabeto
    alphabet_size = 26

    # A fórmula para calcular o número ASCII para a letra decodificada
    # Leve em consideração o loop do alfabeto
    true_letter_code = a_ascii + (((letter_code - a_ascii) + shift_amount) % alphabet_size)

    # Converta o número ASCII em caractere ou letra
    decoded_letter = chr(true_letter_code)

    # Envie a carta decodificada de volta
    return decoded_letter

print(lasso_letter('a', 2))


