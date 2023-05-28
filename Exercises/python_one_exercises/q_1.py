def table() :
    text = (input(str('Enter your text : ')).replace(' ',''))
    result = []
    text = list(text)
    for x in text :result.append(f'|   {x}   |     '+str(text.count(x)).center(5)+'     |')
    result = set(result)
    final_text = "+-------+"+"---------------+\n|  NAME |"+"   FREQUENCY   |\n+-------+"+"---------------+\n"
    for x in result :final_text += str(x)+'\n'
    final_text += '+-------+'+'---------------+'
    print(final_text)
table()