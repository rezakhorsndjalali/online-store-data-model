# Online Store Data Model
## Project Introduction
This project is a simple data model for an online store system. The main focus of the code is on defining the structure of the main entities such as vendor,shopping cart,transaction,wallet and discountcode.

This project does not contain implementation logic and is mostly used for system design, educational purposes and further developments.
## Project Structure

The following main components are modeled in this project:
- Discount codes and their restrictions
- Shopping cart and applied discounts
- Financial transactions
- Wallet information
- Vendors and their products
- Central store management
## Discount Code Class
1. This class represents a discount code in the system.
The Time field stores the creation time or expiration date of the discount code.
2. The Customers field contains a list of customers who are allowed to use this discount code.
3. The product field specifies which products the discount code can be used on.
4. The limit field specifies the number of times the discount code can be used.
## Shopping Cart Class
1. This class models a customer's shopping cart.
2. The item field specifies the item added to the shopping cart.
3. The vendor field indicates the vendor that offers the item.
4. The time field stores the time the shopping cart was created or last edited.
5. The discount codes field is a list of discount codes applied to the shopping cart.
## Transaction Class
1. This class stores information about a financial transaction.
2. The time field specifies the time the transaction was made.
3. The tracking number field is the unique tracking number of the transaction.
4. The amount field indicates the final amount of the transaction.
## Wallet Class
1. This class represents wallet information.
2. The Order Time field stores the time of the last order placed.
3. The Discount Code field stores the discount code used in the order.
## Seller Class
1. This class manages information about the seller.
2. The Products field is a list of products that the seller offers.
3. The Location field specifies the seller's location.
4. The Rating field displays the seller's rating.
5. The Order List field stores orders placed for the seller.
6. The Wallet field displays the seller's credit rating.
7. The Statistics field stores the seller's statistics (this field name may have a typo).
8. The field is the user number, contact number, or seller ID.
## Store Class
1. This class forms the core of the store.
2. The sellers field is a list of all active sellers in the system.
3. The products field contains all the products available in the store.
4. The customers field stores the list of registered customers. The discount_codes field contains all the discount codes active in the store.

These menus that you see below are going to be written and executed in the continuation of this code, which I will write the descriptions of the menus below.
 ## root menu
 1. login
 2. register
 3. exit
## login menu
1. operator
2. seller
3. customer
4. back

# Console Menu Structure

This project is implemented as a console-based application with a hierarchical menu system.
Users interact with the system through different roles: Operator, Seller, and Customer.
#### Below is the full menu flow and available options.

## Root Menu
When the application starts, the following main menu is shown:
1. Login:
Allows a user to log in as Operator, Seller, or Customer.

2. Register:
Allows new users to register in the system.

3. Exit:
Exits the application.

## Role Selection Menu
After login, the user selects a role:
1. Operator

2. Seller

3. Customer

4. Back
## Operator Menu
The operator has full system management access.
#### Available options:
1. View Sellers:
Displays the list of all registered sellers.

2. Confirm Seller:
Approves or verifies seller accounts.

3. View Customers:
Displays all registered customers.

4. Confirm Customer:
Confirms customer accounts.

5. View Orders:
Shows all orders in the system.

6. Create Discount Code:
Creates new discount codes.

7. View System Statistics:
Displays system-level statistics such as total orders, users, and sales.

8. Back:
Returns to the previous menu.
## Seller Menu

Sellers manage their products and orders.

#### Available options:

1. View My Items:
Displays items listed by the seller.

2. Add Item:
Adds a new product item to the seller’s inventory.

3. View Orders:
Displays orders related to the seller.

4. Back:
Returns to the previous menu.
## Customer Menu

Customers interact with products, baskets, and payments.

#### Available options:

1. View Products:
Shows all available products.

#### Inside this section:

Add product to basket

Write comment

View sellers

View product properties

Back

1. View Baskets
Allows navigation between shopping baskets:

Current basket

Previous basket

Next basket

3. Wallet
    Wallet management options:

        Increase inventory (add balance)

        Withdrawal

        View inventory (balance)

        Back

4. Checkout
    Finalizes the purchase and creates an order.

5. Back
    Returns to the previous menu.




## LICENCE : 
MIT