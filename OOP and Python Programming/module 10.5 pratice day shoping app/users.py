class user:
    def __init__(self,email,password) -> None:
        self.email=email
        self.password=password
    def login_pass_chek(self,password):
        if self.password==password:
            print("Login Successfull..")
            return True
        else:
            print("Login Failed !! Incorrect Password!! ")
            return False
            
       
            
class order:
    def __init__(self,customer ,product,quantity) -> None:
        self.customer=customer
        self.product=product
        self.quantity=quantity
        self.status="Pending"
        
    def process_order(self):
        if self.quantity <= self.product.stock:
            self.product.update_stock(self.quantity)
            self.status="completed"
        else:
            self.status="failed"
            print("Not enough stock!!!")    
                
      
# # Initialize marketplace
# market = marketplace()

# # Create users
# alice = customer('alice@example.com', 'password123')
# bob = seller('bob@example.com', 'pswd123')

# # Register users
# market.register_customer(alice)
# market.register_seller(bob)

# # Bob adds a product
# laptop = products('Laptop', 1000, 5)
# market.add_product(bob, laptop)

# # Display products
# market.display_products()

# # Alice places an order
# market.place_order(alice, laptop, 2)

# # Check stock update
# market.display_products()

        
    # # Initialize marketplace
    # market = marketplace()

    # # Create and register users
    # alice = customer('alice@example.com', 'password123')
    # bob = seller('bob@example.com', 'pswd123')
    # nahin=seller('nahinn75@gmail.com','nahin')
    # market.register_customer(alice)
    # market.register_seller(bob)
    # market.register_seller(nahin)

    # # Attempt to log in
    # market.login_user('alice@example.com', 'password123')  # Expected: Login successful!
    # market.login_user('bob@example.com', 'wrongpassword')  # Expected: Login failed. Incorrect password.
    # market.login_user('nahinn75@gmail.com','nahin')
