import random

print( "Character Scrambler - For your convenience, please enter a space after every character, although it is not required." )

print()

print( "Copy here and paste in the line below for special characters and numbers (excluding ~ and `: & [ $ { } ( = * ) + ] ! # @ ^ \  | - _ / ? \' \" ; : % < > 7 5 3 1 9 0 2 4 6 8")

print()

print( "Copy here and paste in the line below for the alphabet: a b c d e f g h i j k l m n o p q r s t u v w x y z" )

print()

print( "Copy here and paste in the line below for combined alphabet and special characters (excluding ~ and `): a b c d e f g h i j k l m n o p q r s t u v w x y z & [ $ { } ( = * ) + ] ! # @ ^ \  | - _ / ? \' \" ; : % < > 7 5 3 1 9 0 2 4 6 8" )

print()

print( "Full list of all special characters, capitalized letters, and lowercase letters, excluding ~ and `")

print( "& [ $ { } ( = * ) + ] ! # @ ^ \  | - _ / ? \' \" ; : % < > 7 5 3 1 9 0 2 4 6 8 a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")

print()

characters = input( "Enter characters: " )

print()

number_of_words = input( "Enter number of words: " )

print()

max_word_length = input( "Enter maximum word length: " )

print()

characters = characters.strip()

characters = characters.replace( " ", "" )

number_of_words = number_of_words.strip()

number_of_words = int( number_of_words )

max_word_length = max_word_length.strip()

max_word_length = int( max_word_length )

max_word_length = max_word_length + 1

word_string = ""

for j in range(0, number_of_words ) :

    j = random.randrange( 1, max_word_length)

    temp_word_string = ""

    for char in range( 0, j ) :

        rawr = random.choice( characters )

        temp_word_string = temp_word_string + rawr

    word_string = word_string + temp_word_string + " "

print( "Here is your final word list:")

print( word_string )
