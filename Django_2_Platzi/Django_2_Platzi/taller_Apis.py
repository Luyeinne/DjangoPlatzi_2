from urllib.request import urlopen

url = "http://baconmockup.com/1000/1000/"
resultado = urlopen(url)
lectura = resultado.read()
f = open("holder.jpg", "wb")
f.write(lectura)
f.close()
