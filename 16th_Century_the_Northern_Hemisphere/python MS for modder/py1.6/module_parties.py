from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *

####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0
#pf_town = pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction
pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium
pf_village = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small

#sample_party = [(trp_swadian_knight,1,0), (trp_swadian_peasant,10,0), (trp_swadian_crossbowman,1,0), (trp_swadian_man_at_arms, 1, 0), (trp_swadian_footman, 1, 0), (trp_swadian_militia,1,0)]

# NEW TOWNS:
# NORMANDY: Rouen, Caen, Bayeux, Coutances, Evreux, Avranches
# Brittany: Rennes, Nantes,
# Maine: Le Mans
# Anjou: Angers


parties = [
  ("main_party","Main Party",icon_player|pf_limit_members, no_menu, pt_none,fac_player_faction,0,ai_bhvr_hold,0,(17, 52.5),[(trp_player,1,0)]),
  ("temp_party","{!}temp_party",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
  ("camp_bandits","{!}camp_bandits",pf_disabled, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(1,1),[(trp_temp_troop,3,0)]),
#parties before this point are hardwired. Their order should not be changed.

  ("temp_party_2","{!}temp_party_2",pf_disabled, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0,0),[]),
#Used for calculating casulties.
  ("temp_casualties","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_2","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_casualties_3","{!}casualties",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_wounded","{!}enemies_wounded",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("temp_killed", "{!}enemies_killed", pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("main_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("encountered_party_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
#  ("ally_party_backup","_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends_backup","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("player_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("ally_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

  ("collective_enemy","{!}collective_enemy",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  #TODO: remove this and move all to collective ally
  ("collective_ally","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
  ("collective_friends","{!}collective_ally",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),
   
  ("total_enemy_casualties","{!}_",  pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #ganimet hesaplari icin #new:
  ("routed_enemies","{!}routed_enemies",pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]), #new:  

#  ("village_reinforcements","village_reinforcements",pf_is_static|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(1,1),[]),

#################################16th_map##############################  
  ("zendar","Zendar",pf_disabled|icon_town|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18,60),[]),

  ("town_1","London",  icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-203.415,53.675),[], 170),
  ("town_2","Stockholm",     icon_town_snow|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.08,84.09),[], 120),
  ("town_3","Paris",   icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-180.847,24.8735),[], 80),
  ("town_4","Bordeaux",     icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-203.018,9.5638),[], 290),
  ("town_5","Sevilla",  icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-221.71,-35.35),[], 90),
  ("town_6","Naples",   icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-153.44,-21.0293),[], 155),
  ("town_7","Vienna",   icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-138.57,17.1149),[], 240),

  ("town_8","Frankfurt", icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-163.64,30.26),[], 175),
  ("town_9","Krakow",   icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-124.899,30.2001),[], 90),
  ("town_10","Moscow",   icon_town_snow|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-54.3383,68.6981),[], 310),
  ("town_11","Vinice",   icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-151.291,-0.957392),[], 150),
  ("town_12","Rome", icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-157.476,-13.081),[], 25),
  ("town_13","Algiers",icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-188.377,-43.7266),[], 60),
  ("town_14","Tripoli",  icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-166.653,-62.8218),[], 135),

  ("town_15","UlanBato",  icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(97.2389,48.1215),[], 45),
  ("town_16","XiAn",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(119.473,-10.6734),[], 0),
  ("town_17","Yingtian",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(159.62,-35.66),[], 90),
  ("town_18","Shuntian",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(150.725,15.1088),[], 135),

  ("town_19","Istanbul", icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-92.4109,-12.0988),[], 45),
  ("town_20","Caro", icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-81.9465,-68.3188),[], 270),
  ("town_21","Jerusalem", icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-60.3656,-52.6272),[], 330),
  ("town_22","Baghdad", icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.2596,-53.0231),[], 225),
  ("town_23","Kyoto",  icon_castle_x_11|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(228.48,-12.61),[], 90),
  ("town_24","Dehli",  icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.9013,-71.054),[], 45),
  ("town_25","Kafa",  icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.8678,4.15394),[], 45),
  ("town_26","Astana",  icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.9547,58.5422),[], 45),
  ("town_27","Lisben",  icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-230.566,-27.8984),[], 170),

  #new
   ("town_28","Tenochtitlan",  icon_aztec|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-541.38,-90.88),[], 45),
#spa 
 ("town_29","Barcelona", icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-188.94,-14.737),[], 225),
#eng
 ("town_30","York", icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-205.209,61.8078),[], 225),
#fra
 ("town_31","Marseilles", icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-176.966,0.651269),[], 225),
#kar
 ("town_32","Oslo", icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-164.433,76.4697),[], 225),
#pol
 ("town_33","Vilnius", icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-112.738,56.388),[], 225),
#hr
 ("town_34","lvbeike", icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-153.086,50.4285),[], 225),
#ott
 ("town_35","Ankara", icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-70.1281,-21.5651),[], 225),
 ("town_36","Alepo", icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-46.699,-36.3607),[], 225),
