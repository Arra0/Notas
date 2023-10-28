from guizero import App, Text, PushButton, TextBox

app = App("ICI app")
message = Text(app,text="bien vendio a ICI")
name = TextBox(app)
#buttom = PushButton(app, text="click me")
app.display()