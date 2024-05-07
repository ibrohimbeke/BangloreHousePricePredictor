from tkinter import *
from tkinter import messagebox
import random, os, tempfile, smtplib
import tkinter as tk


# Functionality part


def send_email():
    def send_gmail():
        try:
            ob = smtplib.SMTP('smpt.gmail.com', 587)
            ob.starttls()
            ob.login(senderEntry.get(), passwordEntry.get())
            message = email_textarea.get(1.0, END)
            ob.sendmail(senderEntry.get(), receiverEntry.get(), message)
            ob.quit()
            messagebox.showinfo('Success', 'Bill is successfully sent')
            root1.destroy()
        except:
            messagebox.showerror('Error', 'Something went wrong, Please try again')

    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is empty')
    else:
        root1 = Toplevel()
        root.grab_set()
        root1.title('send gmail')
        root.config(bg='slate gray')
        root1.resizable(0, 0)
        senderFrame = LabelFrame(root1, text='SENDER', font=('arial', 16, 'bold'), bd=6, bg='slate gray', fg='white')
        senderFrame.grid(row=0, column=0, padx=40, pady=20)
        senderLabel = Label(senderFrame, text="Sender's Email", font=('arial', 14, 'bold'), bd=6, bg='slate gray',
                            fg='white')
        senderLabel.grid(row=0, column=0, padx=10, pady=8)
        senderEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        senderEntry.grid(row=0, column=1, padx=10, pady=8)

        passwordLabel = Label(senderFrame, text="Password", font=('arial', 14, 'bold'), bd=6, bg='slate gray',
                              fg='white')
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)

        passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE, show='*')
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        recipientFrame = LabelFrame(root1, text='Recipient', font=('arial', 16, 'bold'), bd=6, bg='slate gray',
                                    fg='white')
        recipientFrame.grid(row=1, column=0, padx=40, pady=20)

        receiverLabel = Label(recipientFrame, text="Email Address", font=('arial', 14, 'bold'), bd=6, bg='slate gray',
                              fg='white')
        receiverLabel.grid(row=0, column=0, padx=10, pady=8)

        receiverEntry = Entry(recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        receiverEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(recipientFrame, text="Message", font=('arial', 14, 'bold'), bd=6, bg='slate gray',
                             fg='white')
        messageLabel.grid(row=1, column=0, padx=10, pady=8)

        email_textarea = Text(recipientFrame, font=('arial', 14, 'bold'), bd=2, relief=SUNKEN,
                              width=42, height=11)
        email_textarea.grid(row=2, column=0, columnspan=2)
        email_textarea.delete(1.0, END)
        email_textarea.insert(END, textarea.get(1.0, END).replace('=', '').replace('-', '').replace('\t\t\t', '\t\t'))

        sendButton = Button(root1, text='SEND', font=('arial', 16, 'bold'), width=15, command=send_gmail)
        sendButton.grid(row=2, column=0, pady=20)
        root1.mainloop()


def clear_entries():
    # Clear all the entry fields
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    billnumberEntry.delete(0, END)

    # Reset the quantities of all products to 0
    bathsoapEntry.delete(0, END)
    bathsoapEntry.insert(0, 0)
    hairsprayEntry.delete(0, END)
    hairsprayEntry.insert(0, 0)
    hairgelEntry.delete(0, END)
    hairgelEntry.insert(0, 0)
    bodylotionEntry.delete(0, END)
    bodylotionEntry.insert(0, 0)
    facecreamEntry.delete(0, END)
    facecreamEntry.insert(0, 0)
    facewashEntry.delete(0, END)
    facewashEntry.insert(0, 0)

    suitsEntry.delete(0, END)
    suitsEntry.insert(0, 0)
    shoesEntry.delete(0, END)
    shoesEntry.insert(0, 0)
    t_shirtsEntry.delete(0, END)
    t_shirtsEntry.insert(0, 0)
    trousersEntry.delete(0, END)
    trousersEntry.insert(0, 0)
    sweatersEntry.delete(0, END)
    sweatersEntry.insert(0, 0)
    beltsEntry.delete(0, END)
    beltsEntry.insert(0, 0)

    watchesEntry.delete(0, END)
    watchesEntry.insert(0, 0)
    braceletEntry.delete(0, END)
    braceletEntry.insert(0, 0)
    ringEntry.delete(0, END)
    ringEntry.insert(0, 0)
    necklacesEntry.delete(0, END)
    necklacesEntry.insert(0, 0)
    fragrancesEntry.delete(0, END)
    fragrancesEntry.insert(0, 0)
    scarfEntry.delete(0, END)
    scarfEntry.insert(0, 0)

    # Clear the bill area
    textarea.delete(1.0, END)

    # Clear the price and tax entries
    menclothespriceEntry.delete(0, END)
    menclothespriceEntry.insert(0, '0 $')
    cosmeticspriceEntry.delete(0, END)
    cosmeticspriceEntry.insert(0, '0 $')
    accessoriespriceEntry.delete(0, END)
    accessoriespriceEntry.insert(0, '0 $')
    menclothestaxEntry.delete(0, END)
    menclothestaxEntry.insert(0, '0 $')
    cosmeticstaxEntry.delete(0, END)
    cosmeticstaxEntry.insert(0, '0 $')
    accessoriestaxEntry.delete(0, END)
    accessoriestaxEntry.insert(0, '0 $')


def print_bill():
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is empty')
    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w').write(textarea.get(1.0, END))
        os.startfile(file, 'print')


def search_bill():
    found = False
    for filename in os.listdir('bills/'):
        if filename.startswith(billnumberEntry.get()):
            with open(f'bills/{filename}', 'r') as f:
                textarea.delete(1.0, END)
                for data in f:
                    textarea.insert(END, data)
            found = True
            break
    if not found:
        messagebox.showerror('Error', 'No bill found with the provided bill number')

)

