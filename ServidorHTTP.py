import socket
HOST = "127.0.0.1"  
PORT = 8080

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR,1)
servidor.bind((HOST, PORT))
servidor.listen(5)

while True:
    conn,add=servidor.accept()
    request=conn.recv(1024).decode("utf-8")
    print(request)
    
    lista=request.split(' ')
    metodo=lista[0]
    resquest_cliente=lista[1]
    print(resquest_cliente)

    file=resquest_cliente.split('?')[0]
    file=file.lstrip("/")
    
    if(file==''):
        file='index.html'

    try:
        
        archivo=open(file, 'rb')
        salida=archivo.read()
        archivo.close()
        
        cabecera='HTTP/1.1 200 OK\n'
        #MIME
        if(file.endswith('.png')):
            typeFile='image/png'
        elif(file.endswith('.pdf')):
            typeFile='application/pdf'
        elif(file.endswith('.gif')):
            typeFile='image/gif'
        else:
            Filetype='text/html'
        cabecera+='Content.Type'+str(Filetype)+'\n\n'
    
    except Exception as e:
        cabecera='HTTP/1.1 404 404 Not Found\n'
        salida='<hmtl><body>ERROR 404</body></html>'.encode('utf-8')
    rps=cabecera.encode('utf-8')
    rps+=salida
    conn.send(rps)
    conn.close()