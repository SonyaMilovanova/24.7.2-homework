from api import PetFriends
from settings import valid_email, valid_password
import os
import json

pf = PetFriends()

#Test1
def test_post_add_uncorrect_information_about_new_pet(name ='Bob', animal_type='mops',
                                     age='-5'):
    """Проверяем, что нельзя добавить питомца с отрицательным возрастом"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    #Запрашиваем ключ и сохраняем в пременную

    status, result = pf.post_add_information_about_new_pet(auth_key, name, animal_type, age)
    #Добавляем питомца

    assert status == 200
    assert result['name'] == name

#Test2
def test_post_add_information_about_new_pet_without_name(animal_type='mops',
                                     age='5'):
    """Проверяем, что нельзя добавить питомца без имени"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    #Запрашиваем ключ и сохраняем в пременную

    status, result = pf.post_add_information_about_new_pet(auth_key, name, animal_type, age)
    #Добавляем питомца

    assert status == 200
    assert result['name'] == name

#Test3
def test_post_add_information_about_new_pet(name ='Bob', animal_type='mops',
                                     age='5'):
    """Проверяем, что можно добавить питомца с корректными данными"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    #Запрашиваем ключ и сохраняем в пременную

    status, result = pf.post_add_information_about_new_pet(auth_key, name, animal_type, age)
    #Добавляем питомца

    assert status == 200
    assert result['name'] == name

#Test4
def test_add_pets_photo(pet_photo = 'photo.jpg'):
    """Проверяем, что возможно добавить только фотографию к ранее добавленному питомцу"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    #Получаем ключ и список моих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    #Если ранее добавленных питомцев нет, то добавляем нового
    if len(my_pets['pets']) == 0:
        pf.post_add_information_about_new_pet(auth_key, "Sam", "Humster", "2")
        _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
        #Выбираем последнего добавленного питомца и добавляем ему в профиль фото
        pet_id = my_pets['pets'][0]['id']
        status, result = pf.add_pets_photo(auth_key, pet_id, pet_photo)

        assert status == 200
        assert 'pet_photo' in result

#Test4
def test_get_api_key_uncorrect_email(email="1234", password="Summer2023"):
    """Проверяем, что запрос api ключа с неправильно введенным email невозможен и возвращает статус 403"""

    status, result = pf.get_api_key(email,password)
    assert status == 403

#Test5
def test_get_api_key_uncorrect_password(email="sonyadenisova1@mail.ru", password="1234"):
    """Проверяем, что запрос api ключа с неправильно введенным паролем невозможен и возвращает статус 403"""

    status, result = pf.get_api_key(email,password)
    assert status == 403

#Test7
def test_get_my_pets_list(filter='my_pets'):
    """Проверяем, что запрос списка моих питомцев возвращает статус код 200,
    в результате есть не пустой список, возвращает список json информации о моих питомцах"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0
    print(result)

#Test8
def test_update_only_name_about_pet(name='Sara', animal_type='mops', age='5'):
    """Проверяем, что возможно изменить только имя у последнего добаленного питомца и возвращается статус 200"""

    # Запрашиваем ключ и сохраняем в пременную
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    #Получаем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    # Если список питомцев не пустой, то обновляем данные о последнем питомце
    if len(my_pets['pets']) > 0:
        status, result = pf.put_update_information_about_pet(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name

    else:
        print("there aren't your pets")

#Test9
def test_unsuccessful_add_pets_photo(pet_photo = 'photo.xls'):
    """Проверяем, что не возможно добавить только фото формата .xls к ранее добавленному питомцу"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    #Получаем ключ и список моих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    #Если ранее добавленных питомцев нет, то добавляем нового
    if len(my_pets['pets']) == 0:
        pf.post_add_information_about_new_pet(auth_key, "Sam", "Humster", "2")
        _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
        #Выбираем последнего добавленного питомца и добавляем ему в профиль фото
        pet_id = my_pets['pets'][0]['id']
        status, result = pf.add_pets_photo(auth_key, pet_id, pet_photo)

        assert status == 415

#Test10
def test_delete_pet_from_database_with_uncorrect_email():
    """Проверка удаления первого питомца из списка моих питомцев с введением неправильного email"""

    #Получаем ключ и список моих питомцев
    _, auth_key = pf.get_api_key(email='1234', password='Summer2023')
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    #Если список моих питомцев пустой, то добавляем нового
    if len(my_pets['pets']) == 0:
        pf.post_add_information_about_new_pet(auth_key, "Spot", "cat",
                                              "6")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    #Берем id первого питомца и отправлем запрос  на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet_from_database(auth_key, pet_id)

    #Ещё раз запрашиваем список моих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    #Проверяем, что статус ответа 200 и в списке нет id удалённого питомца
    assert status == 403
