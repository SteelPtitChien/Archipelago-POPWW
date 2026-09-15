from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import POPWWWorld
    
def create_and_connect_regions(world: POPWWWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: POPWWWorld) -> None:
    
    
    Beach = Region("Beach", world.player, world.multiworld)

    Fortress_Entrance_Present = Region("Fortress Entrance (Present)", world.player, world.multiworld)
    Fortress_Entrance_Past = Region("Fortress Entrance (Past)", world.player, world.multiworld)

    Main_Hall = Region("Main Hall", world.player, world.multiworld)

    Southern_Passage_Present = Region("Southern Passage (Present)", world.player, world.multiworld)
    Southern_Passage_Past = Region("Southern Passage (Past)", world.player, world.multiworld)

    Sacrificial_Altar = Region("Sacrificial Altar", world.player, world.multiworld)

    Mechanical_Tower_Entrance = Region("Mechanical Tower Entrance", world.player, world.multiworld)
    Mechanical_Pit_Present = Region("Mechanical Pit (Present)", world.player, world.multiworld)
    Mechanical_Pit_Past = Region("Mechanical Pit (Past)", world.player, world.multiworld)
    Activation_Room_Present = Region("Activation Room (Present)", world.player, world.multiworld)
    Activation_Room_Past = Region("Activation Room (Past)", world.player, world.multiworld)

    Garden_Tower_Entrance = Region("Garden Tower Entrance",world.player, world.multiworld)
    Garden_Hall_Present = Region("Garden Hall (Present)", world.player, world.multiworld)
    Garden_Hall_Past = Region("Garden Hall (Past)", world.player, world.multiworld)
    Garden_Waterworks_Present = Region("Garden Waterworks (Present)", world.player, world.multiworld)
    Garden_Waterworks_Past = Region("Garden Waterworks (Past)", world.player, world.multiworld)

    Hourglass_Room = Region("Hourglass Room", world.player, world.multiworld)

    Throne_Room = Region("Throne Room", world.player, world.multiworld)

    Catacombs = Region("Catacombs", world.player, world.multiworld)

    Prison_Present = Region("Prison (Present)", world.player, world.multiworld)
    Prison_Past = Region("Prison (Past)", world.player, world.multiworld)

    Library_Present = Region("Library (Present)", world.player, world.multiworld)
    Library_Past = Region("Library (Past)", world.player, world.multiworld)

    Mystic_Caves = Region("Mystic Caves", world.player, world.multiworld)

    Sacred_Caves_Present = Region("Sacred Caves (Present)", world.player, world.multiworld)
    Sacred_Caves_Past = Region("Sacred Caves (Past)", world.player, world.multiworld)
    
    


