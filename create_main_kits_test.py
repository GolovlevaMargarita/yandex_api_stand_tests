import sender_stand_request
import data


def positive_assert_name(name):
    authToken = sender_stand_request.get_auth_token();

    kit = sender_stand_request.get_kit_body(name)
    kits_response = sender_stand_request.get_kits(authToken, kit)

    assert kits_response.status_code == 201
    assert kits_response.json()["name"] == kit["name"];

def negative_assert_name(name):
    authToken = sender_stand_request.get_auth_token();

    body = sender_stand_request.get_kit_body(name)
    kits_response = sender_stand_request.get_kits(authToken, body)

    assert kits_response.status_code == 400

def test_create_kit_1_letter_in_kit_body_get_success_response():
    positive_assert_name("А");

def test_create_kit_511_letter_in_kit_body_get_success_response():
    positive_assert_name("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC");

def test_create_kit_0_letter_in_kit_body_get_failed_response():
    negative_assert_name("");

def test_create_kit_512_letter_in_kit_body_get_failed_response():
    negative_assert_name("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD");

def test_create_kit_english_letter_in_kit_body_get_success_response():
    positive_assert_name("QWErty");

def test_create_kit_russian_letter_in_kit_body_get_success_response():
    positive_assert_name("Мария");

def test_create_kit_special_characters_in_kit_body_get_success_response():
    positive_assert_name("\"№%@\",");

def test_create_kit_space_in_kit_body_get_success_response():
    positive_assert_name("Человек и КО");

def test_create_kit_number_in_kit_body_get_success_response():
    positive_assert_name("123");

def test_create_kit_no_params_in_kit_body_get_failed_response():
    authToken = sender_stand_request.get_auth_token();
    kits_response = sender_stand_request.get_kits(authToken, {})

    print(kits_response.json());
    assert kits_response.status_code == 400


def test_create_kit_other_type_of_params_in_kit_body_get_failed_response():
    negative_assert_name(123);

