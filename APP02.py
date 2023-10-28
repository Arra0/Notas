from guizero import App, Text, PushButton

app = App("ICI app")
message = Text(app,text="bien vendio a ICI")

buttom = PushButton(app, text="click me")
app.display()