def save_bill():
    global billnumber
    result = messagebox.askyesno('Confirm', 'Do you want to save the bill?')
    if result:
        bill_content = textarea.get(1.0, END)
        file = open(f'bills/ {billnumber}.txt', 'w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success', f'bill number {billnumber} is saved successfully')
        billnumber = random.randint(500, 1000)


billnumber = random.randint(500, 1000)


def bill_area():
    if nameEntry.get() == '' or phoneEntry.get() == '':
        messagebox.showerror('Error', 'Customer Details Are Required')
    elif cosmeticspriceEntry.get() == '' and menclothespriceEntry.get() == '' and accessoriespriceEntry.get() == '':
        messagebox.showerror('Error', 'No Products Are Selected')
    elif cosmeticspriceEntry.get() == '0 $' and menclothespriceEntry.get() == '0 $' and accessoriespriceEntry.get() == '0 $':
        messagebox.showerror('Error', 'No Products Are Selected')
    else:
        textarea.delete(1.0, END)

        textarea.insert(END, '\t\t**Welcome Customer**\n')
        textarea.insert(END, f'\nBill Number: {billnumber}\n')
        textarea.insert(END, f'\nCustomer Name: {nameEntry.get()}\n')
        textarea.insert(END, f'\nPhone Number: {phoneEntry.get()}\n')
        textarea.insert(END, '\n=======================================================================')
        textarea.insert(END, 'Product\t\t\t\tQuantity\t\t\t\tPrice')
        textarea.insert(END, '\n=======================================================================')
        textarea.insert(END, '\n=======================================================================')
        if bathsoapEntry.get() != 0:
            textarea.insert(END, f'Bath Soap\t\t\t\t{bathsoapEntry.get()}\t\t\t\t{soapprice} $')
        if hairsprayEntry.get() != 0:
            textarea.insert(END, f'\nHair Spray\t\t\t\t{hairsprayEntry.get()}\t\t\t\t{hairsprayprice} $')
        if hairgelEntry.get() != 0:
            textarea.insert(END, f'\nHair Gel\t\t\t\t{hairgelEntry.get()}\t\t\t\t{hairgelprice} $')
        if bodylotionEntry.get() != 0:
            textarea.insert(END, f'\nBody Lotion\t\t\t\t{bodylotionEntry.get()}\t\t\t\t{bodylotionprice} $')
        if facecreamEntry.get() != 0:
            textarea.insert(END, f'\nFace Cream\t\t\t\t{facecreamEntry.get()}\t\t\t\t{facecreamprice} $')
        if facewashEntry.get() != 0:
            textarea.insert(END, f'\nFace Wash\t\t\t\t{facewashEntry.get()}\t\t\t\t{facewashprice} $')
        # Men Clothes
        if suitsEntry.get() != 0:
            textarea.insert(END, f'\nSuits\t\t\t\t{suitsEntry.get()}\t\t\t\t{suitsprice} $')
        if shoesEntry.get() != 0:
            textarea.insert(END, f'\nShoes\t\t\t\t{shoesEntry.get()}\t\t\t\t{shoesprice} $')
        if t_shirtsEntry.get() != 0:
            textarea.insert(END, f'\nT-shirts\t\t\t\t{t_shirtsEntry.get()}\t\t\t\t{t_shirtsprice} $')
        if trousersEntry.get() != 0:
            textarea.insert(END, f'\nTrousers\t\t\t\t{trousersEntry.get()}\t\t\t\t{trousersprice} $')
        if sweatersEntry.get() != 0:
            textarea.insert(END, f'\nSweaters\t\t\t\t{sweatersEntry.get()}\t\t\t\t{sweatersprice} $')
        if beltsEntry.get() != 0:
            textarea.insert(END, f'\nBelts\t\t\t\t{beltsEntry.get()}\t\t\t\t{beltsprice} $')
        # Accessories
        if watchesEntry.get() != 0:
            textarea.insert(END, f'\nWatches\t\t\t\t{watchesEntry.get()}\t\t\t\t{watchesprice} $')
        if braceletEntry.get() != 0:
            textarea.insert(END, f'\nBracelets\t\t\t\t{braceletEntry.get()}\t\t\t\t{braceletsprice} $')
        if ringEntry.get() != 0:
            textarea.insert(END, f'\nRings\t\t\t\t{ringEntry.get()}\t\t\t\t{ringsprice} $')
        if necklacesEntry.get() != 0:
            textarea.insert(END, f'\nNecklaces\t\t\t\t{necklacesEntry.get()}\t\t\t\t{necklacesprice} $')
        if fragrancesEntry.get() != 0:
            textarea.insert(END, f'\nFragrances\t\t\t\t{fragrancesEntry.get()}\t\t\t\t{fragrancesprice} $')
        if scarfEntry.get() != 0:
            textarea.insert(END, f'\nScarves\t\t\t\t{scarfEntry.get()}\t\t\t\t{scarvesprice} $')
        textarea.insert(END, '\n-----------------------------------------------------------------------')

        if cosmeticstaxEntry.get() != '0.0 $':
            textarea.insert(END, f'\nCosmetic Tax\t\t\t\t {cosmeticstaxEntry.get()}')
        if menclothestaxEntry.get() != '0.0 $':
            textarea.insert(END, f'\nMen Clothes Tax\t\t\t\t {menclothestaxEntry.get()}')
        if accessoriestaxEntry.get() != '0.0 $':
            textarea.insert(END, f'\nAccessories Tax\t\t\t\t {accessoriestaxEntry.get()}')
        textarea.insert(END, f'\nTotal Bill \t\t\t\t {totalbill}')
        textarea.insert(END, '\n-----------------------------------------------------------------------')
        save_bill()


