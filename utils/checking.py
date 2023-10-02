"""Methods for checking requests"""
import json


class Checking():

    """Method for checking status code"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code, f"Failed!!! Status code = {str(result.status_code)}"
        print("Success!!! Status code = " + str(result.status_code))

    """Method for checking required fields in request responses"""
    @staticmethod
    def check_json_token(result, expected_value):
        token = json.loads(result.text)
        assert list(token) == expected_value, f"{expected_value} is not present in response"
        print("All fields are present")

    """Method for checking required values in request responses"""

    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, f"{field_name} 'is not correct!!!'"
        print(field_name + " is correct!!!")

    """Method for checking required values in request responses with word"""

    @staticmethod
    def check_json_search_word_in_value(result, field_name, search_word):
        check = result.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print("Word " + search_word + " is present!!!")
        else:
            print("Word " + search_word + " is not present!!!")

