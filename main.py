import pickle
import  tkinter
from tkinter import ttk


class Camiseta:

    def __init__(self,id, material, talla):
        self.id = id
        self.material = material
        self.talla = talla

if __name__ == '__main__':
    listaCamisetas = []


    ventana = tkinter.Tk()
    ventana.geometry("550x500")
    ventana.title("Camisetas")

    labelTitulo = tkinter.Label(ventana, text = "Lista de camisetas")
    labelTitulo.pack()

    labelId = tkinter.Label(ventana, text="Id")
    labelId.place(x=230, y=50)

    entryId = tkinter.Entry(ventana)
    entryId.place(x=300, y=50)

    labelMaterial = tkinter.Label(ventana, text = "Material")
    labelMaterial.place(x=230,y=90)

    entryMaterial = tkinter.Entry(ventana)
    entryMaterial.place(x=300,y=90)

    labelTalla = tkinter.Label(ventana, text="Talla")
    labelTalla.place(x=230,y=130)

    entryTalla = tkinter.Entry(ventana)
    entryTalla.place(x=300,y=130)

    labelMensajes = tkinter.Label(ventana, text="")##esto es para mostrar mensajes
    labelMensajes.place(x=230, y=200)

    tabla = ttk.Treeview()
    tabla.place(x=50,y=240)

    tabla["columns"] = ("1", "2","3")

    tabla.column("#0", width = 0)
    tabla.column("1", width=150)
    tabla.column("2", width=150)
    tabla.column("3", width=150)
    tabla.heading("1", text="Id")
    tabla.heading("2", text="Material")
    tabla.heading("3", text="Talla")

    def mostrarTabla():
        tabla.delete(*tabla.get_children())#borrar los datos de la tabla
        for i in range(0, len(listaCamisetas)):
            cami: Camiseta = listaCamisetas[i]
            tabla.insert("", i, values=(cami.id, cami.material, cami.talla))

    try:
        ficheroleer = open("Camisetas", "rb")
        listaCamisetas = pickle.load(ficheroleer)##meto lo q hay en el fichero en la lista
        mostrarTabla()

    except:
        print("error al abrir fichero")

    def anadir():
        try:
            idrepetido=0#para ver si id se repite
            labelMensajes['text'] = ""  # q vacie el labelmensajes

            id = entryId.get()
            material = entryMaterial.get()
            talla = entryTalla.get()

            for i in range(0, len(listaCamisetas)):#recorro la lista para ver si el id introducido existe
                cami: Camiseta = listaCamisetas[i]

                if(id==cami.id):#para ver si se repite id, si se repite idrepetido=1
                    idrepetido=1

            if (id != "" and material != "" and talla != "" and idrepetido!=1):
                listaCamisetas.append(Camiseta(id, material, talla))

                entryId.delete(0,"end")
                entryMaterial.delete(0, "end")#q vacie los entry
                entryTalla.delete(0, "end")
                mostrarTabla()

            else:
                labelMensajes['text'] = "Introduce datos o id repetido"  # muestro los mensajes en el label
        except:
            print("Error al añadir")
    buttonAnadir = tkinter.Button(ventana, text = "Añadir", command = anadir)
    buttonAnadir.place(x=50,y=50)



    def modificar():
        labelMensajes['text'] = ""
        try:
            id = entryId.get()
            material = entryMaterial.get()
            talla = entryTalla.get()

            for i in range(0, len(listaCamisetas)):
                cami: Camiseta = listaCamisetas[i]

                if (id == cami.id):
                    listaCamisetas[i].material=material
                    listaCamisetas[i].talla = talla
                    entryId.delete(0, "end")
                    entryMaterial.delete(0, "end")  # q vacie los entry
                    entryTalla.delete(0, "end")
                    mostrarTabla()
        except:
            labelMensajes['text'] = "No existe ese id"

    buttonModificar = tkinter.Button(ventana, text="Modificar", command = modificar)
    buttonModificar.place(x=50,y=90)


    def borrar():
        labelMensajes['text'] = ""
        try:
            registro= tabla.selection()[0]#cojo la posicion del registro seleccionado
            id = tabla.item(registro, option="values")[0]#coge el id del registro seleccionado

            for i in range(len(listaCamisetas)-1,-1,-1):
                cami: Camiseta = listaCamisetas[i]
                if (cami.id == id):
                    listaCamisetas.remove(cami)

            mostrarTabla()
        except:
            labelMensajes['text'] = "Selecciona fila para borrarla"


    buttonBorrar = tkinter.Button(ventana, text="Borrar", command=borrar)
    buttonBorrar.place(x=50, y=130)

    def on_closing():
        fichero = open("Camisetas", "wb")
        pickle.dump(listaCamisetas, fichero)
        fichero.close()
        ventana.destroy()

    ventana.protocol("WM_DELETE_WINDOW", on_closing)
    ventana.mainloop()