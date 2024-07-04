from tkinter import *
from tkinter import messagebox
import genpdf
import cuf
from interfaz2 import *
import os
#---------------------------------------------------------------------------------
#Electronica

ruta_iman=os.getcwd()+"\ima.PNG"
ruta_ima=ruta_iman.replace("\\","/")
def enviar():

    cufe=cuf.generaCadena()

    info={"fech_emi":varfech_emi.get(),"fech_exp":varfech_exp.get(),"fech_ven":varfech_ven.get(),"t_op":vart_op.get(),
    "f_pag":varf_pag.get(),"n_doc":varn_doc.get(),"pais":varpais.get(),"dep":vardep.get(),"mun":varmun.get(),
    "t_contr":vart_contr.get(),"correo":varcorreo.get(),"telef":vartelef.get(),"direcc":vardirecc.get(),"tip":vartip.get(),
    "cantidad":varcantidad.get(),"peso":varpeso.get(),"origen":varorigen.get(),"destino":vardestino.get(),
    "fech_prob":varfech_prob.get(),"s_entreg":vars_entreg.get(),"productos":f_prod2,"adquiriente":adquiriente.get(),
    "r_social":r_social.get(),"total":totf,"cufe":cufe,"subtprec":subtprec,"valorseguro":valorseguro,
    "notas":textcomentarios.get(1.0,END),"ruta_ima":ruta_ima}

    productos="<tr>"
    ruta_template=os.getcwd()+"\Facturaelec.html"
    ruta_template1=ruta_template.replace("\\","/")

    genpdf.crear_pdf(ruta_template1,info,nombredocumento.get())
    

    print(info)
    
    messagebox.showinfo("Proceso","El pdf ha sido generado con exito")
    limpiar()


    return info

#empresarial
def enviar2():


    info={"fech_emi":varfech_emi.get(),"fech_exp":varfech_exp.get(),"fech_ven":varfech_ven.get(),"t_op":vart_op.get(),
    "f_pag":varf_pag.get(),"n_doc":varn_doc.get(),"pais":varpais.get(),"dep":vardep.get(),"mun":varmun.get(),
    "t_contr":vart_contr.get(),"correo":varcorreo.get(),"telef":vartelef.get(),"direcc":vardirecc.get(),"tip":vartip.get(),
    "cantidad":varcantidad.get(),"peso":varpeso.get(),"origen":varorigen.get(),"destino":vardestino.get(),
    "fech_prob":varfech_prob.get(),"s_entreg":vars_entreg.get(),"productos":f_prod2,"adquiriente":adquiriente.get(),
    "r_social":r_social.get(),"total":totf,"subtprec":subtprec,"valorseguro":valorseguro,"n_factur":varn_factur.get(),
    "notas":textcomentarios.get(1.0,END),"ruta_ima":ruta_ima}

    productos="<tr>"

    ruta_template=os.getcwd()+"\Facturaempre.html"
    ruta_template1=ruta_template.replace("\\","/")

    
    genpdf.crear_pdf(ruta_template1,info,nombredocumento.get())
    

    print(info)
    
    messagebox.showinfo("Proceso","El pdf ha sido generado con exito")
    limpiar()


    return info   

def calcular():
    prec=varprecio.get()
    cant=varcantidad.get()
    iva=prec*0.19
    global total
    global subtprec
    subtprec+=(prec*cant)
    total=(prec*cant)+valorseguro+iva
    global totf
    totf+=total
    f_prod="<tr><td>"+str(i)+"</td><td>"+guia.get()+"</td><td>"+descripcion.get()+"</td><td>EA</td><td>"+str(cant)+"</td><td>"+str(prec)+"</td><td>100000</td><td>"+str(valorseguro)+"</td><td>"+str(iva)+"</td><td>0</td><td>0</td><td>"+str(total)+"</td></tr>"
    
    tabul(f_prod)

    limpiar2()

def tabul(fprod):
    global f_prod2
    global i
    if(f_prod2==""):
        f_prod2=fprod
        i+=1
    else:
        f_prod2=f_prod2+fprod
        i+=1
    messagebox.showinfo("Proceso","Producto agregado con exito")
    print(f_prod2)

def info():
	messagebox.showinfo("Acerca de...","Autor: Jhon Arredondo\nDesarrollado en Python\nCorreo de contacto: jhonarredondo15@gmail.com")


