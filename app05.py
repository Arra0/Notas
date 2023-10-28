from guizero import App, Text, PushButton, TextBox

app = App("ICI app")

def saludo():
    app.info("mensaje ", f"hola {name.value}")
    #message.value = "Hola "+ name.value


message = Text(app,text="como te llamas?")
name = TextBox(app)


buttom = PushButton(app, text="click me", command=saludo)
message = Text(app,)
app.display()