#mos
 ("town_37","Smolensk", icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.6941,57.3817),[], 225),
#saf
 ("town_38","Kabuer", icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7.40056,-28.213),[], 225),
#SE
   ("town_39","Chunpei",  icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(106.397,-84.1988),[], 45),
#korea
  ("town_40","Hansuwng",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(188.344,5.15888),[], 0),
#china
  ("town_41","Jingzhou",  icon_town|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(135.622,-46.6193),[], 0),
#mog
  ("town_42","Aksu",  icon_town_desert|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(58.39,5.81),[], 45),
#scot
 ("town_43","Edinburg", icon_town_volencia|pf_town, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-206.798,67.6354),[], 225),

#   Aztaq_Castle       
#  Malabadi_Castle
  ("castle_1","Bominhan",icon_castle_x_21|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-209.965,53.7728),[],50),
  ("castle_2","Bristol",icon_castle_x_21|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-214.942,48.7472),[],75),
  ("castle_3","Dublin",icon_castle_x_21|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-225.948,58.7618),[],100),
  ("castle_4","Kar",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-148.578,74.0337),[],180),
  ("castle_5","Copenhagen",icon_castle_x_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-153.781,58.4122),[],90),
  ("castle_6","Flensburg",icon_castle_x_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-163.222,56.1181),[],55),
  ("castle_7","Goteborg",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-157.882,72.0319),[],45),
  ("castle_8","Rouen",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-189.234,34.6736),[],30),
  ("castle_9","Reon",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-200.175,31.6896),[],100),
  ("castle_10","Toulouse",icon_castle_x_14|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-190.573,6.20337),[],110), 
  ("castle_11","Madrid",icon_castle_x_15|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-211.231,-19.8513),[],75),
  ("castle_12","Volencia",icon_castle_x_16|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-195.51,-27.8645),[],95),
  ("castle_13","Sihong",icon_castle_x_3|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-222.792,0.693164),[],115),
  ("castle_14","Milan",icon_castle_x_22|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-165.493,-0.551126),[],90),
  ("castle_15","Palermo",icon_castle_x_23|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-163.616,-34.8122),[],235),
  ("castle_16","Amsterdam",icon_castle_x_1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-172.786,47.0177),[],45),
  ("castle_17","Florenca",icon_castle_x_1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-160.564,-6.69373),[],15),
  ("castle_18","Ragusa",icon_castle_x_1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-135.7,-12.78),[],300),
  ("castle_19","Irakliom",icon_castle_x_1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-112.111,-46.9322),[],280),
  ("castle_20","Nicosia",icon_castle_x_1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-69.7067,-41.5243),[],260),
  ("castle_21","Berne",icon_castle_x_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-167.024,14.9836),[],260),
  ("castle_22","Hamburg",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-162.031,47.5571),[],260),
  ("castle_23","Leipzig",icon_castle_x_1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-139.86,39.59),[],80),
  ("castle_24","Prague",icon_castle_x_4|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-135.839,29.2744),[],260),
  ("castle_25","Zagreb",icon_castle_x_5|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-137.178,7.01049),[],260),
##poland
  ("castle_26","Warsaw",icon_castle_x_10|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-114.942,43.17),[],260),
  ("castle_27","Poznan",icon_castle_x_10|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-132.666,48.2359),[],260),
  ("castle_28","Kiev",icon_castle_x_10|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-87.2239,36.5952),[],260),

  ("castle_29","Weryodi",icon_castle_x_10|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-110.453,73.6745),[],280),
  ("castle_30","Leref",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-80.0815,69.354),[],260),
  ("castle_31","Saratov",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-25.3595,38.4863),[],260),
  ("castle_32","kazan",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.072,53.0515),[],260),
  ("castle_33","Perth",icon_castle_x_1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-123.094,10.514),[],80),
  ("castle_34","Athens",icon_castle_x_18|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-109.255,-29.4747),[],260),
  ("castle_35","Bucharest",icon_castle_x_12|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-98.8773,2.10647),[],260),
  ("castle_36","Miras",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-95.6173,-30.1401),[],260),
  ("castle_37","Nisia",icon_castle_x_21|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-89.3318,-18.9747),[],260),
  ("castle_38","Tabriz",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.0659,-8.28929),[],260),
  ("castle_39","Kaseri",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.8013,-21.7519),[],280),
  ("castle_40","Damascus",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-49.5721,-48.0261),[],260),

  ("castle_41","Trabzon",icon_castle_x_13|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.3113,-9.16363),[],260),
  ("castle_42","Thessaloniki",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-108.58,-13.9021),[],80),
  ("castle_43","Dehran",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-2.85048,-13.9003),[],260),
  ("castle_44","Ryazan",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.2948,43.6683),[],260),
  ("castle_45","Alsh_abad",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(12.5862,-9.79084),[],260),
  ("castle_46","Isfahan",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.7893,-38.0564),[],260),
  ("castle_47","Kerman",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-3.88514,-46.2575),[],260),
  ("castle_48","Hohhot",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(116.424,25.8276),[],260),

  ("castle_49","Undurkhaan",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(120.141,37.5141),[],100),
  ("castle_50","Khovd",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(63.8884,37.4322),[],110),
  ("castle_51","Kumul",icon_town_steppe|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(76.5836,15.4593),[],75),
  ("castle_52","Caganbugd",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(91.9672,26.6607),[],95),
  ("castle_53","Chengdu",icon_town_steppe|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(112.425,-30.5227),[],115),

  ("castle_54","JiNan",icon_town_steppe|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(150.68,-10.85),[],90),
  ("castle_55","Quanzhou",icon_town_steppe|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(155.922,-55.8496),[],235),

  ("castle_56","Changsha",icon_town_steppe|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(135.858,-36.46),[],260),

  ("castle_57","Lanzhou",icon_town_steppe|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(105.994,3.56605),[],260),
  ("castle_58","Taiyuan",icon_town_steppe|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(127.5,10),[],260),

  ("castle_59","Edo",icon_castle_x_11|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(248.44,0.93),[],280),
  ("castle_60","Nagasaki",icon_castle_x_11|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(198.735,-20.9438),[],260),
  ("castle_61","Tottori_ken",icon_castle_x_11|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(215.532,-13.0211),[],80),

  ("castle_62","Fez",icon_castle_desert_1|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-218.286,-48.8874),[],260),
  ("castle_63","Tunisia",icon_castle_desert_2|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-170.814,-45.9315),[],260),
  ("castle_64","Oran",icon_castle_desert_3|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-201.976,-48.5823),[],260),
