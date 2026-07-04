def add_setting(settings_dict,my_tup):
    key,value = my_tup
    key = key.lower()
    value = value.lower()
    if key in settings_dict:
        return (f"Setting '{key}' already exists! Cannot add a new setting with this name.")
    settings_dict[key] = value
    return (f"Setting '{key}' added with value '{value}' successfully!")
    
test_settings = {"Name":"Steve"`}
``
def update_setting(settings_dict,my_tup):
    key,value = my_tup
    key = key.lower()
    value = value.lower()
    if key not in settings_dict:
        return (f"Setting '{key}' does not exist! Cannot update a non-existing setting.")
    settings_dict[key] = value
    if key in settings_dict:
        return (f"Setting '{key}' updated to '{value}' successfully!")

def delete_setting(settings_dict,key):
    key = key.lower()
    if key in settings_dict:
        settings_dict.pop(key)
        return (f"Setting '{key}' deleted successfully!")
    else:
        return "Setting not found!"

def view_settings(settings_dict):
    if len(settings_dict) == 0:
        return "No settings available."

    new_string = "Current User Settings:\n"

    for key,value in settings_dict.items():
        cap_key = key.capitalize()
        new_string += f"{cap_key}: {value}\n"
    return new_string
