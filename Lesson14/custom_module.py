from random import choice

capital = "Dhaka"
bird = "Magpie"
flower = "Water Lily"
song = "Bangladeshi Song"

def randomfunfact():
    funfact = [
        "Dhaka is known as the rickshaw capital of the world, with over 800,000 rickshaw pullers in the city.",
        "The University of Dhaka, established in 1921, is the oldest active university in Bangladesh. ",
        "Dhaka was originally named Jahangirnagar, after the Mughal Emperor Jahangir, when it became the capital of the Bengal Subah in 1610.",
        "Dhaka is also known as the 'City of Mosques' and the 'City of Muslin'."
    ]
    return choice(funfact)

# prevent running the function if the file is just imported
if __name__ == "__main__":
    print(randomfunfact())