#yifeng new land
    ("castle_65","Waco",icon_castle_snow_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-537.42,-19.97),[],260),
  ("castle_66","Kiaha",icon_castle_snow_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-498.97,-8),[],260),
  ("castle_67","Kentucky",icon_castle_snow_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-517.74,6.07),[],260),
  ("castle_68","Havana",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-466.10,-70.61),[],260),

#main land pol
    ("castle_69","Bortu",icon_castle_x_14|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-231.63,-13.4809),[],260),
  ("castle_70","Marade",icon_castle_x_14|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-273.67,-60.15),[],260),
#krimu
 # ("castle_70","krimu1",icon_castle_desert_3|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79.5829,1.74923),[],260),
  ("castle_71","Yedkushile",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-68.9805,13.7035),[],260),
#indo
    ("castle_72","Chandigarh",icon_castle_desert_3|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.5402,-57.7409),[],260),
  ("castle_73","Jaipur",icon_castle_desert_3|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(46.227,-82.8541),[],260),
  ("castle_74","Capur",icon_castle_desert_3|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(66.0563,-75.0513),[],260),
#eastsouth
   ("castle_75","Mandalay",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(89.5954,-72.578),[],260),
  ("castle_76","Qianjiang ",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(124.23,-95.51),[],260),
  ("castle_77","Ha Noi",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(124.123,-81.3624),[],260),
#korea 
  ("castle_78","Guangzhou",icon_town_steppe|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(188.096,-2.47545),[],260),
  ("castle_79","Pyongyang",icon_town_steppe|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(184.7,11.7135),[],260),
#Nvzhen
    ("castle_80","Shuangchengwei",icon_town_steppe|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(194.414,43.7029),[],260),
  ("castle_81","Sacahewei",icon_town_steppe|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(168.087,43.9716),[],260),
  ("castle_82","Nuergandusi",icon_town_steppe|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(238.864,75.2938),[],260),
#kzakh
 ("castle_83","Karaganda",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(27.1417,37.4918),[],260),
 ("castle_84","Atero",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-15.2733,25.984),[],260),
  ("castle_85","Syvansto",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-77.97,1.47),[],260),  

  #add new
#az
  ("castle_86","Tollan",icon_aztec|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-547.31,-57.37),[],260),
 ("castle_87","Tehuacan",icon_aztec|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-545.67,-110.9),[],260),
 ("castle_88","Mictlan",icon_aztec|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-529.92,-125),[],260),
#maya
 ("castle_89","Canpech",icon_aztec|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-500,-105),[],260),
 ("castle_90","Tikal",icon_aztec|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-499,-125),[],260),
#new spa
 ("castle_91","Vera Cruz",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-525.06,-90.42),[],260),
 #por
  ("castle_92","Yasuer",icon_castle_x_14|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-319.54,-13.19),[],260),
#sp eu
 ("castle_93","Karilia",icon_castle_x_14|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-169.616,-23.9849),[],260),
#NAfrica
 ("castle_94","Sute",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-146.605,-71.3833),[],260),
#fran
 ("castle_95","Dirong",icon_castle_x_14|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-173.664,15.9424),[],260),
#hr
 ("castle_96","Nelenburg",icon_castle_x_14|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-148.057,29.4932),[],260),
#pol
 ("castle_97","Roz",icon_castle_x_14|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-122.092,38.5087),[],260),
 ("castle_98","Castle",icon_castle_a|pf_disabled|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(563,207),[],260),
 ("castle_99","Chercase",icon_castle_x_14|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-78.5294,33.2516),[],260),
