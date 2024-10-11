import PySimpleGUI as sg
sg.theme("LightGreen")
sg.theme_text_color("#007FFF")
window = sg.Window(title="Profile",
                   layout = [[sg.Text("SELAMAT DATANG DI KELAS",
                                      font=("Times", 25, "italic","bold","underline"))],
                            [sg.Text("NPM       : 2210010091")],
                            [sg.Text("NAMA      : ELZA ILHAM ADI PRATAMA")],
                            [sg.Text("KELAS     : 5N REGULER BANJARMASIN")],
                            [sg.Text("MATKUL    : PEMROGRAMAN VISUAL 3")],
                            ], 
                    size = (510,200),
                    font=("Times", 18))
window()
window.close()