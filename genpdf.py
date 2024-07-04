import jinja2
import pdfkit
import os

def crear_pdf(ruta_template1,info,nfact):
    nombre_template=ruta_template1.split("/")[-1]
    ruta_template=ruta_template1.replace(nombre_template,'')

    env=jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_template))
    template=env.get_template(nombre_template)
    html=template.render(info)
    
    options={"page-size":"Letter", "encoding": 'UTF-8','enable-local-file-access': None}
    config=pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")

    ruta_sal=os.getcwd()+"/Facturas/"
    ruta_sal1=ruta_sal.replace("\\","/")

    ruta_salida=ruta_sal1+nfact+".pdf"
    pdfkit.from_string(html,ruta_salida,options=options,configuration=config)