def total():
    global soapprice, hairsprayprice, hairgelprice, bodylotionprice, facecreamprice, facewashprice
    global suitsprice, shoesprice, t_shirtsprice, trousersprice, sweatersprice, beltsprice
    global watchesprice, braceletsprice, ringsprice, necklacesprice, fragrancesprice, scarvesprice
    global totalbill
    soapprice = int(bathsoapEntry.get()) * 2
    facecreamprice = int(facecreamEntry.get()) * 5
    facewashprice = int(facewashEntry.get()) * 10
    hairsprayprice = int(hairsprayEntry.get()) * 15
    hairgelprice = int(hairgelEntry.get()) * 8
    bodylotionprice = int(bodylotionEntry.get()) * 6

    totalcosmeticsprice = soapprice + facewashprice + facecreamprice + hairgelprice + hairsprayprice + bodylotionprice
    cosmeticspriceEntry.delete(0, END)
    cosmeticspriceEntry.insert(0, f'{totalcosmeticsprice} $')
    cosmeticstax = totalcosmeticsprice * 0.10
    cosmeticstaxEntry.delete(0, END)
    cosmeticstaxEntry.insert(0, str(cosmeticstax) + ' $')

    # men clothes calculation

    suitsprice = int(suitsEntry.get()) * 40
    shoesprice = int(shoesEntry.get()) * 30
    t_shirtsprice = int(t_shirtsEntry.get()) * 25
    trousersprice = int(trousersEntry.get()) * 30
    sweatersprice = int(sweatersEntry.get()) * 15
    beltsprice = int(beltsEntry.get()) * 7

    totalmenclothesprice = suitsprice + shoesprice + t_shirtsprice + trousersprice + sweatersprice + beltsprice
    menclothespriceEntry.delete(0, END)
    menclothespriceEntry.insert(0, str(totalmenclothesprice) + ' $')
    menclothestax = totalmenclothesprice * 0.10
    menclothestaxEntry.delete(0, END)
    menclothestaxEntry.insert(0, str(menclothestax) + ' $')

    # Accessories calculation

    watchesprice = int(watchesEntry.get()) * 50
    braceletsprice = int(braceletEntry.get()) * 25
    ringsprice = int(ringEntry.get()) * 65
    necklacesprice = int(necklacesEntry.get()) * 10
    fragrancesprice = int(fragrancesEntry.get()) * 90
    scarvesprice = int(scarfEntry.get()) * 18

    totalaccessoriesprice = watchesprice + braceletsprice + ringsprice + necklacesprice + fragrancesprice + scarvesprice
    accessoriespriceEntry.delete(0, END)
    accessoriespriceEntry.insert(0, str(totalaccessoriesprice) + ' $')
    accessoriestax = totalaccessoriesprice * 0.05
    accessoriestaxEntry.delete(0, END)
    accessoriestaxEntry.insert(0, str(accessoriestax) + ' $')

    totalbill = totalcosmeticsprice + totalmenclothesprice + totalaccessoriesprice + cosmeticstax + menclothestax + accessoriestax


