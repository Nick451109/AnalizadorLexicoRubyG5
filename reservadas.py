def crear(palabras):
  reservadas = {}
  for i in palabras:
    reservadas.update({i.lower():i.upper()})
    reservadas.update({i.capitalize():i.upper()})
    reservadas.update({i.upper():i.upper()})
  return reservadas