from BaseClasses import ItemClassification, Location, Region, CollectionState
from dataclasses import dataclass
from typing import Callable, Optional
from worlds.AutoWorld import World


@dataclass(frozen=True)
class LocationData:
    region: str
    id: int
    rule: Optional[Callable[[CollectionState, int], bool]] = None
    
class POPWWWorld(World):
    game = "POPWW"

class POPWWLocation(Location):
    game = "POPWW"
    
    
location_table: dict[str,LocationData] = {
    "Sandwraith Mask": LocationData("Sacred Caves", id = 1),
    "Wooden Stick": LocationData("Beach", id = 2),
    "Spider Sword": LocationData("Fortress Entrance (Past)", id = 3),
    "Serpend Sword": LocationData("Hourglass Room", id = 4),
    "Lion Sword": LocationData("Main Hall", id = 5, rule = lambda state, player: state.has("One Tower Activated",player)),
    "Scorpion Sword": LocationData("Prison (Past)", id = 6),
    "Water Sword": LocationData("Hourglass Room",id = 7, rule = lambda state, player: state.has("Health Upgrade",player,9)),
    #Secondary Weapons
    #Axes
    "Airyaman - Axe": LocationData("Beach",id = 8),
    "Allatum - Axe":  LocationData("",id = 9),
    "Natat - Axe":  LocationData("",id = 10),
    "Apaosa - Axe":  LocationData("",id = 11),
    "Vahishta - Axe":  LocationData("",id = 12),
    "Vidatu - Axe":  LocationData("",id = 13),
    "Ahura (Fork)- Axe":  LocationData("",id = 14),
    "Drvaspa - Axe":  LocationData("",id = 15),
    "Apam - Axe":  LocationData("",id = 16),
    "Ereta - Axe":  LocationData("",id = 17),
    "Mainyu - Axe":  LocationData("",id = 18),
    "Ahura (Scythe) - Axe":  LocationData("",id = 19),
    "Bahram - Axe":  LocationData("",id = 20),
    "Spentas - Axe":  LocationData("",id = 21),
    #Swords
    "Buyasta - Sword":  LocationData("Beach",id = 22),
    "Zarich - Sword":  LocationData("",id = 23),
    "Haoma - Sword":  LocationData("",id = 24),
    "Spenta - Sword":  LocationData("",id = 25),
    "Yasht - Sword":  LocationData("",id = 26),
    "Vanant - Sword":  LocationData("",id = 27),
    "Kerena - Sword":  LocationData("",id = 28),
    "Camros - Sword":  LocationData("",id = 29),
    "Fravashis - Sword":  LocationData("",id = 30),
    "Tasan - Sword":  LocationData("",id = 31),
    "Asto - Sword":  LocationData("",id = 32),
    "Agas - Sword":  LocationData("",id = 33),
    "Srosh - Sword":  LocationData("",id = 34),
    "Rustam - Sword":  LocationData("",id = 35),
    "Mainyu - Sword":  LocationData("",id = 36),
    "Mahre - Sword":  LocationData("",id = 37),
    "Dena - Sword":  LocationData("",id = 38),
    "Asman - Sword":  LocationData("",id = 39),
    #Maces
    "Peris - Mace":  LocationData("Beach",id = 40),
    "Zend - Mace":  LocationData("",id = 41),
    "Vata - Mace":  LocationData("",id = 42),
    "Sraosa - Mace":  LocationData("",id = 43),
    "Menog - Mace":  LocationData("",id = 44),
    "Baga - Mace":  LocationData("",id = 45),
    "Yima - Mace":  LocationData("",id = 46),
    "Izha - Mace":  LocationData("",id = 47),
    #Daggers
    "Khara - Dagger":  LocationData("",id = 48),
    "Indra - Dagger":  LocationData("",id = 49),
    "Abathur - Dagger":  LocationData("",id = 50),
    "Armaiti - Dagger":  LocationData("",id = 51),
    "Yazata - Dagger":  LocationData("",id = 52),
    "Vanishta - Dagger":  LocationData("",id = 53),
    #Secret Weapons
    "Teddy Bear":  LocationData("",id = 54),
    "Glove":  LocationData("",id = 55),
    "Pink Flamingo":  LocationData("",id = 56),
    "Hockey Stick":  LocationData("",id = 57),
    "Light Sword":  LocationData("",id = 58),
    #Chests
    "Secret Chest 1 - Beach (Present) near the stairs": LocationData("Beach",id =  59),
    "Secret Chest 2 - Beach (Present) on the platform above the pillars": LocationData("Beach",id = 60),
    "Secret Chest 3 - Fortress Entrance (Past) on the platform when climbing the pillar": LocationData("Fortress Entrance (Past)",id = 61),
    "Secret Chest 4 - Fortress Entrance (Past) near the health upgrade entrance": LocationData("Fortress Entrance (Past)",id = 62),
    "Secret Chest 5 - Southern Passage (Past) left platform at ground level":  LocationData("Southern Passage (Past)",id = 63),
    "Secret Chest 6 - Southern Passage (Past) left platform at top level":  LocationData("Southern Passage (Past)",id = 64),
    "Secret Chest 7 - Sacrificial Altar (Past) right after the stairs":  LocationData("Sacrificial Altar",id = 65),
    "Secret Chest 8 - Hourglass Room left of the stairs":  LocationData("Hourglass Room",id = 66),
    "Secret Chest 9 - Main Hall (Past) top of the platform to the Mechanical Tower": LocationData("Main Hall",id = 67),
    "Secret Chest 10 - Mechanical Tower Entrance (Past) after the Brute":  LocationData("Mechanical Tower Entrance",id = 68),
    "Secret Chest 11 - Mechanical Pit (Past) Lone room with a raider": LocationData("Mechanical ¨Pit (Past)",id = 69),
    "Secret Chest 12 - Mechanical Pit (Past) balcony through the ledge, after the big wheel": LocationData("Mechanical Pit (Past)",id = 70),
    "Secret Chest 13 - Mechanical Pit (Past) up the ladder in the gated room":  LocationData("Mechanical Pit (Past)",id = 71),
    "Secret Chest 14 - Mechanical Pit (Past next to the Sandwraith lever": LocationData("Mechanical Pit (Past)",id = 72),
    "Secret Chest 15 - Mechanical Pit (Past) behind the wall of the Brute room": LocationData("Mechanical Pit (Past)",id = 73),
    "Secret Chest 16 - Activation Room (Past) climb the wall on the left of the entrance": LocationData("Acitvation Room (Past)",id = 74),
    "Secret Chest 17 - Activation Room (Past) behind a wall broken by a thrown beast, close to the brute on its left": LocationData("Activation Room (Past)",id = 75),
    "Secret Chest 18 - Activation Room (Past) behing a small window on a giant gear axle": LocationData("Activation Room (Past)",id = 76),
    "Secret Chest 19 - Main Hall (Past) on top of the platform to the Garden Tower": LocationData("Main Hall",id = 77),
    "Secret Chest 20 - Garden Tower Entrance in the pit leading to the hall": LocationData("Garden Tower Entrance",id = 78),
    "Secret Chest 21 - Garden Hall (Past) near the left statue":  LocationData("Garden Hall (Past)",id = 79),
    "Secret Chest 22 - Garden Hall (Past) behind a wall before climbing up the trees": LocationData("Garden Hall (Past)",id = 80),
    "Secret Chest 23 - Garden Hall (Past) climbing down the wall at the back":  LocationData("Garden Hall (Past)",id = 81),
    "Secret Chest 24 - Garden Waterworks (Present) small room opposite to the crowmaster":  LocationData("Garden Waterworks (Present)",id = 82),
    "Secret Chest 25 - Garden Waterworks (Past) left of the garden at the back":  LocationData("Garden Waterworks (Past)",id = 83),
    "Secret Chest 26 - Garden Waterworks (Past) before the lever":  LocationData("Garden Waterworks (Past)",id = 84),
    "Secret Chest 27 - Garden Hall (Past) next to the button": LocationData("Garden Hall (Past)",id = 85),
    "Secret Chest 28 - Garden Hall (Past) wall jump after the rope on the left": LocationData("Garden Hall (Past)",id = 86),
    "Secret Chest 29 - Throne Room (Past) next to the first left statue":  LocationData("Throne Room (Past)",id = 87),
    "Secret Chest 30 - Throne Room (Past) next to the second right statue": LocationData("Throne Room (Past)",id = 88),
    "Secret Chest 31 - Catacombs ground level": LocationData("Catacombs",id = 89),
    "Secret Chest 32 - Catacombs after escaping the Dahaka":  LocationData("Catacombs",id = 90),
    "Secret Chest 33 - Prison (Past) inside a cell on the left": LocationData("Prison (Past)",id = 91),
    "Secret Chest 34 - Prison (Past) inside a cell in the room with a pillar at the center":  LocationData("Prison (Past)",id = 92),
    "Secret Chest 35 - Prison (Past) on top of the ladder after the golem": LocationData("Prison (Past)",id = 93),
    "Secret Chest 36 - Library (Past) on the left after the ladder":  LocationData("Library (Past)",id = 94),
    "Secret Chest 37 - Library (Past) going through the big hole in the wall": LocationData("Library (Past)",id = 95),
    "Secret Chest 38 - Library (Past) falling from a wooden beam before the machanical tower": LocationData("Library (Past)",id = 96),
    "Secret Chest 39 - Southern Passage (Past) behind the cracked gate":  LocationData("Southern Passage (Past)",id = 97,rule = lambda state, player: state.has("Scorpion Sword",player)),
    "Secret Chest 40 - Sacrificial Altar just right of the entrance": LocationData("Sacrificial Altar",id = 98),
    "Secret Chest 41 - Garden (Past) behing the cracked wall above the entrance":  LocationData("",id = 99,rule = lambda state, player: state.has("Scorpion Sword",player)),
    "Secret Chest 42 - Sacred Caves (Past) just before the griffin": LocationData("Sacred Caves (Past)",id = 100),
    "Secret Chest 43 - Garden Waterworks (Past) at the end of the bridge": LocationData("Garden Waterworks (Past)",id = 101),
    "Secret Chest 44 - Cliff (Past) before jumping on the falling pillars":  LocationData("Cliff (Past)",id = 102),
    "Secret Chest 45 - Cliff (Past) before the breakable wall": LocationData("Cliff (Past)",id = 103),
    "Secret Chest 46 - Fortress Entrance (Past) backtrack after throwing yourself an axe": LocationData("Fortress Entrance (Past)",id =  104),
    "Secret Chest 47 - Foundry (Past) behind the button on the right": LocationData("Foundry (Past)",id = 105),
    "Secret Chest 48 - Foundry (Past) on the left": LocationData("Foundry (Past)",id = 106),
    "Secret Chest 49 - Foundry (Past) on the platform at the far end of the room": LocationData("Foundry (Past)",id = 107),
    "Secret Chest 50 - Mystic Caves (Past) on a ledge after a jump": LocationData("Mystic Caves (Past)",id = 108),
    #Health Upgrades
    "Health Upgrade 1 - Fortess Entrance (Past)": LocationData("Fortresse Entrance (Past)",id = 109),
    "Health Upgrade 2 - Sacrificial Altar (Past)": LocationData("Sacrificial Altar",id = 110),
    "Health Upgrade 3 - Main Hall (Past)": LocationData("Main Hall",id = 111),
    "Health Upgrade 4 - Activation Room (Past)": LocationData("Activation Room (Past)",id = 112),
    "Health Upgrade 5 - Garden (Past)": LocationData("Garden (Past)",id = 113),
    "Health Upgrade 6 - Garden Waterworks (Past)": LocationData("Garden Waterworks (Past)",id = 114),
    "Health Upgrade 7 - Prison (Past)":  LocationData("Prison (Past)",id = 115,rule = lambda state, player: state.has("Scorpion Sword",player)),
    "Health Upgrade 8 - Library (Past)":  LocationData("Library (Past)",id = 116),
    "Health Upgrade 9 - Southern Passage (Past)":  LocationData("Southern Passage (Past)",id = 117,rule = lambda state, player: state.has("Scorpion Sword",player)),
    #Boss progression
    "Lose to Shadee":  LocationData("Boat",id = 117),
    "Beat Shadee":  LocationData("Sacrificial Altar",id = 118),
    "Beat Kaileena": LocationData("Throne Room",id = 119),
    "Beat the Griffin": LocationData("Sacred Caves",id = 120),
    "Beat Kaileena again":  LocationData("Sacred Caves",id = 121),
    "Beat the Dahaka":  LocationData("Sacred Caves",id = 122),
    #Time portals which unlock time powers
    "Time Portal - Fortress Entrance (Present)":  LocationData("Fortress Entrance (Present)",id = 123), #Recall
    "Time Portal - Sacrificial Altar (Past)": LocationData("Sacrificial Altar",id = 124), #Eye of the Storm = slow down time
    "Time Portal - Mechanical Tower (Past)":  LocationData("Mechanical Tower (Past)",id = 125), #Breath of Fate = sand wave
    "Time Portal - Activation Room (Present":  LocationData("Activation Room (Present)",id = 126), #Additional Sand Tank
    "Time Portal - Garden Tower (Past)": LocationData("Garden Hall (Past)",id = 127), #Ravage of time = quick attacks in slowed time
    "Time Portal - Garden Waterworks (Present)": LocationData("Garden Waterworks (Present)",id = 128), #Additional Sand Tank
    "Time Portal - Prison (Present)": LocationData("Prison (Present)",id = 129), #Wind of Fate = Breath of Fate upgrade
    "Time Portal - Throne Room (Past)": LocationData("Throne Room (Past)",id = 130,rule = lambda state, player: state.has("Kaileena Defeated" and "Scorpion Sword",player)), #Additional Sand Tank
    "Time Portal - Sacred Caves (Present)": LocationData("Sacred Caves",id = 131), #Cyclone of Fate = Final Breath of Fate upgrade
}    
    
event_table: dict[str, LocationData(Region, id)]

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int| None]:
    return {location_name: location_table[location_name] for location_name in location_names}


    
