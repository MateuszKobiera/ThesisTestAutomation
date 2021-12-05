def property_data():
    return dict(image="", name="Sukiennice", town="Kraków",
                address1="Rynek Główny", address2="121212", country="AF", state="", gpslat=0, gpslon=0,
                surfacegross=123, people=123, tags=["bos:site:type:other", "bos:usage:government"],
                templateId="")


def building_data():
    return dict(name="Budynek", parentIds=[
        "321dd0e5-5e57-4209-9169-771e5408169a"
    ], surfacenet="123", surfacegross="123", people="123", tags=[
        "bos:building",
        "bos:usage:university"
    ], templateId="")


def floor_data():
    return dict(name="Piętro", parentIds=[
        "25617dbd-681f-4eb0-a0b5-60c395301523"
    ], level="1", surfacenet="123", surfacegross="123", people="123", tags=[
        "bos:structure:floor",
        "bos:usage:cinema"
    ], templateId="")

