#Duración promedio de los cursos
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
este_curso = 1.5

#Duración inicial de los videos antes de la edición
crudo_este_curso = 3.5
crudo_otros_cursos_promedio = 5

#Calculo de que porcentaje dura el video de dalto respecto de los otros videos
diferencia_min = este_curso / otros_cursos_min * 100
diferencia_max = round((este_curso / otros_cursos_max * 100), 2) #Esto es para recortar un poco los decimales
diferencia_promedio = este_curso / otros_cursos_promedio * 100

#Calculo de que porcentaje de video se elimina
porcentaje_eliminado_este_curso = round((100 - este_curso / crudo_este_curso * 100), 2)
porcentaje_eliminado_otros_cursos_promedio = 100 - otros_cursos_promedio / crudo_otros_cursos_promedio * 100

#Cuanto equivalen 10 horas de este curso en los otros cursos
equivalencia_promedio = round((10 / este_curso * otros_cursos_promedio), 2)

print(f"El curso de dalto dura un {diferencia_min}% del curso más rápido, un {diferencia_max}% del más lento y un {diferencia_promedio}% de los de velocidad media.")
print(f"Este curso elimina el {porcentaje_eliminado_este_curso}% de los videos y el promedio de los demas cursos elimina el {porcentaje_eliminado_otros_cursos_promedio}%")
print(f"Ver 10 hs de este curso equivale a ver {equivalencia_promedio}hs de los cursos de duración promedio")