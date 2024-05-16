import FreeSimpleGUI as sg
from zip_creation import make_archieve
label1=sg.Text("select files to compress")
input1=sg.Input()
choose_Button1=sg.FileBrowse('choose',key="files")

label2=sg.Text("select destination  folder")
input2=sg.Input()
choose_Button2=sg.FolderBrowse('compress',key="folder")
compress_Button=sg.Button("compress")
output_label=sg.Text(key='output',text_color="green")

window=sg.Window("file compresseor",layout=[[label1,input1,choose_Button1],
                                            [label2,input2,choose_Button2],
                                            [compress_Button,output_label]])
while True:
    events,values=window.read()

    filepaths=values['files'].split(";")
    folder=values['folder']
    make_archieve(filepaths,folder)
    window["output"].update("compression successful")

window.read()
window.close()