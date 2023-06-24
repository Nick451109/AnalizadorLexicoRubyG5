from lexico import tokens
import ply.yacc as yacc

#Intructions

def p_instuction(p):
  'instruction : ID ASSIGNMENT dataType'

def p_instructionFunction(p):
  '''
  instruction : DEF ID LPAREN parameters RPAREN END
                  | DEF ID LPAREN RPAREN END
  '''

#Parameters
def p_parameters(p):
  '''
    parameters : ID 
               | ID COMMA ID 
  '''

#StructureData

def p_instructionConditional(p):
  '''  
    instructionConditional : IF LPAREN condition RPAREN
  '''

#DataTypes

def p_condition(p):
  '''
    condition : TRUE
               | FALSE 
  '''

def p_dataType(p):
  '''
  dataType : FLOAT
           | INTEGER
           | TRUE
           | FALSE
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
