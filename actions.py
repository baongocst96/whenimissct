# -*- coding: utf-8 -*-
from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, Restarted, AllSlotsReset


# ------book_hottel_form------
class HotelForm(FormAction):

	def name(self) -> Text:
		return "hotel_form"

	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:

		return ["num_people_hotel", "num_room", "phone_hotel", "price_hotel", "add_request_hotel"]

	def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

		return {
			"num_people_hotel": [
				self.from_entity(entity="num_people_hotel"),
				self.from_text(),
			],
			"num_room": [
				self.from_entity(entity="num_room"),
				self.from_text()
			],
			"price_hotel": self.from_entity(entity="price_hotel", intent="book_hotel"),
			"add_request_hotel": [
				self.from_intent(intent="deny", value="No"),
				self.from_text(),
			],
			"phone_hotel": self.from_text()
		}

	@staticmethod
	def is_int(string: Text) -> bool:
		"""Check if a string is an integer"""

		try:
			int(string)
			return True
		except ValueError:
			return False

	def validate_num_people_hotel(
		self,
		value: Text,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
		)-> Optional[Text]:

		if self.is_int(value) and int(value) > 0:
			return {"num_people_hotel": value}
		else:
			dispatcher.utter_template("utter_wrong_num_people_hotel", tracker)
			return {"num_people_hotel": None}

	def validate_num_room(
		self,
		value: Text,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
	) -> Optional[Text]:

		if self.is_int(value) and int(value) > 0:
			return {"num_room": value}
		else:
			dispatcher.utter_template("utter_wrong_num_room", tracker)
			return {"num_room": None}

	def validate_phone_hotel(
		self,
		value: Text,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
	) -> Optional[Text]:
		
		import re

		pattern = "^(0)[0-9]{8}"
		z = re.match(pattern, value)
	
		if z and len(value) == 9:
			return {"phone_hotel": value}
		else:
			dispatcher.utter_template("utter_wrong_phone", tracker)
			return {"phone_hotel": None}

	def submit(
		self,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
	) -> List[Dict]:

		msg = "Đang thiết lập..."
		dispatcher.utter_message(msg)
		dispatcher.utter_template("utter_confirm_hotel", tracker)
		return []

class ConfirmTransactionHotel(Action):
	def name(self) -> Text:
		return "action_confirm_hotel"

	def run(
		self,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
		) -> List[Dict]:
		msg1 = "Đang thực hiện giao dịch..."
		dispatcher.utter_message(msg1)
		msg2 = "✔ Đã đặt chỗ thành công!\
				\nTrong vòng 5p sẽ có nhân viên liên hệ với bạn."
		dispatcher.utter_message(msg2)
		return []

# ------book_restaurant------
class RestaurantForm(FormAction):

	def name(self) -> Text:
		return "restaurant_form"

	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:

		return ["num_people_res", "add_request_res", "phone_res"]

	def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

		return {
			"num_people_res": [
				self.from_entity(entity="num_people_res"),
				self.from_text(),
			],
			"add_request_res": [
				self.from_intent(intent="deny", value="No"),
				self.from_text(),
			],
			"phone_res": self.from_text()
		}

	@staticmethod
	def is_int(string: Text) -> bool:
		"""Check if a string is an integer"""

		try:
			int(string)
			return True
		except ValueError:
			return False

	def validate_num_people_res(
		self,
		value: Text,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
		)-> Optional[Text]:

		if self.is_int(value) and int(value) > 0:
			return {"num_people_res": value}
		else:
			dispatcher.utter_template("utter_wrong_num_people_res", tracker)
			return {"num_people_res": None}

	def validate_phone_res(
		self,
		value: Text,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
	) -> Optional[Text]:
		
		import re

		pattern = "^(0)[0-9]{8}"
		z = re.match(pattern, value)
	
		if z and len(value) == 9:
			return {"phone_res": value}
		else:
			dispatcher.utter_template("utter_wrong_phone", tracker)
			return {"phone_res": None}

	def submit(
		self,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
	) -> List[Dict]:

		msg = "Đang thiết lập..."
		dispatcher.utter_message(msg)
		return []

class ConfirmTransactionRestaurant(Action):
	def name(self) -> Text:
		return "action_confirm_restaurant"

	def run(
		self,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
		) -> List[Dict]:
		msg1 = "Đang thực hiện giao dịch..."
		dispatcher.utter_message(msg1)
		msg2 = "✔ Đã đặt chỗ thành công!\
				\nTrong vòng 5p sẽ có nhân viên liên hệ với bạn."
		dispatcher.utter_message(msg2)
		return []

