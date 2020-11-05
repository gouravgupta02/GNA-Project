import tkinter
from  tkinter import *

from tkinter import filedialog

root=tkinter.Tk()
root.title("server")
global T
global B

topFrame=tkinter.Frame(root,bg="grey",highlightbackground="black",borderwidth=6,relief=SUNKEN)
chatstart=tkinter.Button(topFrame, text="Chat enable", command=lambda : start_server())
chatstart.pack(side=tkinter.LEFT)
chatstop=tkinter.Button(topFrame, text="Chat disable", command=lambda : stop_server(), state= tkinter.DISABLED)
chatstop.pack(side=tkinter.RIGHT)
topFrame.pack(anchor=NW,pady=(5,0))

middleFrame=tkinter.Frame(root,bg="grey",highlightbackground="black",borderwidth=6,relief=GROOVE)
lblHost=tkinter.Label(middleFrame, text="Host: X.X.X.X.")
lblHost.pack(side=tkinter.LEFT)
lblPort= tkinter.Label(middleFrame, text="Port:XXXX")
lblPort.pack(side=tkinter.RIGHT)
middleFrame.pack(anchor=NW,pady=(10,0))

clientFrame = tkinter.Frame(root,bg="grey",highlightbackground="black",borderwidth=5,relief=SUNKEN)
lblLine = tkinter.Label(clientFrame, text="CLIENT LIST")
lblLine.pack(side=tkinter.TOP)
scrollBar = tkinter.Scrollbar(clientFrame)

scrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
tkDisplay = tkinter.Text(clientFrame,height=50,width=15)
tkDisplay.pack(side=tkinter.LEFT, padx=(5,0))
scrollBar.config(command=tkDisplay.yview)
tkDisplay.config(yscrollcommand=scrollBar.set,background="white",highlightbackground="black",state="disabled")
clientFrame.pack(side=LEFT,pady=(5,0))

leftFrame=tkinter.Frame(root,height=60,width=900,bg="grey",borderwidth=4,relief=SUNKEN)
leftDisplay=tkinter.Label(leftFrame,text="FILE").pack()
btn=tkinter.Button(leftFrame,text="Browse file",command=lambda:fileDialog()).pack(side=LEFT,anchor=SE)
cf=tkinter.Button(leftFrame, text="close file",command=lambda:closefile()).pack(side=RIGHT,anchor=SW)
quiz=tkinter.Button(leftFrame,text="Take quiz",command =lambda:openQuizWindow()).pack(side=BOTTOM,anchor=CENTER)

def openQuizWindow():  

    import srv 
#     from tkinter import ttk
#     global total
    
#     y=0  
#     n= ttk.Notebook()
#     f1= ttk.Frame(n)
#     f2= ttk.Frame(n)
#     f3= ttk.Frame(n)
#     f4= ttk.Frame(n)
#     f5= ttk.Frame(n)
#     f6= ttk.Frame(n)

#     window= ttk.Frame(n)


#     def main(x):
#         global total
#         n.add(f1, text="One")
#         n.add(f2, text="Two")
#         n.add(f3, text="Three")
#         n.add(f4, text="Four")
#         n.add(f5, text="Five")
#         n.add(f6, text="Six")
 
#         total= ttk.Label(window, text="0")


#         Label(f1, text="What is Tkinter?").grid(row=2,column=2)
#         Button(f1, text="Guided User Interface").bind(correct)
#         Button(f1, text="Guided User Interface").grid(row=3,column=1)
#         Button(f1, text="Variable", command=incorrect).grid(row=3,column=2)
#         Button(f1, text="Function", command=incorrect).grid(row=3,column=3)


#         Label(f2, text="What is Turtle?").grid(row=2,column=2)
#         Button(f2, text="GuidedUserInterface",command=incorrect2).grid(row=3,column=1)
#         Button(f2, text="Module", command=correct2).grid(row=3,column=2)
#         Button(f2, text="Boolean Value", command=incorrect2).grid(row=3,column=3)

#         Label(f3, text="What does the 'Print' command do?").grid(row=2,column=2)
#         Button(f3, text="Creater a window",command=incorrect3).grid(row=3,column=1)
#         Button(f3, text="Show a message in the Python Shell", command=correct3).grid(row=3,column=2)
#         Button(f3, text="Print to the printer", command=incorrect3).grid(row=3,column=3)

#         Label(f4, text="What is the moniter?").grid(row=2,column=2)
#         Button(f4, text="A display that shows what the computer is doing",command=correct4).grid(row=3,column=1)
#         Button(f4, text="A circut board", command=incorrect4).grid(row=3,column=2)
#         Button(f4, text="A Program", command=incorrect4).grid(row=3,column=3)


