import tkinter
import re

## Function which shows result of query
def show():
    value_label['text'] = text_area.get(0.0, 'end')
    print(text_area.index('end - 1c'))

## Function to add highlight to the text
def check():
    buf = text_area.get(0.0, 'end').upper()
    if re.search('SELECT', buf):
        print(buf.index('SELECT'))

## Function to add line number
def add_line_number(event):
    ## Set focus on text widget
    text_area.focus_set()

    ## Check whether text widget was modified if 'yes' set 'no'
    if text_area.edit_modified():
        text_area.edit_modified(False)
    
    ## Quantity of lines at the text
    limit = [str(i) + '\n' for i in range(1, text_area.get('0.0', 'end')\
                                          .count('\n') + 1)]

    ## Index of last characters at the text represent as (Row, Column) pair
    index = text_area.index('end - 1c')

    ## Check if column index greater then border value
    ## if yes carry on new line
    if int(index.split('.')[1]) > 79:
        text_area.insert(index, '\n')
    
    ## Reassign all values of num_label text
    num_label['text'] = ''
    for i in limit:
        num_label['text'] += i

    ## Call check function to check whether text includes keywords
    check()


root = tkinter.Tk()
root.title('Script DB manager')
text_area = tkinter.Text(root)
button = tkinter.Button(master = root, text="button", command = show)
value_label = tkinter.Label(root)
num_label = tkinter.Label(master = root,
                          width = int(text_area['width'] * 0.03),
                          text='1\n',
                          font=('TkDefaultFont', 10, 'bold'),
                          fg='blue')


num_label.grid(row = 0, column = 0, sticky = 'N')
text_area.grid(row = 0, column = 1)
button.grid(row = 1, column = 1)
value_label.grid(row = 2, column = 1)

text_area.bind('<<Modified>>', add_line_number)

root.mainloop()