def escribaFecha(event):
    if event.char.isdigit():
        texto = cuadrofech_emi.get()
        texto2= cuadrofech_exp.get()
        texto3= cuadrofech_ven.get()
        texto4= cuadrofech_prob.get()

        letras = 0
        for j in texto:
            letras +=1
        if letras == 2:
            cuadrofech_emi.insert(2,"/")
        elif letras == 5:
            cuadrofech_emi.insert(5,"/")
        
        letras2 = 0
        for j in texto2:
            letras2 +=1
        if letras2 == 2:
                cuadrofech_exp.insert(2,"/")
        elif letras2 == 5:
                cuadrofech_exp.insert(5,"/")

        letras3 = 0
        for j in texto3:
                letras3 +=1
        if letras3 == 2:
                cuadrofech_ven.insert(2,"/")
        elif letras3 == 5:
                cuadrofech_ven.insert(5,"/")

        letras4 = 0
        for j in texto4:
            letras4 +=1
        if letras4 == 2:
            cuadrofech_prob.insert(2,"/")
        elif letras4 == 5:
                cuadrofech_prob.insert(5,"/") 
            
    else:
        return "break"

def limpiar():
    varfech_emi.set("")
    varfech_exp.set("")
    varfech_ven.set("")
    vart_op.set("")
    varf_pag.set("")
    varn_doc.set("")
    varpais.set("")
    vardep.set("")
    varmun.set("")
    vart_contr.set("")
    varcorreo.set("")
    vartelef.set("")
    vardirecc.set("")
    vartip.set("")
    varpeso.set("")
    varorigen.set("")
    vardestino.set("")
    varfech_prob.set("")
    vars_entreg.set("")
    descripcion.set("")
    guia.set("")
    adquiriente.set("")
    r_social.set("")
    nombredocumento.set("")
    varcantidad.set(0)
    varprecio.set(0)
    textcomentarios.delete(1.0,END)

def limpiar2():
    varcantidad.set(0)
    varprecio.set(0)
    descripcion.set("")
    guia.set("")


def fr2():
    root.destroy()
    fri2()

def salir():
        root.destroy()    
       
#------------------------------Frame-----------------------------------------------------    

root=Tk()
root.title("Factura electronica y comercial")
#root.iconbitmap("interrogacion.ico")
root.geometry("900x650+250+0")
bm=Menu(root)
root.config(menu=bm)

menu1=Menu(bm,tearoff=0)
menu1.add_command(label="Salir",command=salir)

menu2=Menu(bm,tearoff=0)
menu2.add_command(label="Acerca de...",command=info)

menu3=Menu(bm,tearoff=0)
menu3.add_command(label="Factura personal",command=fr2)

bm.add_cascade(label="Facturas",menu=menu3)
bm.add_cascade(label="Info",menu=menu2)
bm.add_cascade(label="Salir",menu=menu1)

#----------------------------------------------------------------------------------------------------------

frame1=Frame(root)

frame1.pack()
frame1.config(width="600",height="600")


cufe=""
f_prod2=""
i=1
totf=0
subtprec=0
iva=0.19
varfech_emi=StringVar()
varfech_exp=StringVar()
varfech_ven=StringVar()
vart_op=StringVar()
varf_pag=StringVar()
varn_doc=StringVar()
varpais=StringVar()
vardep=StringVar()
varmun=StringVar()
vart_contr=StringVar()
varcorreo=StringVar()
vartelef=StringVar()
vardirecc=StringVar()
vartip=StringVar()
varcantidad=IntVar()
varpeso=StringVar()
varorigen=StringVar()
vardestino=StringVar()
varfech_prob=StringVar()
vars_entreg=StringVar()
varprecio=IntVar()
valorseguro=1000
descripcion=StringVar()
guia=StringVar()
adquiriente=StringVar()
r_social=StringVar()
nombredocumento=StringVar()
varn_factur=IntVar()

#-----------------------------------------------------------------------------------------------

etiquetafech_emi=Label(frame1,text="Fecha de Emision")
etiquetafech_emi.grid(row=0,column=0,pady=10,padx=10)

cuadrofech_emi=Entry(frame1,textvariable=varfech_emi)
cuadrofech_emi.grid(row=0,column=1,pady=10,padx=10)

cuadrofech_emi.bind("<Key>", escribaFecha)
cuadrofech_emi.bind("<BackSpace>", lambda _:cuadrofech_emi.delete(root.END))

etiquetafech_exp=Label(frame1,text="Fecha de expedicion")
etiquetafech_exp.grid(row=0,column=2,pady=10,padx=10)

cuadrofech_exp=Entry(frame1,textvariable=varfech_exp)
cuadrofech_exp.grid(row=0,column=3,pady=10,padx=10)

