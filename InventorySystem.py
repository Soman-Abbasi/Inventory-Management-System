import tkinter as tk
from tkinter import ttk, messagebox

from tkinter import PhotoImage

class Product:
    def __init__(self,product_id,name,price,quantity):
        self.product_id=product_id
        self.name=name
        self.price=price
        self.quantity=quantity

    def __str__(self):
        return  f"ID: {self.product_id:5} | Product Name: {self.name:15} | Price: {self.price:8.2f} | Quantity: {self.quantity:4}"

class Inventory:
    def __init__(self):
        self.products=[]
    def add_products(self,product):
        self.products.append(product)
        return f"Product '{product.name}' added successfully."
    def remove_products(self,product_id):
        for product in self.products:
            if product.product_id==product_id:
                self.products.remove(product)
                return f"Product '{product.name}' removed successfully."
        return f"Product with ID '{product_id} not found. '"

    def update_products(self,product_id,new_quantity=None,new_price=None,new_name=None):
        for product in self.products:
            if product.product_id==product_id:
                if new_quantity is not None:
                    product.quantity=new_quantity
                if new_price is not None:
                    product.price=new_price
                if new_name is not None:
                    product.name=new_name
                return f" Product '{product.name}' Updated Successfully. "

            return f"Product with ID '{product_id}' not found."
    def view_inventory(self):
        if not self.products:
            return f"Inventory is empty."
        # return "\n".join(str(product) for product in sorted(self.products,key=lambda x: x.product_id))
        return "\n".join(str(product) for product in sorted(self.products,key=lambda x: x.product_id))


