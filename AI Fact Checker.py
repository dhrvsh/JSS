import customtkinter
import google.generativeai as genai

customtkinter.set_default_color_theme("themes/breeze.json")
font="SF Pro Display"

genai.configure(api_key="AIzaSyCJ2jhk3vCvFwIZL8GTb3yFnNxOcfiAHDs")

model = genai.GenerativeModel('gemini-2.5-flash')

app = customtkinter.CTk()
app.geometry("400x350")
app.title("AI Fact Checker")
app.resizable(False, False)

title = customtkinter.CTkLabel(app, text="AI Fact Checker", fg_color="transparent", font=(font, 40))
title.place(relx=0.5, rely=0.14, anchor=customtkinter.CENTER)

info = customtkinter.CTkEntry(app, placeholder_text="Enter claim here.", width=350, height=32, font=(font, 13))
info.place(relx=0.5, rely=0.28, anchor=customtkinter.CENTER)

TF = customtkinter.CTkTextbox(app, wrap=customtkinter.WORD, width=350, height=64, font=(font, 15))
TF.place(relx=0.5, rely=0.455, anchor=customtkinter.N)
TF.configure(state="disabled")

src = customtkinter.CTkTextbox(app, wrap=customtkinter.WORD, width=350, height=64, font=(font, 15))
src.place(relx=0.5, rely=0.95, anchor=customtkinter.S)
src.configure(state="disabled")

cb = customtkinter.CTkProgressBar(app, orientation="horizontal", width=220)
cb.place(relx=0.91, rely=0.7, anchor=customtkinter.E)
cb.set(0)
cbtxt = customtkinter.CTkLabel(app, text="Credibility Score", fg_color="transparent", font=(font, 15))
cbtxt.place(relx=0.07, rely=0.7, anchor=customtkinter.W)


def factCheck():
    response = model.generate_content(f"""Fact check this information: {info.get()}
    Seperate your answer into 3 lines.
    Line 1: True/False. Explaination in the same line, must be VERY breif
    Line 2: Credibility score in percentage. Must be in the format: <percent>. NO NEED FOR PERCENTAGE SYMBOL
    Line 3: Sources you got the answer from.
    DO NOT DO ANY TEXT FORMAT""")

    accResponse = response.text
    LOO = accResponse.split("\n")
    LOO[1] = int(LOO[1])
    
    TF.configure(state="normal")
    TF.delete("0.0", "end")
    TF.insert("0.0", LOO[0])    
    TF.configure(state="disabled")

    src.configure(state="normal")
    src.delete("0.0", "end")
    src.insert("0.0", "Sources:\n"+LOO[2])    
    src.configure(state="disabled")

    cb.set(LOO[1])

enter = customtkinter.CTkButton(app, text="Fact Check", width=350, height=32, command=factCheck, font=(font, 15))
enter.place(relx=0.5, rely=0.385, anchor=customtkinter.CENTER)

app.mainloop()