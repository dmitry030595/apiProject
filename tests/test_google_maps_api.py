from utils.api import GoogleMapsApi
from utils.checking import Checking
import allure

"""Creation, update and deletion of new location"""
@allure.epic("Test create place")
class TestCreatePlace():

    @allure.description("Test creation, update and deletion of new location")
    def test_create_new_place(self):

        print("POST method")
        result_post = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'scope', 'APP')

        print("GET POST method")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print("PUT method")
        result_put = GoogleMapsApi.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ["msg"])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("GET PUT method")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print("DELETE method")
        result_delete = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print("GET DELETE method")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
        Checking.check_json_value(result_get, 'msg', 'Get operation failed, looks like place_id  doesn\'t exists')
        Checking.check_json_search_word_in_value(result_get, 'msg', 'failed')

        print("Test 'Creation, update and deletion of new location' completed successfully")

