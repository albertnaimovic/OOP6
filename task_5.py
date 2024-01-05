# Create a SpaceStation class with the following specifications:

# The SpaceStation class should have an attribute astronauts which is a list of dictionaries.
# Each dictionary represents an astronaut and has keys: name, nationality, and mission_duration.
# It should have an instance method add_astronaut that takes a name, nationality, and mission duration, creates a new astronaut dictionary, and adds it to the astronauts list.
# It should have an instance method find_astronaut that takes a name and returns the astronaut dictionary with that name, or None if no such astronaut is found.
# Add a class method from_astronaut_list that takes a list of astronauts (each represented as a dictionary) and returns a new SpaceStation instance with those astronauts.
# Add a static method is_long_term_mission that takes an astronaut dictionary and returns True if the astronaut's mission duration is more than 6 months, and False otherwise.
# Add an instance method remove_astronaut that takes a name and removes the astronaut with that name from the astronauts list.


class SpaceStation:
    ASTROUNAUTS: list[dict] = []

    # def __init__(self) -> None:
    #     pass

    def add_astronaut(name: str, nationality: str, mission_duration: int) -> None:
        SpaceStation.ASTROUNAUTS.append(
            {
                "name": name,
                "nationality": nationality,
                "mission_duration": mission_duration,
            }
        )

    def find_astronaut(name: str) -> dict:
        result = [
            astronaut
            for astronaut in SpaceStation.ASTROUNAUTS
            if astronaut["name"] == name
        ]
        if result:
            return result[0]
        else:
            None

    def remove_astronaut(name: str) -> None:
        result = SpaceStation.find_astronaut(name)
        if result:
            SpaceStation.ASTROUNAUTS.remove(result)

# Add a class method from_astronaut_list that takes a list of astronauts (each represented as a dictionary) and returns a new SpaceStation instance with those astronauts.
# Add a static method is_long_term_mission that takes an astronaut dictionary and returns True if the astronaut's mission duration is more than 6 months, and False otherwise.
# Add an instance method remove_astronaut that takes a name and removes the astronaut with that name from the astronauts list.

    @classmethod
    def from_astronaut_list(cls, astronauts) -> "SpaceStation":
        pass

    @staticmethod
    def is_long_term_mission():
        pass


SpaceStation.add_astronaut(name="Jonas", nationality="LT", mission_duration=50)
SpaceStation.add_astronaut(name="Thomas", nationality="US", mission_duration=46)
SpaceStation.add_astronaut(name="Kawasaki", nationality="CN", mission_duration=98)

print(SpaceStation.find_astronaut("Thomas"))
SpaceStation.remove_astronaut("Thomas")
print(SpaceStation.find_astronaut("Thomas"))
