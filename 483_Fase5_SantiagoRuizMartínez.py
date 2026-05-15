# Nombre del estudiante: Santiago Ruiz Martínez
# Grupo: 483
# Programa: Ingenieria de Sistemas
# Código fuente: Autoría propia

horasxdia = [
    ["Docente", 6, 6, 6, 7 , 6], 
    ["Secretaria", 7, 7, 7, 7, 7], 
    ["Aseadoras", 8, 8, 9, 9 ,9], 
    ["Celador", 10, 10, 10, 10, 11] 
]

umbral = 40

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
