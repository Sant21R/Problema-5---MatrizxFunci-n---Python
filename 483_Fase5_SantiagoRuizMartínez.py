# Nombre del estudiante: Santiago Ruiz Martínez
# Grupo: 483
# Programa: Ingenieria de Sistemas
# Código fuente: Autoría propia

# Crear una matriz con 4 recursos y horas trabajadas por día (valores numéricos). 

horasxdia = [
    ["Docente", 6, 6, 6, 7 , 6], # 6 horas semanales cada docente. Nota: Los docentes dan una hora de más los días jueves"
    ["Secretaria", 7, 7, 7, 7, 7], # 7 horas semanales cada secretaria. 
    ["Aseadoras", 8, 8, 9, 9 ,9], # 8 horas semanales cada aseadora. Nota: Las aseadoras trabajan una hora más los días miércoles, jueves y viernes.
    ["Celador", 10, 10, 10, 10, 11] # 10 horas semanales cada celador. Nota: El celador trabaja una hora más el día viernes para asegurar la seguridad del colegio durante el fin de semana.
]

umbral = 40
# Se requiere un módulo (función) para calcular la suma total de horas semanales por recurso y clasificar su jornada. 

def cal_horas(horasxdia):
    umbral = 40
    resultados = []
    for fila in horasxdia:
        nombre_del_recurso = fila[0]
        total_semanal_horas = sum(fila[1:])
        clasificación_según_total = "SOBRETIEMPO" if total_semanal_horas > umbral else "HORARIO ESTÁNDAR"
        resultados.append((nombre_del_recurso, total_semanal_horas, clasificación_según_total))
    return resultados 

def imp_final(resultados):
    for nombre_del_recurso, total_semanal_horas, clasificación_según_total in resultados:
        print(f"- {nombre_del_recurso}: {total_semanal_horas} horas -----> {clasificación_según_total}")
        print("")

resultados = cal_horas(horasxdia)
imp_final(resultados)
