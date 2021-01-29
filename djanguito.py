from http.server import BaseHTTPRequestHandler,HTTPServer
import datetime
import mimetypes
import random

PORT = 8080

def render(archivo, context):
    with open('templates/'+archivo,'r') as templatefile:
        template = templatefile.read()
        template_renderizado = template.format_map(context)
        return template_renderizado.encode('utf-8')
    
def get_static(file_name):
    mime = mimetypes.MimeTypes().guess_type(file_name)[0]
    with open(file_name, "rb") as file:
        static_file = file.read()
        return static_file, mime
    
def titulos():
    titulo = random.choice([
                'Conferencia de prensa del presidente',
                'Introducción a Flickr 2.0 ',
                'Ponga un tigre en su tanque',
                'Confiesa Angelina Jol',
                'Mi entrevista exclusiva con Steve Jobs',
                '¿Quién más quiere hacerse rico online?',
                'Rami Malek comparte una emotiva historia sobre Robin Williams',
                'Gal Gadot recordó a las víctimas del Holocausto: "Fui a encender una vela en el muro de Auchwitz en recuerdo de mi abuelo"',
                'Muere el destacado cantautor argentino César Isella'
                ])
    return titulo
    
    
    
class myHandler(BaseHTTPRequestHandler):
    
    #Handler for the GET requests
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            # Send the html message
            
            context = {
                'titulo1':titulos(),
                'titulo2':titulos(),
                'titulo3':titulos(),
                'hora':str(datetime.datetime.now()),
                'saludo':'Zdrastvuytie'
            }
            self.wfile.write(render('inicio.html',context))
        
        elif self.path == '/empresa':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            context = {
                'titulo':'Nuestra Empresa',
                'parrafo':'''Somos uno de los más grandes y prestigiosos 
                conglomerados de retail en América Latina. Contamos con operaciones activas en Argentina, Brasil, Chile, Perú y Colombia, 
                donde día a día desarrollamos una exitosa estrategia multiformato que hoy da 
                trabajo a más de 140 mil colaboradores'''
            }
            # Send the html message
            self.wfile.write(render('empresa.html',context))

        elif self.path == '/contacto':
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            # Send the html message
            
            
            context = {
                'titulo':'formulario de contacto',
                'direccion': '''Vicuña Mackenna 4230, Macul, RM, Chile''',
                'nombre':'nombre',
                'correo':'correo',
                'mensaje':'mensaje',
                
            }
            self.wfile.write(render('contacto.html',context))

        elif self.path == '/static/img/Putin.jpeg':
            content, mime = get_static('static/img/Putin.jpeg')
            self.send_response(200)
            self.send_header('Content-type',mime)
            self.end_headers()
            # Send the html message
            self.wfile.write(content)
        
        elif self.path == '/static/css/style.css':
            content, mime = get_static('static/css/style.css')
            self.send_response(200)
            self.send_header('Content-type',mime)
            self.end_headers()
            # Send the html message
            self.wfile.write(content)
        
        
            
            
server = HTTPServer(('', PORT), myHandler)
print('Started httpserver on port ', PORT)

#Wait forever for incoming http requests
server.serve_forever()