measure = float(input('Enter a value: '))
km = measure/1000
hm = measure/100
dam = measure/10
m = measure/1
dm = measure*10
cm = measure*100
mm = measure*1000

print('MEASUREMENT CONVERSION TABLE')
print('Kilometers(km) = {}\nHectometers(hm) = {}\nDecameters(dam) = {}\nMeters(m) = {}\nDecimeter(dm) = {}\nCentimeter(cm) = {}\nMilimeter(mm) = {}'.format(km, hm, dam, m, dm, cm, mm))