cuadrofech_exp.bind("<Key>", escribaFecha)
cuadrofech_exp.bind("<BackSpace>", lambda _:cuadrofech_exp.delete(root.END))

etiquetfech_ven=Label(frame1,text="Fecha de vencimiento")
etiquetfech_ven.grid(row=1,column=0,pady=10,padx=10)

cuadrofech_ven=Entry(frame1,textvariable=varfech_ven)
cuadrofech_ven.grid(row=1,column=1,pady=10,padx=10)

cuadrofech_ven.bind("<Key>", escribaFecha)
cuadrofech_ven.bind("<BackSpace>", lambda _:cuadrofech_ven.delete(root.END))

etiquetat_op=Label(frame1,text="Tipo de operacion")
etiquetat_op.grid(row=1,column=2,pady=10,padx=10)

cuadrot_op=Entry(frame1,textvariable=vart_op)
cuadrot_op.grid(row=1,column=3,pady=10,padx=10)

etiquetaf_pag=Label(frame1,text="Forma de pago")
etiquetaf_pag.grid(row=2,column=0,pady=10,padx=10)

cuadrof_pag=Entry(frame1,textvariable=varf_pag)
cuadrof_pag.grid(row=2,column=1,pady=10,padx=10)

#--------------------------------------------------------------------------------------------------------

etiquetaadquir=Label(frame1,text="Adquiriente")
etiquetaadquir.grid(row=3,column=0,pady=10,padx=10)
etiquetaadquir.config(fg="red")

cuadroadquir=Entry(frame1,textvariable=adquiriente)
cuadroadquir.grid(row=3,column=1,pady=10,padx=10)

etiquetan_doc=Label(frame1,text="Numero Documento")
etiquetan_doc.grid(row=4,column=0,pady=10,padx=10)

cuadron_doc=Entry(frame1,textvariable=varn_doc)
cuadron_doc.grid(row=4,column=1,pady=10,padx=10)

etiquetaadquir=Label(frame1,text="Razón Social")
etiquetaadquir.grid(row=3,column=2,pady=10,padx=10)
etiquetaadquir.config(fg="red")

cuadror_soc=Entry(frame1,textvariable=r_social)
cuadror_soc.grid(row=3,column=3,pady=10,padx=10)

etiquetapais=Label(frame1,text="Pais")
etiquetapais.grid(row=4,column=2,pady=10,padx=10)

cuadropais=Entry(frame1,textvariable=varpais)
cuadropais.grid(row=4,column=3,pady=10,padx=10)

etiquetadep=Label(frame1,text="Departamento")
etiquetadep.grid(row=5,column=0,pady=10,padx=10)

cuadrodep=Entry(frame1,textvariable=vardep)
cuadrodep.grid(row=5,column=1,pady=10,padx=10)


etiquetamun=Label(frame1,text="Municipio")
etiquetamun.grid(row=5,column=2,pady=10,padx=10)

cuadromun=Entry(frame1,textvariable=varmun)
cuadromun.grid(row=5,column=3,pady=10,padx=10)

etiquetat_contr=Label(frame1,text="Tipo contribuyente")
etiquetat_contr.grid(row=6,column=0,pady=10,padx=10)

cuadrot_contr=Entry(frame1,textvariable=vart_contr)
cuadrot_contr.grid(row=6,column=1,pady=10,padx=10)


etiquetacorreo=Label(frame1,text="Correo")
etiquetacorreo.grid(row=6,column=2,pady=10,padx=10)

cuadrocorreo=Entry(frame1,textvariable=varcorreo)
cuadrocorreo.grid(row=6,column=3,pady=10,padx=10)


etiquetatelef=Label(frame1,text="Telefono")
etiquetatelef.grid(row=7,column=0,pady=10,padx=10)

cuadrotelef=Entry(frame1,textvariable=vartelef)
cuadrotelef.grid(row=7,column=1,pady=10,padx=10)

etiquetadirecc=Label(frame1,text="Direccion")
etiquetadirecc.grid(row=7,column=2,pady=10,padx=10)

cuadrodirecc=Entry(frame1,textvariable=vardirecc)
cuadrodirecc.grid(row=7,column=3,pady=10,padx=10)

#---------------------------------------------------------------------------------------------

etiquetaadquir=Label(frame1,text="Informacion del tipo de transporte")
etiquetaadquir.place(x=245,y=315)
etiquetaadquir.config(fg="red")

etiquetatip=Label(frame1,text="Tipo")
etiquetatip.grid(row=8,column=0,pady=10,padx=10)

cuadrotip=Entry(frame1,textvariable=vartip)
cuadrotip.grid(row=8,column=1,pady=10,padx=10)