# GUI part
root = tk.Tk()
root.title("Retail Billing System")
root.geometry("1270x685")
root.iconbitmap('icon.ico')
headingLabel = Label(root, text='Retail Billing System', font=('times new roman', 30, 'bold')
                     , bg='slate gray', fg='Gold', bd=12, relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame = tk.LabelFrame(root, text='Customer Details', font=('times new roman', 15, 'bold'),
                                       bd=8, relief=tk.GROOVE, bg='slate gray')
customer_details_frame.pack()

nameLabel = Label(customer_details_frame, text='Name', font=('times new roman', 15, 'bold'),
                  bg='slate gray', fg='white')

customer_details_frame.pack(fill=X)
nameLabel.grid(row=0, column=0, padx=20, pady=2)

nameEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
nameEntry.grid(row=0, column=1, padx=8)

phoneLabel = Label(customer_details_frame, text='Phone Number', font=('times new roman', 15, 'bold'),
                   bg='slate gray', fg='white')

phoneLabel.grid(row=0, column=2, padx=20, pady=2)

phoneEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
phoneEntry.grid(row=0, column=3, padx=8)

billnumberLabel = Label(customer_details_frame, text='Bill Number', font=('times new roman', 15, 'bold'),
                        bg='slate gray', fg='white')

billnumberLabel.grid(row=0, column=4, padx=20, pady=2)

billnumberEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
billnumberEntry.grid(row=0, column=5, padx=8)

searchButton = Button(customer_details_frame, text='Search',
                      font=('arial', 12, 'bold'), bd=7, width=10, command=search_bill)
searchButton.grid(row=0, column=6, padx=20, pady=8)

productsFrame = Frame(root)
productsFrame.pack()

clothesFrame = LabelFrame(productsFrame, text='Men Clothes', font=('times new roman', 15, 'bold'),
                          fg='gold', bd=8, relief=GROOVE, bg='slate gray')
clothesFrame.grid(row=0, column=0)

suitsLabel = Label(clothesFrame, text='Suits', font=('times new roman', 15, 'bold'),
                   bg='slate gray', fg='white')
suitsLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

suitsEntry = Entry(clothesFrame, font=('arial', 15), bd=4, width=10)
suitsEntry.grid(row=0, column=1, pady=9, padx=10)
suitsEntry.insert(0, 0)

shoesLabel = Label(clothesFrame, text='Shoes', font=('times new roman', 15, 'bold'),
                   bg='slate gray', fg='white')
shoesLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

shoesEntry = Entry(clothesFrame, font=('arial', 15), bd=4, width=10)
shoesEntry.grid(row=1, column=1, pady=9, padx=10)
shoesEntry.insert(0, 0)

t_shirtsLabel = Label(clothesFrame, text='T-shirts', font=('times new roman', 15, 'bold'),
                      bg='slate gray', fg='white')
t_shirtsLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

t_shirtsEntry = Entry(clothesFrame, font=('arial', 15), bd=4, width=10)
t_shirtsEntry.grid(row=2, column=1, pady=9, padx=10)
t_shirtsEntry.insert(0, 0)

trousersLabel = Label(clothesFrame, text='Trousers', font=('times new roman', 15, 'bold'),
                      bg='slate gray', fg='white')
trousersLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

trousersEntry = Entry(clothesFrame, font=('arial', 15), bd=4, width=10)
trousersEntry.grid(row=3, column=1, pady=9, padx=10)
trousersEntry.insert(0, 0)

sweatersLabel = Label(clothesFrame, text='Sweaters', font=('times new roman', 15, 'bold'),
                      bg='slate gray', fg='white')
sweatersLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

sweatersEntry = Entry(clothesFrame, font=('arial', 15), bd=4, width=10)
sweatersEntry.grid(row=4, column=1, pady=9, padx=10)
sweatersEntry.insert(0, 0)

beltsLabel = Label(clothesFrame, text='Belts', font=('times new roman', 15, 'bold'),
                   bg='slate gray', fg='white')
beltsLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

beltsEntry = Entry(clothesFrame, font=('arial', 15), bd=4, width=10)
beltsEntry.grid(row=5, column=1, pady=9, padx=10)
beltsEntry.insert(0, 0)

cosmeticsFrame = LabelFrame(productsFrame, text='Cosmetics', font=('times new roman', 15, 'bold'),
                            fg='gold', bd=8, relief=GROOVE, bg='slate gray')
cosmeticsFrame.grid(row=0, column=1)

facecreamLabel = Label(cosmeticsFrame, text='Face Cream', font=('times new roman', 15, 'bold'),
                       bg='slate gray', fg='white')
facecreamLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

facecreamEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=4, width=10)
facecreamEntry.grid(row=0, column=1, pady=9, padx=10)
facecreamEntry.insert(0, 0)

