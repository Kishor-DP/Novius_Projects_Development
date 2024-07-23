import random
from EventLogger2 import app_event
import string



# Define a function to generate random code
def generate_code(length):
    # Define the character set from which to generate the code
    characters = string.ascii_letters + string.digits
    # Generate a random code of specified length
    return ''.join(random.choice(characters) for _ in range(length))


def generated_code_trigger():
    global generated_code
    # Generate the code
    code_length = 10
    generated_code = generate_code(code_length)
    stored_generated_code = generated_code
    #print("Generated Codeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee:", generated_code)
    app_event.debug("Generated code: %s", generated_code)
    
    #generated_code_trigger()
    return generated_code
    

# Example usage:
generated_code = generated_code_trigger()
# Each time you call generated_code_trigger(), it will generate and return a new code
print("New generated code:", generated_code)

