## hello
* greet
    - utter_greet
    
## happy path direct help
* direct_and_help
    - utter_ask_help
    - utter_after_ask_help
* find_location{"name_location":"nhà hàng"}
    - action_place_search
    - utter_after_search_res1
* find_location{"name_location":"nhà hàng", "num_dis":"2000"}
    - action_place_search
    - utter_after_search_res2
* request_inform_common_location_travel
    - utter_inform_common_location_travel
    - utter_after_inform_common_location_travel
* request_inform_detail_location_travel{"loc_travel":"chợ hoa mỹ tho"}
    - utter_show_cho_hoa_mytho
    - utter_more_inform_cho_hoa_mytho
* direct_chmt{"loc_travel":"chợ hoa mỹ tho"}
    - action_direction_place
    - utter_after_direct_chmt
* what_can_help
    - utter_what_help
* request_event
    - utter_show_event
* thankyou
    - utter_noworries


## book res
* book_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
    - form{"name": null}
    - utter_confirm_res
* affirm
    - action_confirm_restaurant
* thankyou
    - utter_noworries


## book res
* book_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
    - form{"name": null}
    - utter_confirm_res
* edit_form_res
    - utter_edit_inform_res
* edit_res
    - form_edit_res
    - form{"name": "form_edit_res"}
    - form{"name": null}
    - restart_form_edit_res
    - utter_confirm_after_edit_res
* edit_form_res
    - utter_edit_inform_res
* edit_res
    - form_edit_res
    - form{"name": null}
    - restart_form_edit_res
    - utter_confirm_after_edit_res
* affirm
    - action_confirm_restaurant


## Generated Story 21692699625902188
* book_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "num_people_res"}
* form: book_restaurant{"num_people_res": "4"}
    - form: restaurant_form
    - slot{"num_people_res": "4"}
    - slot{"requested_slot": "add_request_res"}
* form: deny
    - form: restaurant_form
    - slot{"add_request_res": "No"}
    - slot{"requested_slot": "phone_res"}
* form: book_restaurant
    - form: restaurant_form
    - slot{"phone_res": "090909090"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_confirm_res
* edit_form_res
    - utter_edit_inform_res
* edit_res{"edit_inform_res": "số người"}
    - slot{"edit_inform_res": "số người"}
    - form_edit_res
    - form{"name": "form_edit_res"}
    - slot{"requested_slot": "edit_num_people_res"}
* form: book_restaurant{"num_people_res": "3"}
    - form: form_edit_res
    - slot{"edit_num_people_res": "3"}
    - slot{"num_people_res": "3"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - restart_form_edit_res
    - slot{"edit_inform_res": null}
    - slot{"edit_num_people_res": null}
    - slot{"edit_inform_res": null}
    - slot{"edit_add_request_res": null}
    - utter_confirm_after_edit_res
* edit_form_res
    - utter_edit_inform_res
* edit_res{"edit_inform_res": "số người"}
    - slot{"edit_inform_res": "số người"}
    - form_edit_res
    - form{"name": "form_edit_res"}
    - slot{"requested_slot": "edit_num_people_res"}
* form: book_restaurant
    - form: form_edit_res
    - slot{"edit_num_people_res": "2"}
    - slot{"num_people_res": "2"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - restart_form_edit_res
    - slot{"edit_inform_res": null}
    - slot{"edit_num_people_res": null}
    - slot{"edit_inform_res": null}
    - slot{"edit_add_request_res": null}
    - utter_confirm_after_edit_res
* affirm
    - action_confirm_restaurant

##search perfect
* request_hottel
    - hottel_form
    - form{"name": "hottel_form"}
    - form{"name": null}    
    - utter_slots_values_ht
    - action_restart
* affirm    
    - action_yes_sure
    - action_search_hottel
* deny 
    - action_no_sure
    - action_search_hottel    

## thanksyou
* thankyou
    - utter_noworries
    - action_restart