facewashLabel = Label(cosmeticsFrame, text='Face Wash', font=('times new roman', 15, 'bold'),
                      bg='slate gray', fg='white')
facewashLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

facewashEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=4, width=10)
facewashEntry.grid(row=1, column=1, pady=9, padx=10)
facewashEntry.insert(0, 0)

bathsoapLabel = Label(cosmeticsFrame, text='Bath Soap', font=('times new roman', 15, 'bold'),
                      bg='slate gray', fg='white')
bathsoapLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

bathsoapEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=4, width=10)
bathsoapEntry.grid(row=2, column=1, pady=9, padx=10)
bathsoapEntry.insert(0, 0)

hairsprayLabel = Label(cosmeticsFrame, text='Hair Spray', font=('times new roman', 15, 'bold'),
                       bg='slate gray', fg='white')
hairsprayLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

hairsprayEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=4, width=10)
hairsprayEntry.grid(row=3, column=1, pady=9, padx=10)
hairsprayEntry.insert(0, 0)

hairgelLabel = Label(cosmeticsFrame, text='Hair Gel', font=('times new roman', 15, 'bold'),
                     bg='slate gray', fg='white')
hairgelLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

hairgelEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=4, width=10)
hairgelEntry.grid(row=4, column=1, pady=9, padx=10)
hairgelEntry.insert(0, 0)
bodylotionLabel = Label(cosmeticsFrame, text='Body Lotion', font=('times new roman', 15, 'bold'),
                        bg='slate gray', fg='white')
bodylotionLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

bodylotionEntry = Entry(cosmeticsFrame, font=('arial', 15), bd=4, width=10)
bodylotionEntry.grid(row=5, column=1, pady=9, padx=10)
bodylotionEntry.insert(0, 0)

accessoriesFrame = LabelFrame(productsFrame, text='Accessories', font=('times new roman', 15, 'bold'),
                              fg='gold', bd=8, relief=GROOVE, bg='slate gray')
accessoriesFrame.grid(row=0, column=2)

watchesLabel = Label(accessoriesFrame, text='Watches', font=('times new roman', 15, 'bold'),
                     bg='slate gray', fg='white')
watchesLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

watchesEntry = Entry(accessoriesFrame, font=('arial', 15), bd=4, width=10)
watchesEntry.grid(row=0, column=1, pady=9, padx=10)
watchesEntry.insert(0, 0)

braceletLabel = Label(accessoriesFrame, text='Bracelets', font=('times new roman', 15, 'bold'),
                      bg='slate gray', fg='white')
braceletLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

braceletEntry = Entry(accessoriesFrame, font=('arial', 15), bd=4, width=10)
braceletEntry.grid(row=1, column=1, pady=9, padx=10)
braceletEntry.insert(0, 0)

ringLabel = Label(accessoriesFrame, text='Rings', font=('times new roman', 15, 'bold'),
                  bg='slate gray', fg='white')
ringLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

ringEntry = Entry(accessoriesFrame, font=('arial', 15), bd=4, width=10)
ringEntry.grid(row=2, column=1, pady=9, padx=10)
ringEntry.insert(0, 0)

necklacesLabel = Label(accessoriesFrame, text='Necklaces', font=('times new roman', 15, 'bold'),
                       bg='slate gray', fg='white')
necklacesLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

necklacesEntry = Entry(accessoriesFrame, font=('arial', 15), bd=4, width=10)
necklacesEntry.grid(row=3, column=1, pady=9, padx=10)
necklacesEntry.insert(0, 0)

fragrancesLabel = Label(accessoriesFrame, text='Fragrances', font=('times new roman', 15, 'bold'),
                        bg='slate gray', fg='white')
fragrancesLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

fragrancesEntry = Entry(accessoriesFrame, font=('arial', 15), bd=4, width=10)
fragrancesEntry.grid(row=4, column=1, pady=9, padx=10)
fragrancesEntry.insert(0, 0)

scarfLabel = Label(accessoriesFrame, text='Scarves', font=('times new roman', 15, 'bold'),
                   bg='slate gray', fg='white')
scarfLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

scarfEntry = Entry(accessoriesFrame, font=('arial', 15), bd=4, width=10)
scarfEntry.grid(row=5, column=1, pady=9, padx=10)
scarfEntry.insert(0, 0)

