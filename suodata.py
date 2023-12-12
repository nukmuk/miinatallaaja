def filter_errors(listi, arvo):
    listi2 = []
    for i in listi:
        if i < arvo:
            listi2.append(i)
            pass
    listi.clear()
    listi.extend(listi2)


measurements = [12.2, 54.2, 42345.2, 23534.1, 55.7, 8982.4]
filter_errors(measurements, 8000)
print(measurements)
