from guizero import App, Text, PushButton, TextBox

app = App(title="ICI aclucladora sumas")


def suma():
    app.info ("la suma es ", text= f"{int(numero1.value)+int(numero2.value)}")


messge = Text(app, text="ingrese el primer numero")
numero1 = TextBox(app)
messge_2 = Text(app, text="ingrese el primer numero")
numero2= TextBox(app)
buttom = PushButton(app, text="sumar", command=suma)
messge = Text(app)
app.display()
