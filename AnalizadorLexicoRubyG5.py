import ply.lex as lex

reserved = {
  #Andres
  'if':'IF',
  'else':'ElSE',
  'print':'PRINT',
  'end':'END',
  #Nick
  'def':'DEF',
  'break':'BREAK',
  'class':'CLASS',
  'while':'WHILE',
  'for':'FOR',
  'true':'TRUE',
  'false':'FALSE'
}


tokens = (
  #Andres
  'GREATERTHAN',
  'EQUALS',
  'STRING',
  'AND',
  'GREATEROREQUALS',
  'VARIABLE',
  #Nick
  'ASSIGNMENT',
  'ASSIGNINCREMENT',
  'ASSIGNDECREMENT',
  'LPAREN',
  'RPAREN',
  'NUMBER',
) + tuple(reserved.values())

#Andres
t_GREATERTHAN = r'>'
t_EQUALS = r'=='
t_GREATEROREQUALS = r'>='
t_STRING =r'"[^".]*"'
t_AND = r'&&'

#Nick
t_ASSIGNMENT = r'='
t_ASSIGNINCREMENT = r'\+='
t_ASSIGNDECREMENT = r'-='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NUMBER = r'\d+(\.\d)?'

t_ignore = ' \t'

#Andres
def t_VARIABLE(t):
  r'(\$|@)?[a-zA-Z]+'
  t.type = reserved.get(t.value, 'VARIABLE')
  return t

def t_newLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
def t_COMMENTS(t):
  r'\#.*'

def t_error(t):
  print("Componente léxico no reconocido '%s'" % t.value[0])
  t.lexer.skip(1)


lexer = lex.lex()
#Andres
algoritmoAndres = '''edad = 18
licencia = true

if(edad>=18 && licencia == true)
    print "Puede manejar"
else
    print "No puede manejar"
end
'''


lexer.input(algoritmoAndres)
# Tokenizador
while True:
  tok = lexer.token()
  if not tok:
    break
  print(tok)