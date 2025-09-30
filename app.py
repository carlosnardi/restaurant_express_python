import os

restaurants = [{'name': 'Cantina Liliana', 'category': 'Italian food', 'status': True}, 
               {'name': 'Dags', 'category': 'Snack Bar', 'status': True},
               {'name': 'Padrela', 'category': 'Bakery', 'status': False}]

def app_menu():
    os.system('clear')
    print('ｒｅｓｔａｕｒａｎｔ ｅｘｐｒｅｓｓ')
    print('\nChoose one option below:')
    print('1. Register a restaurant')
    print('2. List all restaurants registered')
    print('3. Activate restaurant')
    print('4. Exit application')
    app_options()
    
def return_to_menu():
    input('\nPress any key to return to menu: ')
    app_menu()

def app_options():
    try: 
        option = int(input('Choose an option by the according number (1 - 4): '))
        if option == 1:
            option_title('Registering a restaurant') 
            register_restaurant()
        elif option == 2: 
            option_title('Listing all restaurants')
            list_restaurants()
        elif option == 3: 
            option_title('Changing restaurant status')
            change_restaurant_status()
        elif option == 4: 
            exit_application()
    except:
        print('Type a valid option from 1 to 4')
        return_to_menu()

def option_title(title):
    os.system('clear')
    print(title, '\n')

def register_restaurant():
    restaurant_name = input('What\'s the restaurant name: ').title()
    restaurant_category = input('What is the category of the restaurant: ')
    restaurant = {'name': restaurant_name, 'category': restaurant_category, 'status': False}
    restaurants.append(restaurant)
    print(f'{restaurant_name} was registered successfully')
    return_to_menu()

def list_restaurants():
    for restaurant in restaurants:
        name = restaurant['name']
        category = restaurant['category']
        status = 'Activated' if restaurant["status"] else 'Deactivated'
        print(f'- {name} | {category} | {status}')
    return_to_menu()

def change_restaurant_status():    
    restaurant_selected = input('What is the name of the restaurant to change status: ')
    for restaurant in restaurants:
        if restaurant['name'] == restaurant_selected:
            restaurant['status'] = not restaurant['status']
        else:
            print('Restaurant not found')
    return_to_menu()

def exit_application():
    os.system('clear')
    print('Exiting application...\n')

def main(): 
    app_menu()
    

if __name__ == '__main__':
    main()