billframe = Frame(productsFrame, bd=8, relief=GROOVE)
billframe.grid(row=0, column=3, padx=10)

billareaLabel = Label(billframe, text='BIll Area', font=('times new roman', 15, 'bold'), bd=7, relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar = Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
textarea = Text(billframe, height=21, width=71, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame = LabelFrame(root, text='Bill Menu', font=('times new roman', 14, 'bold'),
                           fg='gold', bd=15, relief=GROOVE, bg='slate gray')
billmenuFrame.pack()

menclothespriceLabel = Label(billmenuFrame, text='Men Clothes Price', font=('times new roman', 14, 'bold'),
                             bg='slate gray', fg='white')
menclothespriceLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

menclothespriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10,
                             bd=5)
menclothespriceEntry.grid(row=0, column=1, pady=9, padx=10)

cosmeticspriceLabel = Label(billmenuFrame, text='Cosmetics Price', font=('times new roman', 14, 'bold'),
                            bg='slate gray', fg='white')
cosmeticspriceLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

cosmeticspriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10,
                            bd=5)
cosmeticspriceEntry.grid(row=1, column=1, pady=9, padx=10)

accessoriespriceLabel = Label(billmenuFrame, text='Accessories Price', font=('times new roman', 14, 'bold'),
                              bg='slate gray', fg='white')
accessoriespriceLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

accessoriespriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10,
                              bd=5)
accessoriespriceEntry.grid(row=2, column=1, pady=9, padx=10)

menclothestaxLabel = Label(billmenuFrame, text='Men Clothes Tax', font=('times new roman', 14, 'bold'),
                           bg='slate gray', fg='white')
menclothestaxLabel.grid(row=0, column=2, pady=9, padx=10, sticky='w')

menclothestaxEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10,
                           bd=5)
menclothestaxEntry.grid(row=0, column=3, pady=9, padx=10)

cosmeticstaxLabel = Label(billmenuFrame, text='Cosmetics Tax', font=('times new roman', 14, 'bold'),
                          bg='slate gray', fg='white')
cosmeticstaxLabel.grid(row=1, column=2, pady=9, padx=10, sticky='w')

cosmeticstaxEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10,
                          bd=5)
cosmeticstaxEntry.grid(row=1, column=3, pady=9, padx=10)

accessoriestaxLabel = Label(billmenuFrame, text='Accessories Tax', font=('times new roman', 14, 'bold'),
                            bg='slate gray', fg='white')
accessoriestaxLabel.grid(row=2, column=2, pady=9, padx=10, sticky='w')

accessoriestaxEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10,
                            bd=5)
accessoriestaxEntry.grid(row=2, column=3, pady=9, padx=10)

buttonFrame = Frame(billmenuFrame, bd=8, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=3)

totalButton = Button(buttonFrame, text='Total', font=('arial', 16, 'bold'), bg='slate gray',
                     bd=5, width=8, pady=10, command=total)
totalButton.grid(row=0, column=0, pady=20, padx=5)

billButton = Button(buttonFrame, text='Bill', font=('arial', 16, 'bold'), bg='slate gray',
                    bd=5, width=8, pady=10, command=bill_area)
billButton.grid(row=0, column=1, pady=20, padx=5)

emailButton = Button(buttonFrame, text='Email', font=('arial', 16, 'bold'), bg='slate gray',
                     bd=5, width=8, pady=10, command=send_email)
emailButton.grid(row=0, column=2, pady=20, padx=5)

printButton = Button(buttonFrame, text='Print', font=('arial', 16, 'bold'), bg='slate gray',
                     bd=5, width=8, pady=10, command=print_bill)
printButton.grid(row=0, column=3, pady=20, padx=5)

clearButton = Button(buttonFrame, text='Clear', font=('arial', 16, 'bold'), bg='slate gray',
                     bd=5, width=8, pady=10, command=clear_entries)
clearButton.grid(row=0, column=4, pady=20, padx=5)

root.mainloop()
