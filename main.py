from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import csv


class Bill_app:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x1000+0+0")
        self.root.title("Billing Software")

        # Image1
        img = Image.open("image/Nart.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        lbl_image = Label(self.root, image=self.photoimg)
        lbl_image.place(x=0, y=0, width=600, height=230)

        # Image2
        img_1 = Image.open("image/GROCER.jpeg")
        img_1 = img_1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        lbl_img_1 = Label(self.root, image=self.photoimg_1)
        lbl_img_1.place(x=500, y=0, width=600, height=230)

        # Image3
        img_2 = Image.open("image/Walmart.jpg")
        img_2 = img_2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        lbl_img_2 = Label(self.root, image=self.photoimg_2)
        lbl_img_2.place(x=1000, y=0, width=500, height=230)

        lbl_title = Label(self.root, text="BILLING SOFTWARE USING PYTHON", font=("time new roman", 35, "bold"),
                          bg="white", fg="red")
        lbl_title.place(x=0, y=130, width=1920, height=45)

        Main_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="White")
        Main_Frame.place(x=0, y=175, width=1920, height=620)

        # Product LabelFrame
        Product_Frame = LabelFrame(Main_Frame, text="Product", font=("time new roman", 12, "bold"), bg="white",
                                   fg="red")
        Product_Frame.place(x=370, y=500, width=500, height=140)

        # Category
        self.lblCategory = Label(Product_Frame, font=('arial', 12, 'bold'), bg="white", text="Select Categories", bd=4)
        self.lblCategory.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.combo_category = ttk.Combobox(Product_Frame, font=('arial', 10, 'bold'), width=24, state="readonly")
        self.combo_category.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        # SubCategory
        self.lblSubCategory = Label(Product_Frame, font=('arial', 12, 'bold'), bg="white", text="Subcategories", bd=4)
        self.lblSubCategory.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.combo_Subcategory = ttk.Combobox(Product_Frame, state="readonly", font=('arial', 10, 'bold'), width=24)
        self.combo_Subcategory.grid(row=1, column=1, sticky=W, padx=5, pady=2)

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
        img_12 = img_12.resize((490, 340), Image.ANTIALIAS)
        self.photoimg_12 = ImageTk.PhotoImage(img_12)

        lbl_img_12 = Label(self.root, image=self.photoimg_12)
        lbl_img_12.place(x=490, y=0, width=490, height=340)

        # Image2
        img_13 = Image.open("image/OIPT.jpeg")
        img_13 = img_13.resize((490, 340), Image.ANTIALIAS)
        self.photoimg_13 = ImageTk.PhotoImage(img_13)

        lbl_img_13 = Label(self.root, image=self.photoimg_13)
        lbl_img_13.place(x=490, y=0, width=490, height=340)

        # search
        Search_frame = Frame(Main_Frame, bd=2, bg="white", )
        Search_frame.place(x=1020, y=15, width=500, height=40)

        self.lblBill = Label(Search_frame, font=('arial', 12, 'bold'), fg="white", bg="Red", text="Bill Number")
        self.lblBill.grid(row=0, column=0, sticky=W, padx=1)

        self.txt_Entry_Search = ttk.Entry(Search_frame, font=('arial', 10, 'bold'), width=24)
        self.txt_Entry_Search.grid(row=0, column=1, sticky=W, padx=2)

        self.BtnSearch = Label(Search_frame, text="Search", font=('arial', 10, 'bold'), bg="Orangered", fg="white",
                               width=15, cursor="hand2")
        self.BtnSearch.grid(row=0, column=2)

        # RightFrame Bill Aria
        RightLabelFrame = LabelFrame(Main_Frame, text="Bill Aria", font=("time new roman", 12, "bold"), bg="white",
                                     fg="red")
        RightLabelFrame.place(x=1000, y=45, width=480, height=440)

        scroll_y = Scrollbar(RightLabelFrame, orient=VERTICAL)
        self.textarea = Text(RightLabelFrame, yscrollcommand=scroll_y.set, bg="white", fg="blue",
                             font=("time new roman", 12, "bold"))
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # Bill Counter LabelFrame
        BOTTOM_Frame = LabelFrame(Main_Frame, text="Bill Counter", font=("time new roman", 12, "bold"), bg="white",
                                  fg="red")
        BOTTOM_Frame.place(x=370, y=485, width=1920, height=128)

        self.lblSubTotal = Label(BOTTOM_Frame, font=('arial', 12, 'bold'), bg="white", text="Sub Total", bd=4)
        self.lblSubTotal.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.EntrySubTotal = ttk.Entry(BOTTOM_Frame, font=('arial', 10, 'bold'), width=24, )
        self.EntrySubTotal.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.lbl_tax = Label(BOTTOM_Frame, font=('arial', 12, 'bold'), bg="white", text="Gov Tax", bd=4)
        self.lbl_tax.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.lbl_tax = ttk.Entry(BOTTOM_Frame, font=('arial', 10, 'bold'), width=24)
        self.lbl_tax.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.AmountTotal = ttk.Entry(BOTTOM_Frame, font=('arial', 10, 'bold'), bg="white", text="Total", bd=4)
        self.AmountTotal.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.AmountTotal = ttk.Entry(BOTTOM_Frame, font=('arial', 10, 'bold'), width=24)
        self.AmountTotal.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        # Buttom Frame
        Btn_frame = Frame(BOTTOM_Frame, bd=2, bg="white", )
        Btn_frame.place(x=320, y=0)

        self.BtnAddToCart = Button(Btn_frame, height=2, text="Add To Cart", font=('arial', 15, 'bold'),bg="Orangered", fg="white", width=15, cursor="hand2")
        self.BtnAddToCart.grid(row=0, column=0)

        self.Btngenerate_Bill = Button(Btn_frame, height=2, text="Generate Bill", font=('arial', 15, 'bold'),bg="Orangered", fg="white", width=15, cursor="hand2")
        self.Btngenerate_Bill.grid(row=0, column=1)

        self.BtnSave = Button(Btn_frame, height=2, text="Save", font=('arial', 15, 'bold'),bg="Orangered", fg="white", width=15, cursor="hand2")
        self.BtnSave.grid(row=0, column=2)

        self.BtnPrint = Button(Btn_frame, height=2, text="Print", font=('arial', 15, 'bold'),bg="Orangered", fg="white", width=15, cursor="hand2")
        self.BtnPrint.grid(row=0, column=3)

        self.BtnClear = Button(Btn_frame, height=2, text="Clear", font=('arial', 15, 'bold'),bg="Orangered", fg="white", width=15, cursor="hand2")
        self.BtnClear.grid(row=0, column=4)

        self.BtnExit = Button(Btn_frame, height=2, text="Exit", font=('arial', 15, 'bold'),bg="Orangered", fg="white", width=15, cursor="hand2")
        self.BtnExit.grid(row=0, column=5)

        # Load data from CSV file
        self.load_data()

    def load_data(self):
        try:
            with open('products.csv', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)  # You can replace this with populating your combo boxes
        except FileNotFoundError:
            print("Error: File not found")


if __name__ == '__main__':
    root = Tk()
    obj = Bill_app(root)
    root.mainloop()
