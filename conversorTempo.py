# Time converter - receives seconds and prints time in hours, minutes and seconds

segundos = int(input("Digite o tempo em segundos: "))
horas = segundos // 3600

segundos_restantes = segundos % 3600
minutos = segundos_restantes // 60
segundos_final = segundos_restantes % 60

print(f"{horas} horas, {minutos} minutos e {segundos_final} segundos")
