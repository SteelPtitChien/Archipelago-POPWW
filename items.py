from __future__ import annotations

from typing import TYPE_CHECKING, List, Dict, Set

from BaseClasses import Item, ItemClassification

from enum import Enum


if TYPE_CHECKING:
    from .world import POPWWWorld


ITEM_NAME_TO_ID = {
    "Primary Sword":1,
    "Secondary Weapon":2,
    "Sand Power": 3,
    "Health Upgrade": 4,
    
    }
#Filler/Trap need to be included, add them later
#Perhaps need to differentiate the sand powers, although upgrades will be in the same category

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Primary Sword": ItemClassification.progression,
    "Secondary Weapon": ItemClassification.useful,
    "Sand Power": ItemClassification.useful,
    "Health Upgrade": ItemClassification.progressive #Might be considered useful if separated from water sword/ having Kaileena as goal
      
    }

class ItemType(Enum):
    Primary_Sword = 0
    Secondary_Weapon = 1
    Sand_Tank = 2
    Sand_Power = 3
    Health_Upgrade = 4
    Sandwraith_Mask = 5
    



class POPWWItem:
    name: str
    type: ItemType
    tracker_strings: List[str] = None
    
def get_random_filler_item(world: POPWWWorld) -> str:
    
    if world.random.randing(0,99) < world.options.trap_chance:
        return "Trap"
    return "Filler"
#Add all filler and traps/ create a list with them


def create_item_with_correct_classification(world: POPWWWorld, name:str) -> POPWWItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    
    return POPWWItem(name, classification,ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: POPWWWorld) -> None:
    
    itempool: list[Item]
    
item_list: List[POPWWItem] = [
    
    POPWWItem("Progressive Health Upgrade ", ItemType.Health_Upgrade, ["progressive"]),
  
    
    POPWWItem("Wooden Stick", ItemType.Primary_Sword, ["progressive"]),
    POPWWItem("Spider Sword", ItemType.Primary_Sword, ["progressive"]),
    POPWWItem("Serpent Sword", ItemType.Primary_Sword, ["progressive"]),
    POPWWItem("Lion Sword", ItemType.Primary_Sword, ["progressive"]),
    POPWWItem("Scorpion Sword", ItemType.Primary_Sword, ["progressive"]),
    POPWWItem("Water Sword", ItemType.Primary_Sword, ["progressive"]),
    
    
    POPWWItem("Airyaman - Axe", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Natat - Axe", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Apaosa - Axe", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Vahishta - Axe", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Vidatu - Axe", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Ahura (Fork) - Axe", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Drvaspa - Axe", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Apam - Axe", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Ereta - Axe", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Mainyu - Axe", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Ahura (Scythe) - Axe", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Bahram - Axe", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Spentas - Axe", ItemType.Secondary_Weapon, ["Useful"]),

    
    POPWWItem("Buyasta - Sword", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Zarich - Sword", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Haoma - Sword", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Spenta - Sword", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Yasht - Sword", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Vanant - Sword", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Kerena - Sword", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Camros - Sword", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Fravashis - Sword", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Tasan - Sword", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Asto - Sword", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Agas - Sword", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Srosh - Sword", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Rustam - Sword", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Mainyu - Sword", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Mahre - Sword", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Dena - Sword", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Asman - Sword", ItemType.Secondary_Weapon, ["Useful"]),
    
    
    POPWWItem("Peris - Mace", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Zend - Mace", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Vata - Mace", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Sraosa - Mace", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Menog - Mace", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Baga - Mace", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Yima - Mace", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Izha - Mace", ItemType.Secondary_Weapon, ["Useful"]),
    
    
    POPWWItem("Khara - Dagger", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Indra - Dagger", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Abathur - Dagger", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Armaiti - Dagger", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Yazata - Dagger", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Vanishta - Dagger", ItemType.Secondary_Weapon, ["Useful"]),
    
    POPWWItem("Teddy Bear", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Glove", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Pink Flamingo", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Hockey Stick", ItemType.Secondary_Weapon, ["Useful"]),
    POPWWItem("Light Sword", ItemType.Secondary_Weapon, ["Useful"]),
    
    POPWWItem(("Kaileena's sword"), ItemType.Secondary_Weapon, ["Useful"]),

    
    POPWWItem("Sandwraith Mask", ItemType.Sandwraith_Mask, ["progressive"]),
    
    POPWWItem("Progressive Sand Tank", ItemType.Sand_Tank, ["Useful"]),
    
    POPWWItem("Recall", ItemType.Sand_Power,["Useful"]),
    POPWWItem("Eye of the Storm", ItemType.Sand_Power, ["progressive"]),
    POPWWItem("Progressive Cyclone of Fate", ItemType.Sand_Power, ["Useful"]),
    POPWWItem("Ravage of Time", ItemType.Sand_Power, ["Useful"]),
    
        
    
    
    ]