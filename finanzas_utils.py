#1º Defino la funcion para calculo de retorno diario a partri de dos datos, precio actual y precio anterior.
def calcular_retorno_diario(precio_actual, precio_anterior):
    
    if precio_anterior == 0:
        return 0.0
    
    retorno = ((precio_actual - precio_anterior) / precio_anterior) * 100
    return retorno

#2º Defino la funcion para categorizar la volatilidad a partir de la desviacion estandar
def categorizar_volatilidad(desviacion_estandar):
   
    if desviacion_estandar < 2:
        return "Baja"
    elif 2 <= desviacion_estandar <= 5:
        return "Media"
    else:
        return "Alta"