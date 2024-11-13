from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from twilio.rest import Client

# Existing code...

class Bill_app:
    # Existing methods...

    def generate_bill(self):
        total_bill = self.calculate_total_bill()
        customer_mobile_number = self.c_phon.get()
        self.send_bill_via_sms(customer_mobile_number, total_bill)
        self.send_bill()

    def calculate_total_bill(self):
        # Implement your logic to calculate the total bill here
        # For example:
        price = float(self.prices.get())
        quantity = int(self.qty.get())
        subtotal = price * quantity
        tax = 0.1 * subtotal
        total = subtotal + tax
        return total

    def send_bill_via_sms(self, mobile_number, total_bill):
        account_sid = 'your_account_sid'
        auth_token = 'your_auth_token'
        client = Client(account_sid, auth_token)
        bill_number = random.randint(10000, 99999)
        message_body = f"Your total bill amount is {total_bill}. Bill number: {bill_number}"
        message = client.messages.create(
            body=message_body,
            from_='your_twilio_phone_number',
            to=mobile_number
        )
        print("Bill sent successfully via SMS!")

    def send_bill(self):
        mobile_number = self.c_phon.get()
        email = self.c_email.get()
        total_bill = self.AmountTotal_2.get()
        sender_email = "your_email@example.com"
        sender_password = "your_password"
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = "Your Bill Details"
        body = f"Dear Customer,\n\nYour total bill is: {total_bill}.\n\nThank you for shopping with us!"
        msg.attach(MIMEText(body, 'plain'))
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, email, text)
            server.quit()
            print("Bill sent successfully via email!")
        except Exception as e:
            print(f"Failed to send bill via email: {str(e)}")

    def clear_all(self):
        self.C_name.set("")
        self.c_phon.set("")
        self.c_email.set("")
        self.search_bill.set("")
        self.combo_Category.current(0)
        self.combo_Subcategory.set("")
        self.comboProduct.set("")
        self.prices.set("")
        self.qty.set(0)
        self.EntrySubTotal.delete(0, END)
        self.lbl_tax_value.delete(0, END)
        self.AmountTotal_2.delete(0, END)
        self.textarea.delete("1.0", END)

    def save_bill(self):
        # Placeholder for saving bill details to a file
        pass

    def print_bill(self):
        # Placeholder for printing bill
        pass

    def exit_app(self):
        # Exit application
        self.root.destroy()

    # Existing code...

