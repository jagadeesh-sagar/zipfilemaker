import FreeSimpleGUI as sg
label1=sg.Text("select files to compress")
input1=sg.Input()
choose_Button1=sg.FileBrowse()

label2=sg.Text("select destination  folder")
input2=sg.Input()
choose_Button2=sg.FolderBrowse()
compress_Button=sg.Button("compress")

window=sg.Window("file compresseor",layout=[[label1,input1,choose_Button1],[label2,input2,choose_Button2],[compress_Button]])
window.read()
window.close()