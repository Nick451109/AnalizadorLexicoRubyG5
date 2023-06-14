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

  #Joseph
  'elsif': 'ELSIF',
  'def':'DEF',
  'case':'CASE',
  'then':'THEN',
  'puts':'PUTS',
  'gets':'GETS',
  'chomp':'CHOMP',
  'to_i':'TO_I',
  'to_f':'TO_F'
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
  'INTEGER',
  #Joseph
  'DIVISION',
  'PLUS',
  'COMMA',
  'LESSTHAN',
  'POWER',
  'MULTIPLICATION',
  'MINUS',
  'FLOAT',
  'DOT',
  'OPENBRACKET',
  'CLOSEDBRACKET',
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
t_INTEGER = r'\d+'
t_DOT = r'\.'
t_OPENBRACKET = r'\['
t_CLOSEDBRACKET = r'\]'
#Joseph
t_DIVISION = r'\/'
t_PLUS = r'\+'
t_COMMA = r'\,'
t_LESSTHAN = r'\<'
t_POWER = r'\*\*'
t_MULTIPLICATION = r'\*'
t_MINUS = r'\-'
t_FLOAT =r'([0-9]*\.[0-9]+)'

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
algoritmoAndres = '''def busquedaBinaria(arreglo, numero)
    inicio = 0
    fin = arreglo.length - 1
    while inicio <= fin
      mid = (inicio + fin) / 2
      if arreglo[mid] == numero
        return mid  
      elsif arreglo[mid] > numero
        fin = mid - 1  
      else
        inicio = mid + 1
      end
    end
    return nil 
end
'''
algoritmoNick = '''cantNumeros = 10
if cantNumeros <= 0
  puts "Ingrese un numero valido"
else
  fibonacci = [0,1]
  while fibonacci.length < cantNumeros
    next_number = fibonacci[-1] + fibonacci[-2]
    fibonacci << next_number
  end
  puts fibonacci.join(", ")
end
'''
algoritmoYoser = '''
def adivinarResultado(lado_1, lado2, lado3)
  resultado = lado_1**lado2 / lado3
  intentos = 3
  print "trate de adivinar el resultado \n"
  print "Usted tiene #{intentos} intentos\n"
  
  while intentos > 0
    
     print "Ingrese un numero: "
     num = gets.chomp.to_f
    
    if num == resultado
      print "adivino"
      intentos == 0
    elsif num < resultado
      print "numero es mayor"
    elsif num > resultado
      print "numero es menor"
    end
    
    intentos -= 1
    puts "Intentos restantes: #{intentos}\n\n"
  end
  puts "Se acabaron los intentos, el resultado era #{resultado}"
end
  end

'''
lexer.input(algoritmoAndres)
# Tokenizador
while True:
  tok = lexer.token()
  if not tok:
    break
  print(tok)
