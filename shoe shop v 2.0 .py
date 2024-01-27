
import mysql.connector as a
import matplotlib.pyplot as pl
import pyttsx3 
engine = pyttsx3.init()
engine.setProperty("rate",100)

print("Enter mysql password (if not correct then exit) :")
mysql=input("Enter your password: ")

mydb=a.connect(host="localhost",user='root',passwd=mysql)
c=mydb.cursor()
print('''
------------ SHOP 3000  ---------------------------------
''')
aa=5

def encrypt(plain_text, key):
    encrypted_text = ""
    key_index = 0

    for char in plain_text:
        if char.isalpha():
            key_char = key[key_index % len(key)]
            key_index += 1

            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            encrypted_char = chr((ord(char) - base + ord(key_char.upper()) - ord('A')) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

def decrypt(encrypted_text, key):
    decrypted_text = ""
    key_index = 0

    for char in encrypted_text:
        if char.isalpha():
            key_char = key[key_index % len(key)]
            key_index += 1

            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            decrypted_char = chr((ord(char) - base - (ord(key_char.upper()) - ord('A')) + 26) % 26 + base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text

def cash(x):                                                                                       
    c.execute("select * from cash")
    for i in c:
        continue
    cash,=i
    cash=cash+x
    c.execute("update cash set cash = '"+str(cash)+"'")
    mydb.commit()

def guide():
    print('''
    ====== Guide ====== 
          
        ==== How to use programme  
        All libraries used:
          1. matplotlib 
          2. sql-connector 
          3. pyttsx3 
        
        === Bibliography ===
        
        1. Vigenere cipher 
        2. Sales managment project tutorial 
          
          
          
          ''')
    engine.say('''
          
        How to use programe  
        All libraries used 
          1. matplotlib 
          2. sql-connector 
          3. pyttsx3 
        
        Bibliography 
               
        1. Vigenere cipher 
        2. Sales managment project tutorial '''
        )
    engine.runAndWait()

defpass=encrypt(encrypt(encrypt("ant",mysql),mysql),mysql)
def pretables():
    c.execute("create database if not exists shop3000")
    c.execute("use shoeshop3000")
    c.execute("create table if not exists login(username varchar(30) default 'admin' , password varchar(40) default '"+defpass+"')")
    c.execute("create table if not exists purchases(order_date date,name varchar(30) not null,product_code int not null,amount int)")
    c.execute("create table if not exists stock(product_code int not null,product_name varchar(40),quantity int,price int)")
    c.execute("create table if not exists cash(cash int default 0 )")
    c.execute("insert into cash values()")
    c.execute("insert into login values()")
    mydb.commit()

# default user 
    

def graph():
    grcode=()
    grname=()
    grquantity=()
    grprice=()
    print('''Which graph do you wish to see
        a. Line graph (quantity)
        b. Pie chart(items remaining)
        c. Price comparision graph
        ''')
    engine.say(''' 
Accessing data regarding sales ... 
    ''')
    engine.runAndWait()
    choice4=input("Enter your choice :")
    if choice4=="a":
        c.execute("select * from stock")
        for i in c:
            code,name,quantity,price=i
            grcode+=(code,)
            grname+=(name,)
            grquantity+=(quantity,)
            grprice+=(price,)
        pl.plot(grname,grquantity)
        pl.show()
        admin()        
    if choice4=="b":
        c.execute("select * from stock")
        for i in c:
            code,name,quantity,price=i
            grcode+=(code,)
            grname+=(name,)
            grquantity+=(quantity,)
            grprice+=(price,)
        pl.pie(grquantity, labels=grname) # type: ignore
        pl.show()
        admin()
    if choice4=="c":
        c.execute("select * from stock")
        for i in c:
            code,name,quantity,price=i
            grcode+=(code,)
            grname+=(name,)
            grquantity+=(quantity,)
            grprice+=(price,)
        pl.bar(grname,grprice) # type: ignore
        pl.show()
        engine.say(''' 
Great sales
    ''')
        engine.runAndWait()
        admin()
    else:
        print("Inaccurate choice. Try again!")    
        admin()

def login():
    global aa  
    loginuser=input("Enter administrator username :")
    loginpass=input("Enter your password :")
    c.execute("select * from login")
    for i in c:
        continue
    if i==(loginuser,encrypt(encrypt(encrypt(loginpass,mysql),mysql),mysql)):
        print("Login succesfull! Opening Administrator Controls... ")
        admin()
    else:
        print("Login failed. Please try again."
              " Attempts remaining =",aa)
        aa-=1
        if aa==0:
            engine.say(''' 
Access denied ! SELF DISTRUCT PROTOCOL Activated.
    ''')
            engine.runAndWait()
            print("Quiting ..... ....")
            quit()
        login()


def admin():
    print('''
    === Administrator controls ===

    a. Show graphs (LineGraph/PieChart..)
    b. Configure products (Add/Remove...) . 
    c. Configure cash (Deposit/Withdrawal...).
    d. View accounts. 
    e. Change admin password.
    f. Back to main menu.
    ''')
# loook thiss 
    engine.say(''' admin controls 

    a. show fancy graphs 
    b. configure products  
    c. configure cash
    d. view accounts
    e. change admin password
    f. back to main menu 
    ''')
    engine.runAndWait()

    choice2=input("Enter your choice :")
    if choice2=="a":
        graph()
    if choice2=="b":
        print('''Select from below:
        a. Add a new product. 
        b. Change price of a product.
        c. Show all products.
        d. Remove product from stock.
        e. Back to main menu.
        ''')
        engine.say('''choose what to do 
        a. add new product 
        b. change price of product
        c. show all products
        d. remove product from stock
        e. back to main menu
        ''')
        engine.runAndWait()
        choice3=input("Enter your choice:")
        if choice3=="a":
            pcode=int(input("Enter product code:"))
            c.execute("Select product_code from stock")
            ii=()
            for i in c:
                ii=ii+i
            if pcode not in ii:
                pname=input("Enter product name :")
                quantity=input("Enter quantity :")
                price=input("Enter the price :")
                c.execute("insert into stock values('"+str(pcode)+"','"+pname+"','"+quantity+"','"+price+"')")
                mydb.commit()
                print("Product added succesfully.")
                productcost=int(input("How much did this product cost?(each) :"))
                q=int(quantity)
                
                cog=productcost*q
                c.execute("select * from cash")
                for i in c:
                    continue
                cash,=i
                int(cash) # type: ignore
                cash=cash-cog # type: ignore
                c.execute("update cash set cash = '"+str(cash)+"'")
                mydb.commit()
                admin()
                
            else:
                print("Product code not found. Returning to main menu..")
                admin()



        if choice3=="b":
            print("")
            pcode=input("Eneter product code :")
            newprice=input("Enter new price :")
            c.execute("update stock set price='"+newprice+"' where product_code='"+pcode+"'")
            mydb.commit()
            print("Price changed successfully! Returning to main menu ....  ")
            admin()


# enter y while funtion 


        if choice3=="c":
            c.execute("select * from stock")
            F="%15s %15s %15s %15s"
            print(F % ("product code", "  product name",  "quantity", "price"))
            print("="*125)
            for i in c:
                for j in i:
                    print("%14s" % j, end=' ')
                print()
            print("="*125)
            admin()
            

        if choice3=="d":
            pcode=input("Enter product code of the product u want to delete :")
            y=input("Confirm? (Y/N) :")
            if y=="y"or"Y":
                c.execute("delete from stock where product_code='"+pcode+"'")
                mydb.commit()
                admin()
            else:
                print("Returning to main menu ...")
                admin()
        if choice3=="e":
            mainmenu()

# account acces ------------------------------------------------

    if choice2=="c":
        c.execute("select * from cash")
        for i in c:
            continue
        cash,=i
        print("balance =",cash)
        withdraw=int(input("How much cash do be withdrawn? (0 to skip) :"))
        deposit=int(input("How much cash to be deposited? :"))
        int(cash) # type: ignore
        cash=cash-withdraw # type: ignore
        cash=cash+deposit
        print("Balance of Cash available =",cash)
        admin()


    if choice2=="d":
        print('''Select the Account
        a. Sales
        b. Products ''')
        choice4=input("Enter your choice :")
        if choice4=="a":
            c.execute("select * from purchases")
            F="%15s %15s %15s %15s"
            print(F % ("Date", "  Customer name",  "Product code", "Amount"))
            print("="*125)
            for i in c:
                for j in i:
                    print("%14s" % j, end=' ')
                print()
            print("="*125)
            admin()
        if choice4=="b":
            c.execute("select * from stock")
            F="%15s %15s %15s %15s"
            print(F % ("Product code", "  Product name",  "Quantity", "Price"))
            print("="*125)
            for i in c:
                for j in i:
                    print("%14s" % j, end=' ')
                print()
            print("="*125)
            admin()
        else:
            print("Inaccurate choice! Please try again.")    
            admin()

# admin =-----------------
    if choice2=="e":
        old=input("Enter the old password :")
        c.execute("select * from login")
        for i in c:
            continue
        old1=encrypt(encrypt(encrypt(old,),mysql),mysql)
        if i==('admin',old1):
            new=input("Enter your new password :")
            new1=encrypt(encrypt(encrypt(new,mysql),mysql),mysql)
            c.execute("update login set password = '"+new1+"'")
            mydb.commit()
            mainmenu()
        else:
            print("Wrong password! Try again.")
            admin()
    if choice2=="f":
        mainmenu()
    else:
        print("Inaccurate choice! ")    
        admin()


def other():
    print('''
    ====== More Options ====
    1. Guide 
    2. Credits 
    3. Project
        ''')
    choice15=int(input("Enter your choice :"))
    if choice15 == 1:
        guide()
    if choice15 == 2:
        print('''
    ===== Credits =====
    1. Insaf
    2. Aamir 
    3. Davidson

''')
    if choice15 == 3:
        print("Project")
    else: 
        other()


def mainmenu():
    while True:
        print('''
    -------- Welcome to the Shop 3000

        1. Buy a product
        2. Administrator login 
        3. Miscellaneous
        0. Quit program?
              
        ''')
        engine.say('''welcome to the shop 

        1. buy something 
        2. administration login 
        3. miscellaneous
        0. quit program 
              
        ''')
        engine.runAndWait()

        choice1=int(input("Enter your choice :"))
        if choice1==2:
            login()
        if choice1==1:
            customer()
        if choice1==3:
            other()
        if choice1==0:
                print("Quiting ..... ....")
                quit()
        else:
            print("404 Error Not found!")
            mainmenu()

def customer():
    while True:
        print("""
    1. Add a product to cart.
    2. Check out.
    3. View Available Items.
    4. Go to menu.
    """)
        engine.say("""
    1. add item to cart 
    2. check out 
    3. View Available Items
    4. Go to menu
    """)
        engine.runAndWait()
# add item to basket  ---mysq
        ch2=int(input("Enter your choice:"))
        if (ch2==1):
            name=input("Enter your name:")
            pcode=int(input("Enter product code:"))
            c.execute("select product_code from stock")
            for i in c:
                if pcode in i:
                    pc=str(pcode)
                    quantity=int(input("Enter product quantity:"))
                    c.execute("select * from stock where product_code = '"+pc+"'")
                    for i in c:
                        t_code,t_name,t_quan,t_price=i
                    net_quan=0
                    int(t_code) # type: ignore
                    int(t_price) # type: ignore
                    int(t_quan) # type: ignore
                    amount=t_price*quantity # type: ignore
                    net_quan=t_quan-quantity # type: ignore
                    q=str(net_quan)
                    codee=str(pcode)
                    amm=str(amount)
                    c.execute("update stock set quantity='"+q+"'where product_code='"+codee+"'")
                    c.execute("insert into purchases values(now(),'"+name+"','"+codee+"','"+amm+"')")
                    print("-------  Added to cart successfully!!. Returning to main menu.. ----------  ")
                    engine.say("""
   added to cart successfully
    """)
                    engine.runAndWait()
                else:
                    print("Wrong product code. Try again!")
                    customer()

        elif(ch2==2):
            print(f"Amount to be paid -- {amount}")
            ch15=input("are u sure u have to buy (y/n)" )
            if ch15=="y"or"Y":
                cash(amount)
                mydb.commit()                                    
            else:
                customer()
            print(" --------  Thank you shopping with us!! Come again soon.  ----------")   
            engine.say("""
   thank you shopping  with us come again soon
    """)
            engine.runAndWait()   
        elif(ch2==3):
            c.execute("select * from stock")
            F="%15s %15s %15s %15s"
            print(F % ("Product code", "  Product name",  "Items left", "Price"))
            print("="*125)
            for i in c:
                for j in i:
                    print("%14s" % j, end=' ')
                print()
            print("="*125)
        elif(ch2==4):
            mainmenu()
        else:
            print("Error 404 not found")
            customer()
    

pretables()
mainmenu()



