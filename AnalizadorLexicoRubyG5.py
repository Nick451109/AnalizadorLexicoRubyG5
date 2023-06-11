import ply.lex as lex

reserved = {
  #Andres
  'if':'IF',
  'else':'ElSE',
  'print':'PRINT',
  'end':'END',
  #Nick
  'break':'BREAK',
  'class':'CLASS',
  'while':'WHILE',
  'for':'FOR',
  'true':'TRUE',
  'false':'FALSE',
  'in':'INARRAY',
  #Yoser
  'elsif': 'ELSIF',
  'def':'DEF',
  'case':'CASE',
  'then':'THEN'
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
  #Yoser
  'DIVISION',
  'SUM',
  'COMA',
  'LESSTHAN',
  'POWER',
  'MULTIPLICATION',
  'MINUS'
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
#Yoser
t_DIVISION = r'\/'
t_SUM = r'\+'
t_COMA = r'\,'
t_LESSTHAN = r'\<'
t_POWER = r'\*\*'
t_MULTIPLICATION = r'\*'
t_MINUS = r'\-'


t_ignore = ' \t'

#Andres
def t_VARIABLE(t):
  r'(\$|@)?[a-zA-Z-0-9_]+'
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
algortimoNick = '''  sum = 0
  for num in numbers
    sum += num
  end
'''
algoritmoYoser = '''
def adivinarResultado(lado_1, lado2, lado3, num )
  resultado = lado1**lado2 / lado3
    if num == resutado
      print "adivino"
    elsif num < resultado
      print "numero muy pequeño"
    elsif num > resultado
      print "numero muy grande"
    end
  end

'''
lexer.input(algoritmoYoser)
# Tokenizador
while True:
  tok = lexer.token()
  if not tok:
    break
  print(tok)