class InventoryApp:
    def __init__(self,root):
        self.root=root
        self.inventory=Inventory()
        self.setup_theme()
        self.setup_gui()

    def setup_theme(self):
        self.bg_color = "#f5f7fa"
        self.primary_color = "#2c7be5"
        self.success_color = "#00d97e"
        self.danger_color = "#e63757"
        self.warning_color = "#f6c343"
        self.text_color = "#12263f"
        self.card_bg = "#ffffff"
        self.border_color = "#e3ebf6"

        style=ttk.Style()
        style.theme_use('alt')    #Theme name
        #Main Frame
        style.configure('Main.TFrame',background=self.bg_color)
        #Card Frame Style
        style.configure('Card.TFrame',background=self.card_bg,relief='flat',borderwidth=0)
        #Label Styles
        style.configure('Title.TLabel',font=('Segoe UI',24,'bold'),foreground=self.text_color,background=self.bg_color)
        style.configure('CardTitle.TLabel',font=('Segoe UI',18,'bold'),foreground=self.primary_color,background=self.card_bg)
        style.configure('SubTitle.TLabel',font=('Segoe UI',12,'bold'),foreground="#6e84a3",background=self.bg_color)
        style.configure('Regular.TLabel',font=('Segoe UI',10,'bold'),foreground=self.text_color,background=self.card_bg)

        #Buttons Style
        button_font=font=('Segoe UI',10,'bold')
        button_padding=10

        style.configure('Primary.TButton',foreground='white',font=button_font,background=self.primary_color,
                        borderwidth=0,focusthickness=3,focuscolor='none',padding=button_padding)
        style.map('Primary.TButton',
                  background=[('active', '#1a68d1'),#Darker when hovered
                ('pressed', '#1658b8')]) #Even Darker when clicked

        style.configure('Success.TButton',
                        foreground='white',font=button_font,background=self.success_color,
                        borderwidth=0,focusthickness=3,focuscolor='none',padding=button_padding)
        style.map('Success.TButton',background=([('active', '#00c571'), ('pressed', '#00b168')]))

        style.configure('Danger.TButton',
                        font=button_font,
                        foreground='white',
                        background=self.danger_color,
                        borderwidth=0,
                        focusthickness=3,
                        focuscolor='none',
                        padding=button_padding)
        style.map('Danger.TButton',
                  background=[('active', '#d42d4d'), ('pressed', '#c22743')])

        style.configure('Warning.TButton',
                        font=button_font,
                        foreground='white',
                        background=self.warning_color,
                        borderwidth=0,
                        focusthickness=3,
                        focuscolor='none',
                        padding=button_padding)
        style.map('Warning.TButton',
                  background=[('active', '#e5b53d'), ('pressed', '#d4a938')])

        style.configure('Secondary.TButton',
                        font=('Segoe UI', 10),
                        foreground=self.text_color,
                        background='#edf2f9',
                        borderwidth=0,
                        focusthickness=3,
                        focuscolor='none',
                        padding=8)
        style.map('Secondary.TButton',
                  background=[('active', '#d8e2f3'), ('pressed', '#c5d4ec')])

        #Entry Style
        style.configure('TEntry',
                        font=('Segoe UI',10),
                        foreground=self.text_color,
                        fieldbackground='white',
                        bordercolor=self.border_color,
                        lightcolor=self.border_color,
                        darkcolor=self.border_color,
                        padding=8
                        )
        #Text Widget Style
        style.configure('TText',
                        font=('Consolas',10),
                        foreground=self.text_color,
                        background='white',
                        relief='flat')


    def setup_gui(self):
        self.clear_windows()
        self.main_frame=ttk.Frame(self.root,style='Main.TFrame')
        self.main_frame.pack(fill=tk.BOTH,expand=True)
        #Center Container for main contents
        center_frame=ttk.Frame(self.main_frame,style='Main.TFrame')
        center_frame.place(relx=0.5,rely=0.5,anchor='center')

        header_frame=ttk.Frame(center_frame,style='Main.TFrame')
        header_frame.pack(pady=(0,30))

        ttk.Label(header_frame,text="Inventory Management System",style='Title.TLabel').pack()
        ttk.Label(header_frame,text="Manage your products and stock efficiently",style='SubTitle.TLabel').pack()

        #Menu Buttons Card
        card_frame=ttk.Frame(center_frame,style='Card.TFrame',padding=30)
        card_frame.pack()

        self.add_icon=PhotoImage(file="icons/add.png")
        add_btn = ttk.Button(card_frame,
                             text="Add Product",
                             image=self.add_icon,
                             compound='left',
                             command=self.show_add_product,
                             style="Primary.TButton",
                             width=20)
        add_btn.pack(fill=tk.X, pady=8)

        # Create Remove Product button
        self.remove_icon = PhotoImage(file="icons/remove.png")
        remove_btn = ttk.Button(card_frame,
                                text="Remove Product",
                                image=self.remove_icon,
                                compound='left',
                                command=self.show_remove_product,
                                style="Danger.TButton",
                                width=20)
        remove_btn.pack(fill=tk.X, pady=8)

        # Create Update Product button
        self.update_icon = PhotoImage(file="icons/update.png")
        update_btn = ttk.Button(card_frame,
                                text="Update Product",
                                image=self.update_icon,
                                compound='left',
                                command=self.show_update_product,
                                style="Warning.TButton",
                                width=20)
        update_btn.pack(fill=tk.X, pady=8)
        self.view_icon = PhotoImage(file="icons/view.png")
        view_btn=ttk.Button(card_frame,
                            text="View Inventory",
                            image=self.view_icon,
                            compound='left',

                            command=self.show_inventory,width=20,
                            style="Success.TButton")
        view_btn.pack(fill=tk.X,pady=8)

        exit_frame=ttk.Frame(center_frame,style='Main.TFrame',padding=(0,20,0,0))
        exit_frame.pack()
        self.exit_icon = PhotoImage(file="icons/exit.png")
        ttk.Button(
            exit_frame,text="Exit System",
            image=self.exit_icon,
            compound='left',
            command=self.root.quit,style='Secondary.TButton'
        ).pack()

    def show_add_product(self):
        self.clear_windows()
        main_frame=ttk.Frame(self.root,style='Main.TFrame')
        main_frame.pack(fill=tk.BOTH,expand=True)

        header_frame=ttk.Frame(main_frame,style='Main.TFrame',padding=(30,20,30,10)) #left,top,right,bottom
        header_frame.pack(fill=tk.X)

        ttk.Label(header_frame,text="Add New Products",style='SubTitle.TLabel').pack(side=tk.LEFT)

        self.back_icon=PhotoImage(file='icons/back.png')
        ttk.Button(header_frame,text="Back to Menu",
                   image=self.back_icon,
                   compound='left',
                   command=self.setup_gui,style='Secondary.TButton').pack(side=tk.RIGHT)

        form_card=ttk.Label(main_frame,style='Card.TFrame',padding=30)
        form_card.pack(fill=tk.BOTH,expand=True,padx=30,pady=(0,30))

        product_id_frame=ttk.Frame(form_card,style='Card.TFrame')
        product_id_frame.pack(fill=tk.X,pady=5)

        ttk.Label(product_id_frame,text="Product ID: ",width=15,style='Regular.TLabel').pack(side=tk.LEFT,padx=(0,10))
        self.product_id_entry=ttk.Entry(product_id_frame,style='TEntry')
        self.product_id_entry.pack(side=tk.LEFT,fill=tk.X,expand=True)

        #Product Name
        product_name_frame=ttk.Frame(form_card,style='Card.TFrame')
        product_name_frame.pack(fill=tk.X,pady=5)

        ttk.Label(product_name_frame,text="Product Name: ",style='Regular.TLabel',width=15).pack(side=tk.LEFT,padx=(0,10))
        self.product_name_entry=ttk.Entry(product_name_frame,style='TEntry')
        self.product_name_entry.pack(side=tk.LEFT,fill=tk.X,expand=True)

        #Product Price
        product_price_frame = ttk.Frame(form_card, style='Card.TFrame')
        product_price_frame.pack(fill=tk.X, pady=5)

        ttk.Label(product_price_frame, text="Product Price: ", style='Regular.TLabel', width=15).pack(side=tk.LEFT,
                                                                                                    padx=(0, 10))
        self.product_price_entry = ttk.Entry(product_price_frame, style='TEntry')
        self.product_price_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        #Product Quantity
        product_quantity_frame = ttk.Frame(form_card, style='Card.TFrame')
        product_quantity_frame.pack(fill=tk.X, pady=5)

        ttk.Label(product_quantity_frame, text="Quantity : ", style='Regular.TLabel', width=15).pack(side=tk.LEFT,
                                                                                                     padx=(0, 10))
        self.product_quantity_entry = ttk.Entry(product_quantity_frame, style='TEntry')
        self.product_quantity_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        #Save Buttons
        self.save_icon=PhotoImage(file='icons/save.png')
        btn_frame=ttk.Frame(form_card,style='Card.TFrame',padding=(0,20,0,0))
        btn_frame.pack(fill=tk.X)

        ttk.Button(btn_frame,text="Save Button",
                   image=self.save_icon,
                   compound='left',
                   style='Success.TButton',command=self.save_products).pack()
    def save_products(self):
        try:
            product_id=self.product_id_entry.get().strip()
            name=self.product_name_entry.get()
            price=float(self.product_price_entry.get())
            quantity=int(self.product_quantity_entry.get())
            if not all([product_id,name]):
                messagebox.showerror("Error","All fields are required. ")

                return
            product=Product(product_id,name,price,quantity)
            result=self.inventory.add_products(product)
            messagebox.showinfo("Success",result)
            self.setup_gui()


        except ValueError:
            messagebox.showerror("Error","Please enter valid numbers for price and quantity! ")



    def show_remove_product(self):
        self.clear_windows()

        main_frame=ttk.Frame(self.root,style='Main.TFrame')
        main_frame.pack(fill=tk.BOTH,expand=True)

        header_frame=ttk.Frame(main_frame,style='Main.TFrame',padding=(30,20,30,10))
        header_frame.pack(fill=tk.X)

        ttk.Label(header_frame,text="Remove Product",style='SubTitle.TLabel').pack(side=tk.LEFT)


        self.back_icon=PhotoImage(file='icons/back.png')
        ttk.Button(header_frame,text="Back to Menu",
                   image=self.back_icon,
                   compound='left',
                   command=self.setup_gui,style='Secondary.TButton').pack(side=tk.RIGHT)

        form_card=ttk.Frame(main_frame,style='Card.TFrame',padding=30)
        form_card.pack(fill=tk.BOTH,expand=True,padx=30,pady=(0,30))


        product_id_frame=ttk.Frame(form_card,style='Card.TFrame')
        product_id_frame.pack(fill=tk.X,pady=5)

        ttk.Label(product_id_frame,text="Product ID: ",style='Regular.TLabel',width=15).pack(side=tk.LEFT,padx=(0,10))

        self.product_id_entry = ttk.Entry(product_id_frame,style='TEntry')
        self.product_id_entry.pack(side=tk.LEFT,fill=tk.X,expand=True)

        btn_frame=ttk.Frame(form_card,padding=(0,20,0,0),style='Card.TFrame')
        btn_frame.pack(fill=tk.X)

        self.remove_icon = PhotoImage(file="icons/remove.png")
        ttk.Button(btn_frame,text="Remove Product ",
                   image=self.remove_icon,
                   compound='left',
                   command=self.remove_product,style='Danger.TButton').pack()

    def remove_product(self):
        product_id=self.product_id_entry.get()
        if not product_id:
            messagebox.showerror("Error","Please enter a product ID!")
            return
        result=self.inventory.remove_products(product_id)
        messagebox.showinfo("Success",result)
        self.setup_gui()

    def show_update_product(self):
        self.clear_windows()

        main_frame = ttk.Frame(self.root, style='Main.TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True)

        header_frame = ttk.Frame(main_frame, style='Main.TFrame', padding=(30, 20, 30, 10))
        header_frame.pack(fill=tk.X)

        ttk.Label(header_frame, text="Update Product", style='SubTitle.TLabel').pack(side=tk.LEFT)


        self.back_icon=PhotoImage(file='icons/back.png')
        ttk.Button(header_frame,text="Back to Menu",
                   image=self.back_icon,
                   compound='left',
                   command=self.setup_gui,style='Secondary.TButton').pack(side=tk.RIGHT)

        form_card = ttk.Frame(main_frame, style='Card.TFrame', padding=30)
        form_card.pack(fill=tk.BOTH, expand=True, padx=30, pady=(0, 30))

        product_id_frame = ttk.Frame(form_card, style='Card.TFrame')
        product_id_frame.pack(fill=tk.X, pady=5)
        ttk.Label(product_id_frame, text="Product ID: *", width=15, style='Regular.TLabel').pack(side=tk.LEFT,
                                                                                                 padx=(0, 10))
        self.product_id_entry = ttk.Entry(product_id_frame, style='TEntry')
        self.product_id_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.search_icon=PhotoImage(file='icons/search.png')
        fetch_frame = ttk.Frame(form_card, style='Card.TFrame')
        fetch_frame.pack(fill=tk.X, pady=5)
        ttk.Button(fetch_frame,
                   text="Fetch Product Details",
                   image=self.search_icon,
                   compound='left',
                   command=self.fetch_product_details,
                   style='Secondary.TButton').pack()

        product_name_frame = ttk.Frame(form_card, style='Card.TFrame')
        product_name_frame.pack(fill=tk.X, pady=5)
        ttk.Label(product_name_frame, text="New Name:", style='Regular.TLabel', width=15).pack(side=tk.LEFT,
                                                                                               padx=(0, 10))
        self.product_name_entry = ttk.Entry(product_name_frame, style='TEntry')
        self.product_name_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        product_price_frame = ttk.Frame(form_card, style='Card.TFrame')
        product_price_frame.pack(fill=tk.X, pady=5)
        ttk.Label(product_price_frame, text="New Price:", style='Regular.TLabel', width=15).pack(side=tk.LEFT,
                                                                                                 padx=(0, 10))
        self.product_price_entry = ttk.Entry(product_price_frame, style='TEntry')
        self.product_price_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Product Quantity (optional)
        product_quantity_frame = ttk.Frame(form_card, style='Card.TFrame')
        product_quantity_frame.pack(fill=tk.X, pady=5)
        ttk.Label(product_quantity_frame, text="New Quantity:", style='Regular.TLabel', width=15).pack(side=tk.LEFT,
                                                                                                       padx=(0, 10))
        self.product_quantity_entry = ttk.Entry(product_quantity_frame, style='TEntry')
        self.product_quantity_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Update button
        btn_frame = ttk.Frame(form_card, style='Card.TFrame', padding=(0, 20, 0, 0))
        btn_frame.pack(fill=tk.X)
        self.update_icon=PhotoImage(file='icons/update.png')
        ttk.Button(btn_frame,
                   text="Update Product",
                   image=self.update_icon,
                   compound='left',
                   command=self.update_product,
                   style='Warning.TButton').pack()

    def fetch_product_details(self):
        product_id = self.product_id_entry.get().strip()
        if not product_id:
            messagebox.showerror("Error", "Please enter a Product ID first")
            return

        # Find the product in inventory
        for product in self.inventory.products:
            if product.product_id == product_id:

                self.product_name_entry.delete(0, tk.END)
                self.product_name_entry.insert(0, product.name)

                self.product_price_entry.delete(0, tk.END)
                self.product_price_entry.insert(0, str(product.price))

                self.product_quantity_entry.delete(0, tk.END)
                self.product_quantity_entry.insert(0, str(product.quantity))
                return

        messagebox.showerror("Error", f"Product with ID {product_id} not found")

    def update_product(self):
        product_id = self.product_id_entry.get().strip()
        if not product_id:
            messagebox.showerror("Error", "Product ID is required!")
            return

        new_name = self.product_name_entry.get().strip() or None
        new_price = self.product_price_entry.get().strip()
        new_quantity = self.product_quantity_entry.get().strip()

        # Check if at least one field is being updated
        if all(not value for value in [new_name, new_price, new_quantity]):
            messagebox.showerror("Error", "No changes provided! Please fill at least one field to update.")
            return

        try:
            new_price = float(new_price) if new_price else None
            new_quantity = int(new_quantity) if new_quantity else None
        except ValueError:
            messagebox.showerror("Error", "Price must be a number and quantity must be an integer!")
            return

        # Call update method
        result = self.inventory.update_products(
            product_id,
            new_quantity=new_quantity,
            new_price=new_price,
            new_name=new_name
        )

        messagebox.showinfo("Success", result)
        self.setup_gui()

    def update_products(self, product_id, new_quantity=None, new_price=None, new_name=None):
        for product in self.products:
            if product.product_id == product_id:
                if new_quantity is not None:
                    product.quantity = new_quantity
                if new_price is not None:
                    product.price = new_price
                if new_name is not None:
                    product.name = new_name
                return f"Product '{product.name}' Updated Successfully."
        return f"Product with ID '{product_id}' not found."


    def show_inventory(self):
        self.clear_windows()
        main_frame=ttk.Frame(self.root,style='Main.TFrame')
        main_frame.pack(fill=tk.BOTH,expand=True)

        header_frame=ttk.Frame(main_frame,style='Main.TFrame',padding=(30,20,30,10))
        header_frame.pack(fill=tk.X)

        ttk.Label(header_frame,text="Current Inventory",style='SubTitle.TLabel').pack(side=tk.LEFT)


        self.back_icon=PhotoImage(file='icons/back.png')
        ttk.Button(header_frame,text="Back to Menu",
                   image=self.back_icon,
                   compound='left',
                   command=self.setup_gui,style='Secondary.TButton').pack(side=tk.RIGHT)


        form_card=ttk.Label(main_frame,style='Card.TFrame',padding=20)
        form_card.pack(fill=tk.BOTH,expand=True,padx=30,pady=(0,30))

        inventory_txt=self.inventory.view_inventory()
        #Frame for txt widget and scrollbar
        txt_frame=ttk.Frame(form_card,style='Card.TFrame')
        txt_frame.pack(fill=tk.BOTH,expand=True)

        txt_widget=tk.Text(txt_frame,
                           wrap=tk.WORD,
                           font=('Consolas',10),
                           width=80,
                           height=20,
                           bg=self.card_bg,
                           fg=self.text_color,
                           padx=10,
                           pady=10,
                           borderwidth=0,
                           relief='flat')
        txt_widget.insert(tk.END,inventory_txt)
        txt_widget.config(state=tk.DISABLED)
        txt_widget.pack(expand=True,fill=tk.BOTH,side=tk.LEFT)

        scrollbar=ttk.Scrollbar(txt_frame,orient=tk.VERTICAL,command=txt_widget.yview)
        txt_widget.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT,fill=tk.Y)


    def clear_windows(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__=="__main__":
    root=tk.Tk()
    root.title("Inventory Management System")
    root.state('zoomed')


    app=InventoryApp(root)
    root.mainloop()

