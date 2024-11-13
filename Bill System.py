from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import csv
import random
class Bill_app:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Billing Software")
        
        #=================Variable===================
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

        
        
        #Product Categories List
        self.Category=["Select Option","Clothing","LifeStyle","Mobiles"]
        
        # SubCatClothing
        self.SubCatClothing=["Jeans","Shirt","T-Shirt","Trouser"]
        self.Jeans=["Levis","Wrangle","Spyker","Mufti","Tommy Hilfiger","Calvin Klein","Pepe Jeans"]
        self.price_levis=3000
        self.price_Wrangle=2500
        self.price_Spyker=2000
        self.price_Mufti=5500
        self.price_TommyHilfiger=3000
        self.price_CalvinKlein=2800
        self.price_PepeJeans=2500
        
        self.Shirt=["Spyker","Mufti","Tommy Hilfiger","Roadster","Polo"]
        self.price_Spyker=4000
        self.price_Mufti=1200
        self.price_TommyHilfiger=2000
        self.price_Roadster=500
        self.price_Polo=1300
        
        self.T_Shirt=["Spyker","Mufti","Tommy Hilfiger","Roadster","Polo"]
        self.price_Spyker=800
        self.price_Mufti=1200
        self.price_TommyHilfiger=1600
        self.price_Roadster=500
        self.price_Polo=1300
        
        self.Trouser=["Spyker","Mufti","Tommy Hilfiger","Roadster","Polo"]
        self.price_Spyker=1699
        self.price_Mufti=1299
        self.price_TommyHilfiger=1600
        self.price_Roadster=400
        self.price_Polo=1300
        
        
        # SubCatLifeStype
        self.SubCatLifeStyle=["Bath Soap","Face Cream","Hair Oil"]
        self.BathSoap=["LifeBoy","Dove","Lux","Pears","Dettol"]
        self.price_LifeBoy=20
        self.price_Dove=45
        self.price_Lux=30
        self.price_Pears=40
        self.price_Dettol=30
        
        self.FaceCream=["Fair&Lovely","Dove","Jhonson Baby","Ponds","Beardo"]
        self.price_FaireLovely=50
        self.price_Dove=110
        self.price_Jhonsonsbaby=80
        self.price_Ponds=60
        self.price_Beardo=150
        
        self.HairOil=["Parachute","jashmine","Jhonson Baby","Bajaj"]
        self.price_Parachute=50
        self.price_Jashmine=110
        self.price_Jhonsonsbaby=80
        self.price_bajaj=150
        
        # SubCatMobiles
        self.SubCatMobiles=["Samsung","Vivo","Realme","Oneplus"]
        self.Samsung=["S23 Ultra","S24 Ulta+","A73","A53"]
        self.price_S23Ultra=150000
        self.price_S24Ultra=190000
        self.price_A73=70000
        self.price_A53=55000
        
        self.Vivo=["vivo V29 5G","vivo X80 Pro","vivo X100 Pro","vivo X100"]
        self.price_vivoV295G=50000
        self.price_vivoX80Pro=79999
        self.price_vivoX100Pro=90000
        self.price_vivoX100=60000
        
        self.Realme=["Realme X2 Pro ","Realme GT Neo 3 ","Realme GT 2 Pro","Realme X50 Pro 5G"]
        self.price_RealmeX2Pro=50000
        self.price_RealmeGTNeo3=50000
        self.price_RealmeGT2Pro=45000
        self.price_RealmeX50Pro5G=39999
        
        self.Oneplus=["OnePlus 11 5G","OnePlus 12","OnePlus Open"]
        self.price_OnePlus115G=50000
        self.price_OnePlus12=80000
        self.price_OnePlusOpen=110000
        

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

        lbl_title = Label(self.root, text="BILLING SOFTWARE USING PYTHON", font=("time new roman", 35, "bold"),bg="white", fg="red")
        lbl_title.place(x=0, y=130, width=1920, height=45)

        Main_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="White")
        Main_Frame.place(x=0, y=175, width=1920, height=620)

        # Product LabelFrame
        Product_Frame = LabelFrame(Main_Frame, text="Product", font=("time new roman", 12, "bold"), bg="white", fg="red")
        Product_Frame.place(x=370, y=500, width=500, height=140)

        # Category
        self.lblCategory = Label(Product_Frame, font=('arial', 12, 'bold'), bg="white", text="Select Categories", bd=4)
        self.lblCategory.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.Combo_Category = ttk.Combobox(Product_Frame,value=self.Category, font=('arial', 10, 'bold'), width=24, state="readonly")
        self.Combo_Category.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>", self.CategoriesClothing)
        self.Combo_Category.bind("<<ComboboxSelected>>", self.CategoriesLifeStyle)
        self.Combo_Category.bind("<<ComboboxSelected>>", self.CategoriesMobiles)


        
        # SubCategory
        self.lblSubCategory = Label(Product_Frame, font=('arial', 12, 'bold'), bg="white", text="Subcategories", bd=4)
        self.lblSubCategory.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.Combo_Subcategory = ttk.Combobox(Product_Frame,value=[""],state="readonly", font=('arial', 10, 'bold'), width=24)
        self.Combo_Subcategory.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.Combo_Subcategory.bind("<<ComboboxSelected>>", self.Product_add)

        # Product Name
        self.lblProduct = Label(Product_Frame, font=('arial', 12, 'bold'), bg="white", text="Select Product", bd=4)
        self.lblProduct.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.comboProduct = ttk.Combobox(Product_Frame, state="readonly", font=('arial', 10, 'bold'), width=24)
        self.comboProduct.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        # Price
        self.lblPrice = Label(Product_Frame, font=('arial', 12, 'bold'), bg="white", text="Price", bd=4)
        self.lblPrice.grid(row=0, column=2, sticky=W, padx=5, pady=2)

        self.comboPrice = ttk.Combobox(Product_Frame, state="readonly", font=('arial', 10, 'bold'), width=24)
        self.comboPrice.grid(row=0, column=3, sticky=W, padx=5, pady=2)

        # Qty
        self.lblQty = Label(Product_Frame, font=('arial', 12, 'bold'), bg="white", text="Qty", bd=4)
        self.lblQty.grid(row=0, column=2, sticky=W, padx=5, pady=2)

        self.comboQty = ttk.Combobox(Product_Frame, font=('arial', 10, 'bold'), width=24)
        self.comboQty.grid(row=1, column=3, sticky=W, padx=5, pady=2)

        # Middle Frame
        MiddleFrame = Frame(Main_Frame, bd=10)
        MiddleFrame.place(x=10, y=150, width=980, height=340)

        # Image1
        img_12 = Image.open("image/Woman gr.jpg")
        img_12 = img_12.resize((590, 335))
        self.photoimg_12 = ImageTk.PhotoImage(img_12)

        lbl_img_12 = Label(MiddleFrame, image=self.photoimg_12)
        lbl_img_12.place(x=10, y=0, width=590, height=335)

        # Image2
        img_13 = Image.open("image/OIPT.jpeg")
        img_13 = img_13.resize((590, 325))
        self.photoimg_13 = ImageTk.PhotoImage(img_13)

        lbl_img_13 = Label(MiddleFrame, image=self.photoimg_13)
        lbl_img_13.place(x=510, y=0, width=600, height=325)
        
        #customer Label Frame
        cust_Frame=LabelFrame(Main_Frame,text="customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        cust_Frame.place(x=10,y=5,width=360,height=140)
        
        self.lbl_mob=Label(cust_Frame,text="Mobile No.",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)
        
        self.entry_mob=ttk.Entry(cust_Frame,textvariable=self.c_phon,font=("times to new roman",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)
        
        self.lblCustName=Label(cust_Frame,font=("arial",12,"bold"),bg="white",text="Customer Name",bd=4)
        self.lblCustName.grid(row=1,column=0,stick=W,padx=5,pady=2)
        
        self.txtCustname=ttk.Entry(cust_Frame,textvariable=self.C_name,font=("arial",10,"bold"),width=24)
        self.txtCustname.grid(row=1,column=1,sticky=W,padx=5,pady=2) 

        
        self.lblEmail=Label(cust_Frame,font=("arial",12,"bold"),bg="white",text="Email",bd=4)
        self.lblEmail.grid(row=2,column=0,stick=W,padx=5,pady=2)
        
        self.entryEmail=ttk.Entry(cust_Frame,textvariable=self.c_email,font=("arial",10,"bold"),width=24)
        self.entryEmail.grid(row=2,column=1,stick=W,padx=5,pady=2)
        
        # Product Label Frame
        Product_Frame = LabelFrame(Main_Frame, text="Product", font=("time new roman", 12, "bold"), bg="white", fg="red")
        Product_Frame.place(x=380, y=5, width=650, height=140)
        
        # Category
        self.lblCategory = Label(Product_Frame, font=("arial", 12, "bold"), bg="white", text="Select Categories", bd=4)
        self.lblCategory.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        
        self.combo_Category = ttk.Combobox(Product_Frame, value=self.Category, font=("Arial", 10, "bold"), width=24, state="readonly")
        self.combo_Category.current(0)
        self.combo_Category.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.combo_Category.bind("<<Comboboxselected>>", self.Category)
        
        # SubCategory
        self.lblSubCategory = Label(Product_Frame, font=("arial", 12, "bold"), bg="white", text="Sub Categories", bd=4)
        self.lblSubCategory.grid(row=1, column=0, sticky=W, padx=5, pady=2)
        
        self.comboSubCategory = ttk.Combobox(Product_Frame, font=("Arial", 10, "bold"), width=24, state="readonly")
        self.comboSubCategory.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        
        # Product Name
        self.lblProduct = Label(Product_Frame, font=("arial", 12, "bold"), bg="white", text="Product Name", bd=4)
        self.lblProduct.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        
        self.comboProduct = ttk.Combobox(Product_Frame, textvariable=self.product, font=("Arial", 10, "bold"), width=24, state="readonly")
        self.comboProduct.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.comboProduct.bind("<<Comboboxselected>>", self.price)
        
        # Price
        self.lblPrice = Label(Product_Frame, font=("arial", 12, "bold"), bg="white", text="Price", bd=4)
        self.lblPrice.grid(row=0, column=2, sticky=W, padx=5, pady=2)
        
        self.ComboPrice = ttk.Combobox(Product_Frame, textvariable=self.prices, font=("Arial", 10, "bold"), width=24, state="readonly")
        self.ComboPrice.grid(row=0, column=3, sticky=W, padx=5, pady=2)
        
        # Qty
        self.lblQty = Label(Product_Frame, font=("arial", 12, "bold"), bg="white", text="Qty", bd=4)
        self.lblQty.grid(row=1, column=2, sticky=W, padx=5, pady=2)
        
        self.ComboQty = ttk.Entry(Product_Frame, textvariable=self.qty, font=("Arial", 10, "bold"), width=24)
        self.ComboQty.grid(row=1, column=3, sticky=W, padx=5, pady=2)

        
        # search
        Search_frame = Frame(Main_Frame, bd=2, bg="white", )
        Search_frame.place(x=1035, y=15, width=500, height=40)

        self.lblBill = Label(Search_frame, font=('arial', 12, 'bold'), fg="white", bg="Red", text="Bill Number")
        self.lblBill.grid(row=0, column=0, sticky=W, padx=1)

        self.txt_Entry_Search = ttk.Entry(Search_frame, textvariable=self.search_bill,font=('arial', 10, 'bold'), width=24)
        self.txt_Entry_Search.grid(row=0, column=1, sticky=W, padx=2)

        self.BtnSearch = Label(Search_frame, text="Search", font=('arial', 10, 'bold'), bg="Orangered", fg="white", width=15, cursor="hand2")
        self.BtnSearch.grid(row=0, column=2)

        # RightFrame Bill Area
        RightLabelFrame = LabelFrame(Main_Frame, text="Bill Aria", font=("time new roman", 12, "bold"), bg="white", fg="red")
        RightLabelFrame.place(x=1035, y=45, width=480, height=440)

        scroll_y = Scrollbar(RightLabelFrame, orient=VERTICAL)
        self.textarea = Text(RightLabelFrame, yscrollcommand=scroll_y.set, bg="white", fg="blue", font=("time new roman", 12, "bold"))
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # Bill Counter LabelFrame
        BOTTOM_Frame = LabelFrame(Main_Frame, text="Bill Counter", font=("time new roman", 12, "bold"), bg="white", fg="red")
        BOTTOM_Frame.place(x=10, y=485, width=1508, height=128)

        self.lblSubTotal = Label(BOTTOM_Frame, font=('arial', 12, 'bold'), bg="white", text="Sub Total", bd=4)
        self.lblSubTotal.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.EntrySubTotal = ttk.Entry(BOTTOM_Frame, font=('arial', 10, 'bold'), width=24, )
        self.EntrySubTotal.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.lbl_tax = Label(BOTTOM_Frame, font=('arial', 12, 'bold'), bg="white", text="Gov Tax", bd=4)
        self.lbl_tax.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.lbl_tax_value = ttk.Entry(BOTTOM_Frame, font=('arial', 10, 'bold'), width=24)
        self.lbl_tax_value.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.AmountTotal = Label(BOTTOM_Frame, font=('arial', 12, 'bold'), bg="white", text="Total", bd=4)
        self.AmountTotal.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.AmountTotal_2 = ttk.Entry(BOTTOM_Frame, font=('arial', 10, 'bold'), width=24)
        self.AmountTotal_2.grid(row=2, column=1, sticky=W, padx=5, pady=2)


        # Buttom Frame
        Btn_frame = Frame(BOTTOM_Frame, bd=2, bg="white", )
        Btn_frame.place(x=420, y=0)

        self.BtnAddToCart = Button(Btn_frame, height=2, text="Add To Cart", font=('arial', 10, 'bold'), bg="Orangered", fg="white", width=20, cursor="hand2")
        self.BtnAddToCart.grid(row=0, column=0)

        self.Btngenerate_Bill = Button(Btn_frame, height=2, text="Generate Bill", font=('arial', 10, 'bold'),bg="Orangered", fg="white", width=20, cursor="hand2")
        self.Btngenerate_Bill.grid(row=0, column=1)

        self.BtnSave = Button(Btn_frame, height=2, text="Save", font=('arial', 10, 'bold'),bg="Orangered", fg="white", width=20, cursor="hand2")
        self.BtnSave.grid(row=0, column=2)

        self.BtnPrint = Button(Btn_frame, height=2, text="Print", font=('arial', 10, 'bold'),bg="Orangered", fg="white", width=20, cursor="hand2")
        self.BtnPrint.grid(row=0, column=3)

        self.BtnClear = Button(Btn_frame, height=2, text="Clear", font=('arial', 10, 'bold'),bg="Orangered", fg="white", width=20, cursor="hand2")
        self.BtnClear.grid(row=0, column=4)

        self.BtnExit = Button(Btn_frame, height=2, text="Exit", font=('arial', 10, 'bold'),bg="Orangered", fg="white", width=20, cursor="hand2")
        self.BtnExit.grid(row=0, column=5)
        
    def CategoriesClothing(self, event=""):
        if self.Combo_Category.get() == "Clothing":
            self.combo_Subcategory.config(values=self.SubCatClothing)
            self.combo_Subcategory.current(0)
            
    def CategoriesLifeStyle(self, event=""):
        if self.Combo_Category.get() == "LifeStyle":
            self.combo_Subcategory.config(values=self.SubCatLifeStyle)
            self.combo_Subcategory.current(0)
            
    def CategoriesMobiles(self, event=""):
        if self.Combo_Category.get() == "Mobiles":
            self.combo_Subcategory.config(values=self.SubCatMobiles)
            self.combo_Subcategory.current(0)

            
    def Product_add(self, event=""):
        # Add logic for adding products based on selected subcategory
        pass
    
    def price(self, event=""):
        # Add logic for setting prices based on selected product
        pass

    def load_data(self):
        try:
            with open('products.csv', newline='') as file:
                reader = csv.reader(file)
                data = list(reader)
                
                # Assuming the first row contains column headers
                headers = data[0]
                
                # Assuming the data starts from the second row
                products_data = data[1:]
                
                # Assuming the first column contains categories
                categories = set(row[0] for row in products_data)
                self.combo_Category['values'] = tuple(categories)
                
                # Assuming the second column contains subcategories
                subcategories = set(row[1] for row in products_data)
                self.combo_Subcategory['values'] = tuple(subcategories)
                
                # Assuming the third column contains product names
                product_names = set(row[2] for row in products_data)
                self.comboProduct['values'] = tuple(product_names)
                
                # Assuming the fourth column contains prices
                prices = set(row[3] for row in products_data)
                self.comboPrice['values'] = tuple(prices)
                
                # Assuming the fifth column contains quantities
                quantities = set(row[4] for row in products_data)
                self.comboQty['values'] = tuple(quantities)
                
        except FileNotFoundError:
            print("Error: File not found")


if __name__ == '__main__':
    root = Tk()
    obj = Bill_app(root)
    root.mainloop()