#knight
("castle_100","Tartu",icon_castle_x_14|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-102.234,73.0223),[],260),
#scot
 ("castle_101","Abotin",icon_castle_x_14|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-202.292,76.5845),[],260),
#hospita
 ("castle_102","Rode",icon_castle_x_14|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-93.0307,-39.5074),[(trp_hospital_skirmisher,250,250),(trp_hospital_lancer,150,150),(trp_hospital_sergeant,150,150)],260),#yifeng
#ott
 ("castle_103","Purishdina",icon_castle_x_14|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-120.893,-4.2642),[],260),
#egyp
 ("castle_104","Bansia",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-114.991,-59.0711),[],260),
 ("castle_105","Alexandria",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-88.1097,-61.7805),[],260),
 ("castle_106","Alish",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-72.0264,-62.7906),[],260),
#china
 ("castle_107","Wusizangdusi",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(65.1465,-44.6285),[],260),
 ("castle_108","Nanning",icon_town_steppe|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(132.369,-63.7138),[],260),
 ("castle_109","Liaodongdusi",icon_town_steppe|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(177.22,28.77),[],260),

 ##yifeng add in V1.1
 ##arfican
 ("castle_110","Massawa",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-65.5,-102.75),[],260),
 ("castle_111","Makiltin",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-39.1,-123.73),[],260),
("castle_112","Sofala",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-74.7,-194.8),[],260),
("castle_113","Cape of Good Hope",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-115,-255),[],260),
("castle_114","Rugo",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-154.3,-169.9),[],260),
##south american
("castle_115","San Amaru",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-429.57,-241.4),[],260),
#pol

#north american
("castle_116","Barbados",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-405.76,-153.07),[],260),
("castle_117","Incan1",icon_aztec|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-498.5,-194.93),[],260),
("castle_118","Incan2",icon_aztec|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-505.55,-208.31),[],260),

##ocean land for north arfica?
("castle_119","NA1",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-235.28,-58.86),[],260),

##arabean
("castle_120","Hassa",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-37.4,-68.5),[],260),
("castle_121","Aden",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-40.3,-104.4),[],260),
("castle_122","Muscat",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.9,-83.9),[],260),

##greenland
("castle_123","Reykjavik",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-302.43,131.51),[],260),

("castle_124","Brunei",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(157.4,-118.07),[],260),

 ("castle_125","Bahia",icon_castle_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-415.63,-200.32),[],260),
 ##sanghai
  ("castle_126","Dendy",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-187.98,-116.96),[],260),
 ("castle_127","Cumahi",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-211.77,-137.45),[],260),
 ("castle_128","Cabu",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-255.32,-120.1),[],260),

 ## commoner
 ("castle_129","East Congo",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-107.5,-163),[],260),
 ("castle_130","Getagan",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-69.22,-152.58),[],260),
 ("castle_131","new to viking",icon_castle_snow_a|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-150.74,93.47),[],260),
 ("castle_132","japan1",icon_castle_x_11|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(239.54,-4.26),[],260),
 
  ("castle_133","Incan3",icon_aztec|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-539.37,-230.17),[],260),
 ("castle_134","Huron",icon_castle_snow_b|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-496.63,61.18),[],260),

 ("castle_135","indu1",icon_castle_d|pf_castle, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(35.6,-90.2),[],260),

 