#         Label(f5, text="What does the 'from ____ import' command do?").grid(row=2,column=2)
#         Button(f5, text="Import an image",command=incorrect5).grid(row=3,column=1)
#         Button(f5, text="Import text", command=incorrect5).grid(row=3,column=2)
#         Button(f5, text="Import a module", command=correct5).grid(row=3,column=3)

#         Label(f6, text="Which of these is a Boolean Value?").grid(row=2,column=2)
#         Button(f6, text="Enter",command=incorrect6).grid(row=3,column=1)
#         Button(f6, text="Esc", command=incorrect6).grid(row=3,column=2)
#         Button(f6, text="True", command=correct6).grid(row=3,column=3)
#         return total



#     def correct():
#         global total
#         Label(f1, text="Correct").grid(row=1,column=2)
#         counter()
#     def incorrect():
#         Label(f1, text="Incorrect").grid(row=1,column=2)

#     def correct2():
#         global total
#         Label(f2, text="Correct").grid(row=1,column=2)
#         counter()

#     def incorrect2():
#         Label(f2, text="Incorrect").grid(row=1,column=2)

#     def correct3():
#         global total
#         Label(f3, text="Correct").grid(row=1,column=2)
#         counter()

#     def incorrect3():
#         Label(f3, text="Incorrect").grid(row=1,column=2)

#     def correct4():
#         global total
#         Label(f4, text="Correct").grid(row=1,column=2)
#         counter()

#     def incorrect4():
#         Label(f4, text="Incorrect").grid(row=1,column=2)

#     def correct5():
#         global total
#         Label(f5, text="Correct").grid(row=1,column=2)
#         counter()

#     def incorrect5():
#         Label(f5, text="Incorrect").grid(row=1,column=2)

#     def correct6():
#         global total
#         Label(f6, text="Correct").grid(row=1,column=2)
#         counter()

#     def incorrect6():
#         Label(f6, text="Incorrect").grid(row=1,column=2)


#     def counter():
#         global total
#         total['text'] = str(int(total['text']) + 1)


#     main(y)


#     n.pack()

#     n.mainloop()


leftFrame.pack(side=RIGHT,padx=50)
T= tkinter.Text(leftFrame, height=40, width=100)
T.pack(side=LEFT,padx=0,pady=5)




    
    
    
    


displayFrame=tkinter.Frame(root,bg="grey",highlightbackground="black",borderwidth=5,relief=SUNKEN)
lblLine=tkinter.Label(displayFrame, text="PUBLIC CHAT").pack()
scrollbar=tkinter.Scrollbar(displayFrame)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
TkDisplay=tkinter.Text(displayFrame,height=47,width=60)
TkDisplay.pack(side=tkinter.LEFT,fill=tkinter.Y,padx=(5,0))
TkDisplay.tag_config("Enter your message",foreground="blue")
scrollbar.config(command=TkDisplay.yview)
TkDisplay.config(yscrollcommand=scrollbar.set, background="white",highlightbackground="white",state="disabled")
displayFrame.pack(anchor=NW,padx=(5,0))



bottomFrame=tkinter.Frame(root,bg="grey",borderwidth=3,relief=SUNKEN,)
tkMessage=tkinter.Text(bottomFrame,height=2,width=37)
tkMessage.pack(side=tkinter.LEFT,padx=(5,13),pady=(5,10))
tkMessage.config(highlightbackground="black",state="disabled")
tkMessage.bind("<Return>",(lambda event:getChatMessage(tkMessage.get("1.0",tkinter.END))))
bottomFrame.pack(anchor=NW,pady=(2,0))


    
import socket
import threading
import time



global clients,client_name,clients_names,message_list,client_connect,server_messages,server
clients=[]
client_name=" "
clients_names=[]
message_list = []
client_connect=[]
server_messages=[]
global connection

def server_vriables(conn):
    connection = conn
    return(connection)
def start_server():
    global server, host_addr, host_port 
    server=None
    host_addr="127.0.0.1"
    host_port=6537
    
   
    chatstart.config(state=tkinter.DISABLED)
    tkMessage.config(state=tkinter.NORMAL)
    chatstop.config(state=tkinter.NORMAL)
    
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # print (socket.AF_INET)
    # print (socket.SOCK_STREAM)
 
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 3)
   
    server.bind((host_addr,host_port))
    server.listen(5)
    server_vriables(server)
    threading._start_new_thread(accept_clients,(server," "))
    # print("many")
    lblHost["text"]="Host: " + host_addr
    lblPort["text"]="Port: " + str(host_port)
    