etiquetapeso=Label(frame1,text="Peso")
etiquetapeso.grid(row=8,column=2,pady=10,padx=10)

cuadropeso=Entry(frame1,textvariable=varpeso)
cuadropeso.grid(row=8,column=3,pady=10,padx=10)

etiquetaorigen=Label(frame1,text="Origen")
etiquetaorigen.grid(row=9,column=0,pady=10,padx=10)

cuadroorigen=Entry(frame1,textvariable=varorigen)
cuadroorigen.grid(row=9,column=1,pady=10,padx=10)

etiquetadestino=Label(frame1,text="Destino")
etiquetadestino.grid(row=9,column=2,pady=10,padx=10)

cuadrodestino=Entry(frame1,textvariable=vardestino)
cuadrodestino.grid(row=9,column=3,pady=10,padx=10)

etiquetafech_prob=Label(frame1,text="Fecha probable")
etiquetafech_prob.grid(row=9,column=4,pady=10,padx=10)

cuadrofech_prob=Entry(frame1,textvariable=varfech_prob)
cuadrofech_prob.grid(row=9,column=5,pady=10,padx=10)

cuadrofech_prob.bind("<Key>", escribaFecha)
cuadrofech_prob.bind("<BackSpace>", lambda _:cuadrofech_prob.delete(root.END))

etiquetas_entreg=Label(frame1,text="Sitio entrega")
etiquetas_entreg.grid(row=10,column=0,pady=10,padx=10)

cuadros_entreg=Entry(frame1,textvariable=vars_entreg)
cuadros_entreg.grid(row=10,column=1,pady=10,padx=10)

etiquetaadquir=Label(frame1,text="Detalles del producto")
etiquetaadquir.grid(row=11,column=0,pady=10,padx=10, columnspan=2)
etiquetaadquir.config(fg="red")

butcrear=Button(frame1,text="Añadir nuevo producto",command=calcular)
butcrear.grid(row=11,column=2,pady=10,padx=10,columnspan=2)

etiquetas_entreg=Label(frame1,text="Guia")
etiquetas_entreg.grid(row=12,column=0,pady=10,padx=10)

cuadroguia=Entry(frame1,textvariable=guia)
cuadroguia.grid(row=12,column=1,pady=10,padx=10)

etiquetadescripcion=Label(frame1,text="Descripcion")
etiquetadescripcion.grid(row=12,column=2,pady=10,padx=10)

cuadrosdescr=Entry(frame1,textvariable=descripcion)
cuadrosdescr.grid(row=12,column=3,pady=10,padx=10)

etiquetaprecio=Label(frame1,text="Precio")
etiquetaprecio.grid(row=13,column=0,pady=10,padx=10)

cuadroprecio=Entry(frame1,textvariable=varprecio)
cuadroprecio.grid(row=13,column=1,pady=10,padx=10)

etiquetacantidad=Label(frame1,text="Cantidad")
etiquetacantidad.grid(row=13,column=2,pady=10,padx=10)

cuadrocantidad=Entry(frame1,textvariable=varcantidad)
cuadrocantidad.grid(row=13,column=3,pady=10,padx=10)

etiquetanombre=Label(frame1,text="Nombre factura")
etiquetanombre.grid(row=14,column=0,pady=10,padx=10)

cuadronombre=Entry(frame1,textvariable=nombredocumento)
cuadronombre.grid(row=14,column=1,pady=10,padx=10)

etiquetan_factur=Label(frame1,text="Numero factura")
etiquetan_factur.grid(row=14,column=4,pady=10,padx=10)

cuadron_factur=Entry(frame1,textvariable=varn_factur)
cuadron_factur.grid(row=14,column=5,pady=10,padx=10)

butcrear=Button(frame1,text="Factura Electronica",command=enviar)
butcrear.grid(row=14,column=2,pady=10,padx=10)

butcrear=Button(frame1,text="Factura empresarial",command=enviar2)
butcrear.grid(row=14,column=3,pady=10,padx=10)

etiquetcoment=Label(frame1,text="Notas")
etiquetcoment.grid(row=12,column=4,pady=10,padx=10,rowspan=2)

textcomentarios=Text(frame1,width=16,height=5)
textcomentarios.grid(row=12,column=5,pady=10,padx=10, rowspan=2)
scrollvert=Scrollbar(frame1,command=textcomentarios.yview)
scrollvert.grid(row=12,column=6,sticky="nsew")

textcomentarios.config(yscrollcommand=scrollvert.set)

#----------Etiquetas-------------

root.mainloop()