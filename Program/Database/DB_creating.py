from mysql.connector import *
from Program.Database.DB_queries import *



def create_db_human_friends(config):
    """Создать базу данных human_friends, таблицы и заполнить их данными"""
    try:
        with connect(
                host=config[0],
                user=config[1],
                password=config[2],
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(create_db_query)
                cursor.execute(use_db_query)
                cursor.execute(create_table_animals)
                cursor.execute(create_table_pets)
                cursor.execute(create_table_pack_animals)
                cursor.execute(create_table_dogs)
                cursor.execute(create_table_cats)
                cursor.execute(create_table_hamsters)
                cursor.execute(create_table_horses)
                cursor.execute(create_table_camels)
                cursor.execute(create_table_donkeys)
                cursor.execute(insert_animals_query)
                cursor.execute(insert_pets_query)
                cursor.execute(insert_pack_animals_query)
                cursor.execute(insert_dogs_query)
                cursor.execute(insert_cats_query)
                cursor.execute(insert_hamsters_query)
                cursor.execute(insert_horses_query)
                cursor.execute(insert_camels_query)
                cursor.execute(insert_donkeys_query)
                connection.commit()
                print(f'The human friends database has been successfully established!')
    except Error as e:
        print(e)
