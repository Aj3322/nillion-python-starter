from nada_dsl import *

def nada_main():
    # Define the party involved in the computation
    party1 = Party(name="Party1")

    # Define the secret integers as inputs
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform computation: multiply my_int1 and my_int2
    result = my_int1 * my_int2

    # Return the result of the computation as the output
    return [Output(result, "product_output", party1)]
