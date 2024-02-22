bill_label = customtkinter.CTkLabel(bill_frame,
    text ="Bill",
    font=('times new roman',30,'bold'),
  text_color='yellow',)


bill_frame.rowconfigure(0,weight =1,uniform="a")
bill_frame.rowconfigure(1,weight =5,uniform="a")
bill_frame.columnconfigure(0,weight =1,uniform="a")
#now i will place widgets in cart frame
bill_label.grid(row=0, column=0,)