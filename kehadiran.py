def tampilan_button():
    return Button(root, text="click here", command=my_click,
                  fg="black", bg="skyblue").pack()


def my_click():
    my_label = Label(root, text="hello").pack()