

tablec = ['make','create','draft','generate','build','construct','form','produce','develop','design','forge','invent',
          'establish','set up','assemble']
tabled = ['delete','remove','erase','clear','discard','eliminate','cancel','cut','omit','exclude','expunge','purge',
          'rub out']





def commando(query):
    for word in tablec:
        if word in query:
            return 'Creating a new file'
    for word in tabled:
        if word in query:
            return 'Deleting the file'
    return 'Sorry, I am not able to understand what you are saying.'