class Bill_app:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Billing Software")

        # =================Variable===================
        self.C_name = StringVar()
        self.c_phon = StringVar()
        self.c_email = StringVar()
        self.search_bill = StringVar()
        z = random.randint(1000, 9999)
        self.bill_no = StringVar()
        self.bill_no.set(str(z))
        self.product = StringVar()
        self.prices = StringVar()
        self.qty = IntVar()
        self.sub_total = StringVar()
        self.tax_input = StringVar()
        self.total = StringVar()

        # Product Categories List
        self.Category = ["Select Option", "Clothing", "LifeStyle", "Mobiles"]

        # SubCatClothing
        self.SubCatClothing = ["Jeans", "Shirt", "T-Shirt", "Trouser"]
        self.Jeans = ["Levis", "Wrangler", "Spyker", "Mufti", "Tommy Hilfiger", "Calvin Klein", "Pepe Jeans"]
        self.price_dict = {
            "Levis": 3000, "Wrangler": 2500, "Spyker": 2000, "Mufti": 5500,
            "Tommy Hilfiger": 3000, "Calvin Klein": 2800, "Pepe Jeans": 2500,
            "Spyker_Shirt": 4000, "Mufti_Shirt": 1200, "Tommy Hilfiger_Shirt": 2000, "Roadster_Shirt": 500, "Polo_Shirt": 1300,
            "Spyker_TShirt": 800, "Mufti_TShirt": 1200, "Tommy Hilfiger_TShirt": 1600, "Roadster_TShirt": 500, "Polo_TShirt": 1300,
            "Spyker_Trouser": 1699, "Mufti_Trouser": 1299, "Tommy Hilfiger_Trouser": 1600, "Roadster_Trouser": 400, "Polo_Trouser": 1300,
            "LifeBoy": 20, "Dove": 45, "Lux": 30, "Pears": 40, "Dettol": 30,
            "Fair&Lovely": 50, "Dove_Cream": 110, "Jhonson Baby": 80, "Ponds": 60, "Beardo": 150,
            "Parachute": 50, "Jashmine": 110, "Bajaj": 150,
            "S23 Ultra": 150000, "S24 Ultra": 190000, "A73": 70000, "A53": 55000,
            "vivo V29 5G": 50000, "vivo X80 Pro": 79999, "vivo X100 Pro": 90000, "vivo X100": 60000,
            "Realme X2 Pro": 50000, "Realme GT Neo 3": 50000, "Realme GT 2 Pro": 45000, "Realme X50 Pro 5G": 39999,
            "OnePlus 11 5G": 50000, "OnePlus 12": 80000, "OnePlus Open": 110000
        }

        # SubCatLifeStype
        self.SubCatLifeStyle = ["Bath Soap", "Face Cream", "Hair Oil"]
        self.BathSoap = ["LifeBoy", "Dove", "Lux", "Pears", "Dettol"]
        self.FaceCream = ["Fair&Lovely", "Dove", "Jhonson Baby", "Ponds", "Beardo"]
        self.HairOil = ["Parachute", "Jashmine", "Jhonson Baby", "Bajaj"]

        # SubCatMobiles
        self.SubCatMobiles = ["Samsung", "Vivo", "Realme", "Oneplus"]
        self.Samsung = ["S23 Ultra", "S24 Ultra", "A73", "A53"]
        self.Vivo = ["vivo V29 5G", "vivo X80 Pro", "vivo X100 Pro", "vivo X100"]
        self.Realme = ["Realme X2 Pro", "Realme GT Neo 3", "Realme GT 2 Pro", "Realme X50 Pro 5G"]
        self.Oneplus = ["OnePlus 11 5G", "OnePlus 12", "OnePlus Open"]

        # Load data from CSV
        self.load_data()

        # Image1
        img = Image.open("image/Nart.jpg")
        img = img.resize((600, 230))
        self.photoimg = ImageTk.PhotoImage(img)

        lbl_image = Label(self.root, image=self.photoimg)
        lbl_image.place(x=0, y=0, width=600, height=230)

        # Image2
        img_1 = Image.open("image/GROCER.jpeg")
        img_1 = img_1.resize((600, 230))
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        lbl_img_1 = Label(self.root, image=self.photoimg_1)
        lbl_img_1.place(x=500, y=0, width=600, height=230)

        # Image3
        img_2 = Image.open("image/Walmart.jpg")
        img_2 = img_2.resize((600, 230))
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        lbl_img_2 = Label(self.root, image=self.photoimg_2)
        lbl_img_2.place(x=1000, y=0, width=600, height=230)

        lbl_title = Label(self.root, text="BILLING SOFTWARE USING PYTHON", font=("times new roman", 35, "bold"), bg="white", fg="red")
        lbl_title.place(x=0, y=130, width=1920, height=45)

        Main_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="White")
        Main_Frame.place(x=0, y=175, width=1920, height=620)

        # Product LabelFrame
        Product_Frame = LabelFrame(Main_Frame, text="Product", font=("times new roman", 12, "bold"), bg="white", fg="red")
        Product_Frame.place(x=370, y=500, width=500, height=140)

        # Category
        self.lblCategory = Label(Product_Frame, font=('arial', 12, 'bold'), bg="white", text="Select Categories", bd=4)
        self.lblCategory.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.Combo_Category = ttk.Combobox(Product_Frame, value=self.Category, font=('arial', 10, 'bold'), width=24, state="readonly")
        self.Combo_Category.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>", self.Categories)

        # SubCategory
        self.lblSubCategory = Label(Product_Frame, font=('arial', 12, 'bold'), bg="white", text="Subcategories", bd=4)
        self.lblSubCategory.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.Combo_Subcategory = ttk.Combobox(Product_Frame, state="readonly", font=('arial', 10, 'bold'), width=24)
        self.Combo_Subcategory.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.Combo_Subcategory.bind("<<ComboboxSelected>>", self.Product_add)

        # Product Name
        self.lblProduct = Label(Product_Frame, font=('arial', 12, 'bold'), bg="white", text="Select Product", bd=4)
        self.lblProduct.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.comboProduct = ttk.Combobox(Product_Frame, state="readonly", font=('arial', 10, 'bold'), width=24)
        self.comboProduct.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.comboProduct.bind("<<ComboboxSelected>>", self.price)

        # Price
        self.lblPrice = Label(Product_Frame, font=('arial', 12, 'bold'), bg="white", text="Price", bd=4)
        self.lblPrice.grid(row=0, column=2, sticky=W, padx=5, pady=2)

        self.comboPrice = ttk.Combobox(Product_Frame, state="readonly", font=('arial', 10, 'bold'), width=24)
        self.comboPrice.grid(row=0, column=3, sticky=W, padx=5, pady=2)

        # Quantity
        self.lblQty = Label(Product_Frame, font=('arial', 12, 'bold'), bg="white", text="Quantity", bd=4)
        self.lblQty.grid(row=1, column=2, sticky=W, padx=5, pady=2)

        self.qty = Entry(Product_Frame, font=('arial', 10, 'bold'), width=24)
        self.qty.grid(row=1, column=3, sticky=W, padx=5, pady=2)

        # Customer
        Customer_Frame = LabelFrame(Main_Frame, text="Customer", font=("times new roman", 12, "bold"), bg="white", fg="red")
        Customer_Frame.place(x=10, y=5, width=350, height=140)

        self.lblCustName = Label(Customer_Frame, text="Customer Name", font=("times new roman", 12, "bold"), bg="white", fg="black")
        self.lblCustName.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.txtCustName = Entry(Customer_Frame, textvariable=self.C_name, font=("times new roman", 12, "bold"), width=24)
        self.txtCustName.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.lblCustPhone = Label(Customer_Frame, text="Phone No.", font=("times new roman", 12, "bold"), bg="white", fg="black")
        self.lblCustPhone.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.txtCustPhone = Entry(Customer_Frame, textvariable=self.c_phon, font=("times new roman", 12, "bold"), width=24)
        self.txtCustPhone.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.lblCustEmail = Label(Customer_Frame, text="Email", font=("times new roman", 12, "bold"), bg="white", fg="black")
        self.lblCustEmail.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txtCustEmail = Entry(Customer_Frame, textvariable=self.c_email, font=("times new roman", 12, "bold"), width=24)
        self.txtCustEmail.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        # Bill Area
        self.bill_area = Text(self.root, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.bill_area.place(x=1500, y=175, width=420, height=400)

        # Button Frame
        Btn_Frame = Frame(Main_Frame, bd=5, relief=GROOVE, bg="white")
        Btn_Frame.place(x=370, y=650, width=1000, height=90)

        self.btnAddToCart = Button(Btn_Frame, text="Add To Cart", command=self.add_item, font=("times new roman", 14, "bold"), bg="orange", fg="black")
        self.btnAddToCart.grid(row=0, column=0, padx=10, pady=10)

        self.btnGenerateBill = Button(Btn_Frame, text="Generate Bill", command=self.generate_bill, font=("times new roman", 14, "bold"), bg="blue", fg="black")
        self.btnGenerateBill.grid(row=0, column=1, padx=10, pady=10)

        self.btnSaveBill = Button(Btn_Frame, text="Save Bill", command=self.save_bill, font=("times new roman", 14, "bold"), bg="green", fg="black")
        self.btnSaveBill.grid(row=0, column=2, padx=10, pady=10)

        self.btnPrint = Button(Btn_Frame, text="Print", command=self.print_bill, font=("times new roman", 14, "bold"), bg="purple", fg="black")
        self.btnPrint.grid(row=0, column=3, padx=10, pady=10)

        self.btnClear = Button(Btn_Frame, text="Clear", command=self.clear_data, font=("times new roman", 14, "bold"), bg="red", fg="black")
        self.btnClear.grid(row=0, column=4, padx=10, pady=10)

        self.btnExit = Button(Btn_Frame, text="Exit", command=self.root.destroy, font=("times new roman", 14, "bold"), bg="red", fg="black")
        self.btnExit.grid(row=0, column=5, padx=10, pady=10)

    def Categories(self, event=""):
        if self.Combo_Category.get() == "Clothing":
            self.Combo_Subcategory.config(value=self.SubCatClothing)
        elif self.Combo_Category.get() == "LifeStyle":
            self.Combo_Subcategory.config(value=self.SubCatLifeStyle)
        elif self.Combo_Category.get() == "Mobiles":
            self.Combo_Subcategory.config(value=self.SubCatMobiles)

    def Product_add(self, event=""):
        selected_subcat = self.Combo_Subcategory.get()
        products = []
        if selected_subcat in ["Jeans", "Shirt", "T-Shirt", "Trouser"]:
            products = getattr(self, selected_subcat)
        elif selected_subcat in ["Bath Soap", "Face Cream", "Hair Oil"]:
            products = getattr(self, selected_subcat.replace(" ", ""))
        elif selected_subcat in ["Samsung", "Vivo", "Realme", "Oneplus"]:
            products = getattr(self, selected_subcat)
        
        self.comboProduct.config(value=products)

    def price(self, event=""):
        selected_product = self.comboProduct.get()
        if selected_product in self.price_dict:
            self.comboPrice.config(value=[self.price_dict[selected_product]])

    def add_item(self):
        product = self.comboProduct.get()
        qty = int(self.qty.get())
        price = self.price_dict[product]
        total = price * qty
        self.bill_area.insert(END, f"\n{product}\t\t{qty}\t\t{price}\t\t{total}")
        self.update_total()

    def update_total(self):
        self.bill_area.insert(END, "\n\n=====================================")
        self.bill_area.insert(END, f"\nTotal Amount:\t\t\t\t{self.calculate_total()}")

    def calculate_total(self):
        total = 0
        for line in self.bill_area.get(1.0, END).split('\n'):
            if line:
                total += float(line.split('\t')[-1])
        return total

    def generate_bill(self):
        self.bill_area.insert(END, "\n\nThank you for shopping with us!")
        self.send_email()

    def save_bill(self):
        pass  # Implement bill saving

    def print_bill(self):
        pass  # Implement bill printing

    def clear_data(self):
        self.bill_area.delete(1.0, END)
        self.C_name.set("")
        self.c_phon.set("")
        self.c_email.set("")
        self.bill_no.set(str(random.randint(1000, 9999)))

    def load_data(self):
        with open("product_data.csv", newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self.price_dict[row[0]] = float(row[1])

    def send_email(self):
        from_address = "your_email@example.com"
        to_address = self.c_email.get()
        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = "Your Bill from Grocery Store"
        
        body = f"Hello {self.C_name.get()},\n\nHere is your bill:\n" + self.bill_area.get(1.0, END)
        msg.attach(MIMEText(body, 'plain'))
        
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_address, "your_password")
            text = msg.as_string()
            server.sendmail(from_address, to_address, text)
            server.quit()
            print("Email sent successfully")
        except Exception as e:
            print(f"Failed to send email: {e}")


if __name__ == "__main__":
    root = Tk()
    root.mainloop()