def connect_regions(world: POPWWWorld) -> None:
    Beach = world.get_region("Beach")
    
    Fortress_Entrance_Present = world.get_region("Fortress Entrance (Present)")
    Fortress_Entrance_Past = world.get_region("Fortress Entrance (Past)")
    
    Main_Hall = world.get_region("Main Hall")
    
    Southern_Passage_Present = world.get_region("Southern Passage (Present)")
    Southern_Passage_Past = world.get_region("Southern Passage (Past)")
    
    Sacrificial_Altar = world.get_region("Sacrificial Altar")
    
    Mechanical_Tower_Entrance = world.get_region("Mechanical Tower Entrance")
    Mechanical_Pit_Present = world.get_region("Mechanical Pit (Present)")
    Mechanical_Pit_Past = world.get_region("Mechanical Pit (Past)")
    Activation_Room_Present = world.get_region("Activation Tower (Present)")
    Activation_Room_Past = world.get_region("Activation Tower (Past)")
    
    
    Garden_Tower_Entrance = world.get_region("Garden Tower Entrance")
    Garden_Hall_Present = world.get_region("Garden Hall (Present)")
    Garden_Hall_Past = world.get_region("Garden Hall (Past)")
    Garden_Waterworks_Present = world.get_region("Garden Waterworks (Present)")
    Garden_Waterworks_Past = world.get_region("Garden Waterworks (Past)")
    
    Hourglass_Room = world.get_region("Hourglass Room")
    Throne_Room = world.get_region("Throne Room")
    
    Catacombs = world.get_region("Catacombs")
    
    Prison_Present = world.get_region("Prison (Present)")
    Prison_Past = world.get_region("Prison (Past)")
    Library_Present = world.get_region("Library (Present)")
    Library_Past = world.get_region("Library (Past)")
    
    Mystic_Caves = world.get_region("Mystic Caves")
    
    Sacred_Caves_Present = world.get_region("Sacred Caves (Present)")
    Sacred_Caves_Past = world.get_region("Sacred Caves (Past)")
    
    #This is the ugly part: connecting all regions together. And gates are oneway, so I need to define A-> B and B-> A 
    Free_Connection = [(Beach, Fortress_Entrance_Present),(Fortress_Entrance_Present,Fortress_Entrance_Past),(Mechanical_Pit_Past, Mechanical_Pit_Present),(Mechanical_Pit_Present,Activation_Room_Present),(Activation_Room_Present,Activation_Room_Past),(Activation_Room_Past,Mechanical_Pit_Past),(Garden_Hall_Past, Garden_Hall_Present),(Garden_Hall_Present, Garden_Waterworks_Present),(Garden_Waterworks_Present, Garden_Waterworks_Past),(Sacrificial_Altar, Southern_Passage_Present),(Main_Hall,Southern_Passage_Past)]
    Free_Connection_Names = [("Beach to Fortress Entrance", "Fortress Entrance to the Beach"),("Time Portal in Fortress Entrance (Present","Time Portal in Fortress Entrance (Past)"), ("Time Portal in Mechanical Pit (Past)", "Time Portal in Mechanical Pit (Present)"),("Mechanical Pit (Present) to Activation Room (Present)","Activation Room (Present) to Mechanical Pit (Present)"),("Time Portal in Activation Room (Present)", "Time Portal in Activation Room (Past)"),("Activation Room (Past) to Mechanical Pit (Past", "Mechanical Pit (Past) to Activation Room (Past)"),("Time Portal in Garden Hall (Past)", "Time Portal in Garden Hall (Present)"),("Garden Tower (Present) to Garden Waterworks (Present)", "Garden Waterworks (Present) to Garden Tower (Present)"),("Time Portal in Garden Waterworks (Present)", "Time Portal in Garden Waterworks (Past)"),("Time Portal in Sacrificial Altar", "Time Portal in Southern Passage"),("Main Hall to Southern Passage (Past)","Southern Passage (Past) to Main Hall" )  ]
    
    for i in range(0, len(Free_Connection)):
        (a,b) = Free_Connection[i]
        (A,B) = Free_Connection_Names[i]
        a.connect(b,A)
        b.connect(a,B)
    
    #Entrances with Conditions
    Conditionnal_Connections = [(Main_Hall,Mechanical_Tower_Entrance),(Main_Hall, Garden_Tower_Entrance),(Mechanical_Tower_Entrance,Mechanical_Pit_Past),(Garden_Tower_Entrance, Garden_Hall_Past),(Main_Hall, Hourglass_Room)]
    Conditionnal_Connections_Names = [("Main Hall to Mechanical Tower","Mechanical Tower to Main Hall"),("Main Hall to Garden Tower Entrance", "Garden Tower Entrance to Main Hall"),("Mechanical Tower Entrance to Mechanical Pit (Past)", "Mechanical Pit (Past) to Mechanical Tower Entrance"),("Garden Tower Entrance to Garden Hall (Past)","Garden Hall (Past) to Garden Tower Entrance"),("Main Hall to Hourglass Room", "Hourglass Room to Main Hall")]
    Conditions_List = ["Serpent_Sword", "Serpent_Sword","Eye_of_the_Storm","Eye_of_the_Storm", "Shahdee_beaten"]
    
    
    #I think there's a shortcut, not sure
    (Garden_Waterworks_Past,Garden_Hall_Past)
    ("Garden Tower Waterworks (Past) to Garden Hall (Past)","Garden Hall (Past) to Garden Waterworks (Past)")
    
    
    #One way passage
    (Southern_Passage_Past, Sacrificial_Altar)
    ("Southern Passage (Past) to Sacrificial Altar")
    
   #I want to check some region connectivity for these ones, the code isn't pretty
    Hourglass_Room.connect(Throne_Room, "Hourglass Room to Throne Room", lambda state: state.has(not("Beat Kaileena"),world.player))
    Throne_Room.connect(Sacred_Caves_Present, "Throne Room to the Sacred Caves", lambda state: state.has("Beat Kaileena" and "Scorpion Sword", world.player))
    Sacred_Caves_Present.connect(Sacred_Caves_Past, "Time Portal in the Sacred Caves")
    
    
    Catacombs.connect(Prison_Present, "Catacombs to the Prison")
    Prison_Present.connect(Prison_Past, "Time Portal in the Prison")
    Prison_Past.connect(Library_Past ,"Prison to the Library ", lambda state: state.has("Scorpion Sword"), world.player)
    Library_Past.connect(Mechanical_Pit_Past, "Library to the Mechanical Pit", lambda state: state.has("Beat Kaileena"), world.player) 

    It's still missing a few ones
    
    
