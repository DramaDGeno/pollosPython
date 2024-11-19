import random #elegir el día de la desviación
import time #añade una pausa entre cada dia de la simulación
import json #coloca la salida en formato JSON

initialWeight = 42
idealWeight = 3500
totalDays = 39
increases = [0, 37.6, 50, 71.42, 85.71, 157.14, 170.5]

while True: #Bucle sin fin
    idealWeight = initialWeight #Reinicia la variable
    actualWeight = initialWeight #Reinicia la variable
    deviationDay = random.randint(8, totalDays)  #día de desviación al azar entre 8 y 39
    print(f"\nDía de desviación seleccionado: {deviationDay}\n")

    #Generar los datos
    for day in range(1, totalDays + 1):
        if day < len(increases): #incrementos
            increase_day = increases[day - 1]
        else:
            increase_day = increases [-1]

        idealWeight += increase_day
        actualWeight += increase_day  if day < deviationDay else increase_day * 0.9 #0.9 para el 90%

        #JSON

        dataDay = {
            "Peso Ideal: ": round(idealWeight, 2),
            "Peso Actual: ": round(actualWeight, 2)
        }

        #conversion a JSON

        data_json = json.dumps(dataDay, ensure_ascii=False)

        # impresion
        if day >= deviationDay:
            print(f"\033[91mDía {day} -> {data_json}\033[0m")
        else:
            print(f"Día {day} -> {data_json}")

        time.sleep(1)

