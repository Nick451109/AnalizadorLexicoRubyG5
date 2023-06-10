import ply.lex as lex

reserved = {
    'if': 'IF',
    'else':'Else',
    'print': 'PRINT',
    'end': 'END'
}


tokens = (
    'GREATERTHAN',
    'EQUALS',
    'STRING',
    'AND',
    'GREATEROREQUALS', 
) + tuple(reserved.values())

t_GREATERTHAN = r'>'
t_EQUALS = r'=='
t_GREATEROREQUALS = r'>='
t_STRING = r'"[^".]*"'
t_AND = r'&&'



def t_newLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
def t_COMMENTS(t):
  r'\#.*'

def t_error(t):
  print("Componente léxico no reconocido '%s'" % t.value[0])
  t.lexer.skip(1)

algoritmo = '''
    edad = 18
    licencia = true

    if(edad>=18 && licencia)
        print "Puede manejar"
    else
        print "No puede manejar"
    end
'''
lexer = lex.lex()

lexer.input(algoritmo)
# Tokenizador
while True:
  tok = lexer.token()
  if not tok:
    break  #Rompe
  print(tok)