def stop_server():
    chatstart.config(state=tkinter.NORMAL)
    chatstop.config(state=tkinter.DISABLED)
    
def accept_clients(the_server, y):
    try:
        
    
        while True:
            conn,addr = the_server.accept()
            
            # print("hi")
            clients.append(conn)
           
            # client_connection.send(b"Welcome "+client_name +b". Use 'exit' to quit")
            # print(clients_names)
            threading._start_new_thread(send_receive_client_message,(conn,addr))
    except:
        print("i")
            


def send_receive_client_message(client_connection, client_ip_addr):
    global server, client_name, clients, client_addr,sending_client_name,B
    client_msg=" "
    client_connect.append(client_connection)
    # print(client_connection,client_ip_addr)
    client_name=client_connection.recv(4096)
    # print("message received by server")
    
    client_connection.send(b"Welcome "+client_name +b". Use 'exit' to quit\n")
    
    clients_names.append(client_name)
    # print(clients_names)
    time.sleep(0.1)
    for j in clients_names:
       


            client_connection.send(b"\n")
            client_connection.send(j)
    client_connection.send(b"\n")
    
    for c in clients:
            if c!=client_connection:
                c.send(b"\n"+clients_names[-1])

  
    update_client_names_display(clients_names)
    
    
    while True:
        data=client_connection.recv(4096)
        if not data: break
        if data == "exit" :break
                
        client_msg=data
        message_list.append(client_msg)
        # print(message_list)
        
       
            
        idx=get_client_index(clients, client_connection)
        sending_client_name=clients_names[idx]
        
        update_client_message_display(sending_client_name,client_msg)    
        for c in clients:
            if c!=client_connection:
                # client_connection.send(b"\n")
                c.send(sending_client_name + b'->' + client_msg +b'\n')
    
    idx=get_client_index(clients, client_connection)
    del clients_names[idx]
    del clients[idx]
    client_connection.close()
    
    update_client_names_display(clients_names)
    
def get_client_index(client_list,curr_client) :
    idx=0
    for conn in client_list:
        if conn== curr_client:
            break
        idx=idx+1
    return idx
def update_client_names_display(name_list):
    tkDisplay.config(state=tkinter.NORMAL)
    tkDisplay.delete('1.0',tkinter.END)
    
    for c in name_list:
        tkDisplay.insert(tkinter.END, c.decode("utf-8") +"\n")
    tkDisplay.config(state=tkinter.DISABLED)
    
                
def update_client_message_display(clients_name,message_list):
    TkDisplay.config(state=tkinter.NORMAL)
    TkDisplay.delete('1.0',tkinter.END)
    server_messages.append('{} -> {}'.format(clients_name.decode('utf-8'),message_list.decode('utf-8')))
    for j in range(len(server_messages)):
    
        # for c in range(len(clients_names)):
            TkDisplay .insert(tkinter.END, server_messages[j] +"\n")
    TkDisplay.config(state=tkinter.DISABLED)              


def getChatMessage(msg):
    msg=msg.replace('\n', '')
    texts=TkDisplay.get("1.0", tkinter.END).strip()
    send_message_to_clinets_from_server(msg)

    
    TkDisplay.config(state=tkinter.NORMAL)
    if len(texts)<1:
        TkDisplay.insert(tkinter.END,"You->"+ msg+"\n","tag_your_message")
    else:
        TkDisplay.insert(tkinter.END, "You->"+msg+"\n","tag_your_message")
        
    # TkDisplay.config(state=tkinter.DISABLED)
    
    TkDisplay.config(state=tkinter.DISABLED)

    # send_message_to_clinets_from_server(msg)

    TkDisplay.see(tkinter.END)
    tkMessage.delete('1.0',tkinter.END) 
    
def send_message_to_clinets_from_server(msg):
    server_messages.append("You" + '->' + msg)
    for c in clients:
            if c!=client_connect:
                # client_connection.send(b"\n")
                c.send(b"Chavi" + b'->' + msg.encode() +b'\n')          
                
                
def fileDialog():
    file=filedialog.askopenfile(mode ='r',title="select a file",filetype=[('Python Files', '*.py')])
    for c in file:
        if file is not None: 
            content = file.read() 
            T.insert(tkinter.END, content) 
    host_addr="127.0.0.1"
    host_port=6537
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 3)
    server.connect((host_addr,host_port))
    server.bind((host_addr,host_port))
    
    server.listen(5)
  
    server.send(b"get_ready_for_the_quiz")
    l = file.read(1024)

    while (l):
        server.send(l)
        l = file.read(1024)
    s.close() 
    

    
def closefile():
    T.delete('1.0', END)          
                
                
                
                
                
                
                
                
                
                
root.mainloop()

