# ind 0
texto = "soy un guerrero y aun respiro"

print(texto[0])
print(texto[1])         

print(texto[0:3])       # ind 0,1,2
print(texto[3:])        # ind 3 hasta el final 
print(texto[:3])       # ind 0,1,2
print(texto[-1])       # ind -1 es el ultimo caracter
print(texto[-2])       # ind -2 es el penultimo caracter

curso = "vas a un concurso de proyectadas pero tu contrincante eres tu mismo que te proyectaste tan recio que creaste un clon tuyo que te recuerda lo lamentable y triste que es tu existecia, como no has logrado nada pese a repetirte a ti mismo que eres capaz de lograr lo que sea pero aun asi no tienes la fuerza para empezar nada, ni para cuidar los vinculos con la gente que genuinamente cree en ti pero aun asi, tu no solo no te quieres, te detestas a ti mismo, te conoces bien y sabes lo que eres y sabes que lo que muestras es lo que quires que las demas personas crean de ti, y sabes que para todo el mundo eres una farsa, una imagen irreal que creaste para no sentirte mal contigo mismo, porque en el fondo sabes que nadie te querria si te conocieran de verdad"
print(curso.replace("tu", "tuturu"))



palabras = curso.split(" ")
print(palabras)

texto2 = "soy un Guerrero y aun respiro"
print("guerrero".lower() in texto2.lower())