#     Rinimad      
#              Rietal Derchios Gerdus
# Tuavus   Pamir   vezona 
  
  ("village_1", "Bradford",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-211.01,61.5564),[], 100),
  ("village_2", "Killarney",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-233.201,52.8697),[], 110),
  ("village_3", "Nottingham",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-207.354,56.7484),[], 120),
  ("village_4", "Dorchester",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-209.453,48.532),[], 130),
  ("village_5", "Brighton",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-201.781,49.4258),[], 170),
  ("village_6", "Norwich",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-202.218,57.0248),[], 100),
  ("village_7", "Frederikshavn",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-163.631,63.323),[], 110),
  ("village_8", "Rondo",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-218.982,-39.3379),[], 120),
  ("village_9", "Buvran",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-118.106,-34.5823),[], 130),
  ("village_10","Royan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-201.196,17.4185),[], 170),

  ("village_11","Orleans",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-187.479,20.6026),[], 100),
  ("village_12","Emer",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-116.359,-10.1184),[], 110),
  ("village_13","Evreux",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-187.831,30.1497),[], 120),
  ("village_14","Reims",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-178.146,32.5726),[], 130),
  ("village_15","Ryibelet",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-173.054,25.526),[], 170),
  ("village_16","Shapeshte",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-144.887,85.6635),[], 170),
  ("village_17","Karlstad",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-158.933,76.8992),[], 35),
  ("village_18","Kurgan",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-16.1369,69.8384),[], 170),
  ("village_19","Penza",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.0166,41.929),[], 170),
  ("village_20","Vologda",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-36.1331,77.2955),[], 170),

  ("village_21","Bazeck",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-113.817,69.0128),[], 100),
  ("village_22","Nizhniy_Novgorod",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-48.9564,58.2432),[], 110),
  ("village_23","Valladolid",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-214.089,-13.4806),[], 120),
  ("village_24","Tereul",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-202.26,-20.6991),[], 130),
  ("village_25","Zaragoza",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-198.93,-8.77117),[], 170),
  ("village_26","Pagundur",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-165.203,-2.76335),[], 170),
  ("village_27","Siracusa",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-160.884,-40.1104),[], 170),
  ("village_28","Cosenza",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-152.614,-31.1763),[], 170),
  ("village_29","Bari",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-142.854,-25.4887),[], 170),

  ("village_30","Bologna",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-156.039,-6.11389),[], 170),
  ("village_31","Verona",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-159.312,-0.112677),[], 100),
  ("village_32","Udine",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-148.339,3.1987),[], 110),
  ("village_33","Ruluns",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-129.481,-15.5798),[], 120),
  ("village_34","Ehlerdah",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-117.19,-48.0308),[], 130),
  ("village_35","Fearichen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-74.0158,-42.6369),[], 170),
  ("village_36","Siena",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-159.359,-10.0438),[], 170),
  ("village_37","Pescara",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-150.778,-12.2351),[], 170),
  ("village_38","Mainz",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-161.953,23.22),[], 170),
  ("village_39","Utrecht",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-169.844,44.5189),[], 170),
  ("village_40","Saren",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-144.182,48.2603),[], 170),

  ("village_41","Dugan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-164.68,37.07),[], 100),
  ("village_42","Dirigh_Aban",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-151.355,22.8011),[], 110),
  ("village_43","Zagush",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-138.654,26.7737),[], 120),
  ("village_44","Peshmi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-144.231,18.6091),[], 130),
  ("village_45","Bulugur",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-131.713,16.9837),[], 170),
  ("village_46","Fedner",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-132.54,8.73642),[], 170),
  ("village_47","Epeshe",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-116.06,14.1348),[], 170),
  ("village_48","Veidar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-110.523,-2.52799),[], 170),
  ("village_49","Tismirr",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-134.707,78.3091),[], 10),
  ("village_50","Bergen",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-172.801,74.2457),[], 170),

  ("village_51","Jelbegi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-94.7928,-6.66265),[], 100),
  ("village_52","Amashke",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100.241,-13.0126),[], 110),
  ("village_53","Balanli",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-94.264,-22.9645),[], 120),
  ("village_54","Chide",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-77.4947,-30.0773),[], 130),
  ("village_55","Tadsamesh",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-47.5061,-7.96278),[], 170),
  ("village_56","Fenada",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-53.4713,-29.9955),[], 170),
  ("village_57","Ningbo",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(160.75,-45.5879),[], 170),
  ("village_58","Hefei",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(148.38,-28.30),[], 170),
  ("village_59","Yan'an",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(117.479,0.345024),[], 170),
  ("village_60","Wuhai",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(113.496,13.1231),[], 170),

  ("village_61","Aldelen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-33.3802,-16.1891),[], 100),
  ("village_62","Yancheng",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(159,-25.65),[], 100),
  ("village_63","Guiyang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(123.81,-49.6979),[], 100),
  ("village_64","Serindiar",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(200.635,-26.3466),[], 100),
  ("village_65","Dongfan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(165.937,-58.1391),[], 100),
  ("village_66","Tokushima",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(216.333,-22.7595),[], 100),
  ("village_67","Nagoya",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(236.61,-12.28),[], 100),
  ("village_68","Ibdeles",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-129.111,43.9073),[], 100),
  ("village_69","Kwynn",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-117.064,32.4473),[], 100),
  ("village_70","Dirigsene",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-93.3253,30.9137),[], 100),

  ("village_71","Tshibtin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-120.714,51.1199),[], 20),
  ("village_72","Elberl",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-106.07,49.5784),[], 60),
  ("village_73","Malaga",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-210.667,-37.5161),[], 55),
  ("village_74","Ayyike",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-77.342,50.178),[], 15),
  ("village_75","Konosha",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-67.4984,76.2046),[], 10),
  ("village_76","Carpentras",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-176.032,6.33099),[], 35),
  ("village_77","Trelleborg",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-152.14,67.0489),[], 160),
  ("village_78","Castrez",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-184.27,1.06084),[], 180),
  ("village_79","Volgograd",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-29.5832,50.1342),[], 0),
  ("village_80","Cahorz",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-191.052,12.1664),[], 40),

  ("village_81","Aletai",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(57.5735,31.2684),[], 20),
  ("village_82","Ejina",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(83.5183,8.14412),[], 60),
  ("village_83","Zhangjiakou",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(129.77,18.17),[], 55),
  ("village_84","Saiyinshanda",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(106.208,30.9323),[], 15),
  ("village_85","Qiaoba",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(109.092,47.009),[], 10),
  ("village_86","Buergan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(84.2282,46.8786),[], 35),
  ("village_87","Bayanzuoer",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(101.863,24.5468),[], 160),
  ("village_88","Shengyang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(167.135,20.8007),[], 180),
  ("village_89","Shanhaiguan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(156.23,17.1),[], 0),
  ("village_90","Handan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(143.604,9.38999),[], 40),

  ("village_91","Linfen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(130.704,2.37227),[], 20),
  ("village_92","Caza",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-65.9743,-59.8043),[], 60),
  ("village_93","riverland",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-84.8286,-75.0651),[], 55),
  ("village_94","Hanzhong",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(106.972,-10.7134),[], 15),
  ("village_95","Suining",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(124.741,-29.1117),[], 10),
  ("village_96","Nanyang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(138.56,-17.96),[], 35),
  ("village_97","Sekhtem",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-35.4726,-47.4274),[], 160),
  ("village_98","Mawiti",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-62.2946,-48.8741),[], 180),
  ("village_99","Fishara",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-19.7593,-61.7591),[], 0),
  ("village_100","Iqbayl",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-8.52317,-54.2518),[], 40),

  ("village_101","Uzgha",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-44.021,-44.5176),[], 20),
  ("village_102","Fes",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-213.471,-47.3579),[], 60),
  ("village_103","Oujda",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-209.361,-48.0902),[], 55),
  ("village_104","Annaba",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-181.099,-43.216),[], 15),
  ("village_105","Setif",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-187.846,-49.3016),[], 10),
  ("village_106","Sfax",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-171.181,-52.459),[], 35),
  ("village_107","Madanin",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-171.182,-57.8308),[], 160),
  ("village_108","Mit Nun",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(7.40428,-2.85732),[], 180),
  ("village_109","Tilimsal",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.42888,-12.76),[], 0),
  ("village_110","Rushdigh",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-14.6191,-31.9203),[], 40),
