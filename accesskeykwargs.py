def get_country(**kwargs):
    if "country" in kwargs:
        print("Country:", kwargs["country"])
    else:
        print("Country not found")

get_country(name="John", age=25, city="New York", country="USA", job="Engineer")