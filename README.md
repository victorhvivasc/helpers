# helpers
### compilado de herramientas para diferentes situaciones

### estare agregando scripts que implementen soluciones simples a situaciones comunes.

### Es necesario clonar la carpeta herramientas ya que para simplificar se crearon modulos particulares

### en el modulo Mecánica_fisica encontraran formulas para: 

    aceleracion_angular_media(w0, w, t0, t)
    
    aceleracion_cinematica(v0, v1, t0, t1, euclidea=False)
    
    distancia_euclidea(x, y)
    
    fuerza_newton(masa, aceleracion, euclinea=True)
            
    momento(brazo, fuerza, euclidea=True)
            
    recorrido_cinematica(v0, a, t1, x0=0, euclidea=True)
    
    velocidad_angular(velocidad, radio, rpm=False)
    
    velocidad_cinematica(x0=None, x1=None, t0=0, t1=0, v0=None, v1=None, euclidea=True)
    
    velocidad_promedio(tiempo, distancia=None, x=None, y=None)
    
    velocidad_tangencial(velocidad, radio)

### en el modulo metricas encontraran funciones para calcular:

    accuracy(comparar, original) -> float
    
    mae(comparar, original) -> float
    
    mse(comparar, original) -> float
    
    rmse(comparar, original) -> float
    
    sse(comparar, original)
