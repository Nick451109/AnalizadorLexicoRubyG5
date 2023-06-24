from lexico import tokens
import ply.yacc as yacc

def p_varibles(p):
  'variable : ID ASSIGNMENT varibles'

def p_variablesP(p):
  '''
  varibles : FLOAT 
           | INTEGER
           | ID
  '''

def p_error(p):
  if p:
    print("Error de sintaxis en token:", p.type)
    #sintactico.errok()
  else:
    print("Syntax error at EOF")


sintactico = yacc.yacc()

while True:
  try:
    s = input('ruby > ')
  except EOFError:
    break
  if not s: continue
  result = sintactico.parse(s)
  if result != None: print(result)