#new land
  ("village_111","south camp",  icon_castle_snow_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-547.11,-15.10),[], 40),
  ("village_112","middle camp",  icon_castle_snow_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-513.19,28.71),[], 40),
  ("village_113","north camp",  icon_castle_snow_b|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-482.05,16.09),[], 40),
  ("village_114","San_Augustin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-471.04,-41.98),[], 40),
#pol
  ("village_115","Ciudad",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-223.27,-49.1697),[], 40),
  ("village_116","Nazare",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-229.212,-20.8684),[], 40),
  ("village_117","Guarda",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-224.311,-13.831),[], 40),
#indo
  ("village_118","Amrim",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(22.0929,-56.6009),[], 40),
  ("village_119","Jotpor",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(31.8639,-74.7663),[], 40),
  ("village_120","Lecoan",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(62.0693,-67.0083),[], 40),
  ("village_121","Anra Abad",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(61.3093,-81.4956),[], 40),
#es
  ("village_122","Langky",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(115.571,-83.7551),[], 40),
  ("village_123","Kinho",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(102.104,-74.129),[], 40),
  ("village_124","Lanbrab",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(112.3,-110.45),[], 40),
#jap
  ("village_125","Akita",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(249.278,4.99455),[], 40),
#korea
 ("village_126","Kujang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(186.839,19.1809),[], 40),
 ("village_127","Daejeon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(194.545,-0.891364),[], 40),
#nvzhen
 ("village_128","Baicheng",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(154.038,47.2621),[], 40),
 ("village_129","Haixi nvzhen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(215.149,51.8965),[], 40),
 ("village_130","Yeren nvzhen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(232.931,57.774),[], 40),
#kzakh  
 ("village_131","Rezcazgan",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(13.8446,24.7963),[], 40),
 ("village_132","Baprodar",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(30.6578,56.8269),[], 40),
 ("village_133","Simibara",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(18.7111,50.0862),[], 40),
  #krimu
 ("village_134","Tarta camp",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-73.5326,7.23581),[], 40),
 ("village_135","West river",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-77.2281,13.9189),[], 40),
 ("village_136","River camp",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-62.2751,17.0009),[], 40),
  
 #new
  ("village_137", "Paquic",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-539.93,-68.67),[], 100),
  ("village_138", "Tixtia",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-550.98,-83.65),[], 100),
  ("village_139", "Taniguiecache",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-535.09,-105.8),[], 100),
  ("village_140", "Tecuantepec",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-521.23,-123.9),[], 100),

("village_141", "dock",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-527.21,-87.25),[], 100),

("village_142", "Uxmal",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-489.73,-94.56),[], 100),
  ("village_143", "Uxmal village",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-495,-113),[], 100),

#  eur
  ("village_144", "Roge",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-230.72,-5),[], 100),

    ("village_145", "Sasari",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-169.68,-17.8301),[], 100),
  ("village_146", "Molri",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-210.929,34.9199),[], 100),

    ("village_147", "Puroen",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-146.358,36.0269),[], 100),
  ("village_148", "Nishi",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-126.083,-1.29496),[], 100),

  #pol
    ("village_149", "Simira",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-81.8223,28.4157),[], 100),
  ("village_150", "Radom",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-112.842,39.1078),[], 100),

    ("village_151", "Lutchic",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100.431,36.0087),[], 100),
