from guizero import App, Text, PushButton

def say_hello():
    message.value = "ICI rocks!!"

app = App("ICI app")
message = Text(app,text="bien vendio a ICI")

buttom = PushButton(app, text="click me", command=say_hello)
app.display()