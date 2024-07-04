from tkinter import *
from tkinter import messagebox
import genpdf
import os

f_prod2=""
i=1
totf=0
iva=0.19
cambio=0 
pagar=0  
pagarf=0 

def fri2():
    
    def enviar():

        

        info={"fech_emi":varfech_emi.get(),"f_pag":varf_pag.get(),"n_doc":varn_doc.get(),"direcc":vardirecc.get(),
        "cantidad":varcantidad.get(),"productos":f_prod2,"adquiriente":adquiriente.get(),
        "total":totf,"v_pag":pagarf,"cambio":cambio}


        ruta_template=os.getcwd()+"\FacturaPOS.html"
        ruta_template1=ruta_template.replace("\\","/")

        genpdf.crear_pdf(ruta_template1,info,nombredocumento.get())
        

        print(info)
        
        messagebox.showinfo("Proceso","El pdf ha sido generado con exito")
        limpiar()

        

        return info
    

    def calcular():
        prec=varprecio.get()
        cant=varcantidad.get()
        pagar=varv_pg.get()
        iva=prec*0.19
        global total
        total=prec*cant
        global totf
        totf+=total
        global cambio
        cambio=totf-pagar
        global pagarf
        pagarf+=pagar
        f_prod="<tr><td>"+str(cant)+"</td><td>"+descripcion.get()+"</td><td>"+str(prec)+"</td></tr>"
        
        tabul(f_prod)

        limpiar2()

    def tabul(fprod):
        global f_prod2
        if(f_prod2==""):
            f_prod2=fprod
        else:
            f_prod2=f_prod2+fprod

        
        print(pagar)
        messagebox.showinfo("Proceso","Producto agregado con exito")    


        print(f_prod2)

    def info():
        messagebox.showinfo("Acerca de...","Autor: Jhon Arredondo\nDesarrollado en Python\nCorreo de contacto: jhonarredondo15@gmail.com")


    def escribaFecha(event):
        if event.char.isdigit():
            texto = cuadrofech_emi.get()
            letras = 0
            for j in texto:
                letras +=1
            if letras == 2:
                cuadrofech_emi.insert(2,"/")
            elif letras == 5:
                cuadrofech_emi.insert(5,"/")
            
            
        else:
            return "break"

    def limpiar():
        varfech_emi.set("")
        varf_pag.set("")
        varn_doc.set("")
        vardirecc.set("")
        descripcion.set("")
        adquiriente.set("")
        nombredocumento.set("")
        varcantidad.set(0)
        varprecio.set(0)
        varv_pg.set(0)

    def limpiar2():
        varcantidad.set(0)
        varprecio.set(0)
        descripcion.set("")
        varv_pg.set(0)

    def salir():
        root2.destroy()
        
    #------------------------------Frame-----------------------------------------------------    

    root2=Tk()
    root2.title("Factura POS")
    #root2.iconbitmap("interrogacion.ico")
    root2.geometry("700x400+400+100")

    bm=Menu(root2)
    root2.config(menu=bm)

    menu1=Menu(bm,tearoff=0)
    menu1.add_command(label="Salir",command=salir)

    menu2=Menu(bm,tearoff=0)
    menu2.add_command(label="Acerca de...",command=info)

    
    bm.add_cascade(label="Info",menu=menu2)
    bm.add_cascade(label="Salir",menu=menu1)

    #----------------------------------------------------------------------------------------------------------

    frame2=Frame(root2)

    frame2.pack()
    frame2.config(width="600",height="600")

    varfech_emi=StringVar()
    varf_pag=StringVar()
    varn_doc=StringVar()
    vardirecc=StringVar()
    varcantidad=IntVar()
    varprecio=IntVar()
    descripcion=StringVar()
    adquiriente=StringVar()
    nombredocumento=StringVar()
    varv_pg=IntVar()
    #-----------------------------------------------------------------------------------------------

    etiquetafech_emi=Label(frame2,text="Fecha de Emision")
    etiquetafech_emi.grid(row=0,column=1,pady=10,padx=10)

    cuadrofech_emi=Entry(frame2,textvariable=varfech_emi)
    cuadrofech_emi.grid(row=0,column=2,pady=10,padx=10,)

    cuadrofech_emi.bind("<Key>", escribaFecha)
    cuadrofech_emi.bind("<BackSpace>", lambda _:cuadrofech_emi.delete(root2.END))

    
    etiquetaf_pag=Label(frame2,text="Forma de pago")
    etiquetaf_pag.grid(row=1,column=2,pady=10,padx=10)

    cuadrof_pag=Entry(frame2,textvariable=varf_pag)
    cuadrof_pag.grid(row=1,column=3,pady=10,padx=10,)


    etiquetaadquir=Label(frame2,text="Adquiriente")
    etiquetaadquir.grid(row=1,column=0,pady=10,padx=10)
    etiquetaadquir.config(fg="red")

    cuadroadquir=Entry(frame2,textvariable=adquiriente)
    cuadroadquir.grid(row=1,column=1,pady=10,padx=10)

    etiquetan_doc=Label(frame2,text="Numero Documento")
    etiquetan_doc.grid(row=2,column=0,pady=10,padx=10)

    cuadron_doc=Entry(frame2,textvariable=varn_doc)
    cuadron_doc.grid(row=2,column=1,pady=10,padx=10)

   
    etiquetadirecc=Label(frame2,text="Direccion")
    etiquetadirecc.grid(row=2,column=2,pady=10,padx=10)

    cuadrodirecc=Entry(frame2,textvariable=vardirecc)
    cuadrodirecc.grid(row=2,column=3,pady=10,padx=10)

    #---------------------------------------------------------------------------------------------

    
    etiquetaadquir=Label(frame2,text="Detalles del producto")
    etiquetaadquir.grid(row=3,column=0,pady=10,padx=10, columnspan=2)
    etiquetaadquir.config(fg="red")

    butcrear=Button(frame2,text="Añadir nuevo producto",command=calcular)
    butcrear.grid(row=3,column=2,pady=10,padx=10,columnspan=2)


    etiquetadescripcion=Label(frame2,text="Descripcion")
    etiquetadescripcion.grid(row=4,column=2,pady=10,padx=10)

    cuadrosdescr=Entry(frame2,textvariable=descripcion)
    cuadrosdescr.grid(row=4,column=3,pady=10,padx=10)

    etiquetaprecio=Label(frame2,text="Precio")
    etiquetaprecio.grid(row=4,column=0,pady=10,padx=10)

    cuadroprecio=Entry(frame2,textvariable=varprecio)
    cuadroprecio.grid(row=4,column=1,pady=10,padx=10)

    etiquetacantidad=Label(frame2,text="Cantidad")
    etiquetacantidad.grid(row=5,column=0,pady=10,padx=10)

    cuadrocantidad=Entry(frame2,textvariable=varcantidad)
    cuadrocantidad.grid(row=5,column=1,pady=10,padx=10)

    etiquetav_pag=Label(frame2,text="Valor a pagar")
    etiquetav_pag.grid(row=5,column=2,pady=10,padx=10)

    cuadrov_pag=Entry(frame2,textvariable=varv_pg)
    cuadrov_pag.grid(row=5,column=3,pady=10,padx=10)


    etiquetanombre=Label(frame2,text="Nombre factura")
    etiquetanombre.grid(row=14,column=0,pady=10,padx=10)

    cuadronombre=Entry(frame2,textvariable=nombredocumento)
    cuadronombre.grid(row=14,column=1,pady=10,padx=10)

    butcrear=Button(frame2,text="Factura POS",command=enviar)
    butcrear.grid(row=14,column=2,pady=10,padx=10,columnspan=2)

   
    root2.mainloop()
