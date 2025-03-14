import data
import sender_stand_request

def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body

def get_new_user_token():
    user_body = data.user_body
    response = sender_stand_request.post_new_user(user_body)
    return response.json()["authToken"]

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400

def test1_create_kit_1_letter_in_name():
    kit_body = get_kit_body(data.test1_name)
    positive_assert(kit_body)

def test2_create_kit_511_letter_in_name():
    kit_body = get_kit_body(data.test2_name)
    positive_assert(kit_body)

def test3_create_kit_0_letter_in_name():
    kit_body = get_kit_body(data.test3_name)
    negative_assert_400(kit_body)

def test4_create_kit_512_letter_in_name():
    kit_body = get_kit_body(data.test4_name)
    negative_assert_400(kit_body)

def test5_create_kit_special_characters_in_name():
    kit_body = get_kit_body(data.test5_name)
    positive_assert(kit_body)

def test6_create_kit_spaces_in_name():
    kit_body = get_kit_body(data.test6_name)
    positive_assert(kit_body)

def test7_create_kit_string_number_in_name():
    kit_body = get_kit_body(data.test7_name)
    positive_assert(kit_body)

def test8_create_kit_without_name_parameter():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_400(kit_body)

def test9_create_kit_number_in_name():
    kit_body = get_kit_body(data.test9_name)
    negative_assert_400(kit_body)