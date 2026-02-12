import products
import store


# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)


def start(best_buy):
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            all_products = best_buy.get_all_products()
            number = 1

            for product in all_products:
                print(f"{number}. ", end="")
                product.show()
                number += 1
        elif choice == "2":
            total = best_buy.get_total_quantity()
            print(f"Total of {total} items in store")
        elif choice == "3":
            shopping_list = []
            all_products = best_buy.get_all_products()
            number = 1

            for product in all_products:
                print(f"{number}. ", end="")
                product.show()
                number += 1

            while True:
                user_input_product = input("When you want to finish order, enter finish.\nWhich product do you want? Enter the number: ")

                if user_input_product.lower() == "finish":
                    break

                user_input_quantity = input("What amount do you want? ")

                try:
                    product_id = int(user_input_product) - 1
                    quantity = int(user_input_quantity)

                    if product_id < 0 or quantity <= 0:
                        print("Please enter positive numbers only!")
                        continue

                    selected_product = all_products[product_id]
                    shopping_list.append((selected_product, quantity))
                    print("Product added to list!\n")

                except (ValueError, IndexError):
                    print("Invalid input! Please try again.")

            if shopping_list:
                try:
                    total_price = best_buy.order(shopping_list)
                    print(f"********\nOrder made! Total payment: {total_price}")
                except Exception as e:
                    print(f"Error during ordering: {e}")
        elif choice == "4":
            print("Goodbye!")
            break  # Beendet die while-Schleife
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    start(best_buy)