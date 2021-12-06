def property_data():
    return dict(image="", name="Sukiennice", town="Kraków",
                address1="Rynek Główny", address2="121212", country="AF", state="", gpslat=0, gpslon=0,
                surfacegross=123, people=123, tags=["bos:site:type:other", "bos:usage:government"],
                templateId="")


def building_data():
    return dict(name="Budynek", parentIds=[""], surfacenet="123", surfacegross="123", people="123", tags=[
        "bos:building",
        "bos:usage:university"
    ], templateId="")


def floor_data():
    return dict(name="Piętro", parentIds=[""], level="1", surfacenet="123", surfacegross="123", people="123", tags=[
        "bos:structure:floor",
        "bos:usage:cinema"
    ], templateId="")