#---Edit inform book restaurant---
class FormEditRestaurant(FormAction):
	def name(self):
		return "form_edit_res"

	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		if tracker.get_slot("edit_inform_res") == "số người":
			return ["edit_num_people_res"]
		elif tracker.get_slot("edit_inform_res") == "sdt":
			return ["edit_phone_res"]
		else:
			return ["edit_add_request_res"]

	def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

		return {
			"edit_num_people_res": [
				self.from_entity(entity="num_people_res"),
				self.from_text(),
			],
			"edit_phone_res": self.from_text(),
			"edit_add_request_res": [
				self.from_intent(intent="deny", value="No"),
				self.from_text(),
			],
		}

	@staticmethod
	def is_int(string: Text) -> bool:
		"""Check if a string is an integer"""

		try:
			int(string)
			return True
		except ValueError:
			return False

	def validate_edit_num_people_res(
		self,
		value: Text,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
		)-> Optional[Text]:

		if self.is_int(value) and int(value) > 0:
			return {"edit_num_people_res": value}
		else:
			dispatcher.utter_template("utter_wrong_num_people_res", tracker)
			return {"edit_num_people_res": None}

	def validate_edit_phone_res(
		self,
		value: Text,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
	) -> Optional[Text]:
		
		import re

		pattern = "^(0)[0-9]{8}"
		z = re.match(pattern, value)
	
		if z and len(value) == 9:
			return {"edit_phone_res": value}
		else:
			dispatcher.utter_template("utter_wrong_phone", tracker)
			return {"edit_phone_res": None}

	def submit(
		self,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
	) -> List[Dict]:

		msg = "Thay đổi của bạn đã đc lưu lại..."
		dispatcher.utter_message(msg)

		if tracker.get_slot("edit_inform_res") == "số người":
			value = tracker.get_slot("edit_num_people_res")
			return [SlotSet("num_people_res", value)]
		elif tracker.get_slot("edit_inform_res") == "sdt":
			value = tracker.get_slot("edit_phone_res")
			return [SlotSet("phone_res", value)]
		else:
			value = tracker.get_slot("edit_add_request_res")
			return [SlotSet("add_request_res", value)]

class RestarFormEditRes(Action):
	def name(self) -> Text:
		return "restart_form_edit_res"

	def run(
		self,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
		) -> List[Dict]:

		return [SlotSet("edit_inform_res", None),
				SlotSet("edit_num_people_res", None),
				SlotSet("edit_inform_res", None),
				SlotSet("edit_add_request_res", None)]
#---End Edit Book Restaurant---

class EditBookRes(Action):
	def name(self) -> Text:
		return "action_edit_book_res"

	def run(
		self,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
		) -> List[Dict]:

		text = tracker.latest_message.get("text")
		print("Text:", text)
		entities = tracker.latest_message.get("entities", [])
		print("Entities: ", entities)

		name = entities[0]["entity"]
		if name == "num_people":
			name = "num_people_res"
			msg = "Oke đã đổi thành {} người".format(entities[0]["value"])

		if name == "phone_num":
			name = "phone_res"
			msg = "Oke đã đổi sdt thành {}".format(entities[0]["value"])

		dispatcher.utter_message(msg)
		return [SlotSet(name, entities[0]["value"])]

# Search place nearby
class ActionPlaceSearch(Action):
	def name(self):
		#define the name of the action		
		return 'action_place_search'

	def run(self, dispatcher, tracker, domain):
		#retrieve slot values	
		query = tracker.get_slot('name_location')
		
		if any(tracker.get_latest_entity_values("num_dis")):
			radius = tracker.get_slot('num_dis')
		else:
			radius = 1000
		
		if query == 'nhà hàng':
			query1 = 'restaurant'
		else:
			pass
		
		if query == 'khách sạn':
			query1 = 'hotel'
		else:
			pass

		import yaml
		import requests
		import json
		#retrieve google api key		
		with open("./ga_credentials.yml", 'r') as ymlfile:
			cfg = yaml.safe_load(ymlfile)
		key = cfg['credentials']['GOOGLE_KEY']

		# #get user's current location		
		get_origin = requests.post(
			"https://www.googleapis.com/geolocation/v1/geolocate?key={}".format(key)).json()
		
		print("Current user location: \n{}".format(get_origin))
		origin_lat = get_origin['location']['lat']
		origin_lng = get_origin['location']['lng']
				
		#look for a place using all the details
		place = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius={}&type={}&key={}'.format(origin_lat, origin_lng, radius, query1, key)).json()

		dispatcher.utter_message("Đang tìm kiếm {} trong bán kính {} mét".format(query, radius))
		if len(place['results'])==0:
			dispatcher.utter_message("Trong bán kính 500 mét không tìm thấy {} nào!".format(query))
			return []
		else:
			msg = "Trong bán kính {} mét có {} {}".format(radius, len(place['results']), query)
			dispatcher.utter_message(msg)

			for i in place['results']:
				name = i['name']
				if 'rating' not in i.keys():
					rating = "Undefined"
				else:
					rating = i['rating']

				if 'vicinity' not in i.keys():
					address = "Undefined"
				else:
					address = i['vicinity']

				if 'opening_hours' not in i.keys():
					opening_hours = "Undefined"
				else:
					if i['opening_hours']['open_now']==True:
						opening_hours = 'open'
					else:
						opening_hours = 'closed'
				speech = "Tên: {}\
						  \n⭐ Rating: {}\
						  \n⏰ Open: {}\
						  \n🏚 Địa chỉ: {}".format(name, rating, opening_hours, address)
				dispatcher.utter_message(speech) #send the response back to the user	
			return []


