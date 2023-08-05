from Program.Service.AddNewAnimal import AddNewAnimal
from Program.Service.Counter import Counter
from Program.Service.TechNewCommand import TeachNewCommands
from Program.View.Output import print_animal


def ls_menu(config):
    """Интерфейс пользователя"""
    count = Counter(6)
    while True:
        print('\nSelect the menu item by entering the appropriate number:\n'
              '1. View the animal register\n'
              '2. Get a new pet\n'
              '3. Actions with animals\n'
              '4. Exit\n')

        user_input = input('Enter: ')
        if user_input.isdigit():
            match int(user_input):
                case 1:
                    print_animal(config)
                case 2:
                    while True:
                        print('Specify the class of the animal.\n'
                              '1. Pets\n'
                              '2. Pack animals\n'
                              '3. Go back\n')
                        class_selection = input('Enter class: ')
                        if class_selection.isdigit():
                            match int(class_selection):
                                case 1:
                                    while True:
                                        print('\nSpecify the type of the animal.\n'
                                              '1. Dogs\n'
                                              '2. Cats\n'
                                              '3. Hamsters\n'
                                              '4. Go back\n')
                                        type_selection = input('Enter type: ')
                                        if type_selection.isdigit():
                                            match int(type_selection):
                                                case 1:
                                                    type_animal = 1
                                                    choose_name = input(
                                                        'Enter the name of the animal: ')
                                                    choose_birthday = input(
                                                        'Enter the date of birth of the animal (yyyyy-mm-dd): ')
                                                    choose_command = input(
                                                        'Enter the commands that the animal can perform, separated by a space: ')
                                                    new_animal = AddNewAnimal(type_animal, choose_name,
                                                                              choose_birthday,
                                                                              choose_command)
                                                    new_animal.new_pet(
                                                        config, count)
                                                    new_animal.print_animal()
                                                case 2:
                                                    type_animal = 2
                                                    choose_name = input(
                                                        'Enter the name of the animal: ')
                                                    choose_birthday = input(
                                                        'Enter the date of birth of the animal (yyyyy-mm-dd): ')
                                                    choose_command = input(
                                                        'Enter the commands that the animal can perform, separated by a space: ')
                                                    new_animal = AddNewAnimal(type_animal, choose_name,
                                                                              choose_birthday,
                                                                              choose_command)
                                                    new_animal.new_pet(
                                                        config, count)
                                                    new_animal.print_animal()
                                                case 3:
                                                    type_animal = 3
                                                    choose_name = input(
                                                        'Enter the name of the animal: ')
                                                    choose_birthday = input(
                                                        'Enter the date of birth of the animal (yyyyy-mm-dd): ')
                                                    choose_command = input(
                                                        'Enter the commands that the animal can perform, separated by a space: ')
                                                    new_animal = AddNewAnimal(type_animal, choose_name,
                                                                              choose_birthday,
                                                                              choose_command)
                                                    new_animal.new_pet(
                                                        config, count)
                                                    new_animal.print_animal()
                                                case 4:
                                                    break
                                        else:
                                            print(
                                                '\nYou entered the wrong number. Try again.')
                                case 2:
                                    while True:
                                        print('\nSpecify the type of the animal.\n'
                                              '1. Horses\n'
                                              '2. Camels\n'
                                              '3. Donkeys\n'
                                              '4. Go back\n')
                                        type_selection = input('Enter type: ')
                                        if type_selection.isdigit():
                                            match int(type_selection):
                                                case 1:
                                                    type_animal = 1
                                                    choose_name = input(
                                                        'Enter the name of the animal: ')
                                                    choose_birthday = input(
                                                        'Enter the date of birth of the animal (yyyyy-mm-dd): ')
                                                    choose_command = input(
                                                        'Enter the commands that the animal can perform, separated by a space: ')
                                                    new_animal = AddNewAnimal(type_animal, choose_name,
                                                                              choose_birthday,
                                                                              choose_command)
                                                    new_animal.new_pack_animal(
                                                        config, count)
                                                    new_animal.print_animal()
                                                case 2:
                                                    type_animal = 2
                                                    choose_name = input(
                                                        'Enter the name of the animal: ')
                                                    choose_birthday = input(
                                                        'Enter the date of birth of the animal (yyyyy-mm-dd): ')
                                                    choose_command = input(
                                                        'Enter the commands that the animal can perform, separated by a space: ')
                                                    new_animal = AddNewAnimal(type_animal, choose_name,
                                                                              choose_birthday,
                                                                              choose_command)
                                                    new_animal.new_pack_animal(
                                                        config, count)
                                                    new_animal.print_animal()
                                                case 3:
                                                    type_animal = 3
                                                    choose_name = input(
                                                        'Enter the name of the animal: ')
                                                    choose_birthday = input(
                                                        'Enter the date of birth of the animal (yyyyy-mm-dd): ')
                                                    choose_command = input(
                                                        'Enter the commands that the animal can perform, separated by a space: ')
                                                    new_animal = AddNewAnimal(type_animal, choose_name,
                                                                              choose_birthday,
                                                                              choose_command)
                                                    new_animal.new_pack_animal(
                                                        config, count)
                                                    new_animal.print_animal()
                                        else:
                                            print(
                                                '\nYou entered the wrong number. Try again.')
                                case 3:
                                    break
                        else:
                            print('\nYou entered the wrong number. Try again.')
                case 3:
                    while True:
                        print('\nChoose an action with an animal.\n'
                              '1. Teaching a new command\n'
                              '2. Show number of animals\n'
                              '3. Go back\n')
                        item = input('Enter menu item: ')
                        if item.isdigit():
                            match int(item):
                                case 1:
                                    type_id_animal_id = print_animal(config)
                                    print(
                                        '\nChoose the animal you want to teach the new command.\n')
                                    animal_id = int(
                                        input("Enter the animal's id: "))
                                    comm = input(
                                        "Enter the command you want to teach the animal: ")
                                    new_command = TeachNewCommands(comm)
                                    new_command.teach_new_command(
                                        config, animal_id, type_id_animal_id)
                                case 2:
                                    count.print_count()
                                case 3:
                                    break
                        else:
                            print('\nYou entered the wrong number. Try again.')
                case 4:
                    print('\nGoodbye!')
                    break
                case _:
                    print(f"\nSorry, I couldn't understand {user_input}.")
        else:
            print('\nYou entered the wrong number. Try again.')
