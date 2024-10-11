import PySimpleGUI as sg
sg.theme("LightGreen")
sg.theme_text_color("#007FFF")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("FTI UNISKA", font = ("Helvetica", 25))],
                           [sg.Text("FAKULTAS TEKNOLOGI INFORMASI", font=("Courier", 18, "italic","bold","underline"))],
                           [sg.Text("UNISKA MAB BANJARMASIN", text_color="#FFCC00")]],
                    size=(430,200),
                    font=("Times", 18))
window()
window.close()