# Direction to place
class ActionDirectionTravel(Action):
	def name(self):
		return "action_direction_place"

	@staticmethod
	def location_travel() -> Dict[Text, Any]:
		"""Database of supported cuisines"""

		return {
			"di tích chiến thắng cổ cò": "ChIJs-AdTliECjERPCPAIjWMzsM", # Chiến thắng Cổ Cò
			"chợ hoa mỹ tho": "ChIJdf7H5euvCjERj7lWiC9RBnA", # Phường 1, Thành phố Mỹ Tho, Tỉnh Tiền Giang
			"nhà cổ cái bè": "ChIJjSAV2aibCjERlAP_LBznpOU", # Nhà cổ Ông Kiệt (Mr. Kiet's Ancient House)
			"nhà đốc phủ hải": "ChIJeUEuoyxOdTERXauoGOQmtLQ", # Dinh Đốc Phủ Hải
			"chùa bửu lâm cổ tự": "ChIJ6QIStsKvCjERBUDapAHM2cw", # Chùa Bửu Lâm
			"chùa vĩnh tràng": "ChIJta3nNcOvCjERoOKB8r_TatI", # Vĩnh Tràng Temple
			"chợ nổi cái bè": "ChIJrf99g7mbCjERS9JQbHEwGYs", # Cai Be Floating Market
			"đình mỹ lương": "ChIJPYZA4KSFCjER3PsNVvTfMZw", #Di tích kiến trúc nghệ thuật Đình Mỹ lương
			"khu du lịch cù lao thới sơn": "ChIJP9pN8XOlCjERjGW3TFsjqdo", # Khu du lịch Thới Sơn
			"đình long trung": "ChIJAQAAAPyYCjERkIxmY9HWZec", # Ubnd Xã Long Trung
			"đình điều hòa": "ChIJo8IrB-qvCjERqxY00sDHZAY", # Đình Điều Hòa
			"vườn hoa mãn đình hồng": "ChIJ78yEU0ulCjERz-IvJKSB0oo", # Vườn hoa Mãn Đình Hồng
			"chùa sắc tứ linh thứu": "ChIJz-buHiulCjERgNBnHbSpFqw", # Chùa Sắc Tứ Linh Thứu (Long Tuyền Tự)
			"làng tre": "ChIJLfRfhzKFCjERg0BY7rghkwE", # Làng Tre Cái Bè
		}

	def run(
		self,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any],
		) -> List[Dict]:

		desPlace = tracker.get_slot('loc_travel')

		if desPlace in self.location_travel().keys():
			placeID = self.location_travel()[desPlace]
		else:
			# do something when not have desPlace in db
			placeID = None
			pass
		print(placeID)

		import yaml
		import requests
		import json
		#retrieve google api key		
		with open("./ga_credentials.yml", 'r') as ymlfile:
			cfg = yaml.safe_load(ymlfile)
		key = cfg['credentials']['GOOGLE_KEY']

		# get user's current location	
		get_origin = requests.post(
			"https://www.googleapis.com/geolocation/v1/geolocate?key={}".format(key)).json()
		
		origin_lat = get_origin['location']['lat']
		origin_lng = get_origin['location']['lng']

		attachment = "https://www.google.com/maps/embed/v1/directions?origin={},{}&destination=place_id:{}&key={}".format(origin_lat, origin_lng, placeID, key)
		dispatcher.utter_attachment(attachment=attachment)
		
		return []



