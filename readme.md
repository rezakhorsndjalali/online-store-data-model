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