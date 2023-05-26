#split_string.py

def parsed_encoded_string(encoded_string):
    parsed_data = {}

    try:
        #split string into segments
        segments = encoded_string.split("000")

        #extract first name, last name and Id

        parsed_data["first_name"] = segments[0]
        parsed_data["last_name"]  = segments[1]
        parsed_data["Id"] = int(segments[2])


    except  Exception as e:
        print(f"Invalid encoded string format : {e}")
    

    return parsed_data

encoded_string = input("Enter the encoded string:  ")
parsed_data = parsed_encoded_string(encoded_string)

if parsed_data:
    print(parsed_data)