#china
  ("village_152", "Lingshan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(139.71,-65.55),[], 100),
   ("village_153","Naquka",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(71.9233,-29.0859),[], 110),

  
    ("village_154", "Dali",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(107.883,-47.5531),[], 100),
#des
  ("village_155","Misurat",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-156.398,-69.2955),[], 35),

    ("village_156","Bardijo",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-105.037,-60.7585),[], 35),
  ("village_157","Materu",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-96.2562,-61.736),[], 35),
  ("village_158","Akba",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-64.3132,-76.788),[], 35),

    ("village_159","Nalehan",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-79.2133,-20.0694),[], 35),

	  ("village_160","Yili",  icon_village_c|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(57,16.5),[], 35),
#Knights
  ("village_161","Gosi",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-109.072,77.9581),[], 100),

  ("village_162", "Siorogens",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-94.3532,-37.9688),[], 100),
#scot
  ("village_163","Aoben",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-217.956,68.2023),[], 100),
  ("village_164","Lyrge",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-207.11,81.3204),[], 100),

  ("village_165","Jartin",  icon_village_snow_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-165.089,52.7694),[], 100),
  ("village_166","Haiyang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(127.49,-73.5612),[], 100),

  ##yifeng add in V1.1
   ("village_167", "Barin",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-24.54,-70),[], 170),
  ("village_168", "Asil",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-51.8,-95.4),[], 170),
  ("village_169", "Dofal",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-28.22,-92.5),[], 170),
  ("village_170", "Tajura",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-60.66,-112.08),[], 170),
  ("village_171", "Mugudusu",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-57.5,-136.5),[], 170),
  ("village_172", "Masamiki",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-83.28,-178.6),[], 170),
  ("village_173", "Cape",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-125,-247.6),[], 170),
  ("village_174", "Cango",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-144.53,-179.31),[], 170),
  ("village_175", "Antigo",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-419.84,-123.29),[], 170),
  ("village_176", "San Tome",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-418.54,-231.65),[], 170),
  ("village_177", "Bowatan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-493.04,-189.7),[], 170),
  ("village_178", "Tacamucock",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-515.1,-208.98),[], 170),
  ("village_179", "Bancalon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-212.55,-59.1),[], 170),
##
   ("village_180", "Beidanian",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-171.36,90.95),[], 170),
  ("village_181", "Greenland",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-382.1,130.4),[], 170),

    ("village_182", "Surilan",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-429.32,-185.9),[], 170),
##sanghai
    ("village_183", "Calon",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-211.3,-100.93),[], 170),
    ("village_184", "Bate",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-240,-107.3),[], 170),
    ("village_185", "Oyo",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-196.4,-142),[], 170),
##
	    ("village_186", "Jiugang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(127.85,-138.15),[], 170),
    ("village_187", "Ramu",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-67.16,-142.47),[], 170),
    ("village_188", "Uganda",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-100.33,-149.58),[], 170),
    ("village_189", "Caragaz",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-534.16,-218.31),[], 170),
    ("village_190", "Crides",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-469.5,74.8),[], 170),
    ("village_191", "Atcaki",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(45.86,-108.71),[], 170),
    ("village_192", "Hawaii island",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(223.62,-18.6),[], 170),
    ("village_193", "village",  icon_village_a|pf_disabled|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(563,207),[], 170),

 ##
#end
    ("gate1","Hebua",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(469.82,-200.91),[], 100),
   ("gate2","San Anna",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-455.04,-257.50),[], 100),

   ("dungeon1","Spanish Manor",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-426.52,-85.03),[], 100),
 ("dungeon2","Diaoyudao",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(171.07,-50.93),[], 100),

  ("dungeon3","Bermuda",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-370.21,64.94),[], 100),
 ("dungeon4","Mari tomb",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-201.83,-130.93),[], 100),
 ("dungeon5","The desert",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-92.47,-80.92),[], 100),
# ("dungeon6","Madagascar camp",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-54.88,-225.81),[], 100),
# ("dungeon7","Ceylon Pearlfishery",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(64.46,-122.72),[], 100),
 ("dungeon8","Dongcang",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(140.29,-31.34),[], 100),
 ("dungeon9","skycity",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-59.8,-35.59),[], 100),
 ("dungeon10","Cossack's Storehouse",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-72.73,21.23),[], 100),
 ("dungeon11","HoaryArena",  icon_village_a|pf_village, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-195.69,26.1),[], 100),
  
  ("salt_mine","Salt_Mine",pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.2, -31),[]),
  ("four_ways_inn","Four_Ways_Inn",pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(4.8, -39.6),[]),
  ("test_scene","test_scene",pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  #("test_scene","test_scene",icon_village_a|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -19.6),[]),
  ("battlefields","battlefields",pf_disabled|pf_is_static|pf_always_visible|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.8, -16.6),[]),
  ("dhorak_keep","Dhorak_Keep",pf_disabled|pf_is_static|pf_always_visible|pf_no_label|pf_hide_defenders, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-50,-58),[]),

  ("training_ground","Training Ground",  pf_disabled|icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-185.191,16.5499),[]),

  ("training_ground_1", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-91.612,21.9653),[], 100),
  ("training_ground_2", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(-179.58,-51.1043),[], 100),
 
 #this one?
 ("training_ground_3", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(10.22,27.3277),[], 100),

 ("training_ground_4", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(139.03,-5.43),[], 100),
  ("training_ground_5", "Training Field",  icon_training_ground|pf_hide_defenders|pf_is_static|pf_always_visible|pf_label_medium, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(151.763,39.6696),[], 100),

  
