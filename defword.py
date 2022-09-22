def word (st):
    elements = [ "." , "," , "/" , "\\" , "[" , "]" , "{" , "}" , "!" , "#" ,
                "&" , "(" , ")" , "*" , "^" , "<" , ":" , ";" , "\'" , "\"" ,
                ">" , "|" , "$" , "%" ,"~" , "`" , "@" , "?"]

    for i in elements:
        st = st.replace(i, " ")
    words = st.split()

    return(len(words))

st = input('Enter your text: ')

print('Number of words:' ,word(st) )