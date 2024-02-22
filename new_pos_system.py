#-----------------now i will work on details frame----------------------

#here first I will make four rows and two column in my details frame

details_frame.rowconfigure(0,weight =1,uniform="a")
details_frame.rowconfigure(1,weight =1,uniform="a")
details_frame.rowconfigure(2,weight =1,uniform="a")
details_frame.rowconfigure(3,weight =1,uniform="a")
details_frame.columnconfigure(0,weight =1,uniform="a")
details_frame.columnconfigure(1,weight =1,uniform="a")

#now i will place widgets in details frame
#putting widgets in order detail frame

order_detail_frame.grid(row=0, column=0, columnspan=2,pady=10)
customer_detail_frame.grid(row=2, column=0,columnspan=2)

#configiring  order detail frame
order_detail_frame.columnconfigure(0,weight =1)
order_detail_frame.rowconfigure(0,weight =1)
order_detail_frame.rowconfigure(1,weight =1)

#configuring customer detail frame
customer_detail_frame.columnconfigure(0, weight=1,)
customer_detail_frame.rowconfigure(0, weight=1,)
customer_detail_frame.rowconfigure(1, weight=1,)

#griding widgets in order details frame

enter_product.grid(row=1, column=0,pady=10,padx=6)
enter_quantity.grid(row=2, column=0,pady=10,padx=6)

#griding button in  details frame

add_to_cart_button.grid(row=1, column=0,sticky=E,pady=10,padx=6)
total_button.grid(row=1, column=1,sticky=W,pady=10,padx=6)

#griding widgets in customer details frame
customer_name.grid(row=0, column=0,pady=10,padx=6)
customer_number.grid(row=1, column=0,pady=10,padx=6)
#griding button in customer details frame
print_bill_button.grid(row=3, column=0, columnspan=2)
#-----------------details frame done------------------

#-----------------now i will work on cart frame----------------------

#first i will make two rows and one columns in my cart frame
cart_frame.rowconfigure(0,weight =1)
cart_frame.rowconfigure(1,weight =5)
cart_frame.rowconfigure(2,weight =5)
cart_frame.columnconfigure(0,weight =1)
#now i will place widgets in cart frame
cart_label.grid(row=0, column=0,)
cart_listbox.grid(row=1, column=0,)
bill_label.grid(row=2, column=0,)



#-----------------cart frame done------------------


#-----------------now i will work on bill box ------------------


#bill box done

bill_frame.rowconfigure(0,weight =1,uniform="a")
bill_frame.rowconfigure(1,weight =5,uniform="a")
bill_frame.columnconfigure(0,weight =1,uniform="a")
#now i will place widgets in cart frame
bill_label.grid(row=0, column=0,)


#now i will do in last cse buttons

cse_button_frame.columnconfigure(0,weight=1,uniform="a")
cse_button_frame.columnconfigure(1,weight=1,uniform="a")
cse_button_frame.columnconfigure(2,weight=1,uniform="a")
cse_button_frame.rowconfigure(0,weight=1)

clear_button.grid(row=0, column=0,padx=7, sticky=tkinter.EW)
save_button.grid(row=0, column=1,padx=7, sticky=tkinter.EW)

exit_button.grid(row=0, column=2,padx=7, sticky=tkinter.EW)

# Start the main loop

root.mainloop()
#lets make a function that will show output from entry box when i click button