## ZZ Manor begin
  ("manor_1","Manor",  pf_village|pf_disabled, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(49.2966,-11.89536),[], 170),
#  ("zhai","My Zhai",icon_castle_d|pf_disabled|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.2, -31),[]),

 
#  bridge_a
  ("Bridge_1","{!}1",icon_river_bridge|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(564.8,201.32),[], 70.8),
 
 ("Bridge_2","{!}2",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(179.03,26.43),[], 200),
  ("Bridge_3","{!}2",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(176,30.5),[], 230),
  ("Bridge_4","{!}2",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(171.2,32.7),[], 256),

  ("Bridge_5","{!}5",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(116.1,9.61),[], -60),
    ("Bridge_6","{!}6",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(111.24,9.04),[], 100),
  
  ("Bridge_7","{!}7",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(103.56,10.03),[], -105),
 #shanhaiguan 
    ("Bridge_8","{!}8",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(153.7,19.21),[], 225),
    ("Bridge_9","{!}9",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(148.87,21.01),[], 265),
	
    ("Bridge_10","{!}10",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(123.6,15.88),[], 285),
    ("Bridge_11","{!}11",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(129.12,17.69),[], 295),
    ("Bridge_12","{!}12",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(143.27,20.26),[], 285),


#	("Bridge_13","{!}13",icon_bridge_b|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(110,-29),[], 285),
   #liaodongdusi
   ("Bridge_14","{!}14",icon_bridge_snow_a|pf_is_static|pf_always_visible|pf_no_label, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(165.85,32.5),[], 285),

  ("looter_spawn_point"   ,"{!}looter_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-135.378,5.83688),[(trp_looter,15,0)]),
  ("steppe_bandit_spawn_point"  ,"the steppes",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-80.9994,24.2872),[(trp_looter,15,0)]),
  ("taiga_bandit_spawn_point"   ,"the tundra",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(31.4075,13.4259),[(trp_looter,15,0)]),
##  ("black_khergit_spawn_point"  ,"black_khergit_sp",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(47.1, -73.3),[(trp_looter,15,0)]),
  ("forest_bandit_spawn_point"  ,"the forests",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(234.22,-13.12),[(trp_looter,15,0)]),
  ("mountain_bandit_spawn_point","the highlands",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(141.01,-20.08),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_1"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-295.43,23.46),[(trp_looter,15,0)]),
  ("sea_raider_spawn_point_2"   ,"the coast",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-277.353,-34.1569),[(trp_looter,15,0)]),
  ("desert_bandit_spawn_point"  ,"the deserts",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-175.644,-52.4174),[(trp_looter,15,0)]),
 
   ("african_tribesman_spawn_point"  ,"the african_tribesman",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-194.75,-117.32),[(trp_looter,15,0)]),
   ("wokou_spawn_point"  ,"the wokou",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(180.99,-42),[(trp_looter,15,0)]),
   ("indu_spawn_point"  ,"the indu",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(8.6,-119.65),[(trp_looter,15,0)]),

      ("indian_spawn_point"  ,"the indian",pf_disabled|pf_is_static, no_menu, pt_none, fac_outlaws,0,ai_bhvr_hold,0,(-520.23,2.09),[(trp_looter,15,0)]),

 # add extra towns before this point 
  ("spawn_points_end"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_1"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_2"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_3"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_4"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  ("reserved_5"                  ,"{!}last_spawn_point",    pf_disabled|pf_is_static, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0., 0),[(trp_looter,15,0)]),
  

#-## Outposts begin
  ("outpost_1","Outpost",icon_training_ground|pf_disabled|pf_is_static|pf_always_visible|pf_show_faction|pf_label_small, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(0, 0),[]),
  ("outpost_2","Outpost",icon_village_a|pf_disabled|pf_is_static|pf_always_visible|pf_show_faction|pf_label_small, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(1, -1),[]),
  ("fort","Fort",icon_castle_a|pf_disabled|pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium, no_menu, pt_none, fac_commoners,0,ai_bhvr_hold,0,(1, 1),[]),
#-## Outposts end
   ("zhai","My Village",icon_village_a|pf_disabled|pf_is_static|pf_always_visible, no_menu, pt_none, fac_neutral,0,ai_bhvr_hold,0,(14.2, -31),[]),

 ##great wall
 
   
   ]
# modmerger_start version=201 type=2
try:
    component_name = "parties"
    var_set = { "parties" : parties }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
