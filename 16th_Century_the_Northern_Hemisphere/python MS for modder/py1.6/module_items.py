from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *

####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################

# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile   = imodbit_bent | imodbit_large_bag
imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent
##yifeng
we_faction = [fac_kingdom_1, fac_kingdom_2, fac_kingdom_3, fac_kingdom_4, fac_kingdom_5, fac_kingdom_8, fac_kingdom_9, fac_kingdom_13, fac_kingdom_16, fac_kingdom_24, fac_kingdom_27,fac_kingdom_28]
arb_faction = [fac_kingdom_6, fac_kingdom_12, fac_kingdom_14, fac_kingdom_17, fac_kingdom_23]

# Replace winged mace/spiked mace with: Flanged mace / Knobbed mace?
# Fauchard (majowski glaive) 
items = [
# item_name, mesh_name, item_properties, item_capabilities, slot_no, cost, bonus_flags, weapon_flags, scale, view_dir, pos_offset
 ["no_item","INVALID ITEM", [("invalid_item",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

 ["tutorial_spear", "Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 0 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
 ["tutorial_club", "Club", [("club",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
 ["tutorial_battle_axe", "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(88) | weapon_length(108)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_arrows","Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(0,pierce)|max_ammo(20),imodbits_missile],
 ["tutorial_bolts","Bolts", [("bolt",0),("flying_bolt",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|abundance(90)|weapon_length(55)|thrust_damage(0,pierce)|max_ammo(18),imodbits_missile],
 ["tutorial_short_bow", "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 0 , weight(1)|difficulty(0)|spd_rtng(98) | shoot_speed(49) | thrust_damage(12 ,  pierce  ),imodbits_bow ],
 ["tutorial_crossbow", "Crossbow", [("crossbow",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0 , weight(3)|difficulty(0)|spd_rtng(42)|  shoot_speed(68) | thrust_damage(32,pierce)|max_ammo(1),imodbits_crossbow ],
 ["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile ],
 ["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
 ["tutorial_shield", "Kite Shield", [("shield_kite_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
 ["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
 ["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],
 ["tutorial_sword", "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(18 , cut) | thrust_damage(15 ,  pierce),imodbits_sword ],
 ["tutorial_axe", "Axe", [("iron_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(4)|difficulty(0)|spd_rtng(91) | weapon_length(108)|swing_damage(19 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

 ["tutorial_dagger","Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(40)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],


 ["horse_meat","Horse Meat", [("raw_meat",0)], itp_type_goods|itp_consumable|itp_food, 0, 12,weight(40)|food_quality(30)|max_ammo(40),imodbits_none],
# Items before this point are hardwired and their order should not be changed!
 ["practice_sword","Practice Sword", [("practice_sword",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(22,blunt)|thrust_damage(20,blunt),imodbits_none],
 ["heavy_practice_sword","Heavy Practice Sword", [("heavy_practicesword",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_greatsword,
    21, weight(6.25)|spd_rtng(94)|weapon_length(128)|swing_damage(30,blunt)|thrust_damage(24,blunt),imodbits_none],
 ["practice_dagger","Practice Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_wooden_attack, itc_dagger|itcf_carry_dagger_front_left, 2,weight(0.5)|spd_rtng(110)|weapon_length(47)|swing_damage(16,blunt)|thrust_damage(14,blunt),imodbits_none],
 ["practice_axe", "Practice Axe", [("hatchet",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 24 , weight(2) | spd_rtng(95) | weapon_length(75) | swing_damage(24, blunt) | thrust_damage(0, pierce), imodbits_axe],
 ["arena_axe", "Axe", [("arena_axe",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 137 , weight(1.5)|spd_rtng(100) | weapon_length(69)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["arena_sword", "Sword", [("arena_sword_one_handed",0),("sword_medieval_b_scabbard", ixmesh_carry),], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 243 , weight(1.5)|spd_rtng(99) | weapon_length(95)|swing_damage(22 , blunt) | thrust_damage(20 ,  blunt),imodbits_sword_high ],
 ["arena_sword_two_handed",  "Two Handed Sword", [("arena_sword_two_handed",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
 670 , weight(2.75)|spd_rtng(93) | weapon_length(110)|swing_damage(30 , blunt) | thrust_damage(24 ,  blunt),imodbits_sword_high ],
 ["arena_lance",         "Lance", [("arena_lance",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
 90 , weight(2.5)|spd_rtng(96) | weapon_length(150)|swing_damage(20 , blunt) | thrust_damage(25 ,  blunt),imodbits_polearm ],
 ["practice_staff","Practice Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(2.5)|spd_rtng(103) | weapon_length(118)|swing_damage(18,blunt) | thrust_damage(18,blunt),imodbits_none],
 ["practice_lance","Practice Lance", [("joust_of_peace",0)], itp_couchable|itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_greatlance, 18,weight(4.25)|spd_rtng(58)|weapon_length(240)|swing_damage(0,blunt)|thrust_damage(15,blunt),imodbits_none],
 ["practice_shield","Practice Shield", [("shield_round_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 20,weight(3.5)|body_armor(1)|hit_points(200)|spd_rtng(100)|shield_width(50),imodbits_none],
 ["practice_bow","Practice Bow", [("hunting_bow",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90) | shoot_speed(40) | thrust_damage(21, blunt),imodbits_bow ],
##                                                     ("hunting_bow",0)],                  itp_type_bow|itp_two_handed|itp_primary|itp_attach_left_hand, itcf_shoot_bow, 4,weight(1.5)|spd_rtng(90)|shoot_speed(40)|thrust_damage(19,blunt),imodbits_none],
 ["practice_crossbow", "Practice Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, weight(3)|spd_rtng(42)| shoot_speed(68) | thrust_damage(32,blunt)|max_ammo(1),imodbits_crossbow],
 ["practice_javelin", "Practice Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_primary|itp_next_item_as_melee,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 0, weight(5) | spd_rtng(91) | shoot_speed(28) | thrust_damage(27, blunt) | max_ammo(50) | weapon_length(75), imodbits_thrown],
 ["practice_javelin_melee", "practice_javelin_melee", [("javelin",0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry , itc_staff, 0, weight(1)|difficulty(0)|spd_rtng(91) |swing_damage(12, blunt)| thrust_damage(14,  blunt)|weapon_length(75),imodbits_polearm ],
 ["practice_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(10)|weapon_length(0),imodbits_thrown ],
 ["practice_throwing_daggers_100_amount", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(100)|weapon_length(0),imodbits_thrown ],
# ["cheap_shirt","Cheap Shirt", [("shirt",0)], itp_type_body_armor|itp_covers_legs, 0, 4,weight(1.25)|body_armor(3),imodbits_none],
 ["practice_horse","Practice Horse", [("saddle_horse",0)], itp_type_horse, 0, 37,body_armor(10)|horse_speed(40)|horse_maneuver(37)|horse_charge(14),imodbits_none],
 ["practice_arrows","Practice Arrows", [("arena_arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_missile],
## ["practice_arrows","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo)], itp_type_arrows, 0, 31,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_none],
 ["practice_bolts","Practice Bolts", [("bolt",0),("flying_bolt",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(49),imodbits_missile],
 ["practice_arrows_10_amount","Practice Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(10),imodbits_missile],
 ["practice_arrows_100_amount","Practice Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(100),imodbits_missile],
 ["practice_bolts_9_amount","Practice Bolts", [("bolt",0),("flying_bolt",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(9),imodbits_missile],
 ["practice_boots", "Practice Boots", [("boot_nomad_a",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 11 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10), imodbits_cloth ],
 ["red_tourney_armor","Red Tourney Armor", [("tourn_armor_a",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["blue_tourney_armor","Blue Tourney Armor", [("mail_shirt",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["green_tourney_armor","Green Tourney Armor", [("leather_vest",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["gold_tourney_armor","Gold Tourney Armor", [("padded_armor",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["red_tourney_helmet","Red Tourney Helmet",[("flattop_helmet",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
 ["blue_tourney_helmet","Blue Tourney Helmet",[("segmented_helm",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
 ["green_tourney_helmet","Green Tourney Helmet",[("hood_c",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
 ["gold_tourney_helmet","Gold Tourney Helmet",[("hood_a",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],

["arena_shield_red", "Shield", [("arena_shield_red",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_blue", "Shield", [("arena_shield_blue",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_green", "Shield", [("arena_shield_green",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_yellow", "Shield", [("arena_shield_yellow",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],

["arena_armor_white", "Arena Armor White", [("arena_armorW_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_red", "Arena Armor Red", [("arena_armorR_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_blue", "Arena Armor Blue", [("arena_armorB_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_green", "Arena Armor Green", [("arena_armorG_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_yellow", "Arena Armor Yellow", [("arena_armorY_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_tunic_white", "Arena Tunic White ", [("arena_tunicW_new",0)], itp_type_body_armor |itp_covers_legs ,0, 47 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_red", "Arena Tunic Red", [("arena_tunicR_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ], 
["arena_tunic_blue", "Arena Tunic Blue", [("arena_tunicB_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ], 
["arena_tunic_green", "Arena Tunic Green", [("arena_tunicG_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_yellow", "Arena Tunic Yellow", [("arena_tunicY_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
#headwear
["arena_helmet_red", "Arena Helmet Red", [("arena_helmetR",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_blue", "Arena Helmet Blue", [("arena_helmetB",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_green", "Arena Helmet Green", [("arena_helmetG",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_yellow", "Arena Helmet Yellow", [("arena_helmetY",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_white", "Steppe Helmet White", [("steppe_helmetW",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["steppe_helmet_red", "Steppe Helmet Red", [("steppe_helmetR",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["steppe_helmet_blue", "Steppe Helmet Blue", [("steppe_helmetB",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["steppe_helmet_green", "Steppe Helmet Green", [("steppe_helmetG",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["steppe_helmet_yellow", "Steppe Helmet Yellow", [("steppe_helmetY",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ], 
["tourney_helm_white", "Tourney Helm White", [("tourney_helmR",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_red", "Tourney Helm Red", [("tourney_helmR",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_blue", "Tourney Helm Blue", [("tourney_helmB",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_green", "Tourney Helm Green", [("tourney_helmG",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_yellow", "Tourney Helm Yellow", [("tourney_helmY",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_red", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_blue", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_green", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_yellow", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],

# A treatise on The Method of Mechanical Theorems Archimedes
 
#This book must be at the beginning of readable books
 ["book_tactics","De Re Militari", [("book_a",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],
 ["book_persuasion","Rhetorica ad Herennium", [("book_b",0)], itp_type_book, 0, 5000,weight(2)|abundance(100),imodbits_none],
 ["book_leadership","The Life of Alixenus the Great", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
 ["book_intelligence","Essays on Logic", [("book_e",0)], itp_type_book, 0, 2900,weight(2)|abundance(100),imodbits_none],
 ["book_trade","A Treatise on the Value of Things", [("book_f",0)], itp_type_book, 0, 3100,weight(2)|abundance(100),imodbits_none],
 ["book_weapon_mastery", "On the Art of Fighting with Swords", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
 ["book_engineering","Method of Mechanical Theorems", [("book_open",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],

#Reference books
#This book must be at the beginning of reference books
 ["book_wound_treatment_reference","The Book of Healing", [("book_c",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
 ["book_training_reference","Manual of Arms", [("book_open",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
 ["book_surgery_reference","The Great Book of Surgery", [("book_c",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],

 #other trade goods (first one is spice)
 ["spice","Spice", [("spice_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none,[], [fac_no_faction]],
 ["salt","Salt", [("salt_sack",0)], itp_merchandise|itp_type_goods, 0, 255,weight(50)|abundance(120),imodbits_none,[], [fac_no_faction]],


 #["flour","Flour", [("salt_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 40,weight(50)|abundance(100)|food_quality(45)|max_ammo(50),imodbits_none],

 ["oil","Oil", [("oil",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 450,weight(50)|abundance(60)|max_ammo(50),imodbits_none,[], [fac_no_faction]],

 ["pottery","Pottery", [("jug",0)], itp_merchandise|itp_type_goods, 0, 100,weight(50)|abundance(90),imodbits_none,[], [fac_no_faction]],

 ["raw_flax","Flax Bundle", [("raw_flax",0)], itp_merchandise|itp_type_goods, 0, 150,weight(40)|abundance(90),imodbits_none,[], [fac_no_faction]],
 ["linen","Linen", [("linen",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbits_none,[], [fac_no_faction]],

 ["wool","Wool", [("wool_sack",0)], itp_merchandise|itp_type_goods, 0, 130,weight(40)|abundance(90),imodbits_none,[], [fac_no_faction]],
 ["wool_cloth","Wool Cloth", [("wool_cloth",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbits_none,[], [fac_no_faction]],

 ["raw_silk","Raw Silk", [("raw_silk_bundle",0)], itp_merchandise|itp_type_goods, 0, 600,weight(30)|abundance(90),imodbits_none,[], [fac_no_faction]],
 ["raw_dyes","Dyes", [("dyes",0)], itp_merchandise|itp_type_goods, 0, 200,weight(10)|abundance(90),imodbits_none,[], [fac_no_faction]],
 ["velvet","Velvet", [("velvet",0)], itp_merchandise|itp_type_goods, 0, 1025,weight(40)|abundance(30),imodbits_none,[], [fac_no_faction]],

 ["iron","Iron", [("iron",0)], itp_merchandise|itp_type_goods, 0,264,weight(60)|abundance(60),imodbits_none,[], [fac_no_faction]],
 ["tools","Tools", [("iron_hammer",0)], itp_merchandise|itp_type_goods, 0, 410,weight(50)|abundance(90),imodbits_none,[], [fac_no_faction]],

 ["raw_leather","Hides", [("leatherwork_inventory",0)], itp_merchandise|itp_type_goods, 0, 120,weight(40)|abundance(90),imodbits_none,[], [fac_no_faction]],
 ["leatherwork","Leatherwork", [("leatherwork_frame",0)], itp_merchandise|itp_type_goods, 0, 220,weight(40)|abundance(90),imodbits_none,[], [fac_no_faction]],
 
 ["raw_date_fruit","Date Fruit", [("date_inventory",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 120,weight(40)|food_quality(10)|max_ammo(10),imodbits_none,[], [fac_no_faction]],
 ["furs","Furs", [("fur_pack",0)], itp_merchandise|itp_type_goods, 0, 391,weight(40)|abundance(90),imodbits_none,[], [fac_no_faction]],

 ["wine","Wine", [("amphora_slim",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 220,weight(30)|abundance(60)|max_ammo(50),imodbits_none,[], [fac_no_faction]],
 ["ale","Ale", [("ale_barrel",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 120,weight(30)|abundance(70)|max_ammo(50),imodbits_none,[], [fac_no_faction]],

# ["dry_bread", "wheat_sack", itp_type_goods|itp_consumable, 0, slt_none,view_goods,95,weight(2),max_ammo(50),imodbits_none],
#foods (first one is smoked_fish)
 ["smoked_fish","Smoked Fish", [("smoked_fish",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 65,weight(15)|abundance(110)|food_quality(50)|max_ammo(25),imodbits_none,[], [fac_no_faction]],
 ["cheese","Cheese", [("cheese_b",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 75,weight(6)|abundance(110)|food_quality(40)|max_ammo(15),imodbits_none,[], [fac_no_faction]],
 ["honey","Honey", [("honey_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 220,weight(5)|abundance(110)|food_quality(40)|max_ammo(15),imodbits_none,[], [fac_no_faction]],
 ["sausages","Sausages", [("sausages",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 85,weight(10)|abundance(110)|food_quality(40)|max_ammo(20),imodbits_none,[], [fac_no_faction]],
 ["cabbages","Cabbages", [("cabbage",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 30,weight(15)|abundance(110)|food_quality(40)|max_ammo(25),imodbits_none,[], [fac_no_faction]],
 ["dried_meat","Dried Meat", [("smoked_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 85,weight(15)|abundance(100)|food_quality(70)|max_ammo(25),imodbits_none,[], [fac_no_faction]],
 ["apples","Fruit", [("apple_basket",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 44,weight(20)|abundance(110)|food_quality(40)|max_ammo(25),imodbits_none,[], [fac_no_faction]],
 ["raw_grapes","Grapes", [("grapes_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 75,weight(40)|abundance(90)|food_quality(10)|max_ammo(5),imodbits_none,[], [fac_no_faction]], #x2 for wine
 ["raw_olives","Olives", [("olive_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 100,weight(40)|abundance(90)|food_quality(10)|max_ammo(5),imodbits_none,[], [fac_no_faction]], #x3 for oil
 ["grain","Grain", [("wheat_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 30,weight(30)|abundance(110)|food_quality(40)|max_ammo(25),imodbits_none,[], [fac_no_faction]],

 ["cattle_meat","Beef", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 80,weight(20)|abundance(100)|food_quality(80)|max_ammo(25),imodbits_none,[], [fac_no_faction]],
 ["bread","Bread", [("bread_a",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 50,weight(30)|abundance(110)|food_quality(40)|max_ammo(25),imodbits_none,[], [fac_no_faction]],
 ["chicken","Chicken", [("chicken",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 95,weight(10)|abundance(110)|food_quality(40)|max_ammo(25),imodbits_none,[], [fac_no_faction]],
 ["pork","Pork", [("pork",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 75,weight(15)|abundance(100)|food_quality(70)|max_ammo(25),imodbits_none,[], [fac_no_faction]],
 ["butter","Butter", [("butter_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 150,weight(6)|abundance(110)|food_quality(40)|max_ammo(15),imodbits_none,[], [fac_no_faction]],
 ["siege_supply","Supplies", [("ale_barrel",0)], itp_type_goods|itp_consumable|itp_food, 0, 2000,weight(40)|abundance(0)|food_quality(50)|max_ammo(100),imodbits_none],

#windmelodie new trade goods begin
 ["good_whisky","whisky", [("good_whisky",0)], itp_merchandise|itp_type_goods, 0, 950,weight(40)|abundance(100),imodbits_none,[], [fac_civilian]],
 ["good_glasswork","glasswork", [("good_glasswork",0)], itp_merchandise|itp_type_goods, 0, 1150,weight(40)|abundance(100),imodbits_none,[], [fac_civilian]],
 ["good_turkish_carpet","turkish_carpet", [("good_turkish_carpet",0)], itp_merchandise|itp_type_goods, 0, 1230,weight(40)|abundance(100),imodbits_none,[], [fac_civilian]],
 ["good_pepper","pepper", [("good_pepper",0)], itp_merchandise|itp_type_goods, 0, 780,weight(40)|abundance(100),imodbits_none,[], [fac_civilian]],
 ["good_nutmeg","nutmeg", [("good_nutmeg",0)], itp_merchandise|itp_type_goods, 0, 1090,weight(40)|abundance(100),imodbits_none,[], [fac_civilian]],
 ["good_chinese_cloth","chinese_cloth", [("good_chinese_cloth",0)], itp_merchandise|itp_type_goods, 0, 1480,weight(40)|abundance(100),imodbits_none,[], [fac_civilian]],
 ["good_studhorse","studhorse", [("good_studhorse",0)], itp_merchandise|itp_type_goods, 0, 1300,weight(40)|abundance(100),imodbits_none,[], [fac_civilian]],
 ["good_vodka","vodka", [("good_vodka",0)], itp_merchandise|itp_type_goods, 0, 700,weight(40)|abundance(100),imodbits_none,[], [fac_civilian]],
 ["good_sake","sake", [("good_sake",0)], itp_merchandise|itp_type_goods, 0, 750,weight(40)|abundance(100),imodbits_none,[], [fac_civilian]],
 ["good_mercury","mercury", [("good_mercury",0)], itp_merchandise|itp_type_goods, 0, 1250,weight(40)|abundance(100),imodbits_none,[], [fac_civilian]],
 ["good_tobacco","tobacco", [("good_tobacco",0)], itp_merchandise|itp_type_goods, 0, 1080,weight(40)|abundance(100),imodbits_none,[], [fac_civilian]],
#windmelodie new trade goods end


 #Would like to remove flour altogether and reduce chicken, pork and butter (perishables) to non-trade items. Apples could perhaps become a generic "fruit", also representing dried fruit and grapes
 # Armagan: changed order so that it'll be easier to remove them from trade goods if necessary.
#************************************************************************************************
# ITEMS before this point are hardcoded into item_codes.h and their order should not be changed!
#************************************************************************************************

# Quest Items

 ["quest_wine","Wine", [("amphora_slim",0)], itp_type_goods, 0, 46,weight(40)|abundance(60)|max_ammo(50),imodbits_none],
 ["quest_ale","Ale", [("ale_barrel",0)], itp_type_goods, 0, 31,weight(40)|abundance(70)|max_ammo(50),imodbits_none],

 
# Tutorial Items

 ["tutorial_sword", "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(18 , cut) | thrust_damage(15 ,  pierce),imodbits_sword ],
 ["tutorial_axe", "Axe", [("iron_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(4)|difficulty(0)|spd_rtng(91) | weapon_length(108)|swing_damage(19 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_spear", "Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 0 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
 ["tutorial_club", "Club", [("club",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
 ["tutorial_battle_axe", "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(88) | weapon_length(108)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_arrows","Arrows", [("arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(0,pierce)|max_ammo(20),imodbits_missile],
 ["tutorial_bolts","Bolts", [("bolt",0),("flying_bolt",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(0,pierce)|max_ammo(18),imodbits_missile],
 ["tutorial_short_bow", "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 0 , weight(1)|difficulty(0)|spd_rtng(98) | shoot_speed(49) | thrust_damage(12 ,  pierce  ),imodbits_bow ],
 ["tutorial_crossbow", "Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0 , weight(3)|difficulty(0)|spd_rtng(42)|  shoot_speed(68) | thrust_damage(32,pierce)|max_ammo(1),imodbits_crossbow ],
 ["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile ],
 ["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
 ["tutorial_shield", "Kite Shield", [("shield_kite_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
 ["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
 ["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],

# Horses: sumpter horse/ pack horse, saddle horse, steppe horse, warm blood, geldling, stallion,   war mount, charger, 
# Carthorse, hunter, heavy hunter, hackney, palfrey, courser, destrier.
 ["sumpter_horse","Sumpter Horse", [("sumpter_horse",0)], itp_merchandise|itp_type_horse, 0, 134,abundance(90)|hit_points(100)|body_armor(14)|difficulty(1)|horse_speed(37)|horse_maneuver(39)|horse_charge(9)|horse_scale(100),imodbits_horse_basic],
 ["saddle_horse","Saddle Horse", [("saddle_horse",0),("horse_c",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 240,abundance(90)|hit_points(100)|body_armor(8)|difficulty(1)|horse_speed(45)|horse_maneuver(44)|horse_charge(10)|horse_scale(104),imodbits_horse_basic],
 ["steppe_horse","Steppe Horse", [("steppe_horse",0)], itp_merchandise|itp_type_horse, 0, 192,abundance(80)|hit_points(120)|body_armor(10)|difficulty(2)|horse_speed(40)|horse_maneuver(51)|horse_charge(8)|horse_scale(98),imodbits_horse_basic, [], []],
 ["arabian_horse_a","Desert Horse", [("arabian_horse_a",0)], itp_merchandise|itp_type_horse, 0, 550,abundance(80)|hit_points(110)|body_armor(10)|difficulty(2)|horse_speed(42)|horse_maneuver(50)|horse_charge(12)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], arb_faction],
 ["courser","Courser", [("courser",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(70)|body_armor(12)|hit_points(110)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(12)|horse_scale(106),imodbits_horse_basic|imodbit_champion],
 ["arabian_horse_b","Sarranid Horse", [("arabian_horse_b",0)], itp_merchandise|itp_type_horse, 0, 700,abundance(80)|hit_points(120)|body_armor(10)|difficulty(3)|horse_speed(43)|horse_maneuver(54)|horse_charge(16)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], arb_faction],
 ["hunter","Hunter", [("hunting_horse",0),("hunting_horse",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 810,abundance(60)|hit_points(160)|body_armor(18)|difficulty(3)|horse_speed(43)|horse_maneuver(44)|horse_charge(24)|horse_scale(108),imodbits_horse_basic|imodbit_champion],
 ["warhorse","War Horse", [("warhorse_chain",0)], itp_merchandise|itp_type_horse, 0, 1224,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], we_faction],
 ["charger","Charger", [("charger_new",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(165)|body_armor(58)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], we_faction],
["warhorse_sarranid","Sarranian War Horse", [("warhorse_sarranid",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(165)|body_armor(58)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_6]],
["warhorse_steppe","Steppe Charger", [("warhorse_steppe",0)], itp_merchandise|itp_type_horse, 0, 1400,abundance(45)|hit_points(150)|body_armor(40)|difficulty(4)|horse_speed(40)|horse_maneuver(50)|horse_charge(28)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_3,fac_kingdom_2]],

#yifeng horse
["red_lion_charger","Red Lion Charger", [("rampant_lion_red2",0)], itp_merchandise|itp_type_horse, 0, 1711,abundance(40)|hit_points(175)|body_armor(48)|difficulty(4)|horse_speed(43)|horse_maneuver(48)|horse_charge(33)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_8]],
["red_yellow_charger","Red Yellow Charger", [("warhorse_vol",0)], itp_merchandise|itp_type_horse, 0, 1424,abundance(50)|hit_points(165)|body_armor(45)|difficulty(4)|horse_speed(45)|horse_maneuver(41)|horse_charge(30)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_9]],
["blue_plate_charger","Bule Plate Charger", [("charger_late_France",0)], itp_merchandise|itp_type_horse, 0, 2211,abundance(30)|hit_points(185)|body_armor(60)|difficulty(4)|horse_speed(38)|horse_maneuver(40)|horse_charge(35)|horse_scale(120),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],
["bule_charger","Bule Charger", [("barded_france",0)], itp_merchandise|itp_type_horse, 0, 1424,abundance(50)|hit_points(165)|body_armor(45)|difficulty(4)|horse_speed(45)|horse_maneuver(41)|horse_charge(30)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1]],
["warhorse_china","Warhorse China", [("warhorse_china",0)], itp_merchandise|itp_type_horse, 0, 1711,abundance(40)|hit_points(175)|body_armor(54)|difficulty(4)|horse_speed(43)|horse_maneuver(48)|horse_charge(33)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_7]],
["song_charger_b","Song Charger", [("Song_charger_b",0)], itp_merchandise|itp_type_horse, 0, 1474,abundance(50)|hit_points(165)|body_armor(48)|difficulty(4)|horse_speed(43)|horse_maneuver(40)|horse_charge(32)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_7]],

["camel","camel", [("camel",0)], itp_merchandise|itp_type_horse, 0, 1011,abundance(40)|hit_points(165)|body_armor(25)|difficulty(2)|horse_speed(35)|horse_maneuver(48)|horse_charge(25)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_14] ],

["charge_france","charge_france", [("charge_france",0)], itp_merchandise|itp_type_horse, 0, 2111,abundance(40)|hit_points(175)|body_armor(45)|difficulty(4)|horse_speed(42)|horse_maneuver(48)|horse_charge(32)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1] ],
["charge_france_2","charge_france_2", [("charge_france_2",0)], itp_merchandise|itp_type_horse, 0, 2111,abundance(40)|hit_points(175)|body_armor(45)|difficulty(4)|horse_speed(42)|horse_maneuver(48)|horse_charge(32)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1] ],
["charge_german","charge_german", [("charge_german",0)], itp_merchandise|itp_type_horse, 0, 2111,abundance(40)|hit_points(175)|body_armor(45)|difficulty(4)|horse_speed(42)|horse_maneuver(48)|horse_charge(32)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_3] ],
["charge_teuton_2","charge_teuton_2", [("charge_teuton_2",0)], itp_merchandise|itp_type_horse, 0, 2111,abundance(40)|hit_points(175)|body_armor(45)|difficulty(4)|horse_speed(42)|horse_maneuver(48)|horse_charge(32)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_3] ],
["platecharger_france","platecharger_france", [("platecharger_france",0)], itp_merchandise|itp_type_horse, 0, 2611,abundance(40)|hit_points(175)|body_armor(60)|difficulty(5)|horse_speed(36)|horse_maneuver(48)|horse_charge(41)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1] ],
["platecharger_france_2","platecharger_france_2", [("platecharger_france_2",0)], itp_merchandise|itp_type_horse, 0, 2711,abundance(40)|hit_points(175)|body_armor(60)|difficulty(5)|horse_speed(36)|horse_maneuver(48)|horse_charge(41)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1] ],
["platecharger_german","platecharger_german", [("platecharger_german",0)], itp_merchandise|itp_type_horse, 0, 2811,abundance(40)|hit_points(175)|body_armor(60)|difficulty(5)|horse_speed(36)|horse_maneuver(48)|horse_charge(41)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_3] ],

  ["yf_ydzx","eliphant1", [("yf_ydzx",0)], itp_merchandise|itp_type_horse, 0, 4811,abundance(40)|hit_points(250)|body_armor(60)|difficulty(5)|horse_speed(35)|horse_maneuver(20)|horse_charge(70)|horse_scale(115),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_17, fac_kingdom_18]],

  ["baima","baima", [("baima",0)], itp_merchandise|itp_type_horse, 0, 1991,abundance(40)|hit_points(155)|body_armor(20)|difficulty(3)|horse_speed(45)|horse_maneuver(48)|horse_charge(25)|horse_scale(108),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_11] ],
["hongma","hongma", [("hongma",0)], itp_merchandise|itp_type_horse, 0, 1991,abundance(40)|hit_points(155)|body_armor(20)|difficulty(3)|horse_speed(45)|horse_maneuver(48)|horse_charge(25)|horse_scale(108),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_7] ],
["huangma","huangma", [("huangma",0)], itp_merchandise|itp_type_horse, 0, 1991,abundance(40)|hit_points(155)|body_armor(20)|difficulty(3)|horse_speed(45)|horse_maneuver(48)|horse_charge(25)|horse_scale(108),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_11] ],
["baima1","baima1", [("limaoma",0)], itp_merchandise|itp_type_horse, 0, 1991,abundance(40)|hit_points(155)|body_armor(20)|difficulty(3)|horse_speed(45)|horse_maneuver(48)|horse_charge(25)|horse_scale(108),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_7] ],

##HolyAce
["qing_horse","horse qing", [("qing_horse",0)], itp_merchandise|itp_type_horse, 0, 1711,abundance(40)|hit_points(175)|body_armor(34)|difficulty(4)|horse_speed(45)|
horse_maneuver(48)|horse_charge(27)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_7]],

["qing_horse_z","Warhorse qing", [("qing_horse_z",0)], itp_merchandise|itp_type_horse, 0, 1711,abundance(40)|hit_points(175)|body_armor(44)|difficulty(4)|horse_speed(43)|
horse_maneuver(48)|horse_charge(33)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_7]],


["long_hospitaller_horse","hospitaller_horse", [("long_hospitaller_horse",0)], itp_merchandise|itp_type_horse, 0, 2011,abundance(40)|hit_points(175)|body_armor(47)|difficulty(4)|horse_speed(43)|horse_maneuver(48)|horse_charge(30)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_8]],



#whalebone crossbow, yew bow, war bow, arming sword 
 ["arrows","Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_default_ammo, itcf_carry_quiver_back, 72,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(50),imodbits_missile],
 ["khergit_arrows","Khergit Arrows", [("arrow_b",0),("flying_missile",ixmesh_flying_ammo),("quiver_b", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 410,weight(3.5)|abundance(30)|weapon_length(95)|thrust_damage(3,pierce)|max_ammo(50),imodbits_missile],
["daming_arrow","DaMing_arrow", [("DaMing_arrow",0),("flying_missile",ixmesh_flying_ammo),("DaMing_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_front_right, 350,weight(2)|abundance(50)|weapon_length(91)|thrust_damage(3,pierce)|max_ammo(50),imodbits_missile, [], [fac_kingdom_7]],

 ["barbed_arrows","Barbed Arrows", [("barbed_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver_d", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 124,weight(3)|abundance(70)|weapon_length(95)|thrust_damage(2,pierce)|max_ammo(50),imodbits_missile],
 ["bodkin_arrows","Bodkin Arrows", [("piercing_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver_c", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 350,weight(3)|abundance(50)|weapon_length(91)|thrust_damage(3,pierce)|max_ammo(50),imodbits_missile],
 ["bolts","Bolts", [("bolt",0),("flying_bolt",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_merchandise|itp_default_ammo|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 64,weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(1,pierce)|max_ammo(50),imodbits_missile],
 ["steel_bolts","Steel Bolts", [("bolt",0),("flying_bolt",ixmesh_flying_ammo),("bolt_bag_c", ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 210,weight(2.5)|abundance(20)|weapon_length(63)|thrust_damage(2,pierce)|max_ammo(50),imodbits_missile],
 ["cartridges","Cartridges", [("DaMing_zidantong",0),("huojian_fly3",ixmesh_flying_ammo)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_default_ammo, 0, 41,weight(2.25)|abundance(160)|weapon_length(3)|thrust_damage(1,pierce)|max_ammo(50),imodbits_missile,[  (ti_on_missile_hit, 
    [
	(particle_system_burst_no_sync, "psys_musket_hit", pos1, 8),
	(particle_system_burst_no_sync, "psys_musket_hit_particle", pos1, 8),

    ])
],[] ],
["grenades1", "cheating Grenades ammo", [("metal_grenade",0),("huojian_fly",ixmesh_flying_ammo)],
itp_type_bullets|itp_can_penetrate_shield|itp_default_ammo, 0, 150000,weight(10)|abundance(150)|weapon_length(8)|thrust_damage(10,blunt)|max_ammo(7),imodbits_missile,
[(ti_on_missile_hit, [
    (store_trigger_param_1, ":shooter_agent_no"),
	(init_position, pos51),
	(position_copy_origin, pos51, pos1), # Copy hit position for the script
	(call_script, "script_oim_deliver_granade_damage", ":shooter_agent_no", 150, 5), 
  ])]],

  ["grenades2", "cheating fire arrow", [("piercing_arrow",0),("huojian_fly",ixmesh_flying_ammo),("quiver_c",ixmesh_carry)],
itp_type_arrows|itp_can_penetrate_shield|itcf_carry_quiver_back_right|itp_default_ammo, 0, 200000,weight(10)|abundance(150)|weapon_length(91)|thrust_damage(10,blunt)|max_ammo(13),imodbits_missile,
[(ti_on_missile_hit, [
    (store_trigger_param_1, ":shooter_agent_no"),
	(init_position, pos51),
	(position_copy_origin, pos51, pos1), # Copy hit position for the script
	(call_script, "script_oim_deliver_granade_damage", ":shooter_agent_no", 150, 5), 
  ])]],


["pilgrim_disguise", "Pilgrim Disguise", [("pilgrim_outfit",0)], 0| itp_type_body_armor |itp_covers_legs |itp_civilian ,0, 25 , weight(2)|abundance(100)|head_armor(0)|body_armor(19)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["pilgrim_hood", "Pilgrim Hood", [("pilgrim_hood",0)], 0| itp_type_head_armor |itp_civilian  ,0, 35 , weight(1.25)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

# ARMOR
#handwear
["leather_gloves","Leather Gloves", [("leather_gloves_L",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(0.25)|abundance(120)|body_armor(2)|difficulty(0),imodbits_cloth],
["mail_mittens","Mail Mittens", [("mail_mittens_L",0)], itp_merchandise|itp_type_hand_armor,0, 350, weight(0.5)|abundance(100)|body_armor(4)|difficulty(0),imodbits_armor],
["scale_gauntlets","Scale Gauntlets", [("scale_gauntlets_b_L",0)], itp_merchandise|itp_type_hand_armor,0, 710, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor],
["lamellar_gauntlets","Lamellar Gauntlets", [("scale_gauntlets_a_L",0)], itp_merchandise|itp_type_hand_armor,0, 910, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor],
["gauntlets","Gauntlets", [("gauntlets_L",0),("gauntlets_L",imodbit_reinforced)], itp_merchandise|itp_type_hand_armor,0, 1040, weight(1.0)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor,[], we_faction],
#yifeng glove
 ["new_gauntlets","New Scale Gauntlets", [("acb1_glv_L",0)], itp_merchandise|itp_type_hand_armor,0, 710, weight(0.75)|abundance(100)|body_armor(12)|difficulty(0),imodbits_armor, [], [fac_kingdom_4]],

 ["zuoshou1_L","zuoshou1_L", [("zuoshou1_L",0)], itp_merchandise|itp_type_hand_armor,0, 1350, weight(2.5)|abundance(100)|body_armor(9)|difficulty(0),imodbits_armor, [], [fac_kingdom_1]],
["zuoshou2_L","zuoshou2_L", [("zuoshou2_L",0)], itp_merchandise|itp_type_hand_armor,0, 1350, weight(2.5)|abundance(100)|body_armor(9)|difficulty(0),imodbits_armor, [], [fac_kingdom_1]],
["zuoshou3_L","zuoshou3_L", [("zuoshou3_L",0)], itp_merchandise|itp_type_hand_armor,0, 1350, weight(2.5)|abundance(100)|body_armor(9)|difficulty(0),imodbits_armor, [], [fac_kingdom_8]],
["zuoshou4_L","zuoshou4_L", [("zuoshou4_L",0)], itp_merchandise|itp_type_hand_armor,0, 1350, weight(2.5)|abundance(100)|body_armor(9)|difficulty(0),imodbits_armor, [], [fac_kingdom_3]],
["zuoshou5_L","zuoshou5_L", [("zuoshou5_L",0)], itp_merchandise|itp_type_hand_armor,0, 1350, weight(2.5)|abundance(100)|body_armor(9)|difficulty(0),imodbits_armor, [], [fac_kingdom_3]],

["hourglass_gauntlets_L","hourglass_gauntlets", [("hourglass_gauntlets_L",0)], itp_merchandise|itp_merchandise|itp_type_hand_armor,0, 1050, weight(2.5)|abundance(100)|body_armor(9)|difficulty(0),imodbits_armor, [], we_faction],
 ["kote_L","kote_L", [("kote_L",0)], itp_merchandise|itp_type_hand_armor,0, 1250, weight(2.5)|abundance(100)|body_armor(8)|difficulty(0),imodbits_armor, [], [fac_kingdom_11]],

 ["black_hand11","black_hand_L", [("black_hand_L",0)], itp_merchandise|itp_type_hand_armor,0, 10, weight(0.1)|abundance(120)|body_armor(1)|difficulty(0),imodbits_cloth],

#glove end

#footwear
["wrapping_boots", "Wrapping Boots", [("wrapping_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 80 , weight(0.25)|abundance(71)|head_armor(0)|body_armor(0)|leg_armor(3)|difficulty(0) ,imodbits_cloth ],
["woolen_hose", "Woolen Hose", [("woolen_hose_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 100, weight(0.25)|abundance(57)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["blue_hose", "Blue Hose", [("blue_hose_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 160 , weight(0.25)|abundance(38)|head_armor(0)|body_armor(0)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["hunter_boots", "Hunter Boots", [("hunter_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature,0,
 50 , weight(0.5)|abundance(125)|head_armor(0)|body_armor(0)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["hide_boots", "Hide Boots", [("hide_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 80 , weight(0.5)|abundance(118)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["ankle_boots", "Ankle Boots", [("ankle_boots_a_new",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 90 , weight(0.75)|abundance(113)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["nomad_boots", "Nomad Boots", [("nomad_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 120 , weight(1)|abundance(104)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["leather_boots", "Leather Boots", [("leather_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 160 , weight(1.25)|abundance(89)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["splinted_leather_greaves", "Splinted Leather Greaves", [("leather_greaves_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 320 , weight(1.75)|abundance(65)|head_armor(0)|body_armor(0)|leg_armor(21)|difficulty(0) ,imodbits_armor,[], we_faction ],
["mail_chausses", "Mail Chausses", [("mail_chausses_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
 450 , weight(2.25)|abundance(58)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_armor,[], we_faction ],
["splinted_greaves", "Splinted Greaves", [("splinted_greaves_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 900 , weight(2.5)|abundance(39)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(7) ,imodbits_armor ],
["mail_boots", "Mail Boots", [("mail_boots_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
 1430 , weight(3)|abundance(31)|head_armor(0)|body_armor(0)|leg_armor(31)|difficulty(8) ,imodbits_armor,[], we_faction ],
["iron_greaves", "Iron Greaves", [("iron_greaves_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 2000 , weight(3.25)|abundance(26)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor,[], we_faction ],
["black_greaves", "Black Greaves", [("black_greaves",0)], itp_type_foot_armor  | itp_attach_armature,0,
2800 , weight(3.5)|abundance(21)|head_armor(0)|body_armor(0)|leg_armor(35)|difficulty(10) ,imodbits_armor,[], we_faction ],
["khergit_leather_boots", "Khergit Leather Boots", [("khergit_leather_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 210 , weight(1.5)|abundance(79)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_cloth ],
["sarranid_boots_a", "Sarranid Shoes", [("sarranid_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 60 , weight(0.25)|abundance(125)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth,[], arb_faction ],
["sarranid_boots_b", "Sarranid Leather Boots", [("sarranid_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 170 , weight(1.25)|abundance(86)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ,[], arb_faction],
["sarranid_boots_c", "Plated Boots", [("sarranid_camel_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 270 , weight(1.75)|abundance(72)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_plate ,[], arb_faction],
["sarranid_boots_d", "Sarranid Mail Boots", [("sarranid_mail_chausses",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 1140 , weight(3)|abundance(36)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(9) ,imodbits_armor,[], arb_faction ],

 #yifeng boots
   ["fysg_bin_shazei01_t", "fysg_bin_shazei01_t", [("fysg_bin_shazei01_t",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 80 , weight(0.5)|abundance(110)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(6) ,imodbits_armor ,[], [fac_kingdom_7]],

 ["new_plate_boots", "Plate Boots", [("acb1_boo",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
 1560 , weight(3)|abundance(28)|head_armor(0)|body_armor(0)|leg_armor(31)|difficulty(10) ,imodbits_armor , [], [fac_kingdom_4]],
["new_leather_boots", "New Leather Boots", [("rus_cav_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 490 , weight(2.5)|abundance(57)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_cloth ],

  ["b_h1", "highlander boots", [("b_h1",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 160 , weight(1)|abundance(84)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_armor , [], [fac_kingdom_8]],
  ["b_h1_1", "highlander boots2", [("b_h1_1",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 160 , weight(1)|abundance(84)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_armor , [], [fac_kingdom_8]],
 ["b_h2", "highlander boots3", [("b_h2",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 270 , weight(1.75)|abundance(72)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_armor , [], [fac_kingdom_8]],
  ["b_h2_1", "highlander boots4", [("b_h2_1",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 270 , weight(1.75)|abundance(72)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_armor , [], [fac_kingdom_8]],

 ["xie1", "xie1", [("xie1",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 1760 , weight(3.25)|abundance(27)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(8) ,imodbits_armor , [], [fac_kingdom_1]],
 
 
 
 
 
 
 
["xie2", "xie2", [("xie2",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 1810 , weight(3.25)|abundance(26)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(10) ,imodbits_armor , [], [fac_kingdom_1]],
["xie3", "xie3", [("xie3",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 1860 , weight(3.5)|abundance(26)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(10) ,imodbits_armor , [], [fac_kingdom_8]],
["xie4", "xie4", [("xie4",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 1860 , weight(3.25)|abundance(26)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(10) ,imodbits_armor , [], [fac_kingdom_3]],
["xie5", "xie5", [("xie5",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 1910 , weight(3.25)|abundance(25)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(10) ,imodbits_armor , [], [fac_kingdom_3]],

 ["splinted_greaves_nospurs", "splinted_greaves_nospurs", [("splinted_greaves_nospurs",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 620 , weight(1.75)|abundance(72)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_armor ],

 ["kalmyk_tapki", "kalmyk_tapki", [("kalmyk_tapki",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 550 , weight(2.25)|abundance(51)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(7) ,imodbits_armor , [], [fac_kingdom_21] ],

   ["mokas", "mokas", [("mokas",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 70 , weight(0.5)|abundance(122)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_15] ],

   ["kazakh_boots", "kazakh_boots", [("kazakh_boots",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
160 , weight(1)|abundance(84)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_armor ],

 
   ["coyote_boots", "coyote_boots", [("coyote_boots",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 100 , weight(0.75)|abundance(109)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_armor , [], [fac_kingdom_15] ],
  ["eagle_boots", "eagle_boots", [("eagle_boots",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 100 , weight(0.75)|abundance(109)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_armor , [], [fac_kingdom_15] ],
  ["jaguar_boots", "jaguar_boots", [("jaguar_boots",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 100 , weight(0.75)|abundance(109)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_15] ],
 ["cuahchiqueh_boots", "cuahchiqueh_boots", [("cuahchiqueh_boots",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 100 , weight(0.75)|abundance(109)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_15] ],

   ["cuahchiqueh_boots3", "cuahchiqueh_boots3", [("cuahchiqueh_boots3",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 100 , weight(0.75)|abundance(109)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_15] ],

  ["cuahchiqueh_boots3333", "cuahchiqueh_boots3333", [("cuahchiqueh_boots3333",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 100 , weight(0.75)|abundance(109)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_15] ],

  ["cuahchiqueh_boots2", "cuahchiqueh_boots2", [("cuahchiqueh_boots2",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 100 , weight(0.75)|abundance(109)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_15] ],

  ["shadow_greaves", "shadow_greaves", [("shadow_greaves",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 100 , weight(0.75)|abundance(102)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_11] ],

  ["korean_boot", "korean_boot", [("korean_boot",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 100 , weight(0.75)|abundance(109)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_19] ],
 ["mongol_boot", "mongol_boot", [("mongol_boot",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 360 , weight(2)|abundance(62)|head_armor(0)|body_armor(0)|leg_armor(22)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_10] ],

 ["suneate", "suneate", [("suneate",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 760 , weight(2.5)|abundance(43)|head_armor(0)|body_armor(0)|leg_armor(27)|difficulty(7) ,imodbits_armor , [], [fac_kingdom_11]],
["yidazzkuixie", "yidazzkuixie", [("yidazzkuixie",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 270 , weight(1.75)|abundance(72)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_armor , [], [fac_kingdom_11]],
["jinyizzxie", "jinyizzxie", [("jinyizzxie",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 280 , weight(1.75)|abundance(70)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_armor , [], [fac_kingdom_11]],

 ["daming_boots", "DaMing_boots", [("DaMing_boots",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 270 , weight(1.75)|abundance(36)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_armor , [], [fac_kingdom_7]],

 ["black_foot11",  "black_Boots", [("black_foot",0)], itp_merchandise|itp_type_foot_armor | itp_attach_armature,0, 15 , weight(0.25)|abundance(120)|head_armor(0)|body_armor(0)|leg_armor(5)|difficulty(0) ,imodbits_cloth , [], []],
 #yifeng test inca  fac_kingdom_30
   ["incan_boots", "Incan_boots", [("incan_boots",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 21 , weight(0.25)|abundance(110)|head_armor(0)|body_armor(0)|leg_armor(5)|difficulty(0) ,imodbits_armor ,[], [fac_kingdom_30]],

#yifeng boots end
["sarranid_head_cloth", "Lady Head Cloth", [("tulbent",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sarranid_head_cloth_b", "Lady Head Cloth", [("tulbent_b",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sarranid_felt_head_cloth", "Head Cloth", [("common_tulbent",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sarranid_felt_head_cloth_b", "Head Cloth", [("common_tulbent_b",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],


#bodywear yifeng 1.5
["lady_dress_ruby", "Lady Dress", [("lady_dress_r",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["lady_dress_green", "Lady Dress", [("lady_dress_g",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["lady_dress_blue", "Lady Dress", [("lady_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["red_dress", "Red Dress", [("red_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["brown_dress", "Brown Dress", [("brown_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["green_dress", "Green Dress", [("green_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["khergit_lady_dress", "Khergit Lady Dress", [("khergit_lady_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["khergit_lady_dress_b", "Khergit Leather Lady Dress", [("khergit_lady_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_lady_dress", "Sarranid Lady Dress", [("sarranid_lady_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_lady_dress_b", "Sarranid Lady Dress", [("sarranid_lady_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_common_dress", "Sarranid Dress", [("sarranid_common_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_common_dress_b", "Sarranid Dress", [("sarranid_common_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(50)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["courtly_outfit", "Courtly Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(50)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["nobleman_outfit", "Nobleman Outfit", [("nobleman_outfit_b_new",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(50)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth ], 
##yifeng 1.5
["nomad_armor", "Nomad Armor", [("nomad_armor_new",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs   ,0, 25 , weight(2)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["khergit_armor", "Khergit Armor", [("khergit_armor_new",0)], itp_merchandise| itp_type_body_armor | itp_covers_legs ,0, 38 , weight(2)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_jacket", "Leather Jacket", [("leather_jacket_new",0)], itp_merchandise| itp_type_body_armor | itp_covers_legs  |itp_civilian ,0, 50 , weight(3)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

#NEW:
["rawhide_coat", "Rawhide Coat", [("coat_of_plates_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 12 , weight(5)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
#NEW: was lthr_armor_a
["leather_armor", "Leather Armor", [("tattered_leather_armor_a",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs  ,0, 65 , weight(7)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["fur_coat", "Fur Coat", [("fur_coat",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 117 , weight(6)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(6)|difficulty(0) ,imodbits_armor ],


#yifeng 1.5
#for future:
["coat", "Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(50)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["leather_coat", "Leather Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(50)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["mail_coat", "Coat of Mail", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(50)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["long_mail_coat", "Long Coat of Mail", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(50)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["mail_with_tunic_red", "Mail with Tunic", [("arena_armorR_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(8), imodbits_armor ],
["mail_with_tunic_green", "Mail with Tunic", [("arena_armorG_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(8), imodbits_armor ],
["hide_coat", "Hide Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(50)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["merchant_outfit", "Merchant Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(50)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["homespun_dress", "Homespun Dress", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(50)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["thick_coat", "Thick Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(50)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["coat_with_cape", "Coat with Cape", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(50)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["steppe_outfit", "Steppe Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(50)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["nordic_outfit", "Nordic Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(50)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["nordic_armor", "Nordic Armor", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(50)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["hide_armor", "Hide Armor", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(50)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["cloaked_tunic", "Cloaked Tunic", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(50)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["sleeveless_tunic", "Sleeveless Tunic", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(50)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["sleeveless_leather_tunic", "Sleeveless Leather Tunic", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(50)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["linen_shirt", "Linen Shirt", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(50)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["wool_coat", "Wool Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(50)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#end

["dress", "Dress", [("dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(50)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["blue_dress", "Blue Dress", [("blue_dress_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(50)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["peasant_dress", "Peasant Dress", [("peasant_dress_b_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(50)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ], 
["woolen_dress", "Woolen Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor|itp_civilian  |itp_covers_legs ,0,
 10 , weight(1.75)|abundance(50)|head_armor(0)|body_armor(8)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],

 ##yifeng 1.5
 
["shirt", "Shirt", [("shirt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 125 , weight(3.75)|abundance(130)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
 #NEW: was "linen_tunic"
["linen_tunic", "Linen Tunic", [("shirt_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 150 , weight(4)|abundance(125)|head_armor(0)|body_armor(6)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
 #NEW was cvl_costume_a
["short_tunic", "Red Tunic", [("rich_tunic_a",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 160 , weight(4.5)|abundance(125)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
#TODO:
 ["red_shirt", "Red Shirt", [("rich_tunic_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 160. , weight(4.5)|abundance(125)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
 ["red_tunic", "Red Tunic", [("arena_tunicR_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 170 , weight(4.5)|abundance(125)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],

 ["green_tunic", "Green Tunic", [("arena_tunicG_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 170 , weight(4.5)|abundance(125)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
 ["blue_tunic", "Blue Tunic", [("arena_tunicB_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 170 , weight(4.5)|abundance(125)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["robe", "Robe", [("robe",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 190 , weight(5)|abundance(121)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#NEW: was coarse_tunic
["coarse_tunic", "Tunic with vest", [("coarse_tunic_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 220 , weight(6)|abundance(112)|head_armor(0)|body_armor(11)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["leather_apron", "Leather Apron", [("leather_apron",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 260 , weight(6.5)|abundance(98)|head_armor(0)|body_armor(12)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
#NEW: was tabard_a
["tabard", "Tabard", [("tabard_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 270 , weight(7.5)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#NEW: was leather_vest
["leather_vest", "Leather Vest", [("leather_vest_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 280 , weight(8)|abundance(101)|head_armor(0)|body_armor(15)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["steppe_armor", "Steppe Armor", [("lamellar_leather",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 720 , weight(8.25)|abundance(40)|head_armor(0)|body_armor(16)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["gambeson", "Gambeson", [("white_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 340 , weight(10)|abundance(93)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["blue_gambeson", "Blue Gambeson", [("blue_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 390 , weight(10)|abundance(85)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
#NEW: was red_gambeson
["red_gambeson", "Red Gambeson", [("red_gambeson_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 390 , weight(10)|abundance(85)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
#NEW: was aketon_a
["padded_cloth", "Aketon", [("padded_cloth_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 380 , weight(11)|abundance(89)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#NEW:
 ["aketon_green", "Padded Cloth", [("padded_cloth_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 400 , weight(11)|abundance(84)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 #NEW: was "leather_jerkin"
["leather_jerkin", "Leather Jerkin", [("ragged_leather_jerkin",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 410 , weight(11.25)|abundance(85)|head_armor(0)|body_armor(23)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["nomad_vest", "Nomad Vest", [("nomad_vest_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 390 , weight(11)|abundance(86)|head_armor(0)|body_armor(22)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["ragged_outfit", "Ragged Outfit", [("ragged_outfit_a_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 450 , weight(11.25)|abundance(77)|head_armor(0)|body_armor(23)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 #NEW: was padded_leather
["padded_leather", "Padded Leather", [("leather_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0,
 540 , weight(13)|abundance(72)|head_armor(0)|body_armor(27)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["tribal_warrior_outfit", "Tribal Warrior Outfit", [("tribal_warrior_outfit_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 660 , weight(14.25)|abundance(64)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["nomad_robe", "Nomad Robe", [("nomad_robe_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0,
 740 , weight(15)|abundance(60)|head_armor(0)|body_armor(32)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
#["heraldric_armor", "Heraldric Armor", [("tourn_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 442 , weight(17)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#NEW: was "std_lthr_coat"
["studded_leather_coat", "Studded Leather Coat", [("leather_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1040 , weight(17)|abundance(47)|head_armor(0)|body_armor(36)|leg_armor(10)|difficulty(7) ,imodbits_armor ],

["byrnie", "Byrnie", [("byrnie_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1260 , weight(18)|abundance(44)|head_armor(0)|body_armor(39)|leg_armor(6)|difficulty(7) ,imodbits_armor,[], we_faction ],
#["blackwhite_surcoat", "Black and White Surcoat", [("surcoat_blackwhite",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 348 , weight(16)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#["green_surcoat", "Green Surcoat", [("surcoat_green",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 348 , weight(16)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#["blue_surcoat", "Blue Surcoat", [("surcoat_blue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 350 , weight(16)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#["red_surcoat", "Red Surcoat", [("surcoat_red",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 350 , weight(16)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#NEW: was "haubergeon_a"
["haubergeon", "Haubergeon", [("haubergeon_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1450 , weight(19)|abundance(40)|head_armor(0)|body_armor(41)|leg_armor(6)|difficulty(7) ,imodbits_armor,[], we_faction  ],

["lamellar_vest", "Lamellar Vest", [("lamellar_vest_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 1410 , weight(18.5)|abundance(40)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_cloth ],

["lamellar_vest_khergit", "Khergit Lamellar Vest", [("lamellar_vest_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 1460 , weight(18.5)|abundance(39)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_cloth ],

 #NEW: was mail_shirt
["mail_shirt", "Mail Shirt", [("mail_shirt_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1190 , weight(17.5)|abundance(43)|head_armor(0)|body_armor(37)|leg_armor(12)|difficulty(7) ,imodbits_armor,[], we_faction  ],

["mail_hauberk", "Mail Hauberk", [("hauberk_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1540 , weight(18.5)|abundance(37)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor,[], we_faction  ],

["mail_with_surcoat", "Mail with Surcoat", [("mail_long_surcoat_new",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 1910 , weight(19.5)|abundance(31)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(7) ,imodbits_armor,[], we_faction  ],
["surcoat_over_mail", "Surcoat over Mail", [("surcoat_over_mail_new",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 2060 , weight(20)|abundance(30)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor ,[], we_faction ],
#["lamellar_cuirass", "Lamellar Cuirass", [("lamellar_armor",0)], itp_type_body_armor  |itp_covers_legs,0, 1020 , weight(25)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(15)|difficulty(9) ,imodbits_armor ],
#NEW: was "brigandine_a"
["brigandine_red", "Brigandine", [("brigandine_b",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 2480 , weight(21)|abundance(27)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(8) ,imodbits_armor ,[], we_faction ],
["lamellar_armor", "Lamellar Armor", [("lamellar_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3010 , weight(23)|abundance(22)|head_armor(0)|body_armor(48)|leg_armor(13)|difficulty(8) ,imodbits_armor ],
["scale_armor", "Scale Armor", [("lamellar_armor_e",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3850 , weight(21)|abundance(24)|head_armor(0)|body_armor(52)|leg_armor(13)|difficulty(8) ,imodbits_armor  ],
 #NEW: was "reinf_jerkin"
["banded_armor", "Banded Armor", [("banded_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3530 , weight(21)|abundance(22)|head_armor(0)|body_armor(49)|leg_armor(14)|difficulty(8) ,imodbits_armor ,[], we_faction ],
#NEW: was hard_lthr_a
["cuir_bouilli", "Cuir Bouilli", [("cuir_bouilli_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3720 , weight(23)|abundance(20)|head_armor(0)|body_armor(50)|leg_armor(15)|difficulty(9) ,imodbits_armor ,[], we_faction ],
["coat_of_plates", "Coat of Plates", [("coat_of_plates_a",0)], itp_type_body_armor  |itp_covers_legs ,0,
 4220 , weight(24)|abundance(19)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(9) ,imodbits_armor,[], we_faction  ],
["coat_of_plates_red", "Coat of Plates", [("coat_of_plates_red",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 4220 , weight(24)|abundance(19)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(9) ,imodbits_armor ,[], we_faction ],
["plate_armor", "Plate Armor", [("full_plate_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 5660 , weight(25)|abundance(15)|head_armor(0)|body_armor(55)|leg_armor(17)|difficulty(9) ,imodbits_plate ,[], we_faction ],
["black_armor", "Black Armor", [("black_armor",0)], itp_type_body_armor  |itp_covers_legs ,0,
 6810 , weight(26)|abundance(13)|head_armor(0)|body_armor(57)|leg_armor(18)|difficulty(9) ,imodbits_plate ,[], we_faction ],

##armors_d
["pelt_coat", "Pelt Coat", [("thick_coat_a",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0,
 180, weight(5)|abundance(125)|head_armor(0)|body_armor(9)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
##armors_e
["khergit_elite_armor", "Khergit Elite Armor", [("lamellar_armor_d",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 4090 , weight(24)|abundance(19)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(9) ,imodbits_armor,[], arb_faction  ],
["vaegir_elite_armor", "Vaegir Elite Armor", [("lamellar_armor_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 4090 , weight(24)|abundance(19)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(9) ,imodbits_armor ,[], arb_faction],
["sarranid_elite_armor", "Sarranid Elite Armor", [("tunic_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian ,0,
 4090 , weight(24)|abundance(19)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(9) ,imodbits_armor,[], arb_faction ],

 ##yifeng armor
 ["volencia_mail_shirt", "Volencia Shirt", [("lauria_brig",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 1770 , weight(19)|abundance(34)|head_armor(0)|body_armor(42)|leg_armor(8)|difficulty(8) ,imodbits_armor ,[], we_faction],
["volencia_red_plate_armor", "Volencia Red Plate Armor", [("volencia_red_plate_armor",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 4890 , weight(24)|abundance(17)|head_armor(0)|body_armor(53)|leg_armor(15)|difficulty(9) ,imodbits_armor,[], we_faction ],
["volencia_king_armor", "Volencia King Armor", [("tiaodun_qishi",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 5720 , weight(25)|abundance(15)|head_armor(0)|body_armor(55)|leg_armor(16)|difficulty(9) ,imodbits_armor ,[], we_faction], 
["surcoat_over_mail_vol", "Volencia surcoat over Mail", [("surcoat_over_mail_vol",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 2420 , weight(21)|abundance(17)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(8) ,imodbits_armor,[], we_faction ],
["volencia_mail_and_plate", "Volencia Mail and Plate", [("light_mail_and_plate",0)], itp_type_body_armor|itp_covers_legs   ,0,
 2280 , weight(21)|abundance(28)|head_armor(0)|body_armor(45)|leg_armor(12)|difficulty(8) ,imodbits_armor ,[], we_faction],
["half_plate_armor", "Half Plate Armor", [("acb1_body",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 5170 , weight(25)|abundance(17)|head_armor(0)|body_armor(55)|leg_armor(10)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_4]],
["blue_plate_armor", "Plate Armor", [("gothic_armor_France",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 10120 , weight(28)|abundance(10)|head_armor(10)|body_armor(62)|leg_armor(18)|difficulty(10) ,imodbits_armor, [], [fac_kingdom_1]],
["blue_normal_surcoat_a", "Normal Surcoat", [("churburg_13",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3560 , weight(23)|abundance(21)|head_armor(0)|body_armor(50)|leg_armor(16)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_1]],
["armour_slashed_blue", "Armour Slashed Blue", [("bnw_armour_slashed_blue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3130 , weight(22)|abundance(23)|head_armor(0)|body_armor(48)|leg_armor(15)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_1]],
["corrazina_blue", "Corrazina Blue", [("corrazina_blue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3570 , weight(23)|abundance(21)|head_armor(0)|body_armor(50)|leg_armor(13)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_1]],
["gambeson_blue", "Gambeson Blue", [("gambeson_it-fran",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 340 , weight(8)|abundance(82)|head_armor(0)|body_armor(15)|leg_armor(15)|difficulty(0) ,imodbits_armor , [], [fac_kingdom_1]],
["breastplate_blue", "Breastplate Blue", [("breastplate_on_blue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 840 , weight(17)|abundance(58)|head_armor(0)|body_armor(35)|leg_armor(8)|difficulty(7) ,imodbits_armor , [], [fac_kingdom_1]],
["brigandine_blue", "Brigandine", [("brigandine_c",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 2560 , weight(21)|abundance(26)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(8) ,imodbits_armor , [], [fac_kingdom_1]],
["han_fu", "Han Fu", [("man_han_fu",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 240 , weight(8)|abundance(114)|head_armor(0)|body_armor(14)|leg_armor(4)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_7]],
["han_fu_b", "Han Fu", [("man_han_fu_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 240 , weight(8)|abundance(114)|head_armor(0)|body_armor(14)|leg_armor(4)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_7]],
["song_tunic_a", "Song Tunic A", [("song_tunic_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0,
 340 , weight(10)|abundance(95)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_7]],
["song_tunic_b", "Song Tunic B", [("song_tunic_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0,
 340 , weight(10)|abundance(95)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_7]],
["song_tunic_c", "Song Tunic C", [("bandit_tunic_b",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian,0,
 1100 , weight(17)|abundance(95)|head_armor(0)|body_armor(37)|leg_armor(10)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_7]],
["song_tunic_d", "Song Tunic D", [("bandit_tunic_a",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian,0,
 1100 , weight(17)|abundance(95)|head_armor(0)|body_armor(37)|leg_armor(10)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_7]],
["song_tunic_e", "Song Tunic E", [("bandit_tunic_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 1100 , weight(17)|abundance(95)|head_armor(0)|body_armor(37)|leg_armor(10)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_7]],
["song_tunic_f", "Song Tunic F", [("bandit_tunic_d",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 1100 , weight(17)|abundance(95)|head_armor(0)|body_armor(37)|leg_armor(10)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_7]],
["song_min_lamellar_a", "Song Min Lamellar A", [("song_min_lamellar_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 1230 , weight(18)|abundance(43)|head_armor(0)|body_armor(38)|leg_armor(11)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_7]],
["heraldic_armor_new", "Heraldic Armor New", [("heraldic_armor_new_KK",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 2000 , weight(19)|abundance(30)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(8) ,imodbits_armor , [], [fac_kingdom_7]],
["summer_leather_armor", "Leather Armor", [("mongol_leather_armor",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 4100 , weight(24)|abundance(19)|head_armor(0)|body_armor(52)|leg_armor(13)|difficulty(9) ,imodbits_armor , [], [fac_kingdom_7]],
["summer_leather_armor_two", "Leather Armor II", [("wuwushen1",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 4100 , weight(24)|abundance(19)|head_armor(0)|body_armor(52)|leg_armor(13)|difficulty(9) ,imodbits_armor , [], [fac_kingdom_7]],
["song_leather_armor", "Leather Armor", [("song_leather_armor",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 2350 , weight(21)|abundance(28)|head_armor(0)|body_armor(45)|leg_armor(12)|difficulty(8) ,imodbits_armor , [], [fac_kingdom_7]],
["song_armor_two", "Song Armor II", [("Song_armor_2",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 5550 , weight(25)|abundance(16)|head_armor(0)|body_armor(55)|leg_armor(16)|difficulty(9) ,imodbits_armor , [], [fac_kingdom_7]],
["song_leather_armor_b", "Leather Armor B", [("burenjia01",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 2280 , weight(21)|abundance(28)|head_armor(0)|body_armor(45)|leg_armor(12)|difficulty(8) ,imodbits_armor , [], [fac_kingdom_7]],
["song_general", "Song General", [("Songgeneral_a",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 7550 , weight(25)|abundance(11)|head_armor(0)|body_armor(55)|leg_armor(30)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_7]],

 ["god_leather_a", "god_leather_a", [("ttr_mega-yushman",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 5110 , weight(25)|abundance(17)|head_armor(0)|body_armor(55)|leg_armor(15)|difficulty(9) ,imodbits_armor , [], [fac_kingdom_22]],
 ["god_leather_b", "god_leather_b", [("ttr_seymen",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2350 , weight(21)|abundance(28)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(8) ,imodbits_armor, [], [fac_kingdom_14]],
["god_leather_c", "god_leather_c", [("yushman",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 5110 , weight(25)|abundance(17)|head_armor(0)|body_armor(55)|leg_armor(15)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_22]],

 ["khassakileather", "khassakileather", [("khassakileather",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 5270 , weight(25)|abundance(16)|head_armor(0)|body_armor(55)|leg_armor(15)|difficulty(9) ,imodbits_armor , [], [fac_kingdom_6]],
["khassakiscales", "khassakiscales", [("khassakiscales",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 5270 , weight(25)|abundance(16)|head_armor(0)|body_armor(55)|leg_armor(15)|difficulty(9) ,imodbits_armor , [], [fac_kingdom_6]],

  ["gunner_half_plate", "gunner_half_plate", [("moskow_reytar",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2420 , weight(21)|abundance(27)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(8) ,imodbits_armor , [], [fac_kingdom_2]],
["dragoon", "dragoon", [("poland_dragoon",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 930 , weight(17)|abundance(52)|head_armor(0)|body_armor(35)|leg_armor(10)|difficulty(7) ,imodbits_armor , [], [fac_kingdom_13]],

 ["kuyak_a", "Kuyak", [("kuyak_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1510 , weight(19)|abundance(37)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(8) ,imodbits_armor , [], [fac_kingdom_13]],
["kuyak_b", "Kuyak", [("kuyak_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1510 , weight(19)|abundance(37)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(8) ,imodbits_armor , [], [fac_kingdom_13]],
["litchina_helm", "litchina helm", [("litchina_helm",0), ("inv_litchina_helm",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 1510 , weight(3)|abundance(18)|head_armor(54)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate , [], [fac_kingdom_13]],
["rus_splint_greaves", "Splinted Greaves", [("rus_splint_greaves",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 1060 , weight(3)|abundance(38)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(7) ,imodbits_plate ],
["rus_lamellar_a", "snow_lamellar_a", [("rus_lamellar_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3010 , weight(22)|abundance(23)|head_armor(0)|body_armor(48)|leg_armor(13)|difficulty(8) ,imodbits_armor , [], [fac_kingdom_2]],
["rus_lamellar_b", "snow_lamellar_b", [("rus_lamellar_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3010 , weight(22)|abundance(23)|head_armor(0)|body_armor(48)|leg_armor(13)|difficulty(8) ,imodbits_armor , [], [fac_kingdom_2]],
["rus_scale", "vale_scale", [("rus_scale",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 5060 , weight(25)|abundance(17)|head_armor(0)|body_armor(55)|leg_armor(13)|difficulty(9) ,imodbits_armor , [], [fac_kingdom_2]],
["drz_kaftan", "drz_kaftan", [("drz_kaftan",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 930 , weight(17)|abundance(53)|head_armor(0)|body_armor(35)|leg_armor(13)|difficulty(7) ,imodbits_armor , [], [fac_kingdom_2]],
["drz_lamellar_armor", "drz_lamellar_armor", [("drz_lamellar_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 5270 , weight(25)|abundance(16)|head_armor(0)|body_armor(55)|leg_armor(15)|difficulty(9) ,imodbits_armor, [], [fac_kingdom_2]], 

  ["a_h1",  "highlander costume", [("a_h1",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 410 , weight(10)|abundance(78)|head_armor(0)|body_armor(20)|leg_armor(15)|difficulty(0) ,imodbits_armor, [], [fac_kingdom_8]],
 ["a_h1_1",  "highlander costume2", [("a_h1_1",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 410 , weight(10)|abundance(78)|head_armor(0)|body_armor(20)|leg_armor(15)|difficulty(0) ,imodbits_armor , [], [fac_kingdom_8]],
 ["a_h2",  "highlander armor", [("a_h2",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 1090 , weight(17)|abundance(45)|head_armor(0)|body_armor(35)|leg_armor(20)|difficulty(7) ,imodbits_armor , [], [fac_kingdom_8]],
 ["a_h2_1",  "highlander armor2", [("a_h2_1",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 1090 , weight(17)|abundance(45)|head_armor(0)|body_armor(35)|leg_armor(20)|difficulty(7) ,imodbits_armor , [], [fac_kingdom_8]],
 ["a_h3",  "elite highlander armor", [("a_h3",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 2890 , weight(21)|abundance(22)|head_armor(0)|body_armor(45)|leg_armor(25)|difficulty(8) ,imodbits_armor , [], [fac_kingdom_8]],
 ["a_h3_1",  "elite highlander armor2", [("a_h3_1",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 2890 , weight(21)|abundance(22)|head_armor(0)|body_armor(45)|leg_armor(25)|difficulty(8) ,imodbits_armor , [], [fac_kingdom_8]],
 ["a_h4",  "highlander merchant costume", [("a_h4",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 600 , weight(12)|abundance(62)|head_armor(0)|body_armor(25)|leg_armor(18)|difficulty(0) ,imodbits_armor , [], [fac_kingdom_8]],
 ["a_h4_1",  "highlander merchant costume2", [("a_h4_1",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 600 , weight(12)|abundance(62)|head_armor(0)|body_armor(25)|leg_armor(18)|difficulty(0) ,imodbits_armor , [], [fac_kingdom_8]],

  ["zuqinga", "zuqinga", [("zuqinga",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 450 , weight(14)|abundance(89)|head_armor(0)|body_armor(28)|leg_armor(4)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_11]],
 ["zuqingm", "zuqingm", [("zuqingm",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 460 , weight(13)|abundance(84)|head_armor(0)|body_armor(27)|leg_armor(4)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_11]],
 ["zuqingq", "zuqingq", [("zuqingq",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 460 , weight(13)|abundance(84)|head_armor(0)|body_armor(27)|leg_armor(4)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_11]],
["qianjing", "qianjing", [("qianjing",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1840 , weight(19)|abundance(32)|head_armor(0)|body_armor(42)|leg_armor(10)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_11]],
["jingyichibei", "jingyichibei", [("jingyichibei",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1840 , weight(19)|abundance(32)|head_armor(0)|body_armor(42)|leg_armor(10)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_11]],

 ["zhongjia_1", "zhongjia_france", [("zhongjia_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 9220 , weight(27)|abundance(11)|head_armor(10)|body_armor(60)|leg_armor(20)|difficulty(10) ,imodbits_cloth , [], [fac_kingdom_1]],
["zhongjia_2", "zhongjia_2", [("zhongjia_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 9220 , weight(27)|abundance(11)|head_armor(10)|body_armor(60)|leg_armor(20)|difficulty(10) ,imodbits_cloth , [], [fac_kingdom_1]],
["zhongjia_3", "zhongjia_england", [("zhongjia_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 9220 , weight(27)|abundance(11)|head_armor(10)|body_armor(60)|leg_armor(20)|difficulty(10) ,imodbits_cloth , [], [fac_kingdom_8]],
["zhongjia_4", "zhongjia_HR", [("zhongjia_4",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 9220 , weight(27)|abundance(11)|head_armor(10)|body_armor(60)|leg_armor(20)|difficulty(10) ,imodbits_cloth , [], [fac_kingdom_3]],
["zhongjia_5", "zhongjia_HR2", [("zhongjia_5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 9220 , weight(27)|abundance(11)|head_armor(10)|body_armor(60)|leg_armor(20)|difficulty(10) ,imodbits_cloth , [], [fac_kingdom_3]],

["jia1", "jia1", [("jia1",0)], itp_type_body_armor|itp_covers_legs   ,0, 4560 , weight(24)|abundance(17)|head_armor(0)|body_armor(52)|leg_armor(20)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_7] ],
["jia2", "jia2", [("jia2",0)], itp_type_body_armor|itp_covers_legs  ,0, 4560 , weight(24)|abundance(17)|head_armor(0)|body_armor(52)|leg_armor(20)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_7] ],
["jia3", "jia3", [("jia3",0)], itp_type_body_armor|itp_covers_legs   ,0, 4560 , weight(24)|abundance(17)|head_armor(0)|body_armor(52)|leg_armor(20)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_7] ],
["jia4", "jia4", [("jia4",0)], itp_type_body_armor|itp_covers_legs   ,0, 4560 , weight(24)|abundance(17)|head_armor(0)|body_armor(52)|leg_armor(20)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_7]],
["mingjia1", "mingjia1", [("mingjia1", 0),],itp_type_body_armor|itp_can_penetrate_shield|itp_merchandise, 0, 720, weight(14)|abundance(59)|body_armor(30)|leg_armor(13)|difficulty(0), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7]],
["mingjia4", "mingjia4", [("mingjia4", 0),],itp_type_body_armor|itp_can_penetrate_shield|itp_merchandise, 0, 7000, weight(25)|abundance(12)|body_armor(55)|leg_armor(33)|difficulty(9), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7]],
["mingjia5", "mingjia5", [("mingjia5", 0),],itp_type_body_armor|itp_can_penetrate_shield|itp_merchandise, 0, 7520, weight(25)|abundance(12)|body_armor(56)|leg_armor(33)|difficulty(9), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7]],
["mingjia7", "mingjia7", [("mingjia7", 0),],itp_type_body_armor|itp_can_penetrate_shield|itp_merchandise, 0, 4590, weight(23)|abundance(16)|body_armor(50)|leg_armor(33)|difficulty(9), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["mingjia8", "mingjia8", [("mingjia8", 0),],itp_type_body_armor|itp_can_penetrate_shield|itp_merchandise, 0, 5650, weight(24)|abundance(14)|body_armor(52)|leg_armor(33)|difficulty(9), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["mingjia10", "mingjia10", [("mingjia10", 0),],itp_type_body_armor|itp_can_penetrate_shield|itp_merchandise, 0, 5050, weight(23)|abundance(15)|body_armor(50)|leg_armor(33)|difficulty(9), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["mingjia11", "mingjia11", [("mingjia11", 0),],itp_type_body_armor|itp_can_penetrate_shield|itp_merchandise, 0, 4520, weight(22)|abundance(17)|body_armor(48)|leg_armor(33)|difficulty(8), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["mingjia12", "mingjia12", [("mingjia12", 0),],itp_type_body_armor|itp_can_penetrate_shield|itp_merchandise, 0, 4750, weight(22)|abundance(15)|body_armor(49)|leg_armor(33)|difficulty(8), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["mingkuei2", "mingkuei2", [("mingkuei2", 0),],itp_type_head_armor|itp_merchandise, 0, 600, weight(3)|abundance(36)|head_armor(45)|difficulty(0), imodbit_cracked|imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["mingjia6", "mingjia6", [("mingjia6", 0),],itp_type_body_armor|itp_can_penetrate_shield|itp_merchandise, 0, 5470, weight(24)|abundance(14)|body_armor(52)|leg_armor(33)|difficulty(9), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["mingjia2", "mingjia2", [("mingjia2", 0),],itp_type_body_armor|itp_can_penetrate_shield|itp_merchandise, 0, 4590, weight(23)|abundance(16)|body_armor(49)|leg_armor(33)|difficulty(8), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["mingjia3", "mingjia3", [("mingjia3", 0),],itp_type_body_armor|itp_can_penetrate_shield|itp_merchandise, 0, 4750, weight(23)|abundance(16)|body_armor(50)|leg_armor(33)|difficulty(9), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["jingyiwei1", "jingyiwei1", [("jingyiwei1", 0),],itp_type_body_armor|itp_can_penetrate_shield|itp_merchandise|itp_civilian, 0, 400, weight(10)|abundance(79)|body_armor(20)|leg_armor(10)|difficulty(0), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["mingjia_j", "mingjia_j", [("mingjia_j", 0),],itp_type_body_armor|itp_can_penetrate_shield|itp_merchandise, 0, 5820, weight(24)|abundance(14)|body_armor(52)|leg_armor(33)|difficulty(9), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["mianjia", "mianjia", [("mianjia", 0),],itp_type_body_armor|itp_can_penetrate_shield|itp_merchandise, 0, 4110, weight(22)|abundance(17)|body_armor(48)|leg_armor(33)|difficulty(8), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["jingyiwei", "jingyiwei", [("jingyiwei", 0),],itp_type_body_armor|itp_can_penetrate_shield|itp_merchandise|itp_civilian, 0, 430, weight(10)|abundance(74)|body_armor(20)|leg_armor(12)|difficulty(0), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],

 ["bnw_armour_eng", "bnw_armour_eng", [("bnw_armour_eng",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1600 , weight(19)|abundance(35)|head_armor(0)|body_armor(40)|leg_armor(15)|difficulty(7) ,imodbits_cloth, [], [fac_kingdom_8] ],
 ["bnw_armour_por", "bnw_armour_por", [("bnw_armour_por",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1600 , weight(19)|abundance(35)|head_armor(0)|body_armor(40)|leg_armor(15)|difficulty(7) ,imodbits_cloth, [], [fac_kingdom_16] ],
 ["bnw_armour_spa", "bnw_armour_spa", [("bnw_armour_spa",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1600 , weight(19)|abundance(35)|head_armor(0)|body_armor(40)|leg_armor(15)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_9] ],
 ["bnw_armour_hr", "bnw_armour_hr", [("bnw_armour_hr",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1600 , weight(19)|abundance(35)|head_armor(0)|body_armor(40)|leg_armor(15)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_3] ],
 ["bnw_armour_fra", "bnw_armour_fra", [("bnw_armour_fra",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1600 , weight(19)|abundance(35)|head_armor(0)|body_armor(40)|leg_armor(15)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_1] ],
 ["bnw_armour_kal", "bnw_armour_kal", [("bnw_armour_kal",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1600 , weight(19)|abundance(35)|head_armor(0)|body_armor(40)|leg_armor(15)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_5] ],
 ["bnw_armour_mil", "bnw_armour_mil", [("bnw_armour_mil",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1600 , weight(19)|abundance(35)|head_armor(0)|body_armor(40)|leg_armor(15)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_4] ],
 ["bnw_armour_sco", "bnw_armour_sco", [("bnw_armour_sco",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs  ,0, 1600 , weight(19)|abundance(35)|head_armor(0)|body_armor(40)|leg_armor(15)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_8] ],

 ["bnw_armour_stripes_fra", "bnw_armour_stripes_fra", [("bnw_armour_stripes_fra",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2660 , weight(21)|abundance(24)|head_armor(0)|body_armor(45)|leg_armor(20)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_1] ],
 ["bnw_armour_stripes_spain", "bnw_armour_stripes_spain", [("bnw_armour_stripes_spain",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2660 , weight(21)|abundance(24)|head_armor(0)|body_armor(45)|leg_armor(20)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_9] ],
["bnw_armour_stripes_eng", "bnw_armour_stripes_eng", [("bnw_armour_stripes_eng",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2660 , weight(21)|abundance(24)|head_armor(0)|body_armor(45)|leg_armor(20)|difficulty(8) ,imodbits_cloth, [], [fac_kingdom_1] ],
["bnw_armour_stripes_por", "bnw_armour_stripes_por", [("bnw_armour_stripes_por",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2660 , weight(21)|abundance(24)|head_armor(0)|body_armor(45)|leg_armor(20)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_16] ],
["bnw_armour_stripes_hr", "bnw_armour_stripes_hr", [("bnw_armour_stripes_hr",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2660 , weight(21)|abundance(24)|head_armor(0)|body_armor(45)|leg_armor(20)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_3] ],
["bnw_armour_stripes_kal", "bnw_armour_stripes_kal", [("bnw_armour_stripes_kal",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2660 , weight(21)|abundance(24)|head_armor(0)|body_armor(45)|leg_armor(20)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_5] ],

 ["kau_padded_mail_a", "kau_padded_mail_a", [("kau_padded_mail_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 420 , weight(12)|abundance(85)|head_armor(0)|body_armor(24)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_8] ],
 ["kau_rus_tunic_b", "kau_rus_tunic_b", [("kau_rus_tunic_b",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 290 , weight(8)|abundance(15)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_2] ],
 ["kau_rus_tunic_c", "kau_rus_tunic_c", [("kau_rus_tunic_c",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 290 , weight(8)|abundance(15)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_2] ],
 ["kau_rus_tunic_d", "kau_rus_tunic_d", [("kau_rus_tunic_d",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 290 , weight(8)|abundance(15)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_2] ],

 ["rus_coat", "rus_coat", [("rus_coat",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 1500 , weight(19)|abundance(38)|head_armor(0)|body_armor(40)|leg_armor(15)|difficulty(8) ,imodbits_cloth ],
 ["kau_mail_b", "kau_mail_b", [("kau_mail_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 1590 , weight(18)|abundance(34)|head_armor(0)|body_armor(39)|leg_armor(16)|difficulty(7) ,imodbits_cloth ],

 ["wei_xiadi_archers_vest01", "Arab_archers_vest01", [("wei_xiadi_archers_vest01",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 380 , weight(12)|abundance(94)|head_armor(0)|body_armor(24)|leg_armor(4)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_12] ],
["wei_xiadi_archers_vest02", "Arab_archers_vest02", [("wei_xiadi_archers_vest02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 380 , weight(12)|abundance(94)|head_armor(0)|body_armor(24)|leg_armor(4)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_12] ],
["wei_xiadi_archers_vest03", "Arab_archers_vest03", [("wei_xiadi_archers_vest03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 380 , weight(12)|abundance(94)|head_armor(0)|body_armor(24)|leg_armor(4)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_12] ],
["wei_xiadi_kher_kaftan", "kaftan", [("wei_xiadi_kher_kaftan",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 320 , weight(10)|abundance(99)|head_armor(0)|body_armor(20)|leg_armor(4)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_10] ],

["wei_xiadi_kher_lamellar_vest01", "lamellar_vest01", [("wei_xiadi_kher_lamellar_vest01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1210 , weight(18)|abundance(44)|head_armor(0)|body_armor(38)|leg_armor(10)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_10] ],
["wei_xiadi_kher_robe", "robe", [("wei_xiadi_kher_robe",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 360 , weight(10)|abundance(88)|head_armor(0)|body_armor(20)|leg_armor(4)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_10] ],
["wei_xiadi_rich_tunic02", "rich_tunic02", [("wei_xiadi_rich_tunic02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 290 , weight(9)|abundance(104)|head_armor(0)|body_armor(18)|leg_armor(4)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_10] ],
["wei_xiadi_samurai_armor01", "samurai_armor01", [("wei_xiadi_samurai_armor01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 3820 , weight(23)|abundance(20)|head_armor(0)|body_armor(50)|leg_armor(18)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_10] ],
["wei_xiadi_samurai_armor02", "samurai_armor02", [("wei_xiadi_samurai_armor02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 3750 , weight(23)|abundance(20)|head_armor(0)|body_armor(50)|leg_armor(17)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_10] ],
["wei_xiadi_sarranid_mamluk_armor", "mamluk_armor", [("wei_xiadi_sarranid_mamluk_armor",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 3560 , weight(23)|abundance(21)|head_armor(0)|body_armor(50)|leg_armor(16)|difficulty(9) ,imodbits_cloth , [], [] ],
["wei_xiadi_sar_leather_chain", "leather_chain", [("wei_xiadi_sar_leather_chain",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1250 , weight(18)|abundance(43)|head_armor(0)|body_armor(38)|leg_armor(10)|difficulty(8) ,imodbits_cloth ],

["breastplate_on_black", "breastplate_on_black", [("breastplate_on_black",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 550 , weight(14)|abundance(73)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_3] ],
["breastplate_on_blue", "breastplate_on_blue", [("breastplate_on_blue",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 550 , weight(14)|abundance(73)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_1] ],
 ["breastplate_on_empire", "breastplate_on_empire", [("breastplate_on_empire",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 550 , weight(14)|abundance(73)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_3] ],
 ["breastplate_on_green", "breastplate_on_green", [("breastplate_on_green",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 550 , weight(14)|abundance(73)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_4] ],
 ["breastplate_on_plain", "breastplate_on_plain", [("breastplate_on_plain",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 550 , weight(14)|abundance(73)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_16] ],
 ["breastplate_on_red", "breastplate_on_red", [("breastplate_on_red",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 550 , weight(14)|abundance(73)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_8] ],

  ["drz_kaftan2", "khasak_kaftan2", [("drz_kaftan2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 450 , weight(11)|abundance(75)|head_armor(0)|body_armor(22)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_21] ],
 ["fur_coat2", "fur_coat_khasak", [("fur_coat2",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 420 , weight(10)|abundance(77)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_21] ],

 ["plate_harness_01", "plate_harness_01", [("plate_harness_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 5748 , weight(23)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(10) ,imodbits_cloth ],
["plate_harness_02", "plate_harness_02", [("plate_harness_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 5848 , weight(23)|abundance(100)|head_armor(0)|body_armor(55)|leg_armor(25)|difficulty(10) ,imodbits_cloth ],
["plate_harness_05", "plate_harness_05", [("plate_harness_05",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 5848 , weight(23)|abundance(100)|head_armor(0)|body_armor(55)|leg_armor(25)|difficulty(10) ,imodbits_cloth ],
["platemail_harness_01", "platemail_harness_01", [("platemail_harness_01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 5848 , weight(23)|abundance(100)|head_armor(0)|body_armor(55)|leg_armor(25)|difficulty(10) ,imodbits_cloth ],
["platemail_harness_02", "platemail_harness_02", [("platemail_harness_02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 5848 , weight(23)|abundance(100)|head_armor(0)|body_armor(55)|leg_armor(25)|difficulty(10) ,imodbits_cloth ],

 ["Gothic_armor_Burgundian", "Gothic_armor_Spain", [("Gothic_armor_Burgundian",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 10050 , weight(27)|abundance(10)|head_armor(10)|body_armor(60)|leg_armor(30)|difficulty(10) ,imodbits_cloth , [], [fac_kingdom_9] ],
["Tur_milanese_armour_Blue", "Tur_milanese_armour_Blue", [("Tur_milanese_armour_Blue",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 5030 , weight(23)|abundance(16)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_1] ],
["Tur_milanese_armour_Green", "Tur_milanese_armour_Green", [("Tur_milanese_armour_Green",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 5030 , weight(23)|abundance(16)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_3] ],
["armour_2", "armour_2", [("armour_2",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 4820 , weight(24)|abundance(16)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_9] ],
["brigandineplate", "brigandineplate", [("brigandineplate",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 550 , weight(14)|abundance(73)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_8] ],
["flamand_plate", "flamand_plate", [("flamand_plate",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1970 , weight(19)|abundance(30)|head_armor(0)|body_armor(42)|leg_armor(15)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_1] ],

["gambeson_1", "gambeson_1", [("gambeson_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 290 , weight(7)|abundance(90)|head_armor(0)|body_armor(13)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_1] ],
["gambeson_2", "gambeson_2", [("gambeson_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 290 , weight(7)|abundance(90)|head_armor(0)|body_armor(13)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_1] ],
["gambeson_3", "gambeson_3", [("gambeson_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 290 , weight(7)|abundance(90)|head_armor(0)|body_armor(13)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_9] ],
["gambeson_4", "gambeson_4", [("gambeson_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 290 , weight(7)|abundance(90)|head_armor(0)|body_armor(13)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_5] ],
["gambeson_5", "gambeson_5", [("gambeson_5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 290 , weight(7)|abundance(90)|head_armor(0)|body_armor(13)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_4] ],
["gambeson_6", "gambeson_6", [("gambeson_6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 290 , weight(7)|abundance(90)|head_armor(0)|body_armor(13)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_3] ],
["gambeson_7", "gambeson_7", [("gambeson_7",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 290 , weight(7)|abundance(90)|head_armor(0)|body_armor(13)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_4] ],
["gambeson_it-fran", "gambeson_it-fran", [("gambeson_it-fran",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 2900 , weight(7)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_1] ],
["gambeson_italy", "gambeson_italy", [("gambeson_italy",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 290 , weight(7)|abundance(90)|head_armor(0)|body_armor(13)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_4] ],
["gambeson_italy-Red", "gambeson_italy-Red", [("gambeson_italy-Red",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 290 , weight(7)|abundance(90)|head_armor(0)|body_armor(13)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_4] ],
["gambeson_num", "gambeson_num", [("gambeson_num",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 290 , weight(7)|abundance(90)|head_armor(0)|body_armor(13)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_5] ],
["gothic_armor_France", "gothic_armor_France", [("gothic_armor_France",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 11120 , weight(27)|abundance(9)|head_armor(10)|body_armor(60)|leg_armor(30)|difficulty(10) ,imodbits_cloth , [], [fac_kingdom_1] ],
["gothic_armor_Holy_Rome", "gothic_armor_Holy_Rome", [("gothic_armor_Holy_Rome",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 12170 , weight(27)|abundance(8)|head_armor(10)|body_armor(60)|leg_armor(30)|difficulty(10) ,imodbits_cloth , [], [fac_kingdom_3] ],

["half_plate_4", "half_plate_4", [("half_plate_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2820 , weight(22)|abundance(24)|head_armor(0)|body_armor(47)|leg_armor(17)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_3] ],
["half_plate_5", "half_plate_5", [("half_plate_5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2820 , weight(22)|abundance(24)|head_armor(0)|body_armor(47)|leg_armor(17)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_4] ],
["half_plate_Ger", "half_plate_Ger", [("half_plate_Ger",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1610 , weight(19)|abundance(35)|head_armor(0)|body_armor(40)|leg_armor(17)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_3] ],
["half_plate_Green", "half_plate_Green", [("half_plate_Green",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1610 , weight(19)|abundance(35)|head_armor(0)|body_armor(40)|leg_armor(17)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_4] ],
["half_plate_Yello", "half_plate_Yello", [("half_plate_Yello",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1610 , weight(19)|abundance(35)|head_armor(0)|body_armor(40)|leg_armor(17)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_9] ],
["half_plate_blue", "half_plate_blue", [("half_plate_blue",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1610 , weight(19)|abundance(35)|head_armor(0)|body_armor(40)|leg_armor(17)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_1] ],
["half_plate_meshco", "half_plate_meshco", [("half_plate_meshco",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1610 , weight(19)|abundance(35)|head_armor(0)|body_armor(40)|leg_armor(17)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_8] ],
["half_plate_red", "half_plate_red", [("half_plate_red",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 1610 , weight(19)|abundance(35)|head_armor(0)|body_armor(40)|leg_armor(17)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_8] ],

["milanese_Eng", "milanese_Eng", [("milanese_Eng",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 6180 , weight(25)|abundance(14)|head_armor(0)|body_armor(55)|leg_armor(20)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_8] ],
["milanese_armour_4", "milanese_armour_4", [("milanese_armour_4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2910 , weight(22)|abundance(24)|head_armor(0)|body_armor(47)|leg_armor(17)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_3] ],
["milanese_armour_6", "milanese_armour_6", [("milanese_armour_6",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2910 , weight(22)|abundance(24)|head_armor(0)|body_armor(47)|leg_armor(17)|difficulty(8) ,imodbits_cloth, [], [fac_kingdom_3] ],
["milanese_armour_7", "milanese_armour_7", [("milanese_armour_7",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2910 , weight(22)|abundance(24)|head_armor(0)|body_armor(47)|leg_armor(17)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_8] ],

["milanese_armour_Fr3", "milanese_armour_Fr3", [("milanese_armour_Fr3",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 4820 , weight(24)|abundance(16)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_1] ],
["milanese_armour_GER", "milanese_armour_GER", [("milanese_armour_GER",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 4820 , weight(24)|abundance(16)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_3] ],
["milanese_armour_GREEN", "milanese_armour_GREEN", [("milanese_armour_GREEN",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 4820 , weight(24)|abundance(16)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_4] ],
["milanese_armour_fr4", "milanese_armour_fr4", [("milanese_armour_fr4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 4820 , weight(24)|abundance(16)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_1] ],

["milanese_plate", "milanese_plate", [("milanese_plate",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 6180 , weight(25)|abundance(14)|head_armor(0)|body_armor(55)|leg_armor(20)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_4] ],
["qsj", "qsj_plate", [("qsj",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 6830 , weight(25)|abundance(13)|head_armor(10)|body_armor(55)|leg_armor(20)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_9] ],

["recruit_gambeson_bezh", "recruit_gambeson_bezh", [("recruit_gambeson_bezh",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 540 , weight(11)|abundance(65)|head_armor(0)|body_armor(23)|leg_armor(17)|difficulty(0) ,imodbits_cloth ],
["lamellar_armor_black", "lamellar_armor_black", [("lamellar_armor_black",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 4820 , weight(24)|abundance(16)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(9) ,imodbits_cloth ],
["landsknecht_a", "landsknecht_a", [("landsknecht_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 360 , weight(9)|abundance(84)|head_armor(0)|body_armor(18)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], we_faction ],
["landsknecht_b", "landsknecht_b", [("landsknecht_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 360 , weight(9)|abundance(84)|head_armor(0)|body_armor(18)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], we_faction],

["black_gambeson_a", "black_gambeson_a", [("black_gambeson_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 210 , weight(6)|abundance(112)|head_armor(0)|body_armor(10)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_3] ],
["blue_gambeson_a", "blue_gambeson_a", [("blue_gambeson_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 210 , weight(6)|abundance(112)|head_armor(0)|body_armor(10)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_1] ],
["empire_gambeson_a", "empire_gambeson_a", [("empire_gambeson_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 210 , weight(6)|abundance(112)|head_armor(0)|body_armor(10)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_9] ],
["green_gambeson_a", "green_gambeson_a", [("green_gambeson_a",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 210 , weight(6)|abundance(112)|head_armor(0)|body_armor(10)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_4] ],
["white_gambeson_a", "white_gambeson_a", [("white_gambeson_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 210 , weight(6)|abundance(112)|head_armor(0)|body_armor(10)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_16] ],

["brig_plate_black", "brig_plate_black", [("brig_plate_black",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 3440 , weight(22)|abundance(21)|head_armor(0)|body_armor(48)|leg_armor(20)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_3] ],
["brig_plate_blue", "brig_plate_blue", [("brig_plate_blue",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 3440 , weight(22)|abundance(21)|head_armor(0)|body_armor(48)|leg_armor(20)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_1] ],
["brig_plate_green", "brig_plate_green", [("brig_plate_green",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 3440 , weight(22)|abundance(21)|head_armor(0)|body_armor(48)|leg_armor(20)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_4] ],
["brig_plate_heraldic", "brig_plate_heraldic", [("brig_plate_black",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 3440 , weight(22)|abundance(21)|head_armor(0)|body_armor(48)|leg_armor(20)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_3] ],
["brig_plate_red", "brig_plate_red", [("brig_plate_red",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 3440 , weight(22)|abundance(21)|head_armor(0)|body_armor(48)|leg_armor(20)|difficulty(8) ,imodbits_cloth, [], [fac_kingdom_8] ],
["brigandine_empire", "brigandine_empire", [("brigandine_empire",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 3440 , weight(22)|abundance(21)|head_armor(0)|body_armor(48)|leg_armor(20)|difficulty(8) ,imodbits_cloth, [], [fac_kingdom_3] ],

["cuirass_on_black", "cuirass_on_black", [("cuirass_on_black",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 490 , weight(11)|abundance(71)|head_armor(0)|body_armor(23)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_3] ],
["cuirass_on_blue", "cuirass_on_blue", [("cuirass_on_blue",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 490 , weight(11)|abundance(71)|head_armor(0)|body_armor(23)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_1] ],
["cuirass_on_empire", "cuirass_on_empire", [("cuirass_on_empire",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 490 , weight(11)|abundance(71)|head_armor(0)|body_armor(23)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_9] ],
["cuirass_on_green", "cuirass_on_green", [("cuirass_on_green",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 490 , weight(11)|abundance(71)|head_armor(0)|body_armor(23)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_4] ],
["cuirass_on_red", "cuirass_on_red", [("cuirass_on_red",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 490 , weight(11)|abundance(71)|head_armor(0)|body_armor(23)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_8] ],
["cuirass_on_white", "cuirass_on_white", [("cuirass_on_white",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 490 , weight(11)|abundance(71)|head_armor(0)|body_armor(23)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_16] ],

["plate_harness_blue", "plate_harness_blue", [("plate_harness_blue",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 4980 , weight(24)|abundance(16)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_1] ],
["plate_harness_green", "plate_harness_green", [("plate_harness_green",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 4980 , weight(24)|abundance(16)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_4] ],
["plate_harness_red", "plate_harness_red", [("plate_harness_red",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 4980 , weight(24)|abundance(16)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_8] ],
["plate_harness_yellow", "plate_harness_yellow", [("plate_harness_yellow",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 4980 , weight(24)|abundance(16)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_9] ],
["platemail_harness_05", "platemail_harness_05", [("platemail_harness_05",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 4980 , weight(24)|abundance(16)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_4] ],

["Pol_svitka_pure_d", "Pol_svitka_pure_d", [("Pol_svitka_pure_d",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 230 , weight(6)|abundance(105)|head_armor(0)|body_armor(10)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_13] ],
["Pol_svitka_pure_b", "Pol_svitka_pure_b", [("Pol_svitka_pure_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 230 , weight(6)|abundance(105)|head_armor(0)|body_armor(10)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_13] ],
["Pol_svitka_pure_c", "Pol_svitka_pure_c", [("Pol_svitka_pure_c",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 230 , weight(6)|abundance(105)|head_armor(0)|body_armor(10)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_13] ],

["Pol_svitka_rich_a", "Pol_svitka_rich_a", [("Pol_svitka_rich_a",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 320 , weight(8)|abundance(86)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_13] ],
["Pol_svitka_rich_b", "Pol_svitka_rich_b", [("Pol_svitka_rich_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 320 , weight(8)|abundance(86)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_13] ],
["Pol_svitka_rich_d", "Pol_svitka_rich_d", [("Pol_svitka_rich_d",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 320 , weight(8)|abundance(86)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_13] ],
["Pol_svitka_rich_e", "Pol_svitka_rich_e", [("Pol_svitka_rich_e",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 320 , weight(8)|abundance(86)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_13] ],

["pol_husar_yaguar", "pol_husar_yaguar", [("pol_husar_yaguar",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 6360 , weight(25)|abundance(14)|head_armor(0)|body_armor(55)|leg_armor(20)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_13] ],
["pol_koja_usilenaya", "pol_koja_usilenaya", [("pol_koja_usilenaya",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 2560 , weight(21)|abundance(26)|head_armor(0)|body_armor(46)|leg_armor(20)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_13] ],
["pol_krilatiy_gusar", "pol_krilatiy_gusar", [("pol_krilatiy_gusar",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 4090 , weight(23)|abundance(18)|head_armor(0)|body_armor(50)|leg_armor(20)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_13] ],
["pol_krilatiy_gusar_b", "pol_krilatiy_gusar_b", [("pol_krilatiy_gusar_b",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 4090 , weight(23)|abundance(18)|head_armor(0)|body_armor(50)|leg_armor(20)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_13] ],

["poland_musket_shinel", "poland_musket_shinel", [("poland_musket_shinel",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 540 , weight(12)|abundance(69)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_13] ],
["poland_shinel", "poland_shinel", [("poland_shinel",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 540 , weight(12)|abundance(69)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_13] ],

["polish_panzernik", "polish_panzernik", [("polish_panzernik",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2890 , weight(21)|abundance(23)|head_armor(0)|body_armor(46)|leg_armor(20)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_13] ],

["reestr_kozak", "reestr_kozak", [("reestr_kozak",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 540 , weight(12)|abundance(69)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_13] ],

["boyar_puzo", "boyar_puzo", [("boyar_puzo",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 3440 , weight(22)|abundance(21)|head_armor(0)|body_armor(48)|leg_armor(20)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_2] ],

["german_line_musketeer", "german_line_musketeer", [("german_line_musketeer",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 540 , weight(12)|abundance(69)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_3] ],
["german_line_pikiner", "german_line_pikiner", [("german_line_pikiner",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1870 , weight(20)|abundance(32)|head_armor(0)|body_armor(42)|leg_armor(17)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_3] ],

["janichar1", "janichar1", [("janichar1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 1330 , weight(18)|abundance(40)|head_armor(0)|body_armor(38)|leg_armor(15)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_6] ],
["janichar2", "janichar2", [("janichar2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 1330 , weight(18)|abundance(40)|head_armor(0)|body_armor(38)|leg_armor(15)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_6] ],

["kalmyk_tors", "kalmyk_tors", [("kalmyk_tors",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 3390 , weight(22)|abundance(21)|head_armor(0)|body_armor(48)|leg_armor(21)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_10] ],

["merc_musketeer_a", "merc_musketeer_a", [("merc_musketeer_a",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 540 , weight(12)|abundance(69)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_5] ],
["merc_musketeer_b", "merc_musketeer_red", [("merc_musketeer_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 540 , weight(12)|abundance(69)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_5] ],
["merc_pikeman_a", "merc_pikeman_a", [("merc_pikeman_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2180 , weight(19)|abundance(27)|head_armor(0)|body_armor(42)|leg_armor(17)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_8] ],
["merc_pikeman_b", "merc_pikeman_b", [("merc_pikeman_b",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 2180 , weight(19)|abundance(27)|head_armor(0)|body_armor(42)|leg_armor(17)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_3] ],

["mosk_bahter_simple", "mosk_bahter_simple", [("mosk_bahter_simple",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 3330 , weight(22)|abundance(21)|head_armor(0)|body_armor(48)|leg_armor(20)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_2] ],
["mosk_civil1", "mosk_civil1", [("mosk_civil1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 310 , weight(8)|abundance(89)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_2] ],
["mosk_civil2", "mosk_civil2", [("mosk_civil2",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 310 , weight(8)|abundance(89)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_2] ],
["mosk_kuyak", "mosk_kuyak", [("mosk_kuyak",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 3960 , weight(23)|abundance(19)|head_armor(0)|body_armor(50)|leg_armor(20)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_2] ],
["mosk_streletz", "mosk_streletz", [("mosk_streletz",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 540 , weight(12)|abundance(69)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_2] ],
["mosk_streletz_pure", "mosk_streletz_pure", [("mosk_streletz_pure",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 540 , weight(12)|abundance(69)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_2] ],
["mosk_streletz_pure_spear", "mosk_streletz_pure_spear", [("mosk_streletz_pure_spear",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 540 , weight(12)|abundance(69)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_2] ],
["mosk_streletz_spear", "mosk_streletz_spear", [("mosk_streletz_spear",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 540 , weight(12)|abundance(69)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_2] ],
 ["mosk_tzar", "mosk_tzar", [("mosk_tzar",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 540 , weight(12)|abundance(69)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_2] ],
["mosk_zertzalo", "mosk_zertzalo", [("mosk_zertzalo",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 3840 , weight(23)|abundance(19)|head_armor(0)|body_armor(50)|leg_armor(20)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_12] ],
["moskow_bahter", "moskow_bahter", [("moskow_bahter",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2980 , weight(22)|abundance(23)|head_armor(0)|body_armor(47)|leg_armor(20)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_12] ],

["reytar_puzo", "reytar_puzo", [("pol_husar_yaguar",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 6360 , weight(25)|abundance(14)|head_armor(0)|body_armor(55)|leg_armor(20)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_13] ],
["rinda", "rinda", [("rinda",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 458 , weight(12.25)|abundance(124)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_2] ],

 
["simple_halat3", "simple_halat3", [("simple_halat3",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 420 , weight(11)|abundance(80)|head_armor(0)|body_armor(22)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_22] ],

["swd_blck_reytar", "swd_blck_reytar", [("swd_blck_reytar",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 5820 , weight(25)|abundance(15)|head_armor(0)|body_armor(55)|leg_armor(20)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_5] ],
["swd_reytar_simple", "swd_reytar_simple", [("swd_reytar_simple",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2120 , weight(19)|abundance(28)|head_armor(0)|body_armor(42)|leg_armor(17)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_3] ],

["swed_civil_1", "swed_civil_blue", [("swed_civil_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 290 , weight(8)|abundance(95)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_5] ],
["swed_civil_2", "swed_civil_black", [("swed_civil_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 290 , weight(8)|abundance(95)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_5] ],
["swed_dragoon", "swed_dragoonred", [("swed_dragoon",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 500 , weight(12)|abundance(73)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_5] ],
["swed_kirasa", "swed_kirasadarkred", [("swed_kirasa",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1000 , weight(17)|abundance(49)|head_armor(0)|body_armor(35)|leg_armor(15)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_5] ],
["swed_kirasa_b", "swed_kirasablue", [("swed_kirasa_b",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 1000 , weight(17)|abundance(49)|head_armor(0)|body_armor(35)|leg_armor(15)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_1] ],
["swed_kirasa_c", "swed_kirasared", [("swed_kirasa_c",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1000 , weight(17)|abundance(49)|head_armor(0)|body_armor(35)|leg_armor(15)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_8] ],
["swed_kirasa_major", "swed_kirasayellow", [("swed_kirasa_major",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1000 , weight(17)|abundance(49)|head_armor(0)|body_armor(35)|leg_armor(15)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_9] ],
["swed_leibguard", "swed_leibguard", [("swed_leibguard",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 520 , weight(12)|abundance(71)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_5] ],
["swed_musketeer", "swed_musketeerblue", [("swed_musketeer",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 520 , weight(12)|abundance(71)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_5] ],
["swed_pikeman", "swed_pikeman", [("swed_pikeman",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2050 , weight(19)|abundance(29)|head_armor(0)|body_armor(42)|leg_armor(17)|difficulty(8) ,imodbits_cloth, [], [fac_kingdom_1] ],
["swed_selyanin_b", "swed_selyanin_black", [("swed_selyanin_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 290 , weight(8)|abundance(95)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_5] ],

["swed_swordmaster", "swed_swordmaster", [("swed_swordmaster",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 5820 , weight(25)|abundance(15)|head_armor(0)|body_armor(55)|leg_armor(20)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_8] ],

["ttr_bahter_a", "ttr_bahter_a", [("ttr_bahter_a",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 3390 , weight(22)|abundance(21)|head_armor(0)|body_armor(48)|leg_armor(21)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_22] ],

["ttr_civil_1", "ttr_civil_1", [("ttr_civil_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 300 , weight(8)|abundance(92)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_6] ],
["ttr_civil_2", "ttr_civil_2", [("ttr_civil_2",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 300 , weight(8)|abundance(92)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_6] ],
["ttr_halat1", "ttr_halat1", [("ttr_halat1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 300 , weight(8)|abundance(92)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_22] ],
["ttr_halat2", "ttr_halat2", [("ttr_halat2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 300 , weight(8)|abundance(92)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_6] ],

["ttr_stega_halat1", "ttr_stega_halat1", [("ttr_stega_halat1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 540 , weight(12)|abundance(69)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_6] ],
["ttr_stega_halat2", "ttr_stega_halat2", [("ttr_stega_halat2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 540 , weight(12)|abundance(69)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_22] ],

["turk_azap", "turk_azap", [("turk_azap",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 540 , weight(12)|abundance(69)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_6] ],

 ["ukr_civil_jupan_1", "ukr_civil_jupan_1", [("ukr_civil_jupan_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 540 , weight(12)|abundance(69)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_13] ],
["ukr_jupan_siniy", "ukr_jupan_siniy", [("ukr_jupan_siniy",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 540 , weight(12)|abundance(69)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_13] ],
["ukr_jupan_usilenuy", "ukr_jupan_usilenuy", [("ukr_jupan_usilenuy",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 930 , weight(17)|abundance(52)|head_armor(0)|body_armor(35)|leg_armor(15)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_13] ],
["ukr_koj_kurtka", "ukr_koj_kurtka", [("ukr_koj_kurtka",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 930 , weight(17)|abundance(52)|head_armor(0)|body_armor(35)|leg_armor(15)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_13] ],

["ukr_pure_jupan_1", "ukr_pure_jupan_1", [("ukr_pure_jupan_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 520 , weight(12)|abundance(71)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_6] ],
["ukr_pure_jupan_2", "ukr_pure_jupan_2", [("ukr_pure_jupan_2",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 520 , weight(12)|abundance(71)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_6] ],
["ukr_pure_jupan_3", "ukr_pure_jupan_3", [("ukr_pure_jupan_3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 520 , weight(12)|abundance(71)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_13] ],

 ["bakak", "bakak", [("bakak",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 520 , weight(12)|abundance(71)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_6] ],
["goldsipahi", "goldsipahi", [("goldsipahi",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 3330 , weight(22)|abundance(21)|head_armor(0)|body_armor(48)|leg_armor(20)|difficulty(8) ,imodbits_cloth, [], [fac_kingdom_6] ],
["janichareteksiz", "janichareteksiz", [("janichareteksiz",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs |itp_civilian  ,0, 1290 , weight(18)|abundance(41)|head_armor(0)|body_armor(38)|leg_armor(15)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_6] ],
["janichareteksiz_mail", "janichareteksiz_mail", [("janichareteksiz_mail",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs |itp_civilian  ,0, 2360 , weight(21)|abundance(27)|head_armor(0)|body_armor(45)|leg_armor(17)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_6] ],
["ola", "ola", [("ola",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 3330 , weight(22)|abundance(21)|head_armor(0)|body_armor(48)|leg_armor(20)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_22] ],
["tasarim", "tasarim", [("tasarim",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 3330 , weight(22)|abundance(21)|head_armor(0)|body_armor(48)|leg_armor(20)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_12] ],
["ttr_kolcha", "ttr_kolcha", [("ttr_kolcha",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 3330 , weight(22)|abundance(21)|head_armor(0)|body_armor(48)|leg_armor(20)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_22] ],

##HolyAce
["qingjia_xianghuang", "qingjia_xianghuang", [("qingjia_xianghuang", 0)], itp_type_body_armor|itp_covers_legs, 
0, 2390, weight(21)|abundance(27)|difficulty(9)|head_armor(0)|body_armor(53)|leg_armor(31), imodbits_cloth, [] ],

["qingjia_xiangbe", "qingjia_xiangbe", [("qingjia_xiangbe", 0)], itp_type_body_armor|itp_covers_legs, 0, 2390, 
weight(21)|abundance(27)|difficulty(8)|head_armor(0)|body_armor(45)|leg_armor(23), imodbits_cloth, [] ],

["qingjia_xianghong", "qingjia_xianghong", [("qingjia_xianghong", 0)], itp_type_body_armor|itp_covers_legs, 0, 
2390, weight(21)|abundance(27)|difficulty(8)|head_armor(0)|body_armor(45)|leg_armor(23), imodbits_cloth, [] ],

["qingjia_xianglan", "qingjia_xianglan", [("qingjia_xianglan", 0)], itp_type_body_armor|itp_covers_legs, 0, 
2390, weight(21)|abundance(27)|difficulty(8)|head_armor(0)|body_armor(45)|leg_armor(23), imodbits_cloth, [] ],

["qingjia_zenhuang", "qingjia_zenhuang", [("qingjia_zenhuang", 0)], itp_type_body_armor|itp_covers_legs, 0, 
2390, weight(23)|abundance(27)|difficulty(9)|head_armor(0)|body_armor(53)|leg_armor(33), imodbits_cloth, [] ],

["qingjia_zenbe", "qingjia_zenbe", [("qingjia_zenbe", 0)], itp_type_body_armor|itp_covers_legs, 0, 2390, 
weight(23)|abundance(27)|difficulty(9)|head_armor(0)|body_armor(53)|leg_armor(31), imodbits_cloth, [] ],

["qingjia_zenhong", "qingjia_zenhong", [("qingjia_zenhong", 0)], itp_type_body_armor|itp_covers_legs, 0, 2390, 
weight(23)|abundance(27)|difficulty(9)|head_armor(0)|body_armor(53)|leg_armor(31), imodbits_cloth, [] ],

["qingjia_zenlan", "qingjia_zenlan", [("qingjia_zenlan", 0)], itp_type_body_armor|itp_covers_legs, 0, 2390, 
weight(23)|abundance(27)|difficulty(9)|head_armor(0)|body_armor(53)|leg_armor(31), imodbits_cloth, [] ],

["qingjia_jiangjun", "qingjia_jiangjun", [("qingjia_jiangjun", 0)], itp_type_body_armor|itp_covers_legs, 0, 
2390, weight(25)|abundance(27)|difficulty(10)|head_armor(0)|body_armor(55)|leg_armor(33), imodbits_cloth, [] ],

["qingjia_jiangjun_tuanlong", "qingjia_jiangjun_tuanlong", [("qingjia_jiangjun_tuanlong", 0)], itp_type_body_armor|itp_covers_legs, 0, 
2390, weight(25)|abundance(27)|difficulty(12)|head_armor(0)|body_armor(58)|leg_armor(36), imodbits_cloth, [] ],

["qingjia1", "qingjia1", [("qingjia1", 0)], itp_type_body_armor|itp_covers_legs, 0, 14350, weight(23)|
abundance(5)|difficulty(10)|head_armor(0)|body_armor(60)|leg_armor(38), imodbits_cloth, [] ],
["qingjia2", "qingjia2", [("yamenyi4", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian, 0, 420, 
weight(10)|abundance(76)|head_armor(0)|body_armor(30)|leg_armor(16), imodbits_cloth, [] ],
["qingjia4", "qingjia4", [("yamenyi3", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian, 0, 420, 
weight(10)|abundance(76)|head_armor(0)|body_armor(30)|leg_armor(16), imodbits_cloth, [] ],
["qingjia5", "qingjia5", [("yamenyi1", 0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian, 0, 420, 
weight(10)|abundance(76)|head_armor(0)|body_armor(20)|leg_armor(16), imodbits_cloth, [] ],
["qingjia_minyong", "qingjia_minyong", [("qingjia_minyong", 0)], itp_type_body_armor|itp_merchandise|itp_merchandise|itp_covers_legs|itp_civilian, 0, 220, 
weight(10)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(16), imodbits_cloth, [] ],
["mingjiaa", "mingjiaa", [("mingjiaa",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 6870 , weight(25)|abundance(13)|head_armor(0)|body_armor(55)|leg_armor(26)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_7] ],
##HolAce End
  ["half_plate_fra", "half_plate_fra", [("half_plate_fra",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2520 , weight(21)|abundance(26)|head_armor(0)|body_armor(45)|leg_armor(17)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_1] ],
 ["half_plate_por", "half_plate_por", [("half_plate_por",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2520 , weight(21)|abundance(26)|head_armor(0)|body_armor(45)|leg_armor(17)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_16] ],
["half_plate_eng", "half_plate_eng", [("half_plate_eng",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2520 , weight(21)|abundance(26)|head_armor(0)|body_armor(45)|leg_armor(17)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_8] ],
["half_plate_spa", "half_plate_spa", [("half_plate_spa",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2520 , weight(21)|abundance(26)|head_armor(0)|body_armor(45)|leg_armor(17)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_5] ],
["half_plate_kal", "half_plate_kal", [("half_plate_kal",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2520 , weight(21)|abundance(26)|head_armor(0)|body_armor(45)|leg_armor(17)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_3] ],

["gambeson_it-fran", "gambeson_it-fran", [("gambeson_it-fran",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 330 , weight(8)|abundance(85)|head_armor(0)|body_armor(15)|leg_armor(15)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_1] ],
["gambeson_it-por", "gambeson_it-por", [("gambeson_it-por",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 330 , weight(8)|abundance(85)|head_armor(0)|body_armor(15)|leg_armor(15)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_16] ],
["gambeson_it-eng", "gambeson_it-eng", [("gambeson_it-eng",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 330 , weight(8)|abundance(85)|head_armor(0)|body_armor(15)|leg_armor(15)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_8] ],
["gambeson_it-spa", "gambeson_it-spa", [("gambeson_it-spa",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 330 , weight(8)|abundance(85)|head_armor(0)|body_armor(15)|leg_armor(15)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_9] ],
["gambeson_it-kal", "gambeson_it-kal", [("gambeson_it-kal",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 330 , weight(8)|abundance(85)|head_armor(0)|body_armor(15)|leg_armor(15)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_5] ],
["gambeson_it-hr", "gambeson_it-hr", [("gambeson_it-hr",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 330 , weight(8)|abundance(85)|head_armor(0)|body_armor(15)|leg_armor(15)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_3] ],

 ["woman_han_fu", "woman_han_fu", [("woman_han_fu",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 300 , weight(8)|abundance(82)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_7] ],
["korea_tunic", "korea_tunic", [("korea_tunic",0)], itp_type_body_armor|itp_covers_legs   ,0, 300 , weight(8)|abundance(82)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_19] ],
["korea_a", "korea_a", [("korea_a",0)], itp_type_body_armor|itp_covers_legs   ,0, 500 , weight(12)|abundance(74)|head_armor(0)|body_armor(25)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_19] ],

["korea1", "korea1", [("korea1",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 2270 , weight(21)|abundance(29)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_19] ],
["korea2", "korea2", [("korea2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 2270 , weight(21)|abundance(29)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_19] ],
["korea3", "korea3", [("korea3",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 2270 , weight(21)|abundance(29)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(8) ,imodbits_cloth, [], [fac_kingdom_19] ],
["korea4", "korea4", [("copy_korea3",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 2270 , weight(21)|abundance(29)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(8) ,imodbits_cloth, [], [fac_kingdom_19] ],

["greatcoat_black", "greatcoat_black", [("huntmodgreatcoat_black_new",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 770 , weight(14)|abundance(55)|head_armor(0)|body_armor(30)|leg_armor(15)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_9] ],
["greatcoat_black1", "greatcoat_black1", [("huntmodgreatcoat_new",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 770 , weight(14)|abundance(55)|head_armor(0)|body_armor(30)|leg_armor(15)|difficulty(7) ,imodbits_cloth, [], [fac_kingdom_8] ],

#["colonial_red_dress", "colonial_red_dress", [("colonial_red_dress",0)], itp_type_body_armor|itp_covers_legs   ,0, 190 , weight(6)|abundance(125)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_8] ],
#["colonial_purple_dress", "colonial_purple_dress", [("colonial_purple_dress",0)], itp_type_body_armor|itp_covers_legs   ,0, 190 , weight(6)|abundance(125)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_1] ],

["indianbody2", "indianbody2", [("indianbody2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 580 , weight(12)|abundance(63)|head_armor(5)|body_armor(25)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_15] ],
["furindianbody", "furindianbody", [("furindianbody",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 580 , weight(12)|abundance(63)|head_armor(5)|body_armor(25)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_15] ],
["ancest_chief_outfit", "ancest_chief_outfit", [("ancest_chief_outfit",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 690 , weight(14)|abundance(61)|head_armor(5)|body_armor(30)|leg_armor(7)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_15] ],
["warrior_outfit", "warrior_outfit", [("warrior_outfit",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 540 , weight(12)|abundance(68)|head_armor(5)|body_armor(25)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_15] ],

["body_tribe", "body_tribe", [("body_tribe",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 290 , weight(8)|abundance(94)|head_armor(5)|body_armor(15)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_15] ],

["armor_adilshahi_chihali", "armor_adilshahi_chihali", [("armor_adilshahi_chihali",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 850 , weight(17)|abundance(58)|head_armor(0)|body_armor(35)|leg_armor(7)|difficulty(8) ,imodbits_cloth, [], [fac_kingdom_17] ],
["armor_adilshahi_chihalii", "armor_adilshahi_chihalii", [("armor_adilshahi_chihalii",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 850 , weight(17)|abundance(58)|head_armor(0)|body_armor(35)|leg_armor(7)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_17] ],
["armor_afghan_mailiii", "armor_afghan_mailiii", [("armor_afghan_mailiii",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 850 , weight(17)|abundance(58)|head_armor(0)|body_armor(35)|leg_armor(10)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_17] ],
["armor_vijaynagri_maili", "armor_vijaynagri_maili", [("armor_vijaynagri_maili",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2120 , weight(21)|abundance(31)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_17] ],
["armor_vijaynagri_mailii", "armor_vijaynagri_mailii", [("armor_vijaynagri_mailii",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 2120 , weight(21)|abundance(31)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_17] ],
["armor_vijaynagri_mailiii", "armor_vijaynagri_mailiii", [("armor_vijaynagri_mailiii",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 2120 , weight(21)|abundance(31)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_17] ],
["armor_vijaynagri_scaleiv", "armor_vijaynagri_scaleiv", [("armor_vijaynagri_scaleiv",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 360 , weight(10)|abundance(88)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_17] ],
["armor_vijaynagri_tunici", "armor_vijaynagri_tunici", [("armor_vijaynagri_tunici",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 250 , weight(7)|abundance(103)|head_armor(0)|body_armor(13)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_17] ],
["armor_vijaynagri_tunicii", "armor_vijaynagri_tunicii", [("armor_vijaynagri_tunicii",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 300 , weight(8)|abundance(92)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_17] ],
["armor_vijaynagri_tuniciii", "armor_vijaynagri_tuniciii", [("armor_vijaynagri_tuniciii",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 250 , weight(8)|abundance(109)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_17] ],

["armor_afghan_mailiv", "armor_khasak_mailiv", [("armor_afghan_mailiv",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2350 , weight(218)|abundance(28)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(8) ,imodbits_cloth, [], [fac_kingdom_21] ],
["kazakh_torso", "kazakh_torso", [("kazakh_torso",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 520 , weight(12)|abundance(71)|head_armor(0)|body_armor(25)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_21] ],

["basketry_armour_blue", "basketry_armour_blue", [("basketry_armour_blue",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 1270 , weight(19)|abundance(44)|head_armor(0)|body_armor(40)|leg_armor(10)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_18] ],
["basketry_armour", "basketry_armour", [("basketry_armour",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 1270 , weight(19)|abundance(44)|head_armor(0)|body_armor(40)|leg_armor(10)|difficulty(8) ,imodbits_cloth, [], [fac_kingdom_18] ],
["rattan_plate_green", "rattan_plate_green", [("rattan_plate_green",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 640 , weight(14)|abundance(67)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_18] ],
["rattan_plate_blue", "rattan_plate_blue", [("rattan_plate_blue",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs |itp_civilian  ,0, 640 , weight(14)|abundance(67)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_18] ],
["mohhom_2_blue", "mohhom_2_blue", [("mohhom_2_blue",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs |itp_civilian  ,0, 260 , weight(8)|abundance(108)|head_armor(0)|body_armor(15)|leg_armor(5)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_18] ],
["mohhom_2_green", "mohhom_2_green", [("mohhom_2_green",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs |itp_civilian  ,0, 260 , weight(8)|abundance(108)|head_armor(0)|body_armor(15)|leg_armor(5)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_18] ],
["mohhom_2_brown", "mohhom_2_brown", [("mohhom_2_brown",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs |itp_civilian  ,0, 260 , weight(8)|abundance(108)|head_armor(0)|body_armor(15)|leg_armor(5)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_18] ],

["heavy_yawshan", "heavy_yawshan", [("zimke_char_aina_c",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 4270 , weight(24)|abundance(19)|head_armor(0)|body_armor(52)|leg_armor(20)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_6] ],
["sipahi_jawshan", "heavy_jawshan1", [("zimke_char_aina_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 4670 , weight(24)|abundance(17)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_6] ],
["zimke_char_aina", "zimke_char_aina", [("zimke_char_aina",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 4668 , weight(24)|abundance(18)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_6] ],
 
 ["undead_body", "undead_body", [("undead_body",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 0 , weight(100)|abundance(0)|head_armor(0)|body_armor(35)|leg_armor(9)|difficulty(10) ,imodbits_cloth,[],  ],

["zimke_kuyak_tors", "kuyak_tors", [("zimke_kuyak_tors",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 4670 , weight(24)|abundance(17)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_2] ],
["reytar_puzo1", "reytar_puzo", [("reytar_puzo",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 5130 , weight(24)|abundance(15)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(9) ,imodbits_cloth ],

["rac_hussar", "rac_hussar", [("rac_hussar",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 1360 , weight(18)|abundance(39)|head_armor(0)|body_armor(38)|leg_armor(20)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_2] ],
["rac_hussar_b", "rac_hussar_b", [("rac_hussar_b",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 1360 , weight(18)|abundance(39)|head_armor(0)|body_armor(38)|leg_armor(20)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_2] ],
["rac_hussar_c", "rac_hussar_c", [("rac_hussar_c",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2410 , weight(21)|abundance(27)|head_armor(0)|body_armor(45)|leg_armor(20)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_2] ],

["jack_of_plate_d", "jack_of_plate_d", [("jack_of_plate_d",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 590 , weight(14)|abundance(68)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_1] ],

["fysg_bin_shazei01", "fysg_shanzeihu", [("fysg_bin_shazei01", 0),],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 400, weight(10)|abundance(79)|body_armor(20)|leg_armor(12)|difficulty(0), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["nvyi", "hanhunvyi", [("nvyi", 0),],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 240, weight(7)|abundance(107)|body_armor(12)|leg_armor(10)|difficulty(0), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["nvyi1", "hanhunvyi1", [("copy_nvyi", 0),],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 240, weight(7)|abundance(107)|body_armor(12)|leg_armor(10)|difficulty(0), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["ylyq_hangyi", "ylyq_hangyi", [("ylyq_hangyi", 0),],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 240, weight(7)|abundance(107)|body_armor(12)|leg_armor(10)|difficulty(0), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["yf_hguanfu_a", "yf_hguanfu_a", [("yf_hguanfu_a", 0),],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 460, weight(11)|abundance(73)|body_armor(22)|leg_armor(10)|difficulty(0), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["yf_hguanfu_b", "yf_hguanfu_b", [("copy_yf_hguanfu_a", 0),],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 460, weight(11)|abundance(73)|body_armor(22)|leg_armor(10)|difficulty(0), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["nvyi2", "hanhunvyi2", [("han_nvfuq", 0),],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 240, weight(7)|abundance(104)|body_armor(12)|leg_armor(10)|difficulty(4), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["nvyi3", "hanhunvyi3", [("copy_han_nvfuq", 0),],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 240, weight(7)|abundance(104)|body_armor(12)|leg_armor(10)|difficulty(4), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["nvyi4", "hanhunvyi4", [("han_nvfuq1", 0),],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 240, weight(7)|abundance(107)|body_armor(12)|leg_armor(10)|difficulty(0), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["nvyi5", "hanhunvyi5", [("han_nvfuq2", 0),],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 240, weight(7)|abundance(107)|body_armor(12)|leg_armor(10)|difficulty(0), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["copy_man_han_fu", "0man_han_fu", [("copy_man_han_fu", 0),],itp_type_body_armor|itp_can_penetrate_shield|itp_merchandise|itp_civilian, 0, 240, weight(7)|abundance(107)|body_armor(12)|leg_armor(10)|difficulty(0), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],

["jaguar_armour", "jaguar_armour", [("jaguar_armour",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 500 , weight(12)|abundance(74)|head_armor(0)|body_armor(25)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_15] ],
["coyote_armour", "coyote_armour", [("coyote_armour",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 480 , weight(13)|abundance(80)|head_armor(0)|body_armor(26)|leg_armor(9)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_15] ],
["eagle_armour", "eagle_armour", [("eagle_armour",0)],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 500 , weight(12)|abundance(74)|head_armor(0)|body_armor(25)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_15] ],
["cuahchiqueh_armour", "cuahchiqueh_armour", [("cuahchiqueh_armour",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 500 , weight(12)|abundance(74)|head_armor(0)|body_armor(25)|leg_armor(0)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_15] ],
["cuahchiqueh_armour3333", "cuahchiqueh_armour3333", [("cuahchiqueh_armour3333",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 500 , weight(12)|abundance(74)|head_armor(0)|body_armor(25)|leg_armor(0)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_15] ],
["cuahchiqueh_armour2", "cuahchiqueh_armour2", [("cuahchiqueh_armour2",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 500 , weight(12)|abundance(74)|head_armor(0)|body_armor(25)|leg_armor(0)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_15] ],
["cuahchiqueh_armour3", "cuahchiqueh_armour3", [("cuahchiqueh_armour3",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 500 , weight(12)|abundance(74)|head_armor(0)|body_armor(25)|leg_armor(0)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_15] ],
["jaguar_armour3", "jaguar_armour3", [("jaguar_armour3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 500 , weight(12)|abundance(74)|head_armor(0)|body_armor(25)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_15] ],

 ["ceremonial_robe", "ceremonial_robe", [("ceremonial_robe", 0),],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 228, weight(6.75)|abundance(140)|body_armor(12)|leg_armor(10)|difficulty(0), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_11] ],
["shadow_outfit_b", "shadow_outfit_b", [("shadow_outfit_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 590 , weight(14.5)|abundance(116)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_11] ],
["sohei_b", "sohei_b", [("sohei_b",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 460 , weight(12.25)|abundance(124)|head_armor(0)|body_armor(25)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_11] ],

 ["samurai_civil_a", "samurai_civil_a", [("samurai_civil_a", 0),],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 390, weight(10)|abundance(82)|body_armor(20)|leg_armor(10)|difficulty(0), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_11] ],

 ["samurai_civil_c", "samurai_civil_c", [("samurai_civil_c", 0),],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 390, weight(10)|abundance(82)|body_armor(20)|leg_armor(10)|difficulty(0), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_11] ],
 
 ["ddddd", "lady01", [("ddddd", 0),],itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 390, weight(10)|abundance(82)|body_armor(20)|leg_armor(10)|difficulty(0), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_11] ],
["forviet", "forviet", [("forviet",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 390 , weight(10)|abundance(82)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_18] ],
["giap_viet1_d", "giap_viet1_d", [("giap_viet1_d",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 3960 , weight(23)|abundance(19)|head_armor(0)|body_armor(50)|leg_armor(20)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_18] ],
["giap_viet1_l", "giap_viet1_l", [("giap_viet1_l",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 3960 , weight(23)|abundance(19)|head_armor(0)|body_armor(50)|leg_armor(20)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_18] ],
["giap_viet1_x", "giap_viet1_x", [("giap_viet1_x",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 3960 , weight(23)|abundance(19)|head_armor(0)|body_armor(50)|leg_armor(20)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_18] ],
["shirt_wg", "shirt_wg", [("shirt_wg",0)], itp_type_body_armor|itp_covers_legs   ,0, 1590 , weight(19)|abundance(35)|head_armor(0)|body_armor(40)|leg_armor(20)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_18] ],

["europe2", "europe2", [("europe2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 2490 , weight(21)|abundance(26)|head_armor(0)|body_armor(45)|leg_armor(20)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_1] ],
["copy_europe2", "europe1", [("copy_europe2",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 2490 , weight(21)|abundance(26)|head_armor(0)|body_armor(45)|leg_armor(20)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_1] ],
["goldtuguese", "goldtuguese", [("goldtuguese",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 4240 , weight(23)|abundance(18)|head_armor(5)|body_armor(50)|leg_armor(22)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_9] ],
["copy_goldtuguese", "goldtuguese1", [("copy_goldtuguese",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 4240 , weight(23)|abundance(18)|head_armor(5)|body_armor(50)|leg_armor(22)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_9] ],

  ["yf_hwmf", "yf_hwmf", [("yf_hwmf", 0),],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 550, weight(12)|abundance(67)|body_armor(25)|leg_armor(10)|difficulty(0), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["yf_ydsb", "yf_ydsb", [("yf_ydsb",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 200 , weight(6)|abundance(121)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_15] ],

["korean_armour1", "korean_armour", [("korean_armour",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 270 , weight(8)|abundance(102)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_19] ],
["mongol_armour1", "mongol_armour", [("mongol_armour",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 4980 , weight(24)|abundance(16)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_10] ],

["arabpaded2", "arabpaded2", [("arabpaded2",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 350 , weight(10)|abundance(91)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_19] ],
["arsar2", "arsar2", [("arsar2",0)], itp_type_body_armor|itp_covers_legs   ,0, 1590 , weight(19)|abundance(35)|head_armor(0)|body_armor(40)|leg_armor(20)|difficulty(8) ,imodbits_cloth, [], [fac_kingdom_19] ],

["lamelarghulam", "lamelarghulam", [("lamelarghulam",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 4090 , weight(23)|abundance(18)|head_armor(0)|body_armor(50)|leg_armor(20)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_19] ],
["mailsarazin", "mailsarazin", [("mailsarazin",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 4090 , weight(23)|abundance(18)|head_armor(0)|body_armor(50)|leg_armor(20)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_19] ],
["sarazinass", "sarazinass", [("sarazinass",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 4090 , weight(23)|abundance(18)|head_armor(0)|body_armor(50)|leg_armor(20)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_19] ],
["saracenmail", "saracenmail", [("saracenmail",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 1970 , weight(19)|abundance(30)|head_armor(0)|body_armor(42)|leg_armor(15)|difficulty(8) ,imodbits_cloth, [], [fac_kingdom_19] ],

["saracenmails", "saracenmails", [("saracenmails",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 430 , weight(10)|abundance(75)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_19] ],
["saracenmailss", "saracenmail4", [("saracenmailss",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1060 , weight(17)|abundance(46)|head_armor(0)|body_armor(35)|leg_armor(15)|difficulty(7) ,imodbits_cloth, [], [fac_kingdom_19] ],
["saracenmailsss", "saracenmail3", [("saracenmailsss",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1060 , weight(17)|abundance(46)|head_armor(0)|body_armor(35)|leg_armor(15)|difficulty(7) ,imodbits_cloth, [], [fac_kingdom_19] ],
["saracenmailssss", "saracenmail2", [("saracenmailssss",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 1060 , weight(17)|abundance(46)|head_armor(0)|body_armor(35)|leg_armor(15)|difficulty(7) ,imodbits_cloth, [], [fac_kingdom_19] ],
["saracenmailsssss", "saracenmail1", [("saracenmailsssss",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1550 , weight(18)|abundance(34)|head_armor(0)|body_armor(38)|leg_armor(20)|difficulty(7) ,imodbits_cloth, [], [fac_kingdom_19] ],

["mongol_armor", "mongol_armor", [("mongol_armor",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 1700 , weight(19)|abundance(33)|head_armor(0)|body_armor(40)|leg_armor(20)|difficulty(7) ,imodbits_cloth, [], [fac_kingdom_19] ],
["saracen_armor11", "saracen_armor", [("saracen_armor",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 5130 , weight(24)|abundance(15)|head_armor(0)|body_armor(52)|leg_armor(25)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_19] ],

["black_body_new", "black_body_new", [("black_body_new",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 210 , weight(7)|abundance(122)|head_armor(0)|body_armor(12)|leg_armor(5)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_29] ],

["civil_clothing_final", "civil_clothing", [("civil_clothing_final",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 260 , weight(8)|abundance(106)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_11] ],
["yoroi1", "yoroi", [("yoroi",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs  ,0, 4530 , weight(24)|abundance(17)|head_armor(0)|body_armor(52)|leg_armor(18)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_11] ],
["hongfajia", "hongfajia", [("hongfajia",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs  ,0, 3720 , weight(23)|abundance(20)|head_armor(0)|body_armor(50)|leg_armor(15)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_11] ],
["copy_hongfajia", "copy_hongfajia", [("copy_hongfajia",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs  ,0, 3490 , weight(23)|abundance(21)|head_armor(0)|body_armor(50)|leg_armor(12)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_11] ],
["yidazzkuijia", "Yuzi_yidazzkuijia", [("yidazzkuijia",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs  ,0, 3720 , weight(23)|abundance(21)|head_armor(0)|body_armor(51)|leg_armor(10)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_11] ],
["copy_yidazzkuijia", "yidazzkuijia", [("copy_yidazzkuijia",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs  ,0, 3340 , weight(23)|abundance(22)|head_armor(0)|body_armor(50)|leg_armor(10)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_11] ],

["korean_skirt121", "korean_skirt", [("korean_skirt",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 300 , weight(8)|abundance(92)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_19] ],

["korean_armor", "korean_armor", [("korean_armor",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs   ,0, 1300 , weight(18)|abundance(41)|head_armor(0)|body_armor(38)|leg_armor(12)|difficulty(7) ,imodbits_cloth, [], [fac_kingdom_19] ],
["korean_black_armor", "korean_black_armor", [("korean_black_armor",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2390 , weight(21)|abundance(27)|head_armor(0)|body_armor(45)|leg_armor(16)|difficulty(8) ,imodbits_cloth, [], [fac_kingdom_19] ],
["korean_armor_2", "korean_armor_2", [("korean_armor_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs   ,0, 2270 , weight(21)|abundance(29)|head_armor(0)|body_armor(45)|leg_armor(15)|difficulty(8) ,imodbits_cloth, [], [fac_kingdom_19] ],
["korean_vest", "korean_vest", [("korean_vest",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 320 , weight(9)|abundance(93)|head_armor(0)|body_armor(18)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_19] ],

["aoqun", "Aoqun pink", [("Aoqun",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 280 , weight(8)|abundance(98)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_7] ],
["aoqun02", "Aoqun green", [("Aoqun02",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 280 , weight(8)|abundance(98)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_7] ],
["aoqun03", "Aoqun good", [("Aoqun03",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 280 , weight(8)|abundance(98)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_7] ],
["aoqun04", "Aoqun good", [("Aoqun04",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 280 , weight(8)|abundance(98)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_7] ],

["daao03", "Aoqun red", [("Daao03",0)],itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 280 , weight(8)|abundance(98)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_7] ],
["hanfu10", "Hanfu10", [("Hanfu10", 0),],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 420, weight(10)|abundance(77)|body_armor(20)|leg_armor(10)|difficulty(0), imodbits_cloth, [], [fac_kingdom_7] ],
["hanfu13", "Hanfu13", [("Hanfu13", 0),],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 420, weight(10)|abundance(77)|body_armor(20)|leg_armor(10)|difficulty(0), imodbits_cloth, [], [fac_kingdom_7] ],

["daopao", "Daopao", [("Daopao", 0),],itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 420, weight(10)|abundance(76)|body_armor(20)|leg_armor(10)|difficulty(0), imodbits_cloth, [], [fac_kingdom_7] ],

["jingyiwei01", "jingyiwei01", [("jingyiwei01", 0),],itp_type_body_armor|itp_can_penetrate_shield|itp_merchandise|itp_civilian, 0, 420, weight(10)|abundance(76)|body_armor(20)|leg_armor(12)|difficulty(0), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["jingyiwei02", "jingyiwei02", [("jingyiwei02", 0),],itp_type_body_armor|itp_can_penetrate_shield|itp_merchandise|itp_civilian, 0, 420, weight(10)|abundance(76)|body_armor(20)|leg_armor(12)|difficulty(0), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["jingyiwei03", "jingyiwei03", [("jingyiwei03", 0),],itp_type_body_armor|itp_can_penetrate_shield|itp_merchandise|itp_civilian, 0, 420, weight(10)|abundance(76)|body_armor(20)|leg_armor(12)|difficulty(0), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["jingyiwei04", "jingyiwei04", [("jingyiwei04", 0),],itp_type_body_armor|itp_can_penetrate_shield|itp_merchandise|itp_civilian, 0, 420, weight(10)|abundance(76)|body_armor(20)|leg_armor(12)|difficulty(0), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],

["minggf", "ming guanfu", [("mingGF", 0),],itp_type_body_armor|itp_can_penetrate_shield|itp_merchandise|itp_civilian, 0, 540, weight(11)|abundance(64)|body_armor(23)|leg_armor(12)|difficulty(0), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["minglp", "ming longpao", [("minglp", 0),],itp_type_body_armor|itp_can_penetrate_shield|itp_merchandise|itp_civilian, 0, 590, weight(12)|abundance(62)|body_armor(25)|leg_armor(12)|difficulty(0), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],

["mjingyiwei", "Jingyiwei Armor", [("MJingyiwei", 0),],itp_type_body_armor|itp_can_penetrate_shield|itp_merchandise, 0, 1750, weight(20)|abundance(34)|body_armor(52)|leg_armor(22)|difficulty(0), imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],

["daming_armor", "DaMing_armor_heavy_blue", [("DaMing_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 6900 , weight(25)|abundance(12)|head_armor(0)|body_armor(55)|leg_armor(30)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_7]],
["daming_armor_01", "DaMing_armor_heavy_red", [("DaMing_armor_01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 6900 , weight(25)|abundance(12)|head_armor(0)|body_armor(55)|leg_armor(30)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_7]],
["daming_armor_02", "DaMing_armor_heavy", [("DaMing_armor_02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 6900 , weight(25)|abundance(12)|head_armor(0)|body_armor(55)|leg_armor(30)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_7]],

["daming_armor_03", "DaMing_armor_light_blue", [("DaMing_armor_03",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 580 , weight(12)|abundance(63)|head_armor(0)|body_armor(25)|leg_armor(15)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_7]],

 ["daming_armor_04", "DaMing_armor_M_red", [("DaMing_armor_04",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 400 , weight(10)|abundance(79)|head_armor(0)|body_armor(45)|leg_armor(20)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_7]],
["daming_armor_05", "DaMing_armor_M_black", [("DaMing_armor_05",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 400 , weight(10)|abundance(79)|head_armor(0)|body_armor(45)|leg_armor(20)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_7]],

 ["daming_armor_06", "DaMing_armor_M_red1", [("DaMing_armor_06",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2160 , weight(19)|abundance(28)|head_armor(0)|body_armor(42)|leg_armor(20)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_7]],
["daming_armor_07", "DaMing_armor_M_black1", [("DaMing_armor_07",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2160 , weight(19)|abundance(28)|head_armor(0)|body_armor(42)|leg_armor(20)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_7]],

 ["daming_armor_08", "DaMing_armor_L_huoqiang1", [("DaMing_armor_08",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 560 , weight(13)|abundance(68)|head_armor(0)|body_armor(26)|leg_armor(14)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_7]],
["daming_armor_09", "DaMing_armor_L_huoqiang2", [("DaMing_armor_09",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 560 , weight(13)|abundance(68)|head_armor(0)|body_armor(26)|leg_armor(14)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_7]],

["daming_armor_10", "DaMing_armor_light_blue1", [("DaMing_armor_10",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 560 , weight(13)|abundance(68)|head_armor(0)|body_armor(25)|leg_armor(15)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_7]],

["daming_armor_11", "DaMing_armor_M_yellow1", [("DaMing_armor_11",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 500 , weight(12)|abundance(74)|head_armor(0)|body_armor(50)|leg_armor(25)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_7] ],
["daming_armor_12", "DaMing_armor_M_red1", [("DaMing_armor_12",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 500 , weight(12)|abundance(74)|head_armor(0)|body_armor(50)|leg_armor(25)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_7]],

["daming_armor_13", "DaMing_armor_M_mianjiaBlue1", [("DaMing_armor_13",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 4180 , weight(22)|abundance(17)|head_armor(0)|body_armor(48)|leg_armor(28)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_7]],
["daming_armor_14", "DaMing_armor_M_mianjiaYellow1", [("DaMing_armor_14",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 4180 , weight(22)|abundance(17)|head_armor(0)|body_armor(48)|leg_armor(28)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_7]],
 
["daming_armor_15", "DaMing_armor_H_mianjiaBlue1", [("DaMing_armor_15",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 5380 , weight(23)|abundance(14)|head_armor(0)|body_armor(51)|leg_armor(28)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_7]],
["daming_armor_16", "DaMing_armor_H_mianjiaYellow1", [("DaMing_armor_16",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 5380 , weight(23)|abundance(14)|head_armor(0)|body_armor(51)|leg_armor(28)|difficulty(9) ,imodbits_cloth, [], [fac_kingdom_7] ],
 
["daming_armor_17", "DaMing_armor_heavy_black", [("DaMing_armor_17",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 6010 , weight(25)|abundance(14)|head_armor(0)|body_armor(54)|leg_armor(30)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_7]],
["daming_armor_18", "DaMing_armor_heavy_yellow", [("DaMing_armor_18",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 6010 , weight(25)|abundance(14)|head_armor(0)|body_armor(54)|leg_armor(30)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_7]],

  ["cavalry_armor_a1111", "cavalry_armor_a", [("cavalry_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 6600 , weight(25)|abundance(13)|head_armor(0)|body_armor(54)|leg_armor(32)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_1]],
["officer_jacket_011", "officer_jacket_01", [("officer_jacket_01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 290 , weight(8)|abundance(94)|head_armor(0)|body_armor(24)|leg_armor(15)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_9]],
["officer_jacket_022", "officer_jacket_02", [("officer_jacket_02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1810 , weight(19)|abundance(31)|head_armor(0)|body_armor(40)|leg_armor(20)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_9]],
["officer_jacket_033", "officer_jacket_03", [("officer_jacket_03",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 4460 , weight(23)|abundance(17)|head_armor(0)|body_armor(50)|leg_armor(25)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_9]],
["pirate_captain_body", "captain_body", [("pirate_captain_body",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 840 , weight(14)|abundance(51)|head_armor(0)|body_armor(30)|leg_armor(16)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_9]],

 
 ##yifeng 1.5 add
["black_body_new1", "black_body11", [("black_body_new1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 200 , weight(6)|abundance(123)|head_armor(0)|body_armor(10)|leg_armor(7)|difficulty(0) ,imodbits_cloth , [], [] ],
["black_shirt11", "black_body_shirt", [("black_shirt",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 220 , weight(7)|abundance(117)|head_armor(0)|body_armor(12)|leg_armor(7)|difficulty(0) ,imodbits_cloth , [], [] ],

#["fattiglinenskjortir", "white_shirt", [("fattiglinenskjortir",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 240 , weight(8)|abundance(114)|head_armor(0)|body_armor(15)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [] ],
#["redvikingshirt", "red_shirt", [("redvikingshirt",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 280 , weight(8)|abundance(102)|head_armor(0)|body_armor(16)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [] ],
#["bluevikingshirt", "blue_shirt", [("bluevikingshirt",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 280 , weight(8)|abundance(102)|head_armor(0)|body_armor(16)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [] ],
#["greenvikingshirt", "green_shirt", [("greenvikingshirt",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 280 , weight(1)|abundance(102)|head_armor(0)|body_armor(16)|leg_armor(10)|difficulty(0) ,imodbits_cloth , [], [] ],

["haubergeon_b", "Haubergeon1", [("haubergeon_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 863 , weight(17)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(6) ,imodbits_armor,[], we_faction  ],

  ["sar_robe_b11", "Worn Robe", [("sar_robe_b11",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(10) ,imodbits_cloth,[], arb_faction ],

  ["sar_robe_a11", "Worn Robe", [("sar_robe_a11",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(10) ,imodbits_cloth,[], arb_faction ],
#Yifeng from12th
["mon_a_from12th", "Mongolia Armor1", [("mon_a_from12th",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3580 , weight(20)|abundance(18)|head_armor(0)|body_armor(48)|leg_armor(28)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_10]],
#Yifeng from12th

  #yifeng test inca  fac_kingdom_30

["yinjiayifu01", "Incan Clothes", [("yinjiayifu01",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 230 , weight(7)|abundance(117)|head_armor(0)|body_armor(14)|leg_armor(7)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_30] ],
["yinjiayifu02", "Incan Colorful Clothes", [("yinjiayifu02",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 220 , weight(7)|abundance(117)|head_armor(0)|body_armor(12)|leg_armor(7)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_30] ],
["yinjiayifu03", "Incan Short Clothes", [("yinjiayifu03",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 220 , weight(7)|abundance(117)|head_armor(0)|body_armor(12)|leg_armor(7)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_30] ],
["yinjiayifu04", "Incan Long Clothes", [("yinjiayifu04",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 240 , weight(7)|abundance(117)|head_armor(0)|body_armor(15)|leg_armor(7)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_30] ],
["yinjiayifu05", "Incan White Clothes", [("yinjiayifu05",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 240 , weight(7)|abundance(117)|head_armor(0)|body_armor(15)|leg_armor(7)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_30] ],
["yinjiayifu06", "Incan Red Clothes", [("yinjiayifu06",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 300 , weight(8)|abundance(117)|head_armor(0)|body_armor(16)|leg_armor(8)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_30] ],

 #yifeng armor end

 ["sarranid_dress_a", "Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 210 , weight(5)|abundance(109)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 ["sarranid_dress_b", "Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 210 , weight(5)|abundance(109)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 ["sarranid_cloth_robe", "Worn Robe", [("sar_robe",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 210 , weight(5)|abundance(109)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_cloth,[], arb_faction ],
 ["sarranid_cloth_robe_b", "Worn Robe", [("sar_robe_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 210 , weight(5)|abundance(109)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_cloth,[], arb_faction ],
["skirmisher_armor", "Skirmisher Armor", [("skirmisher_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 230, weight(5)|abundance(104)|head_armor(0)|body_armor(15)|leg_armor(9)|difficulty(0) ,imodbits_cloth ,[], arb_faction],
["archers_vest", "Archer's Padded Vest", [("archers_vest",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 480 , weight(11)|abundance(73)|head_armor(0)|body_armor(23)|leg_armor(12)|difficulty(0) ,imodbits_cloth,[], arb_faction ],
["sarranid_leather_armor", "Sarranid Leather Armor", [("sarranid_leather_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 770 , weight(15)|abundance(58)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(7) ,imodbits_armor ,[], arb_faction],
["sarranid_cavalry_robe", "Cavalry Robe", [("arabian_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 960 , weight(17)|abundance(52)|head_armor(0)|body_armor(36)|leg_armor(8)|difficulty(7) ,imodbits_armor ,[], arb_faction],
["arabian_armor_b", "Sarranid Guard Armor", [("arabian_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1160 , weight(18)|abundance(46)|head_armor(0)|body_armor(38)|leg_armor(8)|difficulty(7) ,imodbits_armor,[], arb_faction],
 ["sarranid_mail_shirt", "Sarranid Mail Shirt", [("sarranian_mail_shirt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 1620 , weight(19)|abundance(35)|head_armor(0)|body_armor(40)|leg_armor(14)|difficulty(8) ,imodbits_armor ,[], arb_faction],
["mamluke_mail", "Mamluke Mail", [("sarranid_elite_cavalary",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
3290 , weight(22)|abundance(21)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(8) ,imodbits_armor ,[], arb_faction],

#Quest-specific - perhaps can be used for prisoners, 
["burlap_tunic", "Burlap Tunic", [("shirt",0)], itp_type_body_armor  |itp_covers_legs ,0,
 5 , weight(1)|abundance(100)|head_armor(0)|body_armor(3)|leg_armor(1)|difficulty(0) ,imodbits_armor ],


["heraldic_mail_with_surcoat", "Heraldic Mail with Surcoat", [("heraldic_armor_new_a",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 3454 , weight(22)|abundance(0)|head_armor(0)|body_armor(49)|leg_armor(17)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])]],
["heraldic_mail_with_tunic", "Heraldic Mail", [("heraldic_armor_new_b",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 3520 , weight(22)|abundance(0)|head_armor(0)|body_armor(50)|leg_armor(16)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_b", ":agent_no", ":troop_no")])]],
["heraldic_mail_with_tunic_b", "Heraldic Mail", [("heraldic_armor_new_c",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 3610 , weight(22)|abundance(0)|head_armor(0)|body_armor(50)|leg_armor(16)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_c", ":agent_no", ":troop_no")])]],
["heraldic_mail_with_tabard", "Heraldic Mail with Tabard", [("heraldic_armor_new_d",0)],  itp_type_body_armor  |itp_covers_legs ,0,
 3654 , weight(21)|abundance(0)|head_armor(0)|body_armor(51)|leg_armor(15)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_d", ":agent_no", ":troop_no")])]],
["turret_hat_ruby", "Turret Hat", [("turret_hat_r",0)], itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 70 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 
["turret_hat_blue", "Turret Hat", [("turret_hat_b",0)], itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 80 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 
["turret_hat_green", "Barbette", [("barbette_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,70, weight(0.5)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["head_wrappings","Head Wrapping",[("head_wrapping",0)],itp_type_head_armor|itp_fit_to_head,0,16, weight(0.25)|head_armor(3),imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick],
["court_hat", "Turret Hat", [("court_hat",0)], itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 80 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 
["wimple_a", "Wimple", [("wimple_a_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,10, weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["wimple_with_veil", "Wimple with Veil", [("wimple_b_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,10, weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["straw_hat", "Straw Hat", [("straw_hat_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["common_hood", "Hood", [("hood_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["hood_b", "Hood", [("hood_b",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["hood_c", "Hood", [("hood_c",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["hood_d", "Hood", [("hood_d",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["headcloth", "Headcloth", [("headcloth_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_hood", "Woolen Hood", [("woolen_hood",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["arming_cap", "Arming Cap", [("arming_cap_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 5 , weight(1)|abundance(100)|head_armor(7)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["fur_hat", "Fur Hat", [("fur_hat_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["nomad_cap", "Nomad Cap", [("nomad_cap_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["nomad_cap_b", "Nomad Cap", [("nomad_cap_b_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(13)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["steppe_cap", "Steppe Cap", [("steppe_cap_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 14 , weight(1)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["padded_coif", "Padded Coif", [("padded_coif_a_new",0)], itp_merchandise| itp_type_head_armor   ,0, 6 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_cap", "Woolen Cap", [("woolen_cap_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["felt_hat", "Felt Hat", [("felt_hat_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["felt_hat_b", "Felt Hat", [("felt_hat_b_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_cap", "Leather Cap", [("leather_cap_a_new",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 8, weight(1)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["female_hood", "Lady's Hood", [("ladys_hood_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 9 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_steppe_cap_a", "Steppe Cap", [("leather_steppe_cap_a_new",0)], itp_merchandise|itp_type_head_armor   ,0, 
24 , weight(1)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["leather_steppe_cap_b", "Steppe Cap ", [("tattered_steppe_cap_b_new",0)], itp_merchandise|itp_type_head_armor   ,0, 
36 , weight(1)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["leather_steppe_cap_c", "Steppe Cap", [("steppe_cap_a_new",0)], itp_merchandise|itp_type_head_armor   ,0, 51 , weight(1)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["leather_warrior_cap", "Leather Warrior Cap", [("skull_cap_new_b",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 14 , weight(1)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth,[], we_faction ],
["skullcap", "Skullcap", [("skull_cap_new_a",0)], itp_merchandise| itp_type_head_armor   ,0, 60 , weight(1.0)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ,[], we_faction ],
["mail_coif", "Mail Coif", [("mail_coif_new",0)], itp_merchandise| itp_type_head_armor   ,0, 71 , weight(1.25)|abundance(0)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor ,[], we_faction ],
["footman_helmet", "Footman's Helmet", [("skull_cap_new",0)], itp_merchandise| itp_type_head_armor   ,0, 95 , weight(1.5)|abundance(100)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate,[], we_faction  ],
#missing...
["nasal_helmet", "Nasal Helmet", [("nasal_helmet_b",0)], itp_merchandise| itp_type_head_armor   ,0, 121 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,[], we_faction  ],
["norman_helmet", "Helmet with Cap", [("norman_helmet_a",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 147 , weight(1.25)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[], we_faction ],
["segmented_helmet", "Segmented Helmet", [("segmented_helm_new",0)], itp_merchandise| itp_type_head_armor   ,0, 174 , weight(1.25)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[], we_faction ],
["helmet_with_neckguard", "Helmet with Neckguard", [("neckguard_helm_new",0)], itp_merchandise| itp_type_head_armor   ,0, 
190 , weight(1.5)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,[], we_faction  ],
["flat_topped_helmet", "Flat Topped Helmet", [("flattop_helmet_new",0)], itp_merchandise| itp_type_head_armor   ,0, 
203 , weight(1.75)|abundance(100)|head_armor(33)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[], we_faction ],
["kettle_hat", "Kettle Hat", [("kettle_hat_new",0)], itp_merchandise| itp_type_head_armor,0, 
240 , weight(1.75)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,[], we_faction  ],
["spiked_helmet", "Spiked Helmet", [("spiked_helmet_new",0)], itp_merchandise| itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[], we_faction ],
["nordic_helmet", "Nordic Helmet", [("helmet_w_eyeguard_new",0)], itp_merchandise| itp_type_head_armor   ,0, 340 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[], we_faction ],
["khergit_lady_hat", "Khergit Lady Hat", [("khergit_lady_hat",0)],  itp_type_head_armor   |itp_civilian |itp_doesnt_cover_hair | itp_fit_to_head,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["khergit_lady_hat_b", "Khergit Lady Leather Hat", [("khergit_lady_hat_b",0)], itp_type_head_armor  | itp_doesnt_cover_hair | itp_fit_to_head  |itp_civilian ,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sarranid_felt_hat", "Sarranid Felt Hat", [("sar_helmet3",0)], itp_merchandise| itp_type_head_armor   ,0, 16 , weight(2)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth,[], arb_faction  ],
["turban1134", "Turban", [("tuareg_open",0)], itp_merchandise| itp_type_head_armor   ,0, 28 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth ],
["desert_turban", "Desert Turban", [("tuareg",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard ,0, 38 , weight(1.50)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth,[], arb_faction  ],
["sarranid_warrior_cap", "Sarranid Warrior Cap", [("tuareg_helmet",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard  ,0, 90 , weight(2)|abundance(100)|head_armor(19)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,[], arb_faction  ],
["sarranid_horseman_helmet", "Horseman Helmet", [("sar_helmet2",0)], itp_merchandise| itp_type_head_armor   ,0, 180 , weight(2.75)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,[], arb_faction  ],
["sarranid_helmet1", "Sarranid Keffiyeh Helmet", [("sar_helmet1",0)], itp_merchandise| itp_type_head_armor   ,0, 290 , weight(2.50)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,[], arb_faction  ],
["sarranid_mail_coif", "Sarranid Mail Coif", [("tuareg_helmet2",0)], itp_merchandise| itp_type_head_armor ,0, 430 , weight(3)|abundance(100)|head_armor(41)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[], arb_faction ],
["sarranid_veiled_helmet", "Sarranid Veiled Helmet", [("sar_helmet4",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard  ,0, 810 , weight(3.50)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,[], arb_faction  ],
["nordic_archer_helmet", "Nordic Leather Helmet", [("Helmet_A_vs2",0)], itp_merchandise| itp_type_head_armor    ,0, 40 , weight(1.25)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[], we_faction ],
["nordic_veteran_archer_helmet", "Nordic Leather Helmet", [("Helmet_A",0)], itp_merchandise| itp_type_head_armor,0, 70 , weight(1.5)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[], we_faction ],
["nordic_footman_helmet", "Nordic Footman Helmet", [("Helmet_B_vs2",0)], itp_merchandise| itp_type_head_armor |itp_fit_to_head ,0, 150 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[], we_faction ],
["nordic_fighter_helmet", "Nordic Fighter Helmet", [("Helmet_B",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 240 , weight(2)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,[], we_faction  ],
["nordic_huscarl_helmet", "Nordic Huscarl's Helmet", [("Helmet_C_vs2",0)], itp_merchandise| itp_type_head_armor   ,0, 390 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[], we_faction ],
["nordic_warlord_helmet", "Nordic Warlord Helmet", [("Helmet_C",0)], itp_merchandise| itp_type_head_armor ,0, 880 , weight(2.25)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,[], we_faction  ],

["vaegir_fur_cap", "Cap with Fur", [("vaeg_helmet3",0)], itp_merchandise| itp_type_head_armor   ,0, 50 , weight(1)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[], [fac_kingdom_2] ],
["vaegir_fur_helmet", "Vaegir Helmet", [("vaeg_helmet2",0)], itp_merchandise| itp_type_head_armor   ,0, 110 , weight(2)|abundance(100)|head_armor(21)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[], [fac_kingdom_2]],
["vaegir_spiked_helmet", "Spiked Cap", [("vaeg_helmet1",0)], itp_merchandise| itp_type_head_armor   ,0, 230 , weight(2.50)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,[], [fac_kingdom_2] ],
["vaegir_lamellar_helmet", "Helmet with Lamellar Guard", [("vaeg_helmet4",0)], itp_merchandise| itp_type_head_armor   ,0, 360 , weight(2.75)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[], [fac_kingdom_2]],
["vaegir_noble_helmet", "Vaegir Nobleman Helmet", [("vaeg_helmet7",0)], itp_merchandise| itp_type_head_armor   ,0, 710, weight(2.75)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,[], [fac_kingdom_2] ],
["vaegir_war_helmet", "Vaegir War Helmet", [("vaeg_helmet6",0)], itp_merchandise| itp_type_head_armor   ,0, 820 , weight(3)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ,[], [fac_kingdom_2]],
["vaegir_mask", "Vaegir War Mask", [("vaeg_helmet9",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0, 950 , weight(3.50)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,[], [fac_kingdom_2] ],

#TODO:
#["skullcap_b", "Skullcap_b", [("skull_cap_new_b",0)], itp_merchandise| itp_type_head_armor   ,0, 71 , weight(1.5)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
 
 
 ##yifeng helmet
 
 #should delete
 #["mao", "mao", [("mao", 0),],itp_type_head_armor|itp_merchandise, 0, 410, weight(2.000000)|abundance(200)|head_armor(22)|difficulty(7), imodbit_cracked|imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
 #should delete
 ["red_great_helmet", "Red Great Helmet one", [("great_helmet_red",0)],  itp_merchandise|itp_type_head_armor|itp_covers_head,0, 1650 , weight(3)|abundance(17)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate,[], we_faction ],
["red_great_helmet_ex", "Red Great Helmet Ex", [("2bascinet_new",0)],  itp_merchandise|itp_type_head_armor|itp_covers_head,0, 1600 , weight(3)|abundance(17)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate,[], we_faction ],
["great_helmet_red", "Great Helmet Red", [("great_helmet_my",0)],  itp_merchandise|itp_type_head_armor|itp_covers_head,0, 1340 , weight(2.75)|abundance(20)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ,[], we_faction],
["red_great_helmet_wings", "Red Great Helmet Wings", [("helmets_Kevin",0)],  itp_merchandise|itp_type_head_armor|itp_covers_head,0, 2520 , weight(3)|abundance(13)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(15) ,imodbits_plate,[], we_faction ],
["kettle_hat_x", "Kettle Hat", [("kettlehat1_painted",0)],itp_merchandise| itp_type_head_armor,0, 
350 , weight(2.25)|abundance(0)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate ,[], we_faction],
["kettle_hat_z", "Kettle Hat", [("prato_chapel-de-fer",0)],  itp_merchandise|itp_type_head_armor,0, 
830 , weight(2.5)|abundance(0)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate,[], we_faction ],
["new_guard_helmet", "Guard Helmet", [("acb1_helm",0)], itp_merchandise| itp_type_head_armor   ,0, 1650 , weight(3)|abundance(17)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,[], we_faction],
["gete_helmet", "Gete Helmet", [("new_sallet",0)], itp_type_head_armor,0, 3550 , weight(3.25)|abundance(10)|head_armor(65)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ,[], we_faction], 
["pigface_klappvisor", "Pigface Bascinet", [("pigface_klappvisor",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 1790 , weight(3)|abundance(16)|head_armor(56)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ,[], we_faction],
["pigface_klappvisor_open", "Pigface Bascinet", [("pigface_klappvisor_open",0)], itp_merchandise|itp_type_head_armor   ,0, 1190 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,[], we_faction ],
["open_sallet", "Open Sallet", [("open_sallet",0)], itp_merchandise| itp_type_head_armor,0, 1050 , weight(2.5)|abundance(22)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate,[], we_faction ],
["open_sallet_coif", "Open Sallet Coif", [("open_sallet_coif",0)], itp_merchandise| itp_type_head_armor,0, 1150 , weight(2.75)|abundance(25)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,[], we_faction],
["combed_morion1", "Combed Morion", [("combed_morion_blued",0)], itp_merchandise| itp_type_head_armor,0, 1190 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ,[], we_faction],
["new_helmet_a", "New Helmet", [("h_h1",0)], itp_merchandise| itp_type_head_armor,0, 140 , weight(2)|abundance(80)|head_armor(21)|body_armor(0)|leg_armor(0) ,imodbits_plate ,[], we_faction],
["new_helmet_b", "New Helmet", [("h_h1_1",0)], itp_merchandise| itp_type_head_armor,0, 140 , weight(2)|abundance(80)|head_armor(21)|body_armor(0)|leg_armor(0) ,imodbits_plate ,[], we_faction],
["new_helmet_c", "New Helmet", [("h_h2",0)], itp_merchandise| itp_type_head_armor,0, 140 , weight(2)|abundance(80)|head_armor(21)|body_armor(0)|leg_armor(0) ,imodbits_plate ,[], we_faction],
["new_helmet_d", "New Helmet", [("h_h2_1",0)], itp_merchandise| itp_type_head_armor,0, 140 , weight(2)|abundance(80)|head_armor(21)|body_armor(0)|leg_armor(0) ,imodbits_plate ,[], we_faction],
["fabing_head", "Fabing Head", [("fabing_head",0)], itp_merchandise| itp_type_head_armor   ,0, 70 , weight(1.25)|abundance(109)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_7]],
["toujing_head", "Toujing", [("toujing_head",0)], itp_merchandise| itp_type_head_armor   ,0, 90 , weight(1.5)|abundance(102)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_7]],
["zijinguan", "Zi Jin Guan", [("zijinguan",0)], itp_merchandise| itp_type_head_armor   ,0, 80 , weight(1.5)|abundance(105)|head_armor(9)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_7]],
["summer_infantry_helmet", "Summer Infantry Helmet", [("SONG_BUBING_TOUKUI",0)],  itp_merchandise|itp_type_head_armor,0, 1540 , weight(2.75)|abundance(17)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_7]],
["summer_lord_helmet", "Summer Lord Helmet", [("Song_helmet_1",0)], itp_merchandise| itp_type_head_armor,0, 1590 , weight(2.75)|abundance(17)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_7]],
["summer_lord_helmet_black", "Summer Lord Helmet Black", [("SONG_QIBING",0)], itp_merchandise| itp_type_head_armor,0, 1470 , weight(3)|abundance(18)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_7]],
["mon_helmet_kk", "Helmet KK", [("mon_helmet_kk",0)], itp_merchandise|itp_type_head_armor   ,0, 880 , weight(2.5)|abundance(24)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate , [], [fac_kingdom_7]],
["mon_helmet_km", "Helmet KM", [("lamellar_helmet_KK",0)], itp_merchandise|itp_type_head_armor   ,0, 850 , weight(2.5)|abundance(25)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate , [], [fac_kingdom_7]],
["zhanmao", "Zhan Mao", [("zhanmao",0)], itp_merchandise| itp_type_head_armor   ,0, 350 , weight(2.25)|abundance(47)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate , [], [fac_kingdom_7]],

["nikolskoe_helm", "Nikolskoe helm", [("nikolskoe_helm",0), ("inv_nikolskoe_helm",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature  ,0, 1110 , weight(2.5)|abundance(21)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_kingdom_2]],
["novogrod_helm", "Novogrod helm", [("novogrod_helm",0), ("inv_novogrod_helm",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 1020 , weight(2.5)|abundance(22)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_kingdom_2]],
["gnezdovo_helm_a", "Gnezdovo helm", [("gnezdovo_helm_a",0), ("inv_gnezdovo_helm_a",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 850 , weight(2.5)|abundance(25)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_kingdom_2]],
["tagancha_helm_a", "Tagancha helm", [("tagancha_helm_a",0), ("inv_tagancha_helm_a",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 780 , weight(2.5)|abundance(27)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_kingdom_2]],
["tagancha_helm_b", "Tagancha helm", [("tagancha_helm_b",0), ("inv_tagancha_helm_b",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 1110 , weight(2.5)|abundance(21)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_kingdom_2]],
["rus_helm", "Rus helm", [("rus_helm",0), ("inv_rus_helm",ixmesh_inventory)], itp_merchandise| itp_type_head_armor | itp_attach_armature,0, 320 , weight(2)|abundance(48)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate , [], [fac_kingdom_2]],

["toukui1", "toukui1", [("toukui1",0)], itp_merchandise| itp_type_head_armor,0, 1230 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ,[], we_faction],
["toukui2", "toukui2", [("toukui2",0)], itp_merchandise| itp_type_head_armor,0, 1230 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ,[], we_faction],
["toukui3", "toukui3", [("toukui3",0)], itp_merchandise| itp_type_head_armor,0, 1150 , weight(2.75)|abundance(27)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ,[], we_faction],
["toukui4", "toukui4", [("toukui4",0)], itp_merchandise| itp_type_head_armor,0, 1120 , weight(2.75)|abundance(22)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate,[], we_faction ],
["toukui5", "toukui5", [("toukui5",0)], itp_merchandise| itp_type_head_armor,0, 1250 , weight(2.75)|abundance(19)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ,[], we_faction],
["toukui6", "toukui6", [("toukui6",0)], itp_merchandise| itp_type_head_armor,0, 1250 , weight(2.75)|abundance(19)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate,[], we_faction],

["s_kuei", "s_kuei", [("s_kuei", 0),],itp_type_head_armor|itp_merchandise, 0, 350, weight(2.25)|abundance(47)|head_armor(35)|difficulty(6), imodbit_cracked|imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7]],
["s_kuei3", "s_kuei3", [("s_kuei3", 0),],itp_type_head_armor|itp_merchandise, 0, 360, weight(2.25)|abundance(45)|head_armor(35)|difficulty(6), imodbit_cracked|imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["kuei10", "kuei10", [("kuei10", 0),],itp_type_head_armor|itp_merchandise, 0, 340, weight(2.25)|abundance(48)|head_armor(35)|difficulty(6), imodbit_cracked|imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7]],
["qibingkuei", "qibingkuei", [("qibingkuei", 0),],itp_type_head_armor|itp_merchandise, 0, 1370, weight(2.75)|abundance(19)|head_armor(52)|difficulty(8), imodbit_cracked|imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["qibingkuei1", "qibingkuei1", [("qibingkuei1", 0),],itp_type_head_armor|itp_merchandise, 0, 1370, weight(2.75)|abundance(19)|head_armor(52)|difficulty(8), imodbit_cracked|imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["qibingkuei2", "qibingkuei2", [("qibingkuei2", 0),],itp_type_head_armor|itp_merchandise, 0, 1370, weight(2.75)|abundance(19)|head_armor(52)|difficulty(8), imodbit_cracked|imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["mingkuei3", "mingkuei3", [("mingkuei3", 0),],itp_type_head_armor|itp_merchandise, 0, 1370, weight(2.75)|abundance(19)|head_armor(52)|difficulty(8), imodbit_cracked|imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["Ming_kui", "Ming_kui", [("Ming_kui", 0),],itp_type_head_armor|itp_merchandise, 0, 340, weight(2.25)|abundance(48)|head_armor(35)|difficulty(6), imodbit_cracked|imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["mingkuei", "mingkuei", [("mingkuei", 0),],itp_type_head_armor|itp_merchandise, 0, 1370, weight(2.75)|abundance(19)|head_armor(52)|difficulty(8), imodbit_cracked|imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["mingkuei2", "mingkuei2", [("mingkuei2", 0),],itp_type_head_armor|itp_merchandise, 0, 780, weight(2.5)|abundance(27)|head_armor(45)|difficulty(7), imodbit_cracked|imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["kuei12", "kuei12", [("kuei12", 0),],itp_type_head_armor|itp_merchandise, 0, 800, weight(2.5)|abundance(27)|head_armor(45)|difficulty(7), imodbit_cracked|imodbit_rusty|imodbit_crude|imodbit_reinforced|imodbit_battered|imodbit_thick|imodbit_lordly, [], [fac_kingdom_7] ],
["mingkuei11", "mingkuei11", [("mingkuei11", 0),],itp_type_head_armor|itp_merchandise, 0, 130, weight(1.75)|abundance(80)|head_armor(18), imodbit_ragged|imodbit_sturdy|imodbit_thick|imodbit_hardened|imodbit_tattered, [], [fac_kingdom_7] ],

 ["Ansar", "Ansaryellow", [("Ansar",0)], itp_merchandise| itp_type_head_armor,0, 270 , weight(2)|abundance(54)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate , [], [fac_kingdom_6] ],
 ["Assawira_helmet", "Assawira_helmet", [("Assawira_helmet",0)], itp_merchandise| itp_type_head_armor,0, 490 , weight(2.5)|abundance(38)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_kingdom_14] ],
 ["Muslim_leader", "Muslim_leader", [("Muslim_leader",0)], itp_merchandise| itp_type_head_armor,0, 1150 , weight(2.75)|abundance(21)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_6] ],
["Saracen_Masked_helmet", "Saracen_Masked_helmetRed", [("Saracen_Masked_helmet",0)], itp_merchandise| itp_type_head_armor,0, 180 , weight(2)|abundance(70)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_12] ],
["Saracen_Masked_helmet_b", "Saracen_Masked_helmetRedblack1", [("Saracen_Masked_helmet_b",0)], itp_merchandise| itp_type_head_armor,0, 180 , weight(2)|abundance(25)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate , [], [fac_kingdom_12] ],
["Saracen_Masked_helmet_c", "Saracen_Masked_helmetRedyellow", [("Saracen_Masked_helmet_c",0)], itp_merchandise| itp_type_head_armor,0, 180 , weight(2)|abundance(25)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate , [], [fac_kingdom_12] ],
["Saracen_Masked_helmet_d", "Saracen_Masked_helmetRedblack", [("Saracen_Masked_helmet_d",0)], itp_merchandise| itp_type_head_armor,0, 180 , weight(2)|abundance(25)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate , [], [fac_kingdom_12] ],

 ["assassin_helmet2", "assassin_helmet2", [("assassin_helmet2",0)], itp_merchandise| itp_type_head_armor,0, 260 , weight(2)|abundance(56)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate , [], [fac_kingdom_6] ],
 ["burgonet", "burgonet", [("burgonet",0)], itp_merchandise| itp_type_head_armor,0, 1260 , weight(2.75)|abundance(26)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_3] ],
 ["burgonet_trim", "burgonet_trim", [("burgonet_trim",0)], itp_merchandise| itp_type_head_armor,0, 1380 , weight(2.75)|abundance(18)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate, [], [fac_kingdom_3] ],

 ["classichelm_plume", "classichelm_plume", [("classichelm_plume",0)], itp_merchandise| itp_type_head_armor,0, 1230 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_4] ],
["classichelm_v_2", "classichelm_v_2", [("classichelm_v_2",0)], itp_merchandise| itp_type_head_armor,0, 1260 , weight(2.75)|abundance(19)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_4] ],
["combed_morion", "combed_morion1", [("copy_combed_morion",0)], itp_merchandise| itp_type_head_armor,0, 500 , weight(2.5)|abundance(37)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], we_faction],
["combed_morion_blued", "combed_morion_blued", [("combed_morion_blued",0)], itp_merchandise| itp_type_head_armor,0, 500 , weight(2.75)|abundance(37)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate , [], we_faction],
["flemish_armet", "flemish_armet", [("flemish_armet",0)], itp_merchandise| itp_type_head_armor,0, 1230 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], we_faction ],
["hounskull", "hounskull", [("hounskull",0)], itp_merchandise| itp_type_head_armor,0, 1080 , weight(2.75)|abundance(22)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], we_faction],
["kettlehat", "kettlehat", [("kettlehat",0)], itp_merchandise| itp_type_head_armor,0, 1150 , weight(2.75)|abundance(21)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], we_faction],
["klappvisier", "klappvisier", [("klappvisier",0)], itp_merchandise| itp_type_head_armor,0, 1150 , weight(2.75)|abundance(21)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], we_faction],
["landsknecht_hat_f", "landsknecht_hat_f", [("landsknecht_hat_f",0)], itp_merchandise| itp_type_head_armor,0, 160 , weight(1.75)|abundance(71)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], we_faction],
["landsknecht_hat_g", "landsknecht_hat_g", [("landsknecht_hat_g",0)], itp_merchandise| itp_type_head_armor,0, 160 , weight(1.75)|abundance(71)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], we_faction],
["new_sallet", "new_sallet", [("new_sallet",0)], itp_merchandise| itp_type_head_armor,0, 2670 , weight(3)|abundance(12)|head_armor(60)|body_armor(0)|leg_armor(0)|difficulty(15) ,imodbits_plate, [], [fac_kingdom_3] ],
["open_sallet", "open_sallet", [("open_sallet",0)], itp_merchandise| itp_type_head_armor,0, 500 , weight(2.5)|abundance(37)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate , [], we_faction],
["qsk", "qsk", [("qsk",0)], itp_merchandise| itp_type_head_armor,0, 1150 , weight(2.75)|abundance(21)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_9] ],
["sarg_helm", "sarg_helm", [("sarg_helm",0)], itp_merchandise| itp_type_head_armor,0, 830 , weight(2.5)|abundance(26)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate , [], [fac_kingdom_9] ],
["valsgarde_new", "valsgarde_new", [("valsgarde_new",0)],  itp_type_head_armor,0, 1250 , weight(2.75)|abundance(19)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [],  [fac_kingdom_6]],
["visored_sallet_coif", "visored_sallet_coif", [("visored_sallet_coif",0)], itp_merchandise| itp_type_head_armor,0, 1260 , weight(2.75)|abundance(19)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], we_faction],

["armet_01", "armet_01", [("armet_01",0)], itp_merchandise| itp_type_head_armor,0, 1260 , weight(2.75)|abundance(19)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_4] ],
["armet_02", "armet_02", [("armet_02",0)], itp_merchandise| itp_type_head_armor,0, 1260 , weight(2.75)|abundance(19)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_4] ],
["armet_03", "armet_03", [("armet_03",0)], itp_merchandise| itp_type_head_armor,0, 1260 , weight(2.75)|abundance(19)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_4] ],
["armet_04", "armet_04", [("armet_04",0)], itp_merchandise| itp_type_head_armor,0, 1260 , weight(2.75)|abundance(19)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_4] ],
["bascinet_coif_01", "bascinet_coif_01", [("bascinet_coif_01",0)], itp_merchandise| itp_type_head_armor,0, 500 , weight(2.5)|abundance(37)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_kingdom_8] ],

["hounskull_bascinet_01", "hounskull_bascinet_01", [("hounskull_bascinet_01",0)], itp_merchandise| itp_type_head_armor,0, 1230 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_1] ],
["hounskull_bascinet_02", "hounskull_bascinet_02", [("hounskull_bascinet_02",0)], itp_merchandise| itp_type_head_armor,0, 1230 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_3] ],
["hounskull_bascinet_03", "hounskull_bascinet_03", [("hounskull_bascinet_03",0)], itp_merchandise| itp_type_head_armor,0, 1230 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_3] ],
["hounskull_bascinet_04", "hounskull_bascinet_04", [("hounskull_bascinet_04",0)], itp_merchandise| itp_type_head_armor,0, 1230 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_3] ],
["hounskull_bascinet_05", "hounskull_bascinet_05", [("hounskull_bascinet_05",0)], itp_merchandise| itp_type_head_armor,0, 1230 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_1] ],
["hounskull_bascinet_06", "hounskull_bascinet_06", [("hounskull_bascinet_06",0)], itp_merchandise| itp_type_head_armor,0, 1230 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_3] ],
["hounskull_bascinet_07", "hounskull_bascinet_07", [("hounskull_bascinet_07",0)], itp_merchandise| itp_type_head_armor,0, 1230 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_1] ],

["tournament_helmB", "tournament_helmB", [("tournament_helmB",0)], itp_merchandise| itp_type_head_armor,0, 1260 , weight(2.75)|abundance(19)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_1] ],
["tournament_helmG", "tournament_helmG", [("tournament_helmG",0)], itp_merchandise| itp_type_head_armor,0, 1260 , weight(2.75)|abundance(19)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_7] ],
["tournament_helmR", "tournament_helmR", [("tournament_helmR",0)], itp_merchandise| itp_type_head_armor,0, 1260 , weight(2.75)|abundance(19)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_8] ],
["tournament_helmY", "tournament_helmY", [("tournament_helmY",0)], itp_merchandise| itp_type_head_armor,0, 1260 , weight(2.75)|abundance(19)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_9] ],

["visored_bascinet_02", "visored_bascinet_02", [("visored_bascinet_02",0)], itp_merchandise| itp_type_head_armor,0, 1080 , weight(2.75)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_3] ],

["armet", "armet", [("armet",0)], itp_merchandise| itp_type_head_armor,0, 1300 , weight(2.75)|abundance(19)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(12) ,imodbits_plate , [], [fac_kingdom_5] ],
["beret_a", "beret_a", [("beret_a",0)], itp_merchandise| itp_type_head_armor,0, 200 , weight(2)|abundance(64)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_8] ],
["beret_b", "beret_blue", [("beret_b",0)], itp_merchandise| itp_type_head_armor,0, 200 , weight(2)|abundance(64)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_8] ],
["beret_c", "beret_c", [("beret_c",0)], itp_merchandise| itp_type_head_armor,0, 200 , weight(2)|abundance(64)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_8] ],
["blck_reytar_sholom", "blck_reytar_sholom", [("blck_reytar_sholom",0)], itp_merchandise| itp_type_head_armor,0, 1150 , weight(2.75)|abundance(21)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_5] ],
["boyar_sholom", "boyar_sholom", [("boyar_sholom",0)], itp_merchandise| itp_type_head_armor,0, 1190 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_2] ],
["gorshok", "gorshok", [("gorshok",0)], itp_merchandise| itp_type_head_armor,0, 610 , weight(2.5)|abundance(32)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_kingdom_13] ],
["husar_sholom", "husar_sholom", [("husar_sholom",0)], itp_merchandise| itp_type_head_armor,0, 1190 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_13] ],

["janissary_hat_a", "janissary_hat_a", [("janissary_hat_a",0)], itp_merchandise| itp_type_head_armor,0, 410 , weight(2.5)|abundance(43)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate , [], [fac_kingdom_6] ],
["janissary_hat_b", "janissary_hat_b", [("janissary_hat_b",0)], itp_merchandise| itp_type_head_armor,0, 410 , weight(2.5)|abundance(43)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate , [], [fac_kingdom_6] ],
["kabasset", "kabasset", [("kabasset",0)], itp_merchandise| itp_type_head_armor,0, 610 , weight(2.5)|abundance(32)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_3] ],

["kalmyk_helmet", "kalmyk_helmet", [("kalmyk_helmet",0)], itp_merchandise| itp_type_head_armor,0, 1150 , weight(2.75)|abundance(21)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_10] ],

["misurka_a", "misurka_a", [("misurka_a",0)], itp_merchandise| itp_type_head_armor,0, 610 , weight(2.5)|abundance(32)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_kingdom_13] ],
["misurka_b", "misurka_b", [("misurka_b",0)], itp_merchandise| itp_type_head_armor,0, 610 , weight(2.5)|abundance(32)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_kingdom_13] ],
["misurka_c", "misurka_c", [("misurka_c",0)], itp_merchandise| itp_type_head_armor,0, 610 , weight(2.5)|abundance(32)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_kingdom_13] ],
["misurka_e", "misurka_e", [("misurka_e",0)], itp_merchandise| itp_type_head_armor,0, 610 , weight(2.5)|abundance(32)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_kingdom_13] ],
["misurka_rich_a", "misurka_rich_a", [("misurka_rich_a",0)], itp_merchandise| itp_type_head_armor,0, 610 , weight(2.5)|abundance(42)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_kingdom_2] ],
["misurka_rich_a", "misurka_rich_a", [("misurka_rich_a",0)], itp_merchandise| itp_type_head_armor,0, 610 , weight(2.5)|abundance(42)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_kingdom_2] ],

["morion_good", "morion_good", [("morion_good",0)], itp_merchandise| itp_type_head_armor,0, 630 , weight(2.5)|abundance(31)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_kingdom_3] ],
["morion_perfect", "morion_perfect", [("morion_perfect",0)], itp_merchandise| itp_type_head_armor,0, 650 , weight(2.5)|abundance(30)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_kingdom_3] ],

["mosk_hat_streletz_a", "mosk_hat_streletz_a", [("mosk_hat_streletz_a",0)], itp_merchandise| itp_type_head_armor,0, 190 , weight(2)|abundance(67)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_2] ],
["mosk_hat_streletz_c", "mosk_hat_streletz_c", [("mosk_hat_streletz_c",0)], itp_merchandise| itp_type_head_armor,0, 190 , weight(2)|abundance(67)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_2] ],
["mosk_shelom", "mosk_shelom", [("mosk_shelom",0)], itp_merchandise| itp_type_head_armor,0, 630 , weight(2.5)|abundance(31)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_kingdom_2] ],
["mosk_shishak", "mosk_shishak", [("mosk_shishak",0)], itp_merchandise| itp_type_head_armor,0, 650 , weight(2.5)|abundance(30)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate , [], [fac_kingdom_2] ],

["pol_hat_good1", "pol_hat_good1", [("pol_hat_good1",0)], itp_merchandise| itp_type_head_armor,0, 210 , weight(2)|abundance(60)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_13] ],
["pol_hat_good2", "pol_hat_good2", [("pol_hat_good2",0)], itp_merchandise| itp_type_head_armor,0, 210 , weight(2)|abundance(60)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_13] ],
["pol_hat_mehova_pero", "pol_hat_mehova_pero", [("pol_hat_mehova_pero",0)], itp_merchandise| itp_type_head_armor,0, 210 , weight(2)|abundance(60)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_13] ],
["pol_hat_pero1", "pol_hat_pero1", [("pol_hat_pero1",0)], itp_merchandise| itp_type_head_armor,0, 210 , weight(2)|abundance(60)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_13] ],
["pol_hat_pero2", "pol_hat_pero2", [("pol_hat_pero2",0)], itp_merchandise| itp_type_head_armor,0, 210 , weight(2)|abundance(60)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_13] ],
["pol_husar_helm_greben", "pol_husar_helm_greben", [("pol_husar_helm_greben",0)], itp_merchandise| itp_type_head_armor,0, 1260 , weight(2.75)|abundance(19)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_13] ],
["reytar_sholom", "reytar_sholom", [("reytar_sholom",0)], itp_merchandise| itp_type_head_armor,0, 1260 , weight(2.75)|abundance(19)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_13] ],

["shapka_jeleznaya", "shapka_jeleznaya", [("shapka_jeleznaya",0)], itp_merchandise| itp_type_head_armor,0, 590 , weight(2.5)|abundance(33)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_13] ],

["shlapa_black_a", "shlapa_black_a", [("shlapa_black_a",0)], itp_merchandise| itp_type_head_armor,0, 170 , weight(2)|abundance(71)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_5] ],
["shlapa_black_b", "shlapa_black_b", [("shlapa_black_b",0)], itp_merchandise| itp_type_head_armor,0, 170 , weight(2)|abundance(71)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_9] ],
["shlapa_black_c", "shlapa_black_c", [("shlapa_black_c",0)], itp_merchandise| itp_type_head_armor,0, 170 , weight(2)|abundance(71)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_5] ],
["shlapa_blue_a", "shlapa_blue_a", [("shlapa_blue_a",0)], itp_merchandise| itp_type_head_armor,0, 170 , weight(2)|abundance(71)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_1] ],
["shlapa_blue_b", "shlapa_blue_b", [("shlapa_blue_b",0)], itp_merchandise| itp_type_head_armor,0, 170 , weight(2)|abundance(71)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_1] ],
["shlapa_blue_c", "shlapa_blue_c", [("shlapa_blue_c",0)], itp_merchandise| itp_type_head_armor,0, 170 , weight(2)|abundance(71)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_5] ],
["shlapa_brown_a", "shlapa_brown_a", [("shlapa_brown_a",0)], itp_merchandise| itp_type_head_armor,0, 170 , weight(2)|abundance(71)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_9] ],
["shlapa_brown_b", "shlapa_brown_b", [("shlapa_brown_b",0)], itp_merchandise| itp_type_head_armor,0, 170 , weight(2)|abundance(71)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_9] ],

["ttr_kolpak", "ttr_kolpak", [("ttr_kolpak",0)], itp_merchandise| itp_type_head_armor,0, 170 , weight(2)|abundance(73)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_22] ],
["ttr_shapka_civil", "ttr_shapka_civil", [("ttr_shapka_civil",0)], itp_merchandise| itp_type_head_armor,0, 160 , weight(2)|abundance(76)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_6] ],
["ttr_shapka_nogayska_a", "ttr_shapka_nogayska_a", [("ttr_shapka_nogayska_a",0)], itp_merchandise| itp_type_head_armor,0, 160 , weight(2)|abundance(79)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_22] ],
["ttr_shapka_nogayska_b", "ttr_shapka_nogayska_b", [("ttr_shapka_nogayska_b",0)], itp_merchandise| itp_type_head_armor,0, 160 , weight(2)|abundance(79)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_10] ],
["ttr_sholom_a", "ttr_sholom_a", [("ttr_sholom_a",0)], itp_merchandise| itp_type_head_armor,0, 1230 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_22] ],
["ttr_sholom_b", "ttr_sholom_b", [("ttr_sholom_b",0)], itp_merchandise| itp_type_head_armor,0, 1230 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_22] ],
["ttr_sholom_good", "ttr_sholom_good", [("ttr_sholom_good",0)], itp_merchandise| itp_type_head_armor,0, 1300 , weight(2.75)|abundance(11)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_6] ],

["turban", "turban", [("turban",0)], itp_merchandise| itp_type_head_armor|itp_civilian,0, 320 , weight(1)|abundance(43)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_6] ],
["ukr_kozak_shapka_b", "ukr_kozak_shapka_b", [("ukr_kozak_shapka_b",0)], itp_merchandise| itp_type_head_armor,0, 160 , weight(2)|abundance(79)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_13] ],
["ukr_prosta_shapka", "ukr_prosta_shapka", [("ukr_prosta_shapka",0)], itp_merchandise| itp_type_head_armor,0, 320 , weight(1)|abundance(43)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_13] ],
["ukr_shapka_s_perom_a", "ukr_shapka_s_perom_a", [("ukr_shapka_s_perom_a",0)], itp_merchandise| itp_type_head_armor,0, 270 , weight(2)|abundance(54)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_13] ],
["ukr_shapka_s_perom_b", "ukr_shapka_s_perom_b", [("ukr_shapka_s_perom_b",0)], itp_merchandise| itp_type_head_armor,0, 270 , weight(2)|abundance(54)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_13] ],
["ukr_shapka_s_misurkoy", "ukr_shapka_s_misurkoy", [("ukr_shapka_s_misurkoy",0)], itp_merchandise| itp_type_head_armor,0, 360 , weight(2.5)|abundance(29)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_kingdom_13] ],

##HolyAce
["qingkuei_huang", "qingkuei_huang", [("qingkuei_huang", 0)], itp_type_head_armor, 0, 520, weight(2.5)|abundance(36)|
difficulty(9)|head_armor(53)|body_armor(0)|leg_armor(0), imodbits_plate, [] ],

["qingkuei_b", "qingkuei_b", [("qingkuei_b", 0)], itp_type_head_armor, 0, 520, weight(2.5)|abundance(36)|difficulty(8)|
head_armor(50)|body_armor(0)|leg_armor(0), imodbits_plate, [] ],

["qingkuei_hong", "qingkuei_hong", [("qingkuei_hong", 0)], itp_type_head_armor, 0, 520, weight(2.5)|abundance(36)|
difficulty(8)|head_armor(50)|body_armor(0)|leg_armor(0), imodbits_plate, [] ],

["qingkuei_lang", "qingkuei_lang", [("qingkuei_lang", 0)], itp_type_head_armor, 0, 520, weight(2.5)|abundance(36)|
difficulty(8)|head_armor(50)|body_armor(0)|leg_armor(0), imodbits_plate, [] ],

["qingkuei_zhuang", "qingkuei_zhuang", [("qingkuei_zhuang", 0)], itp_type_head_armor, 0, 520, weight(2.5)|abundance(36)|
difficulty(9)|head_armor(53)|body_armor(0)|leg_armor(0), imodbits_plate, [] ],

["qingkuei_zb", "qingkuei_zb", [("qingkuei_zb", 0)], itp_type_head_armor, 0, 520, weight(2.5)|abundance(36)|difficulty
(9)|head_armor(53)|body_armor(0)|leg_armor(0), imodbits_plate, [] ],

["qingkuei_zhong", "qingkuei_zhong", [("qingkuei_zhong", 0)], itp_type_head_armor, 0, 520, weight(2.5)|abundance(36)|
difficulty(9)|head_armor(53)|body_armor(0)|leg_armor(0), imodbits_plate, [] ],

["qingkuei_zlang", "qingkuei_zlang", [("qingkuei_zlang", 0)], itp_type_head_armor, 0, 520, weight(2.5)|abundance(36)|
difficulty(9)|head_armor(53)|body_armor(0)|leg_armor(0), imodbits_plate, [] ],

["qingkuei1", "qingkuei1", [("qingkuei1", 0)], itp_type_head_armor|itp_merchandise, 0, 130, weight(1.75)|abundance(83)|
head_armor(18)|body_armor(0)|leg_armor(0), imodbits_plate, [] ],
["qingkuei2", "qingkuei2", [("qingkuei2", 0)], itp_type_head_armor, 0, 690, weight(2.5)|abundance(29)|difficulty(10)|
head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate, [] ],
["qingkuei3", "qingkuei3", [("qingkuei3", 0)], itp_type_head_armor|itp_merchandise, 0, 140, weight(1.75)|abundance(78)|
head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate, [] ],
["qingkuei_jiangjun", "qingkuei_jiangjun", [("qingkuei_jiangjun", 0)], itp_type_head_armor, 0, 690, weight(2.5)|abundance
(29)|difficulty(10)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate, [] ],
["qingkuei_jiangjun_huang", "qingkuei_jiangjun_huang", [("qingkuei_jiangjun_huang", 0)], itp_type_head_armor, 0, 690, weight(2.5)|abundance
(29)|difficulty(10)|head_armor(55)|body_armor(0)|leg_armor(0), imodbits_plate, [] ],
##HolyAce End
["heiliw", "zuqinghat", [("heiliw",0)], itp_merchandise| itp_type_head_armor,0, 140 , weight(1.75)|abundance(78)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_11] ],
["lanli", "zuqinghat1", [("lanli",0)], itp_merchandise| itp_type_head_armor,0, 190 , weight(2)|abundance(68)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_11] ],

["zhentiankui", "zhentiankui", [("zhentiankui",0)], itp_merchandise| itp_type_head_armor,0, 1150 , weight(2.75)|abundance(21)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_11] ],
["zhentian", "zhentian", [("zhentian",0)], itp_merchandise| itp_type_head_armor,0, 800 , weight(2.5)|abundance(25)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_11] ],

["hat-blue", "hat-blue", [("hat-blue",0)], itp_merchandise| itp_type_head_armor,0, 160 , weight(2)|abundance(77)|head_armor(23)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_1] ],
["hat-black", "hat-black", [("hat-black",0)], itp_merchandise| itp_type_head_armor,0, 160 , weight(2)|abundance(77)|head_armor(23)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_3] ],
["hat-yellow", "hat-yellow", [("hat-yellow",0)], itp_merchandise| itp_type_head_armor,0, 160 , weight(2)|abundance(77)|head_armor(23)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_4] ],
["hat-red", "hat-red", [("hat-red",0)], itp_merchandise| itp_type_head_armor,0, 160 , weight(2)|abundance(77)|head_armor(23)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_8] ],

["head_black", "head_black", [("head_black",0)], itp_merchandise| itp_type_head_armor,0, 180 , weight(2)|abundance(70)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate, [], [fac_kingdom_19] ],
["korea_qibingkuei1", "korea_qibingkuei1", [("korea_qibingkuei1",0)], itp_merchandise| itp_type_head_armor,0, 490 , weight(2.5)|abundance(38)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_19] ],
["korea_qibingkuei2", "korea_qibingkuei2", [("korea_qibingkuei2",0)], itp_merchandise| itp_type_head_armor,0, 490 , weight(2.5)|abundance(38)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_19] ],
["korea_qibingkuei3", "korea_qibingkuei3", [("korea_qibingkuei3",0)], itp_merchandise| itp_type_head_armor,0, 490 , weight(2.5)|abundance(38)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_19] ],
["korea_qibingkuei4", "korea_qibingkuei4", [("copy_korea_qibingkuei3",0)], itp_merchandise| itp_type_head_armor,0, 490 , weight(2.5)|abundance(38)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_19] ],

["beige_turban", "beige_turban", [("beige_turban",0)], itp_merchandise| itp_type_head_armor,0, 110 , weight(1.5)|abundance(90)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_17] ],

["white_headress", "white_headress", [("white_headress",0)], itp_merchandise| itp_type_head_armor,0, 120 , weight(1.5)|abundance(78)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_15] ],
["indian_hat_a", "indian_hat_a", [("indian_hat_a",0)], itp_merchandise| itp_type_head_armor,0, 120 , weight(1.5)|abundance(78)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_15] ],
["horns", "horns", [("horns",0)], itp_merchandise| itp_type_head_armor,0, 120 , weight(1.5)|abundance(78)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_15] ],
["feather_b", "feather_b", [("feather_b",0)], itp_merchandise| itp_type_head_armor|itp_doesnt_cover_hair,0, 60 , weight(1.25)|abundance(122)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_15] ],

["helm_vijaynagri_royal", "helm_vijaynagri_royal", [("helm_vijaynagri_royal",0)], itp_merchandise| itp_type_head_armor,0, 520 , weight(2.5)|abundance(36)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_17] ],
["copy_helm_vijaynagri_royal", "helm_vijaynagri_royal2", [("copy_helm_vijaynagri_royal",0)], itp_merchandise| itp_type_head_armor,0, 520 , weight(2.5)|abundance(36)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_17] ],

["kazakh_hat", "kazakh_hat", [("kazakh_hat",0)], itp_merchandise| itp_type_head_armor,0, 160 , weight(1.75)|abundance(71)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_21] ],

["khan_xep_nau", "khan_xep_nau", [("khan_xep_nau",0)], itp_merchandise| itp_type_head_armor,0, 80 , weight(1)|abundance(97)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_18] ],
["khan_xep_xanh", "khan_xep_xanh", [("khan_xep_xanh",0)], itp_merchandise| itp_type_head_armor,0, 80 , weight(1)|abundance(97)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_18] ],
["khan_xep_luc", "khan_xep_luc", [("khan_xep_luc",0)], itp_merchandise| itp_type_head_armor,0, 80 , weight(1)|abundance(97)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_18] ],
["viet_hat", "non_la", [("non_la",0)], itp_merchandise| itp_type_head_armor,0, 150 , weight(1.75)|abundance(77)|head_armor(21)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_18] ],

["turban_helmet_new", "mamluk_helmet_a", [("mamluk_helmet_a",0)], itp_merchandise| itp_type_head_armor,0, 1260 , weight(2.75)|abundance(19)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate, [], [fac_kingdom_6] ],

["coyote_head", "coyote_head", [("coyote_helmet",0)], itp_merchandise| itp_covers_head|itp_type_head_armor,0, 150 , weight(1.75)|abundance(75)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_15] ],
["jaguar_head", "jaguar_head", [("jaguar_helmet",0)], itp_merchandise| itp_covers_head| itp_type_head_armor,0, 150 , weight(1.75)|abundance(75)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_15] ],
["eagle_head", "eagle_head", [("eagle_helmet",0)], itp_merchandise| itp_covers_head| itp_type_head_armor,0, 150 , weight(1.75)|abundance(75)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_15] ],
["cuahchiqueh_helmet", "cuahchiqueh_helmet", [("cuahchiqueh_helmet",0)], itp_merchandise| itp_type_head_armor,0, 150 , weight(1.75)|abundance(75)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_15] ],

 ["shadow_mask", "shadow_mask", [("shadow_mask",0)], itp_merchandise| itp_type_head_armor,0, 150 , weight(2.5)|abundance(73)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_11] ],
["sohei_hood", "sohei_hood", [("sohei_hood",0)], itp_merchandise| itp_type_head_armor,0, 70 , weight(1.5)|abundance(115)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_11] ],
 ["sg_helm_b1", "sg_helm_b", [("sg_helm_b",0)], itp_merchandise| itp_type_head_armor,0, 850 , weight(2.5)|abundance(25)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_18] ],
 ["burma_t1", "burma_t1", [("burma_t1",0)], itp_merchandise|itp_type_head_armor,0, 70 , weight(1.5)|abundance(115)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_18] ],
 ["hat_black1", "hat_black", [("hat_black",0)], itp_merchandise| itp_type_head_armor,0, 130 , weight(1.5)|abundance(76)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_18] ],
 ["kak1", "kak", [("kak",0)], itp_merchandise| itp_type_head_armor,0, 190 , weight(2)|abundance(65)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate, [], [fac_kingdom_18] ],
 ["prato_chapel1", "prato_chapel", [("prato_chapel-de-fer1",0)], itp_merchandise| itp_type_head_armor,0, 520 , weight(2.5)|abundance(36)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_18] ],
 ["morion_spain", "morion_spain", [("morion_spain",0)], itp_merchandise| itp_type_head_armor,0, 1190 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate, [], [fac_kingdom_9] ],

["toutao_black", "toutao_black", [("toutao_black",0)], itp_merchandise| itp_type_head_armor,0, 130 , weight(2)|abundance(84)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_plate, [], [fac_kingdom_19] ],
["turbmail", "turbmail", [("turbmail",0)], itp_merchandise| itp_type_head_armor,0, 500 , weight(2.5)|abundance(37)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate, [], [fac_kingdom_19] ],
["arhelm_norig", "arhelm_norig", [("arhelm_norig",0)], itp_merchandise| itp_type_head_armor,0, 830 , weight(2.5)|abundance(26)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate, [], [fac_kingdom_19] ],

["kabuto_inv", "kabuto", [("kabuto_inv",0)], itp_merchandise| itp_type_head_armor,0, 1460 , weight(2.75)|abundance(18)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_11]],
 ["baijiakui", "baijiakui", [("baijiakui",0)], itp_merchandise| itp_type_head_armor,0, 1190 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate , [], [fac_kingdom_11]],
["heiyuankuiahei", "heiyuankuiahei", [("heiyuankuiahei",0)], itp_merchandise| itp_type_head_armor,0, 1190 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate , [], [fac_kingdom_11]],
["heimiankui", "heimiankui", [("heimiankui",0)], itp_merchandise| itp_type_head_armor,0, 1190 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate , [], [fac_kingdom_11]],
["shoumiankuihei", "shoumiankuihei", [("shoumiankuihei",0)], itp_merchandise| itp_type_head_armor,0, 1260 , weight(2.75)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_11]],
["jiankuihei", "jiankuihei", [("jiankuihei",0)], itp_merchandise| itp_type_head_armor,0, 1230 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate , [], [fac_kingdom_11]],
#red
["jiankuihong", "jiankuihong", [("jiankuihong",0)], itp_merchandise| itp_type_head_armor,0, 1230 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate , [], [fac_kingdom_11]],
["shoumiankuihong", "shoumiankuihong", [("shoumiankuihong",0)], itp_merchandise| itp_type_head_armor,0, 1230 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate , [], [fac_kingdom_11]],
["miankuihong", "miankuihong", [("miankuihong",0)], itp_merchandise| itp_type_head_armor,0, 1190 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate , [], [fac_kingdom_11]],
["heiyuankuiahong", "heiyuankuiahong", [("heiyuankuiahong",0)], itp_merchandise| itp_type_head_armor,0, 1190 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate , [], [fac_kingdom_11]],

["east_asian_helmet1", "east_asian_helmet", [("east_asian_helmet",0)], itp_merchandise| itp_type_head_armor,0, 500 , weight(2.5)|abundance(37)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(6) ,imodbits_plate , [], [fac_kingdom_19]],
["korean_guard_helmet", "korean_guard_helmet", [("korean_guard_helmet",0)], itp_merchandise| itp_type_head_armor,0, 880 , weight(2.5)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate , [], [fac_kingdom_19]],
["korean_infantrie_helmet", "korean_infantrie_helmet", [("korean_infantrie_helmet",0)], itp_merchandise| itp_type_head_armor,0, 430 , weight(2.5)|abundance(42)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_kingdom_19]],
["korean_footman_hat", "korean_footman_hat", [("korean_footman_hat",0)], itp_merchandise| itp_type_head_armor,0, 160 , weight(2)|abundance(78)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_19]],

["yf_hwwg", "yf_empire hat", [("yf_hwwg",0)], itp_merchandise| itp_type_head_armor|itp_civilian,0, 1110 , weight(2)|abundance(1)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_7]],
 ["hanguan3", "Hanguan3 hat", [("Hanguan3",0)], itp_merchandise| itp_type_head_armor|itp_civilian,0, 120 , weight(1.75)|abundance(86)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_7]],
  ["mwushamao01", "MWuShamao01 ", [("MWuShamao01",0)], itp_merchandise| itp_type_head_armor|itp_civilian,0, 170 , weight(1.75)|abundance(69)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_7]],
 ["mwushamao02", "MWuShamao02", [("MWuShamao02",0)], itp_merchandise| itp_type_head_armor|itp_civilian,0, 160 , weight(2)|abundance(77)|head_armor(23)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_7]],
 ["mwushamao03", "MWuShamao with cloth", [("MWuShamao03",0)], itp_merchandise| itp_type_head_armor|itp_civilian,0, 180 , weight(2)|abundance(25)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_7]],
 ["mwushamao04", "huangmao", [("MWuShamao04",0)], itp_merchandise| itp_type_head_armor|itp_civilian,0, 220 , weight(2)|abundance(62)|head_armor(27)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_7]],

  ["china_hat_a", "china_hat_a", [("china_hat_a",0)], itp_merchandise| itp_type_head_armor|itp_civilian,0, 140 , weight(1.75)|abundance(78)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate , [], [fac_kingdom_7]],

["daming_helmet", "DaMing_helmet_officer", [("DaMing_helmet",0)], itp_merchandise| itp_type_head_armor |itp_attach_armature  ,0, 1420 , weight(2.75)|abundance(18)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_cloth , [], [fac_kingdom_7]],
["daming_helmet_01", "DaMing_helmet_01", [("DaMing_helmet_01",0)], itp_merchandise| itp_type_head_armor |itp_attach_armature  ,0, 910 , weight(2.5)|abundance(24)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_cloth , [], [fac_kingdom_7]],
["daming_helmet_02", "DaMing_helmet_02_officer", [("DaMing_helmet_02",0)], itp_merchandise| itp_type_head_armor |itp_attach_armature  ,0, 1220 , weight(2.5)|abundance(19)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_cloth, [], [fac_kingdom_7] ],
["daming_helmet_03", "DaMing_helmet_03_officer", [("DaMing_helmet_03",0)], itp_merchandise| itp_type_head_armor |itp_attach_armature  ,0, 850 , weight(2.5)|abundance(25)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_7]],

["daming_helmet_04", "DaMing_helmet_04", [("DaMing_helmet_04",0)], itp_merchandise| itp_type_head_armor |itp_attach_armature  ,0, 240 , weight(2)|abundance(60)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_7]],
["daming_helmet_05", "DaMing_helmet_05_sol", [("DaMing_helmet_05",0)], itp_merchandise| itp_type_head_armor |itp_attach_armature  ,0, 220 , weight(2)|abundance(63)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], [fac_kingdom_7] ],
["daming_helmet_06", "DaMing_helmet_06_officer", [("DaMing_helmet_06",0)], itp_merchandise| itp_type_head_armor |itp_attach_armature  ,0, 1230 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_cloth , [], [fac_kingdom_7]],
["daming_helmet_07", "DaMing_helmet_07", [("DaMing_helmet_07",0)], itp_merchandise| itp_type_head_armor |itp_attach_armature  ,0, 1090 , weight(2.75)|abundance(22)|head_armor(49)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_cloth, [], [fac_kingdom_7]],

["daming_helmet_08", "DaMing_helmet_08", [("DaMing_helmet_08",0)], itp_merchandise| itp_type_head_armor |itp_attach_armature  ,0, 1190 , weight(2.75)|abundance(20)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_cloth , [], [fac_kingdom_7]],
["daming_helmet_09", "DaMing_helmet_09", [("DaMing_helmet_09",0)], itp_merchandise| itp_type_head_armor |itp_attach_armature  ,0, 310 , weight(2.25)|abundance(53)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_7]],
["daming_helmet_10", "DaMing_helmet_10_officer", [("DaMing_helmet_10",0)], itp_merchandise| itp_type_head_armor |itp_attach_armature  ,0, 520 , weight(2.5)|abundance(36)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth , [], [fac_kingdom_7]],

["daming_helmet_11", "DaMing_helmet_11_red", [("DaMing_helmet_11",0)], itp_merchandise| itp_type_head_armor |itp_attach_armature  ,0, 1320 , weight(2.5)|abundance(18)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_cloth, [], [fac_kingdom_7] ],
["daming_helmet_12", "DaMing_helmet_12_black", [("DaMing_helmet_12",0)], itp_merchandise| itp_type_head_armor |itp_attach_armature  ,0, 1320 , weight(2.5)|abundance(18)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_cloth , [], [fac_kingdom_7]],
["daming_helmet_13", "DaMing_helmet_13_red1", [("DaMing_helmet_13",0)], itp_merchandise| itp_type_head_armor |itp_attach_armature  ,0, 1280 , weight(2.5)|abundance(19)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_cloth , [], [fac_kingdom_7]],
["daming_helmet_14", "DaMing_helmet_14_bl1", [("DaMing_helmet_14",0)], itp_merchandise| itp_type_head_armor |itp_attach_armature  ,0, 1280 , weight(2.5)|abundance(19)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_cloth, [], [fac_kingdom_7] ],

["daming_helmet_15", "DaMing_helmet_15", [("DaMing_helmet_15",0)], itp_merchandise| itp_type_head_armor |itp_attach_armature  ,0, 310 , weight(2.25)|abundance(53)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_7]],
["daming_helmet_16", "DaMing_helmet_16_hat", [("DaMing_helmet_16",0)], itp_merchandise| itp_type_head_armor |itp_attach_armature  ,0, 320 , weight(2)|abundance(48)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_7]],
["daming_helmet_17", "DaMing_helmet_17_hat", [("DaMing_helmet_17",0)], itp_merchandise| itp_type_head_armor |itp_attach_armature  ,0, 320 , weight(2)|abundance(48)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_7]],
["daming_helmet_18", "DaMing_helmet_18_blue", [("DaMing_helmet_18",0)], itp_merchandise| itp_type_head_armor |itp_attach_armature  ,0, 1150 , weight(2.75)|abundance(21)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_cloth , [], [fac_kingdom_7]],
["daming_helmet_19", "DaMing_helmet_19_yellow", [("DaMing_helmet_19",0)], itp_merchandise| itp_type_head_armor |itp_attach_armature  ,0, 1150 , weight(2.75)|abundance(21)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_cloth , [], [fac_kingdom_7]],
["daming_helmet_20", "DaMing_helmet_20_heavy", [("DaMing_helmet_20",0)], itp_merchandise| itp_type_head_armor |itp_attach_armature  ,0, 1700 , weight(3)|abundance(16)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_cloth , [], [fac_kingdom_7]],

["Gnezdovo_helm", "snow_helm", [("inv_gnezdovo_helm_b",0)], itp_merchandise| itp_type_head_armor   ,0, 650 , weight(2.5)|abundance(30)|head_armor(42)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_kingdom_2]],
##from 12th
["mon_h_from12th", "Mongolia Helmet", [("mon_h_from12th",0)], itp_merchandise| itp_type_head_armor |itp_attach_armature  ,0, 850 , weight(2.5)|abundance(25)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_cloth , [], [fac_kingdom_10]],
##from 12th
 #yifeng test inca  fac_kingdom_30
["16ttoukui03", "Incan Headcloth", [("16ttoukui03",0)], itp_merchandise| itp_type_head_armor|itp_civilian,0, 80 , weight(1)|abundance(80)|head_armor(8)|body_armor(0)|leg_armor(0) ,imodbits_plate ,[], [fac_kingdom_30]],
["16ttoukui02", "Incan Soldier Hat", [("16ttoukui02",0)], itp_merchandise| itp_type_head_armor|itp_civilian,0, 140 , weight(1.5)|abundance(80)|head_armor(15)|body_armor(0)|leg_armor(0) ,imodbits_plate ,[], [fac_kingdom_30]],
["16ttoukui01", "Incan General Hat", [("16ttoukui01",0)], itp_merchandise| itp_type_head_armor|itp_civilian,0, 220 , weight(2.5)|abundance(80)|head_armor(28)|body_armor(0)|leg_armor(0) ,imodbits_plate ,[], [fac_kingdom_30]],
["16ttoukui04", "Incan Feather Hat", [("16ttoukui04",0)], itp_merchandise| itp_type_head_armor|itp_civilian,0, 160 , weight(2)|abundance(80)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_plate ,[], [fac_kingdom_30]],
["16ttoukui05", "Incan Yellow Soldier Hat", [("16ttoukui05",0)], itp_merchandise| itp_type_head_armor|itp_civilian,0, 140 , weight(1.5)|abundance(80)|head_armor(15)|body_armor(0)|leg_armor(0) ,imodbits_plate ,[], [fac_kingdom_30]],
["16ttoukui06", "Incan Yellow Feather Hat", [("16ttoukui06",0)], itp_merchandise| itp_type_head_armor|itp_civilian,0, 160 , weight(2)|abundance(80)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_plate ,[], [fac_kingdom_30]],


 #yifeng helmet end
 
["bascinet", "Bascinet", [("bascinet_avt_new",0)], itp_merchandise|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate,[], we_faction  ],
["bascinet_2", "Bascinet with Aventail", [("bascinet_new_a",0)], itp_merchandise|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ,[], we_faction ],
["bascinet_3", "Bascinet with Nose Guard", [("bascinet_new_b",0)], itp_merchandise|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ,[], we_faction ],
["guard_helmet", "Guard Helmet", [("reinf_helmet_new",0)], itp_merchandise| itp_type_head_armor   ,0, 555 , weight(2.5)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ,[], we_faction ],
["black_helmet", "Black Helmet", [("black_helm",0)], itp_type_head_armor,0, 638 , weight(2.75)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate,[], we_faction  ],
["full_helm", "Full Helm", [("great_helmet_new_b",0)], itp_merchandise| itp_type_head_armor |itp_covers_head ,0, 811 , weight(2.5)|abundance(100)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ,[], we_faction ],
["great_helmet", "Great Helmet", [("great_helmet_new",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 980 , weight(2.75)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ,[], we_faction ],
["winged_great_helmet", "Winged Great Helmet", [("maciejowski_helmet_new",0)], itp_merchandise|itp_type_head_armor|itp_covers_head,0, 1240 , weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate,[], we_faction  ],


#WEAPONS
["wooden_stick",         "Wooden Stick", [("wooden_stick",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 
4 , weight(2.5)|difficulty(0)|spd_rtng(99) | weapon_length(63)|swing_damage(13 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["cudgel",         "Cudgel", [("club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 
4 , weight(2.5)|difficulty(0)|spd_rtng(99) | weapon_length(70)|swing_damage(13 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["hammer",         "Hammer", [("iron_hammer_new",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar, 
7 , weight(2)|difficulty(0)|spd_rtng(100) | weapon_length(55)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["club",         "Club", [("club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 
11 , weight(2.5)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(20 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["winged_mace",         "Flanged Mace", [("flanged_mace",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
122 , weight(3.5)|difficulty(0)|spd_rtng(103) | weapon_length(70)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["spiked_mace",         "Spiked Mace", [("spiked_mace_new",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
180 , weight(3.5)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(28 , blunt) | thrust_damage(0 ,  pierce),imodbits_pick ],
["military_hammer", "Military Hammer", [("military_hammer",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
317 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(70)|swing_damage(31 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["maul",         "Maul", [("maul_b",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down |itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear, 
97 , weight(6)|difficulty(11)|spd_rtng(83) | weapon_length(79)|swing_damage(36 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["sledgehammer", "Sledgehammer", [("maul_c",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear, 
101 , weight(7)|difficulty(12)|spd_rtng(81) | weapon_length(82)|swing_damage(39, blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["warhammer",         "Great Hammer", [("maul_d",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear, 
290 , weight(9)|difficulty(14)|spd_rtng(79) | weapon_length(75)|swing_damage(45 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["pickaxe",         "Pickaxe", [("fighting_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
27 , weight(3)|difficulty(0)|spd_rtng(99) | weapon_length(70)|swing_damage(19 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["spiked_club",         "Spiked Club", [("spiked_club",0)], itp_type_one_handed_wpn|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
83 , weight(3)|difficulty(0)|spd_rtng(97) | weapon_length(70)|swing_damage(21 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["fighting_pick", "Fighting Pick", [("fighting_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
108 , weight(1.0)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(22 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["military_pick", "Military Pick", [("steel_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
280 , weight(1.5)|difficulty(0)|spd_rtng(97) | weapon_length(70)|swing_damage(31 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["morningstar",         "Morningstar", [("mace_morningstar_new",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry|itp_unbalanced, itc_morningstar|itcf_carry_mace_left_hip, 
305 , weight(4.5)|difficulty(13)|spd_rtng(95) | weapon_length(85)|swing_damage(38 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
 #yifeng test inca  fac_kingdom_30
 ["16tchui01",         "Incan Mace", [("16tchui01",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
162 , weight(3)|difficulty(0)|spd_rtng(99) | weapon_length(75)|swing_damage(28 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace, [], [fac_kingdom_30] ],


["sickle",         "Sickle", [("sickle",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver, 
9 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(40)|swing_damage(20 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["cleaver",         "Cleaver", [("cleaver_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver, 
14 , weight(1.5)|difficulty(0)|spd_rtng(103) | weapon_length(35)|swing_damage(24 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["knife",         "Knife", [("peasant_knife_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left, 
18 , weight(0.5)|difficulty(0)|spd_rtng(110) | weapon_length(40)|swing_damage(21 , cut) | thrust_damage(13 ,  pierce),imodbits_sword ],
["butchering_knife", "Butchering Knife", [("khyber_knife_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right, 
23 , weight(0.75)|difficulty(0)|spd_rtng(108) | weapon_length(60)|swing_damage(24 , cut) | thrust_damage(17 ,  pierce),imodbits_sword ],
#yifeng
["dirk", "dirk",[("dirk",0),("dirk_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_dagger|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 183 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(75)|swing_damage(25 , cut) | thrust_damage(19 ,  pierce),imodbits_sword , [], [fac_kingdom_8]],

["bollock_dagger", "Bollock Dagger", [("bollock_dagger",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left, 
 75 , weight(1)|difficulty(0)|spd_rtng(109) | weapon_length(46)|swing_damage(21 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high, [], we_faction ],
["pikeman_dagger", "Pikeman's Dagger", [("pikeman_dagger",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left, 
 64 , weight(1)|difficulty(0)|spd_rtng(108) | weapon_length(41)|swing_damage(23 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high , [], we_faction],
["rondel_dagger", "Rondel Dagger", [("rondel_dagger",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left, 
 91 , weight(1.5)|difficulty(0)|spd_rtng(106) | weapon_length(47)|swing_damage(24 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high , [], we_faction],

  ["mackie_dagger",         "mackie_dagger", [("mackie_dagger",0),("mackie_dagger_scabbard",ixmesh_carry),("mackie_dagger",imodbits_good),("mackie_dagger_scabbard",ixmesh_carry|imodbits_good)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn, 
637 , weight(0.75)|difficulty(0)|spd_rtng(115) | weapon_length(40)|swing_damage(32 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high ],


["dagger",         "Dagger", [("dagger_b",0),("dagger_b_scabbard",ixmesh_carry),("dagger_b",imodbits_good),("dagger_b_scabbard",ixmesh_carry|imodbits_good)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn, 
37 , weight(0.75)|difficulty(0)|spd_rtng(109) | weapon_length(47)|swing_damage(22 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
#["nordic_sword", "Nordic Sword", [("viking_sword",0),("scab_vikingsw", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 142 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(98)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],
#["arming_sword", "Arming Sword", [("b_long_sword",0),("scab_longsw_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 156 , weight(1.5)|difficulty(0)|spd_rtng(101) | weapon_length(100)|swing_damage(25 , cut) | thrust_damage(22 ,  pierce),imodbits_sword ],
#["sword",         "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 148 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(26 , cut) | thrust_damage(23 ,  pierce),imodbits_sword ],
["falchion",         "Falchion", [("falchion_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip, 
105 , weight(2.5)|difficulty(8)|spd_rtng(96) | weapon_length(73)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
#["broadsword",         "Broadsword", [("broadsword",0),("scab_broadsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 122 , weight(2.5)|difficulty(8)|spd_rtng(91) | weapon_length(101)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
#["scimitar",         "Scimitar", [("scimeter",0),("scab_scimeter", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
#108 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["scimitar",         "Scimitar", [("scimitar_a",0),("scab_scimeter_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.5)|difficulty(0)|spd_rtng(101) | weapon_length(97)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["scimitar_b",         "Elite Scimitar", [("scimitar_b",0),("scab_scimeter_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
290 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(103)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["arabian_sword_a",         "Sarranid Sword", [("arabian_sword_a",0),("scab_arabian_sword_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
108 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(26 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["arabian_sword_b",         "Sarranid Arming Sword", [("arabian_sword_b",0),("scab_arabian_sword_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
218 , weight(1.7)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(28 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["sarranid_cavalry_sword",         "Sarranid Cavalry Sword", [("arabian_sword_c",0),("scab_arabian_sword_c", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
310 , weight(1.5)|difficulty(0)|spd_rtng(98) | weapon_length(105)|swing_damage(28 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["arabian_sword_d",         "Sarranid Guard Sword", [("arabian_sword_d",0),("scab_arabian_sword_d", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
420 , weight(1.7)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(30 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],


#["nomad_sabre",         "Nomad Sabre", [("shashqa",0),("scab_shashqa", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 115 , weight(1.75)|difficulty(0)|spd_rtng(101) | weapon_length(100)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
#["bastard_sword", "Bastard Sword", [("bastard_sword",0),("scab_bastardsw", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 279 , weight(2.25)|difficulty(9)|spd_rtng(102) | weapon_length(120)|swing_damage(33 , cut) | thrust_damage(27 ,  pierce),imodbits_sword ],
["great_sword",         "Great Sword", [("b_bastard_sword",0),("scab_bastardsw_b", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
 423 , weight(2.75)|difficulty(10)|spd_rtng(95) | weapon_length(125)|swing_damage(39 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_high ],
["sword_of_war", "Sword of War", [("b_bastard_sword",0),("scab_bastardsw_b", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
 524 , weight(3)|difficulty(11)|spd_rtng(94) | weapon_length(130)|swing_damage(40 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_high ],
["hatchet",         "Hatchet", [("hatchet",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
13 , weight(2)|difficulty(0)|spd_rtng(97) | weapon_length(60)|swing_damage(23 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["hand_axe",         "Hand Axe", [("hatchet",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
24 , weight(2)|difficulty(7)|spd_rtng(95) | weapon_length(75)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["fighting_axe", "Fighting Axe", [("fighting_ax",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 
77 , weight(2.5)|difficulty(9)|spd_rtng(92) | weapon_length(90)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["axe",                 "Axe", [("iron_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 
65 , weight(4)|difficulty(8)|spd_rtng(91) | weapon_length(108)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["voulge",         "Voulge", [("voulge",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 
129 , weight(4.5)|difficulty(8)|spd_rtng(87) | weapon_length(119)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["battle_axe",         "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 
240 , weight(5)|difficulty(9)|spd_rtng(88) | weapon_length(108)|swing_damage(41 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["war_axe",         "War Axe", [("war_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 
264 , weight(5)|difficulty(10)|spd_rtng(86) | weapon_length(110)|swing_damage(43 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["double_axe",         "Double Axe", [("dblhead_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 359 , weight(6.5)|difficulty(12)|spd_rtng(85) | weapon_length(95)|swing_damage(43 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["great_axe",         "Great Axe", [("great_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 415 , weight(7)|difficulty(13)|spd_rtng(82) | weapon_length(120)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

#yifeng two hand sword
["flamberge", "Great_Sword", [("flamberge", 0)], itp_type_two_handed_wpn|itcf_carry_sword_back|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itcf_thrust_polearm|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_horseback_slash_polearm|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback|itcf_parry_forward_polearm|itcf_parry_up_polearm|itcf_parry_right_polearm|itcf_parry_left_polearm, 1500, weight(5)|weapon_length(155)|difficulty(12)|spd_rtng(88)|abundance(100)|swing_damage(40, cut)|thrust_damage(31, pierce), imodbits_sword_high , [], [fac_kingdom_3]],

["khmer_blade", "trammadao", [("tmd", 0),("tmd_scab", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 1200, weight(5)|weapon_length(165)|difficulty(12)|spd_rtng(85)|abundance(100)|swing_damage(45, cut)|thrust_damage(31, pierce), imodbits_sword_high , [], [fac_kingdom_18] ],

["yf_bfhj", "Bafujian", [("yf_bfhj", 0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 3000, weight(5)|weapon_length(145)|difficulty(12)|spd_rtng(91)|abundance(0)|swing_damage(48, cut)|thrust_damage(38, pierce), imodbits_sword_high , [], [fac_kingdom_7] ],

["maquahuitl_two_handed", "maquahuitl_two_handed", [("maquahuitl_two_handed", 0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 1000, weight(5)|weapon_length(145)|difficulty(10)|spd_rtng(91)|abundance(0)|swing_damage(40, blunt)|thrust_damage(25, blunt), imodbits_sword_high , [], [fac_kingdom_15] ],

["danish_greatsword", "Danish Greatsword", [("danish_greatsword",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
 458 , weight(3.0)|difficulty(10)|spd_rtng(96) | weapon_length(114)|swing_damage(42 , cut) | thrust_damage(33 ,  pierce),imodbits_sword_high, [], we_faction ],


 ["daming_guduo",         "DaMing_guduo", [("DaMing_guduo",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear, 
590 , weight(4)|difficulty(0)|spd_rtng(79) | weapon_length(94)|swing_damage(30 , blunt) | thrust_damage(10 ,  pierce),imodbits_mace , [], [fac_kingdom_7]],

 ["summer_military_sword","Summer Military Sword", [("yitiansword_01",0),("yitiansword_01_scab", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
 664 , weight(3.0)|difficulty(10)|spd_rtng(90) | weapon_length(112)|swing_damage(40 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high , [], [fac_kingdom_7]],

 ["mackie_mangler",  "mackie_mangler", [("mackie_mangler",0)], itp_type_two_handed_wpn|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear, 870 , weight(3.25)|difficulty(12)|spd_rtng(75) | weapon_length(187)|swing_damage(42, cut) | thrust_damage(30 ,  pierce),imodbits_polearm , [], [fac_kingdom_8]],
["mackie_morning_star_long",  "mackie_morning_star_long", [("mackie_morning_star_long",0)], itp_type_two_handed_wpn|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear, 570 , weight(3)|difficulty(12)|spd_rtng(75) | weapon_length(120)|swing_damage(35, cut) | thrust_damage(20 ,  pierce),imodbits_polearm , [], [fac_kingdom_8]],
["mackie_pendulum",  "mackie_pendulum", [("mackie_pendulum",0)], itp_type_two_handed_wpn|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff|itcf_carry_spear, 470 , weight(3)|difficulty(10)|spd_rtng(70) | weapon_length(145)|swing_damage(35, cut) | thrust_damage(30 ,  pierce),imodbits_polearm , [], [fac_kingdom_8]],

 ["mackie_celtic_axe",         "celtic_axe", [("mackie_celtic_axe",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 
564 , weight(5)|difficulty(10)|spd_rtng(86) | weapon_length(110)|swing_damage(44 , cut) | thrust_damage(20 ,  pierce),imodbits_axe ],

#two hand sword end

["sword_two_handed_b",         "Two Handed Sword", [("sword_two_handed_b",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
 670 , weight(2.75)|difficulty(10)|spd_rtng(97) | weapon_length(110)|swing_damage(40 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],
["sword_two_handed_a",         "Great Sword", [("sword_two_handed_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
 1123 , weight(2.75)|difficulty(10)|spd_rtng(96) | weapon_length(120)|swing_damage(42 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ],


["khergit_sword_two_handed_a",         "Two Handed Sabre", [("khergit_sword_two_handed_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 523 , weight(2.75)|difficulty(10)|spd_rtng(96) | weapon_length(120)|swing_damage(40 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["khergit_sword_two_handed_b",         "Two Handed Sabre", [("khergit_sword_two_handed_b",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 920 , weight(2.75)|difficulty(10)|spd_rtng(96) | weapon_length(120)|swing_damage(44 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["two_handed_cleaver", "War Cleaver", [("military_cleaver_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 640 , weight(2.75)|difficulty(10)|spd_rtng(93) | weapon_length(120)|swing_damage(45 , cut) | thrust_damage(0 ,  cut),imodbits_sword_high ],
["military_cleaver_b", "Soldier's Cleaver", [("military_cleaver_b",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
 193 , weight(1.5)|difficulty(0)|spd_rtng(96) | weapon_length(95)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["military_cleaver_c", "Military Cleaver", [("military_cleaver_c",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
 263 , weight(1.5)|difficulty(0)|spd_rtng(96) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["military_sickle_a", "Military Sickle", [("military_sickle_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 220 , weight(1.0)|difficulty(9)|spd_rtng(100) | weapon_length(75)|swing_damage(26 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],


["bastard_sword_a", "Bastard Sword", [("bastard_sword_a",0),("bastard_sword_a_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 394 , weight(2.0)|difficulty(9)|spd_rtng(98) | weapon_length(101)|swing_damage(37 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high ],
##yifeng bastard sword
["2h_claymore", "2h_claymore", [("2h_claymore",0)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_back,
 594 , weight(2.0)|difficulty(9)|spd_rtng(98) | weapon_length(101)|swing_damage(35 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high , [], [fac_kingdom_8]],

 ["maquahuitl", "maquahuitl", [("maquahuitl",0)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_back,
 294 , weight(1.5)|difficulty(8)|spd_rtng(95) | weapon_length(105)|swing_damage(33 , blunt) | thrust_damage(19 ,  blunt),imodbits_sword_high , [], [fac_kingdom_15] ],

["broom1", "broom1", [("broom1",0)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_back,
 494 , weight(3.0)|difficulty(9)|spd_rtng(90) | weapon_length(170)|swing_damage(40 , blunt) | thrust_damage(26 ,  blunt),imodbits_sword_high, [], [fac_kingdom_15] ],

 ["longsword", "Longsword", [("longsword_b",0)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip,
 345 , weight(2.0)|difficulty(9)|spd_rtng(97) | weapon_length(100)|swing_damage(36 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high , [], we_faction],

 ["english_longsword", "English Longsword", [("english_longsword",0),("english_longsword_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 370 , weight(2.0)|difficulty(9)|spd_rtng(97) | weapon_length(103)|swing_damage(37 , cut) | thrust_damage(32 ,  pierce),imodbits_sword_high , [], we_faction],
["german_bastard_sword", "German Bastard Sword", [("german_bastard_sword",0),("german_bastard_sword_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 355 , weight(2.0)|difficulty(9)|spd_rtng(97) | weapon_length(107)|swing_damage(36 , cut) | thrust_damage(33 ,  pierce),imodbits_sword_high , [], we_faction],
["crusader_sword", "Crusader's Longsword", [("crusader_sword",0),("crusader_sword_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 310 , weight(2.0)|difficulty(9)|spd_rtng(97) | weapon_length(98)|swing_damage(33 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_high , [], we_faction],
["grosse_messer_b", "Grosse Messer", [("grosse_messer_b",0),("grosse_messer_b_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 185 , weight(2.0)|difficulty(9)|spd_rtng(98) | weapon_length(92)|swing_damage(35 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high , [], we_faction],

  ["mackie_basehuitl", "basehuitl", [("mackie_basehuitl",0)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_back,
 1050 , weight(1.5)|difficulty(8)|spd_rtng(95) | weapon_length(105)|swing_damage(38 , blunt) | thrust_damage(23 ,  blunt),imodbits_sword_high , [], [fac_kingdom_25] ],

 ["mackie_basehuitl_plain", "basehuitl_plain", [("mackie_basehuitl_plain",0)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_back,
 394 , weight(1.5)|difficulty(8)|spd_rtng(95) | weapon_length(105)|swing_damage(34 , blunt) | thrust_damage(19 ,  blunt),imodbits_sword_high , [], [fac_kingdom_25] ],

 ["mackie_bastard", "mackie_bastard", [("mackie_bastard",0)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_back,
 1000 , weight(3)|difficulty(11)|spd_rtng(95) | weapon_length(125)|swing_damage(39 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high, [], we_faction ],

 ["mackie_strange_sword", "mackie_strange_sword", [("mackie_strange_sword",0)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_back,
800 , weight(3)|difficulty(11)|spd_rtng(100) | weapon_length(125)|swing_damage(34 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high ],
 
  ["mackie_kriegsmesser", "mackie_kriegsmesser", [("mackie_kriegsmesser",0)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_back,
700 , weight(2.5)|difficulty(8)|spd_rtng(95) | weapon_length(105)|swing_damage(38 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],

#bastard sword end
 ["bastard_sword_b", "Heavy Bastard Sword", [("bastard_sword_b",0),("bastard_sword_b_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 726 , weight(2.25)|difficulty(9)|spd_rtng(97) | weapon_length(105)|swing_damage(42 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ],

["one_handed_war_axe_a", "One Handed Axe", [("one_handed_war_axe_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 87 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(71)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_battle_axe_a", "One Handed Battle Axe", [("one_handed_battle_axe_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 142 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(73)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_war_axe_b", "One Handed War Axe", [("one_handed_war_axe_b",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 190 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(76)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_battle_axe_b", "One Handed Battle Axe", [("one_handed_battle_axe_b",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 230 , weight(1.75)|difficulty(9)|spd_rtng(98) | weapon_length(72)|swing_damage(36 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_battle_axe_c", "One Handed Battle Axe", [("one_handed_battle_axe_c",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 550 , weight(2.0)|difficulty(9)|spd_rtng(98) | weapon_length(76)|swing_damage(37 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],


["two_handed_axe",         "Two Handed Axe", [("two_handed_battle_axe_a",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 90 , weight(4.5)|difficulty(10)|spd_rtng(96) | weapon_length(90)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["two_handed_battle_axe_2",         "Two Handed War Axe", [("two_handed_battle_axe_b",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 152 , weight(4.5)|difficulty(10)|spd_rtng(96) | weapon_length(92)|swing_damage(44 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["shortened_voulge",         "Shortened Voulge", [("two_handed_battle_axe_c",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 228 , weight(4.5)|difficulty(10)|spd_rtng(92) | weapon_length(100)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["great_axe",         "Great Axe", [("two_handed_battle_axe_e",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 316 , weight(4.5)|difficulty(10)|spd_rtng(94) | weapon_length(96)|swing_damage(47 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["long_axe",         "Long Axe", [("long_axe_a",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_next_item_as_melee|itp_unbalanced|itp_merchandise,itc_staff|itcf_carry_axe_back,
 390 , weight(4.75)|difficulty(10)|spd_rtng(93) | weapon_length(120)|swing_damage(46 , cut) | thrust_damage(19 ,  blunt),imodbits_axe ],
["long_axe_alt",         "Long Axe", [("long_axe_a",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 390 , weight(4.75)|difficulty(10)|spd_rtng(88) | weapon_length(120)|swing_damage(46 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["long_axe_b",         "Long War Axe", [("long_axe_b",0)], itp_type_polearm| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_next_item_as_melee|itp_unbalanced|itp_merchandise, itc_staff|itcf_carry_axe_back,
 510 , weight(5.0)|difficulty(10)|spd_rtng(92) | weapon_length(125)|swing_damage(50 , cut) | thrust_damage(18 ,  blunt),imodbits_axe ],
["long_axe_b_alt",         "Long War Axe", [("long_axe_b",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 510 , weight(5.0)|difficulty(10)|spd_rtng(87) | weapon_length(125)|swing_damage(50 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["long_axe_c",         "Great Long Axe", [("long_axe_c",0)], itp_type_polearm| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_next_item_as_melee|itp_unbalanced|itp_merchandise, itc_staff|itcf_carry_axe_back,
 660 , weight(5.5)|difficulty(10)|spd_rtng(91) | weapon_length(127)|swing_damage(54 , cut) | thrust_damage(19 ,  blunt),imodbits_axe ],
["long_axe_c_alt",      "Great Long Axe", [("long_axe_c",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 660 , weight(5.5)|difficulty(10)|spd_rtng(85) | weapon_length(127)|swing_damage(54 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

 ["bardiche",         "Bardiche", [("two_handed_battle_axe_d",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 291 , weight(4.75)|difficulty(10)|spd_rtng(91) | weapon_length(102)|swing_damage(47 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["great_bardiche",         "Great Bardiche", [("two_handed_battle_axe_f",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 617 , weight(5.0)|difficulty(10)|spd_rtng(89) | weapon_length(116)|swing_damage(50 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],




["voulge",         "Voulge", [("two_handed_battle_long_axe_a",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_staff,
 120 , weight(3.0)|difficulty(10)|spd_rtng(88) | weapon_length(175)|swing_damage(40 , cut) | thrust_damage(18 ,  pierce),imodbits_axe ],
["long_bardiche",         "Long Bardiche", [("two_handed_battle_long_axe_b",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_staff,
390 , weight(4.75)|difficulty(11)|spd_rtng(89) | weapon_length(140)|swing_damage(48 , cut) | thrust_damage(17 ,  pierce),imodbits_axe ],
["great_long_bardiche",         "Great Long Bardiche", [("two_handed_battle_long_axe_c",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_staff,
 660 , weight(5.0)|difficulty(12)|spd_rtng(88) | weapon_length(155)|swing_damage(50 , cut) | thrust_damage(17 ,  pierce),imodbits_axe ],

 #yifeng polearm
["english_bill",  "English Bill", [("english_bill",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff, 730 , weight(3.25)|difficulty(12)|spd_rtng(75) | weapon_length(167)|swing_damage(44, cut) | thrust_damage(32 ,  pierce),imodbits_polearm , [], [fac_kingdom_8]],
["swiss_halberd",  "Swiss Halberd", [("swiss_halberd",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff, 790 , weight(3)|difficulty(11)|spd_rtng(76) | weapon_length(161)|swing_damage(46, cut) | thrust_damage(34 ,  pierce),imodbits_polearm , [], [fac_kingdom_3]],

["pudao",  "Pudao", [("pudao",0)], itp_type_polearm|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itcf_thrust_polearm|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_horseback_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_horseback_slash_polearm|itcf_parry_forward_polearm|itcf_parry_up_polearm|itcf_parry_right_polearm|itcf_parry_left_polearm,
 564 , weight(3.0)|difficulty(10)|spd_rtng(90) | weapon_length(132)|swing_damage(45 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high , [], [fac_kingdom_7]],
["ptpudao",  "Ptpudao", [("ptpudao",0)], itp_type_polearm|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itcf_thrust_polearm|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_horseback_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_horseback_slash_polearm|itcf_parry_forward_polearm|itcf_parry_up_polearm|itcf_parry_right_polearm|itcf_parry_left_polearm,
 664 , weight(3.0)|difficulty(10)|spd_rtng(90) | weapon_length(132)|swing_damage(45 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high , [], [fac_kingdom_7]], 
["long_pudao", "Long Pudao", [("ch_c",0)], itp_type_polearm|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itcf_thrust_polearm|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_horseback_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_horseback_slash_polearm|itcf_parry_forward_polearm|itcf_parry_up_polearm|itcf_parry_right_polearm|itcf_parry_left_polearm,
 664 , weight(3.0)|difficulty(10)|spd_rtng(90) | weapon_length(180)|swing_damage(45 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high , [], [fac_kingdom_7]],
["cjpudao", "Cjpudao", [("cjpudao",0)], itp_type_polearm|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itcf_thrust_polearm|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_horseback_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_horseback_slash_polearm|itcf_parry_forward_polearm|itcf_parry_up_polearm|itcf_parry_right_polearm|itcf_parry_left_polearm,
 604 , weight(3.0)|difficulty(10)|spd_rtng(90) | weapon_length(180)|swing_damage(44 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high , [], [fac_kingdom_7]], 

##HolyAce
["qing_zhandao_2", "qing_zhandao_2", [("qing_zhandao_2", 0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_crush_through, itcf_thrust_twohanded|itcf_overswing_twohanded|itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_parry_forward_twohanded|itcf_parry_up_twohanded|itcf_parry_right_twohanded|itcf_parry_left_twohanded|itcf_carry_sword_back, 
1704, weight(3)|weapon_length(180)|difficulty(10)|spd_rtng(93)|abundance(100)|swing_damage(44, cut)|thrust_damage(32, pierce), imodbits_sword_high, [] ],
["zrd", "zrd", [("zrd", 0), ("zrd_q", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_crush_through, itcf_thrust_onehanded|itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded|itcf_thrust_twohanded|itcf_overswing_twohanded|itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_parry_forward_twohanded|itcf_parry_up_twohanded|itcf_parry_right_twohanded|itcf_parry_left_twohanded|itcf_show_holster_when_drawn|itcf_carry_sword_left_hip,
2264, weight(2)|weapon_length(110)|difficulty(10)|spd_rtng(103)|abundance(100)|swing_damage(45, cut)|thrust_damage(35, pierce), imodbits_sword_high, [] ],
["tdd_jy", "tdd_jy", [("tdd_jy", 0), ("tdd_jy_q", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_crush_through, itcf_thrust_onehanded|itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded|itcf_thrust_twohanded|itcf_overswing_twohanded|itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_parry_forward_twohanded|itcf_parry_up_twohanded|itcf_parry_right_twohanded|itcf_parry_left_twohanded|itcf_show_holster_when_drawn|itcf_carry_sword_left_hip, 
2564, weight(1.5)|weapon_length(101)|difficulty(10)|spd_rtng(108)|abundance(100)|swing_damage(47, cut)|thrust_damage(37, pierce), imodbits_sword_high, [] ],
["kxzd", "kxzd", [("kxzd", 0), ("kxzd_q", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_crush_through, itcf_overswing_twohanded|itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_parry_forward_twohanded|itcf_parry_up_twohanded|itcf_parry_right_twohanded|itcf_parry_left_twohanded|itcf_show_holster_when_drawn|itcf_carry_sword_back, 
1704, weight(3)|weapon_length(160)|difficulty(10)|spd_rtng(93)|abundance(100)|swing_damage(45, cut)|thrust_damage(0, pierce), imodbits_sword_high, [] ],
["qingdao", "qingdao", [("dao1", 0), ("dao1_q", ixmesh_carry)],  itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
864 , weight(2.0)|difficulty(8)|spd_rtng(102) | weapon_length(97)|swing_damage(35 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high, [], [fac_kingdom_7] ],
["daqinglance",         "banner lance", [("DaQing_lance",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 1020 , weight(3)|difficulty(10)|spd_rtng(72) | weapon_length(315)|swing_damage(22 , blunt) | thrust_damage(25 ,  pierce),imodbits_polearm , [], [fac_kingdom_7]],
#HolyAce End

["summer_long_axe",  "Summer Long Axe", [("ch_b",0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itcf_thrust_polearm|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_horseback_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_horseback_slash_polearm|itcf_parry_forward_polearm|itcf_parry_up_polearm|itcf_parry_right_polearm|itcf_parry_left_polearm,
 420 , weight(3.0)|difficulty(10)|spd_rtng(88) | weapon_length(136)|swing_damage(41 , cut) | thrust_damage(18 ,  pierce),imodbits_axe , [], [fac_kingdom_7]],
["hafted_blade_new", "Hafted Blade", [("ch_a",0)], itp_type_polearm|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itcf_thrust_polearm|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_horseback_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_horseback_slash_polearm|itcf_parry_forward_polearm|itcf_parry_up_polearm|itcf_parry_right_polearm|itcf_parry_left_polearm,
 485 , weight(2.75)|difficulty(0)|spd_rtng(95) | weapon_length(153)|swing_damage(37 , cut) | thrust_damage(25 ,  pierce),imodbits_polearm , [], [fac_kingdom_7]],
["hafted_blade_new_2", "Hafted Blade II", [("jlkspudao",0)], itp_type_polearm|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itcf_thrust_polearm|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_horseback_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_horseback_slash_polearm|itcf_parry_forward_polearm|itcf_parry_up_polearm|itcf_parry_right_polearm|itcf_parry_left_polearm,
 585 , weight(2.75)|difficulty(0)|spd_rtng(95) | weapon_length(183)|swing_damage(38 , cut) | thrust_damage(25 ,  pierce),imodbits_polearm , [], [fac_kingdom_7]], 

 ["longhalberd", "longhalberd", [("longhalberd",0)], itp_type_polearm|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itcf_thrust_polearm|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_horseback_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_horseback_slash_polearm|itcf_parry_forward_polearm|itcf_parry_up_polearm|itcf_parry_right_polearm|itcf_parry_left_polearm,
 664 , weight(3.0)|difficulty(10)|spd_rtng(90) | weapon_length(185)|swing_damage(45 , cut) | thrust_damage(40 ,  pierce),imodbits_sword_high , [], [fac_kingdom_7]],
["longhalberd_01", "longhalberd_01", [("longhalberd_01",0)], itp_type_polearm|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_penalty_with_shield, itcf_thrust_polearm|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_horseback_thrust_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_horseback_slash_polearm|itcf_parry_forward_polearm|itcf_parry_up_polearm|itcf_parry_right_polearm|itcf_parry_left_polearm,
 744 , weight(3.0)|difficulty(10)|spd_rtng(90) | weapon_length(185)|swing_damage(45 , cut) | thrust_damage(40 ,  pierce),imodbits_sword_high , [], [fac_kingdom_7]],

 ["poleaxe_a",  "Poleaxe", [("poleaxe_a",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff,
 750 , weight(3.5)|difficulty(10)|spd_rtng(79) | weapon_length(144)|swing_damage(44, cut) | thrust_damage(41 ,  pierce),imodbits_polearm , [], we_faction],
["elegant_poleaxe",  "Poleaxe", [("elegant_poleaxe",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff,
 765 , weight(3.25)|difficulty(9)|spd_rtng(81) | weapon_length(139)|swing_damage(43, cut) | thrust_damage(39 ,  pierce),imodbits_polearm , [], we_faction],
["german_poleaxe",  "German Poleaxe", [("german_poleaxe",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff,
 755 , weight(3)|difficulty(8)|spd_rtng(82) | weapon_length(128)|swing_damage(42, cut) | thrust_damage(39 ,  pierce),imodbits_polearm , [], we_faction],
["simple_poleaxe",  "Burgundian Poleaxe", [("simple_poleaxe",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff,
 705 , weight(3.25)|difficulty(8)|spd_rtng(80) | weapon_length(135)|swing_damage(44, cut) | thrust_damage(39 ,  pierce),imodbits_polearm , [], we_faction],
["guisarme",  "Guisarme", [("guisarme_a",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff,
 745 , weight(3)|difficulty(11)|spd_rtng(74) | weapon_length(164)|swing_damage(40, pierce) | thrust_damage(38 ,  pierce),imodbits_polearm, [], we_faction ],
["glaive_a",  "Glaive", [("glaive1",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff,
 745 , weight(2.5)|difficulty(9)|spd_rtng(82) | weapon_length(163)|swing_damage(39, cut) | thrust_damage(40 ,  pierce),imodbits_polearm , [], we_faction],
["glaive_b",  "Glaive", [("glaive2",0)],itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff,
 720 , weight(2.25)|difficulty(10)|spd_rtng(80) | weapon_length(170)|swing_damage(38, cut) | thrust_damage(39 ,  pierce),imodbits_polearm , [], we_faction],
["partisan",  "Partisan", [("partisan",0)],itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_two_handed, itc_staff,
 705 , weight(2)|difficulty(10)|spd_rtng(84) | weapon_length(158)|swing_damage(39, cut) | thrust_damage(39 ,  pierce),imodbits_polearm , [], we_faction],





 ["hafted_blade_b",         "Hafted Blade", [("khergit_pike_b",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,
 185 , weight(2.75)|difficulty(0)|spd_rtng(95) | weapon_length(135)|swing_damage(37 , cut) | thrust_damage(20 ,  pierce),imodbits_polearm ],
 ["hafted_blade_a",         "Hafted Blade", [("khergit_pike_a",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,
 350 , weight(3.25)|difficulty(0)|spd_rtng(93) | weapon_length(153)|swing_damage(39 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
###yifeng polearm end

["shortened_military_scythe",         "Shortened Military Scythe", [("two_handed_battle_scythe_a",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 264 , weight(3.0)|difficulty(10)|spd_rtng(90) | weapon_length(112)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["sword_medieval_a", "Sword", [("sword_medieval_a",0),("sword_medieval_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 163 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(27 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],
#["sword_medieval_a_long", "Sword", [("sword_medieval_a_long",0),("sword_medieval_a_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 156 , weight(1.5)|difficulty(0)|spd_rtng(97) | weapon_length(105)|swing_damage(25 , cut) | thrust_damage(22 ,  pierce),imodbits_sword ],
["sword_medieval_b", "Sword", [("sword_medieval_b",0),("sword_medieval_b_scabbard", ixmesh_carry),("sword_rusty_a",imodbit_rusty),("sword_rusty_a_scabbard", ixmesh_carry|imodbit_rusty)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 243 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(28 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high ],
["sword_medieval_b_small", "Short Sword", [("sword_medieval_b_small",0),("sword_medieval_b_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 152 , weight(1)|difficulty(0)|spd_rtng(102) | weapon_length(85)|swing_damage(26, cut) | thrust_damage(24, pierce),imodbits_sword_high ],
["sword_medieval_c", "Arming Sword", [("sword_medieval_c",0),("sword_medieval_c_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 410 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(29 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["sword_medieval_c_small", "Short Arming Sword", [("sword_medieval_c_small",0),("sword_medieval_c_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 243 , weight(1)|difficulty(0)|spd_rtng(103) | weapon_length(86)|swing_damage(26, cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["sword_medieval_c_long", "Arming Sword", [("sword_medieval_c_long",0),("sword_medieval_c_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 480 , weight(1.7)|difficulty(0)|spd_rtng(99) | weapon_length(100)|swing_damage(29 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],
["sword_medieval_d_long", "Long Arming Sword", [("sword_medieval_d_long",0),("sword_medieval_d_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 550 , weight(1.8)|difficulty(0)|spd_rtng(96) | weapon_length(105)|swing_damage(33 , cut) | thrust_damage(28 ,  pierce),imodbits_sword ],
 
#["sword_medieval_d", "sword_medieval_d", [("sword_medieval_d",0),("sword_medieval_d_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 131 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(24 , cut) | thrust_damage(21 ,  pierce),imodbits_sword ],
#["sword_medieval_e", "sword_medieval_e", [("sword_medieval_e",0),("sword_medieval_e_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 131 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(24 , cut) | thrust_damage(21 ,  pierce),imodbits_sword ],

#yifeng one hand
 ["sword_renai", "Renai Sword", [("side_sword",0),("side_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 650 , weight(1.25)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(30 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_high,[],we_faction ],
["milanese_medieval", "Milanese Sword", [("milanese_sword",0),("milanese_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 410 , weight(1.5)|difficulty(0)|spd_rtng(110) | weapon_length(76)|swing_damage(29 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high , [], [fac_kingdom_4]],

 ["china_25huanshou", "Sword Summer", [("china_25huanshou",0),("china_scab_25huanshou", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 563 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(27 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high , [], [fac_kingdom_7]],
["cchina_50huanshou", "Sword Summer", [("china_50huanshou",0),("china_scab_50huanshou", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 463 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(100)|swing_damage(27 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high , [], [fac_kingdom_7]],
["dao_summer", "Dao", [("Txz_dkd",0),("Txz_dkd_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 205 , weight(1.25)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(29 , cut),imodbits_sword_high , [], [fac_kingdom_7]],

 ["highlad_broadsword", "highlad_broadsword", [("highlad_broadsword",0),("highlad_broadsword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 463 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(27 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],

  ["Ming_miaodao","Ming_miaodao", [("Zhonghua_miaodao",0),("Zhonghua_miaodao_qiao", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 1264 , weight(2.0)|difficulty(10)|spd_rtng(105) | weapon_length(97)|swing_damage(40 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high, [], [fac_kingdom_7] ],

 ["ibelin_sword", "ibelin_sword", [("ibelin_sword",0),("ibelin_sword_scab", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 1263 , weight(2.5)|difficulty(10)|spd_rtng(99) | weapon_length(120)|swing_damage(42 , cut) | thrust_damage(32 ,  pierce),imodbits_sword_high ],

 ["turk_sablya_a", "turk_sablya_a", [("turk_sablya_a",0),("turk_sablya_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 584 , weight(1.75)|difficulty(0)|spd_rtng(98) | weapon_length(96)|swing_damage(33 , cut),imodbits_sword_high , [], [fac_kingdom_6] ],
["turk_sablya_b", "turk_sablya_b", [("turk_sablya_b",0),("turk_sablya_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 684 , weight(1.75)|difficulty(0)|spd_rtng(98) | weapon_length(96)|swing_damage(35 , cut),imodbits_sword_high , [], [fac_kingdom_6] ],
["turk_sablya_d", "turk_sablya_d", [("turk_sablya_d",0),("turk_sablya_d_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 784 , weight(1.75)|difficulty(8)|spd_rtng(101) | weapon_length(96)|swing_damage(34 , cut),imodbits_sword_high , [], [fac_kingdom_6] ],

 ["macear",         "macear", [("macear",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 412 , weight(2.75)|difficulty(0)|spd_rtng(98) | weapon_length(95)|swing_damage(30 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace,[], arb_faction ],

 ["espada_eslavona_a", "Espada Eslavona", [("espada_eslavona_a",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
 203 , weight(1.75)|difficulty(0)|spd_rtng(99) | weapon_length(90)|swing_damage(29 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high , [], we_faction],
["espada_eslavona_b", "Espada Eslavona", [("espada_eslavona_b",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
 245 , weight(2.0)|difficulty(0)|spd_rtng(97) | weapon_length(101)|swing_damage(31 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high , [], we_faction],

 ["italian_sword", "Italian Sword", [("italian_sword",0),("italian_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 234 , weight(2.0)|difficulty(8)|spd_rtng(96) | weapon_length(98)|swing_damage(32 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high , [], we_faction],
["longbowman_sword", "Archer's Sword", [("longbowman_sword",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
 165 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(83)|swing_damage(28 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high , [], we_faction],
["italian_falchion", "Italian Falchion", [("italian_falchion",0),("italian_falchion_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 215 , weight(1.5)|difficulty(0)|spd_rtng(104) | weapon_length(73)|swing_damage(32 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high , [], we_faction],
["scottish_sword", "Scottish Sword", [("scottish_sword",0),("scottish_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 170 , weight(1.75)|difficulty(0)|spd_rtng(98) | weapon_length(81)|swing_damage(28 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high , [], we_faction],
["grosse_messer", "Grosse Messer", [("grosse_messer",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
 140 , weight(1.75)|difficulty(0)|spd_rtng(98) | weapon_length(86)|swing_damage(29 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high , [], we_faction],

 ["irish_sword", "Irish Sword", [("irish_sword",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
 200 , weight(2.0)|difficulty(0)|spd_rtng(96) | weapon_length(106)|swing_damage(27 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high , [], we_faction],

 ["mackie_bat_nailed",         "bat_nailed", [("mackie_bat_nailed",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
180 , weight(2.5)|difficulty(0)|spd_rtng(98) | weapon_length(90)|swing_damage(28 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["mackie_beefsplitter01",         "mackie_beefsplitter01", [("mackie_beefsplitter01",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
150 , weight(1)|difficulty(0)|spd_rtng(110) | weapon_length(60)|swing_damage(28 , cut) | thrust_damage(0 ,  pierce),imodbits_pick ],
["mackie_beefsplitter02",         "mackie_beefsplitter02", [("mackie_beefsplitter02",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
150 , weight(1)|difficulty(0)|spd_rtng(110) | weapon_length(60)|swing_damage(28 , cut) | thrust_damage(0 ,  pierce),imodbits_pick ],

["mackie_double_axe",         "double_axe", [("mackie_double_axe",0),("mackie_double_axe_carry", ixmesh_carry)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
180 , weight(2.5)|difficulty(0)|spd_rtng(98) | weapon_length(90)|swing_damage(28 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["mackie_great_lakes_mace",         "great_lakes_mace", [("mackie_great_lakes_mace",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
180 , weight(1)|difficulty(0)|spd_rtng(115) | weapon_length(50)|swing_damage(26 , blunt) | thrust_damage(0 ,  pierce),imodbits_pick, [], [fac_kingdom_15] ],
["mackie_mangler_short",         "mackie_mangler_short", [("mackie_mangler_short",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
380 , weight(1.5)|difficulty(0)|spd_rtng(90) | weapon_length(90)|swing_damage(32 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["mackie_morning_star",         "mackie_morning_star", [("mackie_morning_star",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
180 , weight(1)|difficulty(0)|spd_rtng(115) | weapon_length(50)|swing_damage(28 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["mackie_pendulum_axe",         "mackie_pendulum_axe", [("mackie_pendulum_axe",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
280 , weight(1.5)|difficulty(0)|spd_rtng(105) | weapon_length(50)|swing_damage(30 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["mackie_varangian_axe",         "mackie_varangian_axe", [("mackie_varangian_axe",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
380 , weight(1.5)|difficulty(0)|spd_rtng(105) | weapon_length(70)|swing_damage(32 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["xeno_war_pick01",         "xeno_war_pick01", [("xeno_war_pick01",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
380 , weight(1.5)|difficulty(0)|spd_rtng(105) | weapon_length(70)|swing_damage(32 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["xeno_grom",         "xeno_grom", [("xeno_grom",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
280 , weight(1)|difficulty(0)|spd_rtng(110) | weapon_length(45)|swing_damage(30 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],

["mackie_cutlass", "mackie_cutlass", [("mackie_cutlass",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
 365 , weight(1)|difficulty(0)|spd_rtng(110) | weapon_length(50)|swing_damage(25 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],

 ["mackie_falcata01", "mackie_falcata01", [("mackie_falcata01",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
 465 , weight(1.5)|difficulty(0)|spd_rtng(105) | weapon_length(75)|swing_damage(30 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],

  ["mackie_falchion01", "mackie_falchion01", [("mackie_falchion01",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
 465 , weight(1.5)|difficulty(0)|spd_rtng(105) | weapon_length(75)|swing_damage(29 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],

  ["mackie_falchion03", "mackie_falchion03", [("mackie_falchion03",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
 565 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(75)|swing_damage(30 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],

   ["mackie_short_voulge", "mackie_short_voulge", [("mackie_short_voulge",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
 565 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(70)|swing_damage(30 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],

   ["mackie_godenak", "mackie_godenak", [("mackie_godenak",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
 600 , weight(1.75)|difficulty(0)|spd_rtng(100) | weapon_length(90)|swing_damage(32 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],

    ["mackie_swordcane_blade", "mackie_swordcane_blade", [("mackie_swordcane_blade",0),("mackie_swordcane_scabbard_alt", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip,
 700 , weight(1.75)|difficulty(0)|spd_rtng(100) | weapon_length(125)|swing_damage(25 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ],

  ["daming_yaodao","DaMing_yaodao", [("DaMing_yaodao",0),("DaMing_yaodao_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
410 , weight(1.5)|difficulty(0)|spd_rtng(94) | weapon_length(96)|swing_damage(32 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high , [], [fac_kingdom_7]],

#yifeng one hand end
["sword_viking_1", "Nordic Sword", [("sword_viking_c",0),("sword_viking_c_scabbard ", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 147 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(94)|swing_damage(28 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ] ,
["sword_viking_2", "Nordic Sword", [("sword_viking_b",0),("sword_viking_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 276 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(29 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
["sword_viking_2_small", "Nordic Short Sword", [("sword_viking_b_small",0),("sword_viking_b_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 162 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(85)|swing_damage(28 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
["sword_viking_3", "Nordic War Sword", [("sword_viking_a",0),("sword_viking_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 394 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(30 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
#["sword_viking_a_long", "sword_viking_a_long", [("sword_viking_a_long",0),("sword_viking_a_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 142 , weight(1.5)|difficulty(0)|spd_rtng(97) | weapon_length(105)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],
["sword_viking_3_small", "Nordic Short War Sword", [("sword_viking_a_small",0),("sword_viking_a_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 280 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(86)|swing_damage(29 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
#["sword_viking_c_long", "sword_viking_c_long", [("sword_viking_c_long",0),("sword_viking_c_long_scabbard ", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 142 , weight(1.5)|difficulty(0)|spd_rtng(95) | weapon_length(105)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ] ,

["sword_khergit_1", "Nomad Sabre", [("khergit_sword_b",0),("khergit_sword_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 105 , weight(1.25)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(29 , cut),imodbits_sword_high ],
["sword_khergit_2", "Sabre", [("khergit_sword_c",0),("khergit_sword_c_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 191 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(30 , cut),imodbits_sword_high ],
["sword_khergit_3", "Sabre", [("khergit_sword_a",0),("khergit_sword_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 294 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(98)|swing_damage(31 , cut),imodbits_sword_high ],
["sword_khergit_4", "Heavy Sabre", [("khergit_sword_d",0),("khergit_sword_d_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 384 , weight(1.75)|difficulty(0)|spd_rtng(98) | weapon_length(96)|swing_damage(33 , cut),imodbits_sword_high ],



["mace_1",         "Spiked Club", [("mace_d",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 45 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(70)|swing_damage(19 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_2",         "Knobbed_Mace", [("mace_a",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 98 , weight(2.5)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(21 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_3",         "Spiked Mace", [("mace_c",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 152 , weight(2.75)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(23 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_4",         "Winged_Mace", [("mace_b",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 212 , weight(2.75)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
# Goedendag
 ["club_with_spike_head",  "Spiked Staff", [("mace_e",0)],  itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_wooden_parry, itc_bastardsword|itcf_carry_axe_back,
 200 , weight(2.80)|difficulty(9)|spd_rtng(95) | weapon_length(117)|swing_damage(24 , blunt) | thrust_damage(20 ,  pierce),imodbits_mace ],

["long_spiked_club",         "Long Spiked Club", [("mace_long_c",0)], itp_type_polearm|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back,
 264 , weight(3)|difficulty(0)|spd_rtng(96) | weapon_length(126)|swing_damage(23 , pierce) | thrust_damage(20 ,  blunt),imodbits_mace ],
["long_hafted_knobbed_mace",         "Long Hafted Knobbed Mace", [("mace_long_a",0)], itp_type_polearm| itp_can_knock_down|itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back,
 324 , weight(3)|difficulty(0)|spd_rtng(95) | weapon_length(133)|swing_damage(26 , blunt) | thrust_damage(23 ,  blunt),imodbits_mace ],
["long_hafted_spiked_mace",         "Long Hafted Spiked Mace", [("mace_long_b",0)], itp_type_polearm|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back,
 310 , weight(3)|difficulty(0)|spd_rtng(94) | weapon_length(140)|swing_damage(28 , blunt) | thrust_damage(26 ,  blunt),imodbits_mace ],

["sarranid_two_handed_mace_1",         "Iron Mace", [("mace_long_d",0)], itp_type_two_handed_wpn|itp_can_knock_down|itp_two_handed|itp_merchandise| itp_primary|itp_crush_through|itp_unbalanced, itc_greatsword|itcf_carry_axe_back,
470 , weight(4.5)|difficulty(0)|spd_rtng(90) | weapon_length(95)|swing_damage(35 , blunt) | thrust_damage(22 ,  blunt),imodbits_mace ],


["sarranid_mace_1",         "Iron Mace", [("mace_small_d",0)], itp_type_one_handed_wpn|itp_merchandise|itp_can_knock_down |itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 45 , weight(2.0)|difficulty(0)|spd_rtng(99) | weapon_length(73)|swing_damage(22 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["sarranid_axe_a", "Iron Battle Axe", [("one_handed_battle_axe_g",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 250 , weight(1.65)|difficulty(9)|spd_rtng(97) | weapon_length(71)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["sarranid_axe_b", "Iron War Axe", [("one_handed_battle_axe_h",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 360 , weight(1.75)|difficulty(9)|spd_rtng(97) | weapon_length(71)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["sarranid_two_handed_axe_a",         "Sarranid Battle Axe", [("two_handed_battle_axe_g",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 350 , weight(3.0)|difficulty(10)|spd_rtng(89) | weapon_length(95)|swing_damage(49 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["sarranid_two_handed_axe_b",         "Sarranid War Axe", [("two_handed_battle_axe_h",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 280 , weight(2.50)|difficulty(10)|spd_rtng(90) | weapon_length(90)|swing_damage(46 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],




["scythe",         "Scythe", [("scythe",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear, 43 , weight(2)|difficulty(0)|spd_rtng(97) | weapon_length(182)|swing_damage(30 , cut) | thrust_damage(14 ,  pierce),imodbits_polearm ],
["pitch_fork",         "Pitch Fork", [("pitch_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_staff, 19 , weight(1.5)|difficulty(0)|spd_rtng(87) | weapon_length(154)|swing_damage(16 , blunt) | thrust_damage(22 ,  pierce),imodbits_polearm ],
["military_fork", "Military Fork", [("military_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry,itc_staff, 153 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(135)|swing_damage(15 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["battle_fork",         "Battle Fork", [("battle_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry,itc_staff, 282 , weight(2.2)|difficulty(0)|spd_rtng(90) | weapon_length(144)|swing_damage(15, blunt) | thrust_damage(35 ,  pierce),imodbits_polearm ],
["boar_spear",         "Boar Spear", [("spear",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_staff|itcf_carry_spear, 
76 , weight(1.5)|difficulty(0)|spd_rtng(90) | weapon_length(157)|swing_damage(26 , cut) | thrust_damage(23 ,  pierce),imodbits_polearm ],
#["spear",         "Spear", [("spear",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear, 173 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(17 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],


#["jousting_lance", "Jousting Lance", [("joust_of_peace",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance, 158 , weight(5)|difficulty(0)|spd_rtng(61) | weapon_length(240)|swing_damage(0 , cut) | thrust_damage(17 ,  blunt),imodbits_polearm ],
#["lance",         "Lance", [("pike",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 196 , weight(5)|difficulty(0)|spd_rtng(72) | weapon_length(170)|swing_damage(0 , cut) | thrust_damage(20 ,  pierce),imodbits_polearm ],
#["double_sided_lance", "Double Sided Lance", [("lance_dblhead",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff, 261 , weight(4.0)|difficulty(0)|spd_rtng(95) | weapon_length(128)|swing_damage(25, cut) | thrust_damage(27 ,  pierce),imodbits_polearm ],
#["pike",         "Pike", [("pike",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_spear,
# 212 , weight(6)|difficulty(0)|spd_rtng(77) | weapon_length(167)|swing_damage(0 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
["glaive",         "Glaive", [("glaive_b",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear,
 352 , weight(4.5)|difficulty(0)|spd_rtng(90) | weapon_length(157)|swing_damage(39 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],
["poleaxe",         "Poleaxe", [("pole_ax",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff,
 384 , weight(4.5)|difficulty(13)|spd_rtng(77) | weapon_length(180)|swing_damage(50 , cut) | thrust_damage(15 ,  blunt),imodbits_polearm ],
["polehammer",         "Polehammer", [("pole_hammer",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff,
 169 , weight(7)|difficulty(18)|spd_rtng(50) | weapon_length(126)|swing_damage(50 , blunt) | thrust_damage(35 ,  blunt),imodbits_polearm ],
["staff",         "Staff", [("wooden_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,
 36 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(130)|swing_damage(18 , blunt) | thrust_damage(19 ,  blunt),imodbits_polearm ],
["quarter_staff", "Quarter Staff", [("quarter_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,
 60 , weight(2)|difficulty(0)|spd_rtng(104) | weapon_length(140)|swing_damage(20 , blunt) | thrust_damage(20 ,  blunt),imodbits_polearm ],
["iron_staff",         "Iron Staff", [("iron_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary, itc_staff|itcf_carry_sword_back,
 202 , weight(2)|difficulty(0)|spd_rtng(97) | weapon_length(140)|swing_damage(25 , blunt) | thrust_damage(26 ,  blunt),imodbits_polearm ],

#["glaive_b",         "Glaive_b", [("glaive_b",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear,
# 352 , weight(4.5)|difficulty(0)|spd_rtng(83) | weapon_length(157)|swing_damage(38 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],


["shortened_spear",         "Shortened Spear", [("spear_g_1-9m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
 53 , weight(2.0)|difficulty(0)|spd_rtng(102) | weapon_length(120)|swing_damage(19 , blunt) | thrust_damage(25 ,  pierce),imodbits_polearm ],
["spear",         "Spear", [("spear_h_2-15m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
 85 , weight(2.25)|difficulty(0)|spd_rtng(98) | weapon_length(135)|swing_damage(20 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],

 #yifeng spear
["summer_spear", "Summer Spear", [("Txz_hyq",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff,
 85 , weight(2.25)|difficulty(0)|spd_rtng(98) | weapon_length(200)|swing_damage(20 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm , [], [fac_kingdom_7]],
["summer_spear_b", "Summer Spear II", [("Txz_slq",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff,
 85 , weight(2.25)|difficulty(0)|spd_rtng(98) | weapon_length(200)|swing_damage(20 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm , [], [fac_kingdom_7]],

  ["tomon",         "tomon", [("tomon",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff,
 185 , weight(2.25)|difficulty(0)|spd_rtng(98) | weapon_length(200)|swing_damage(20 , blunt) | thrust_damage(33 ,  pierce),imodbits_polearm ],


 ["buffalo_lance", "buffalo_lance", [("buffalo_lance",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff,
 185 , weight(2.25)|difficulty(0)|spd_rtng(98) | weapon_length(220)|swing_damage(20 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm , [], [fac_kingdom_15] ],
["ceremonial_lance", "ceremonial_lance", [("ceremonial_lance",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff,
 185 , weight(2.25)|difficulty(0)|spd_rtng(98) | weapon_length(220)|swing_damage(25 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm , [], [fac_kingdom_15] ],
["rusty_spear", "rusty_spear", [("rusty_spear",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff,
 185 , weight(2.25)|difficulty(0)|spd_rtng(98) | weapon_length(220)|swing_damage(25 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm , [], [fac_kingdom_15] ],
 
 ["mackie_tepoztopilli",         "mackie_tepoztopilli", [("mackie_tepoztopilli",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff,
 180 , weight(2.0)|difficulty(0)|spd_rtng(88) | weapon_length(200)|swing_damage(25 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm , [], [fac_kingdom_25] ],
 #yifeng test inca  fac_kingdom_30
 ["16tqiang01",         "Incan Spear", [("16tqiang01",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff,
 230 , weight(2.25)|difficulty(0)|spd_rtng(88) | weapon_length(220)|swing_damage(25 , blunt) | thrust_damage(28 ,  pierce),imodbits_polearm , [], [fac_kingdom_30] ],

#spear end 
["bamboo_spear",         "Bamboo Spear", [("arabian_spear_a_3m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff,
 80 , weight(2.0)|difficulty(0)|spd_rtng(88) | weapon_length(200)|swing_damage(15 , blunt) | thrust_damage(20 ,  pierce),imodbits_polearm ],




["war_spear",         "War Spear", [("spear_i_2-3m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff,
 140 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(150)|swing_damage(20 , blunt) | thrust_damage(27 ,  pierce),imodbits_polearm ],
#TODO:["shortened_spear",         "shortened_spear", [("spear_e_2-1m",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
# 65 , weight(2.0)|difficulty(0)|spd_rtng(98) | weapon_length(110)|swing_damage(17 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
#TODO:["spear_2-4m",         "spear", [("spear_e_2-25m",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
# 67 , weight(2.0)|difficulty(0)|spd_rtng(95) | weapon_length(125)|swing_damage(17 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
["military_scythe",         "Military Scythe", [("spear_e_2-5m",0),("spear_c_2-5m",imodbits_bad)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff,
 155 , weight(2.5)|difficulty(0)|spd_rtng(90) | weapon_length(155)|swing_damage(36 , cut) | thrust_damage(25 ,  pierce),imodbits_polearm ],
#lance begin
 ["light_lance",         "Light Lance", [("spear_b_2-75m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 180 , weight(2.5)|difficulty(0)|spd_rtng(85) | weapon_length(175)|swing_damage(16 , blunt) | thrust_damage(27 ,  pierce),imodbits_polearm ],
["lance",         "Lance", [("spear_d_2-8m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 270 , weight(2.5)|difficulty(0)|spd_rtng(80) | weapon_length(180)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["heavy_lance",         "Heavy Lance", [("spear_f_2-9m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 360 , weight(2.75)|difficulty(10)|spd_rtng(75) | weapon_length(190)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],

 ["daming_ji",         "DaMing_ji", [("DaMing_ji",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 360 , weight(3)|difficulty(10)|spd_rtng(73) | weapon_length(230)|swing_damage(22 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm, [], [fac_kingdom_7] ],
["daming_hupiji",         "DaMing_hupiji", [("DaMing_hupiji",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 410 , weight(3)|difficulty(10)|spd_rtng(74) | weapon_length(230)|swing_damage(22 , blunt) | thrust_damage(27 ,  pierce),imodbits_polearm , [], [fac_kingdom_7]],
["hanchangmao", "hanchangmao", [("hanchangmao", 0),],itp_type_polearm|itp_couchable|itp_penalty_with_shield|itp_primary|itp_wooden_parry|itp_merchandise|itp_offset_lance, itc_spear|itcf_overswing_polearm, 180, weight(2.500000)|abundance(200)|hit_points(16384)|spd_rtng(85)|weapon_length(175)|thrust_damage(27, pierce)|swing_damage(16, blunt), imodbit_cracked|imodbit_balanced|imodbit_bent, [], [fac_kingdom_7] ],

 ["damingbannerlance",         "banner lance", [("DaMing_banner02",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 1020 , weight(3)|difficulty(10)|spd_rtng(72) | weapon_length(290)|swing_damage(22 , blunt) | thrust_damage(25 ,  pierce),imodbits_polearm , [], [fac_kingdom_7]],

 ["jousting_lance", "Jousting Lance", [("joust_of_peace",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance, 158 , weight(5)|difficulty(0)|spd_rtng(61) | weapon_length(240)|swing_damage(0 , cut) | thrust_damage(17 ,  blunt),imodbits_polearm ],
["double_sided_lance", "Double Sided Lance", [("lance_dblhead",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff, 261 , weight(4.0)|difficulty(0)|spd_rtng(95) | weapon_length(128)|swing_damage(25, cut) | thrust_damage(27 ,  pierce),imodbits_polearm ],

["pol_gusar_lansa_b", "pol_gusar_lansa_b", [("pol_gusar_lansa_b", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itcf_thrust_polearm|itcf_overswing_polearm|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback|itcf_parry_forward_polearm|itcf_parry_up_polearm|itcf_parry_right_polearm|itcf_parry_left_polearm, 2380, weight(5)|weapon_length(300)|difficulty(10)|spd_rtng(65)|abundance(100)|swing_damage(20, blunt)|thrust_damage(30, pierce), imodbits_polearm ],

["colour_heavy_lance", "colour_Heavy_Lance", [("lance_3", 0)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_primary|itp_penalty_with_shield|itp_couchable, itcf_thrust_polearm|itcf_overswing_polearm|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback|itcf_parry_forward_polearm|itcf_parry_up_polearm|itcf_parry_right_polearm|itcf_parry_left_polearm, 1380, weight(5)|weapon_length(240)|difficulty(10)|spd_rtng(75)|abundance(100)|swing_damage(20, blunt)|thrust_damage(28, pierce), imodbits_polearm ],

["great_lance",         "Great Lance", [("heavy_lance",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance, 
 910 , weight(5)|difficulty(11)|spd_rtng(55) | weapon_length(240)|swing_damage(0 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],
#lance end
  
  #pike begin
["pike",         "Pike", [("spear_a_3m",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_is_pike|itp_extra_penetration, itc_pike,
 325 , weight(3.0)|difficulty(0)|spd_rtng(81) | weapon_length(245)|swing_damage(16 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["pike560",         "Pike560", [("asd4",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_is_pike|itp_extra_penetration, itc_pike,
 1125 , weight(5.0)|difficulty(10)|spd_rtng(81) | weapon_length(470)|swing_damage(20 , blunt) | thrust_damage(40 ,  pierce),imodbits_polearm ],

 ["daming_sanjiaocha",         "DaMing_sanjiaocha", [("DaMing_sanjiaocha",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_is_pike|itp_extra_penetration, itc_pike,
 1125 , weight(4.0)|difficulty(10)|spd_rtng(81) | weapon_length(224)|swing_damage(20 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm, [], [fac_kingdom_7] ],

 ["pike400",         "Pike400", [("spear_a_3-50m",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_is_pike|itp_extra_penetration, itc_pike,
 625 , weight(5.0)|difficulty(10)|spd_rtng(81) | weapon_length(300)|swing_damage(20 , blunt) | thrust_damage(33 ,  pierce),imodbits_polearm ],
["pike500",         "Pike500", [("spear_a_4m",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_is_pike|itp_extra_penetration, itc_pike,
 925 , weight(5.0)|difficulty(10)|spd_rtng(81) | weapon_length(370)|swing_damage(20 , blunt) | thrust_damage(37 ,  pierce),imodbits_polearm ],
##["spear_e_3-25m",         "Spear_3-25m", [("spear_e_3-25m",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
## 150 , weight(4.5)|difficulty(0)|spd_rtng(81) | weapon_length(225)|swing_damage(19 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],

["ashwood_pike", "Ashwood Pike", [("pike",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_cutting_spear,
 205 , weight(3.5)|difficulty(9)|spd_rtng(90) | weapon_length(170)|swing_damage(19 , blunt) | thrust_damage(29,  pierce),imodbits_polearm ],
["awlpike",    "Awlpike", [("awl_pike_b",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 345 , weight(2.25)|difficulty(0)|spd_rtng(92) | weapon_length(165)|swing_damage(20 , blunt) | thrust_damage(33 ,  pierce),imodbits_polearm ],
["awlpike_long",  "Long Awlpike", [("awl_pike_a",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 385 , weight(2.25)|difficulty(0)|spd_rtng(89) | weapon_length(185)|swing_damage(20 , blunt) | thrust_damage(32 ,  pierce),imodbits_polearm ],
#["awlpike",         "Awlpike", [("pike",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
# 378 , weight(3.5)|difficulty(12)|spd_rtng(92) | weapon_length(160)|swing_damage(20 ,blunt) | thrust_damage(31 ,  pierce),imodbits_polearm ],
["whitebanner",         "whitebanner", [("whitebanner",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_extra_penetration, itc_pike,
 525 , weight(7.0)|difficulty(8)|spd_rtng(81) | weapon_length(350)|swing_damage(20 , blunt) | thrust_damage(22 ,  pierce),imodbits_polearm ],
["yellowbanner",         "yellowbanner", [("yellowbanner",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_extra_penetration, itc_pike,
 525 , weight(7.0)|difficulty(8)|spd_rtng(81) | weapon_length(350)|swing_damage(20 , blunt) | thrust_damage(22 ,  pierce),imodbits_polearm ],
["greenbanner",         "greenbanner", [("greenbanner",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_extra_penetration, itc_pike,
 525 , weight(7.0)|difficulty(8)|spd_rtng(81) | weapon_length(350)|swing_damage(20 , blunt) | thrust_damage(22 ,  pierce),imodbits_polearm ],
["bluebanner",         "bluebanner", [("bluebanner",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_extra_penetration, itc_pike,
 525 , weight(7.0)|difficulty(8)|spd_rtng(81) | weapon_length(350)|swing_damage(20 , blunt) | thrust_damage(22 ,  pierce),imodbits_polearm ],
["redbanner1",         "redbanner1", [("redbanner1",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_extra_penetration, itc_pike,
 525 , weight(7.0)|difficulty(8)|spd_rtng(81) | weapon_length(350)|swing_damage(20 , blunt) | thrust_damage(22 ,  pierce),imodbits_polearm ],
["redbanner",         "redbanner", [("redbanner",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_extra_penetration, itc_pike,
 525 , weight(7.0)|difficulty(8)|spd_rtng(81) | weapon_length(350)|swing_damage(20 , blunt) | thrust_damage(22 ,  pierce),imodbits_polearm ],
#ming flag
["daming_banner01",         "daming_banner01", [("DaMing_banner01",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_extra_penetration, itc_pike,
 525 , weight(7.0)|difficulty(8)|spd_rtng(81) | weapon_length(320)|swing_damage(20 , blunt) | thrust_damage(25 ,  pierce),imodbits_polearm , [], [fac_kingdom_7]],
["daming_banner02",         "daming_banner02", [("DaMing_banner02",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_extra_penetration, itc_pike,
 525 , weight(7.0)|difficulty(8)|spd_rtng(81) | weapon_length(320)|swing_damage(20 , blunt) | thrust_damage(25 ,  pierce),imodbits_polearm , [], [fac_kingdom_7]],
["daming_banner03",         "daming_banner03", [("DaMing_banner03",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_extra_penetration, itc_pike,
 525 , weight(7.0)|difficulty(8)|spd_rtng(81) | weapon_length(320)|swing_damage(20 , blunt) | thrust_damage(25 ,  pierce),imodbits_polearm , [], [fac_kingdom_7]],
["daming_banner04",         "daming_banner04", [("DaMing_banner04",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_extra_penetration, itc_pike,
 525 , weight(7.0)|difficulty(8)|spd_rtng(81) | weapon_length(320)|swing_damage(20 , blunt) | thrust_damage(25 ,  pierce),imodbits_polearm , [], [fac_kingdom_7]],

 ["blackbanner",         "blackbanner", [("blackbanner",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_extra_penetration, itc_pike,
 525 , weight(7.0)|difficulty(8)|spd_rtng(81) | weapon_length(350)|swing_damage(20 , blunt) | thrust_damage(22 ,  pierce),imodbits_polearm ],
["pbanner",         "pbanner", [("pbanner",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_extra_penetration, itc_pike,
 525 , weight(7.0)|difficulty(8)|spd_rtng(81) | weapon_length(350)|swing_damage(20 , blunt) | thrust_damage(22 ,  pierce),imodbits_polearm ],

["bec_de_corbin_a",  "War Hammer", [("bec_de_corbin_a",0)],itp_type_two_handed_wpn|itcf_carry_sword_back|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary|itp_bonus_against_shield, itcf_thrust_polearm|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_horseback_slash_polearm|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback|itcf_parry_forward_polearm|itcf_parry_up_polearm|itcf_parry_right_polearm|itcf_parry_left_polearm,
 425 , weight(3.0)|difficulty(0)|spd_rtng(81) | weapon_length(120)|swing_damage(38, blunt) | thrust_damage(38 ,  pierce),imodbits_polearm ],



# SHIELDS

["wooden_shield", "Wooden Shield", [("shield_round_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
##["wooden_shield", "Wooden Shield", [("shield_round_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield,

#yifeng shield
["red_lion_shield_cav", "Red Lion Knightly Shield",   [("shb1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  400 , weight(2.6)|hit_points(350)|body_armor(22)|spd_rtng(110)|shield_width(32)|shield_height(55),imodbits_shield,[], we_faction],
["volencia_lion_round_shield", "Volencia Lion Round Shield", [("shb2",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  480 , weight(4)|hit_points(380)|body_armor(23)|spd_rtng(90)|shield_width(70),imodbits_shield ,[], we_faction],
["red_shield_kite", "Red Kite Shield",   [("red_shield_kite" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
303 , weight(2)|hit_points(165)|body_armor(8)|spd_rtng(96)|shield_width(36)|shield_height(70),imodbits_shield,[], we_faction],
["new_round_shield", "Summer Round Shield", [("mongol_small_round_01",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  140 , weight(4)|hit_points(330)|body_armor(16)|spd_rtng(90)|shield_width(40),imodbits_shield , [], [fac_kingdom_7]],
["new_round_shield_b", "Summer Round Shield II ", [("mongol_small_round_02",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  450 , weight(4)|hit_points(330)|body_armor(22)|spd_rtng(90)|shield_width(40),imodbits_shield , [], [fac_kingdom_7]],

["s_h1", "Improved Highlander shield1", [("s_h1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  500 , weight(3.5)|hit_points(350)|body_armor(16)|spd_rtng(100)|shield_width(60),imodbits_shield , [], [fac_kingdom_8]],
 ["s_h1_1", "Improved Highlander shield2", [("s_h1_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  500 , weight(3.5)|hit_points(360)|body_armor(16)|spd_rtng(100)|shield_width(60),imodbits_shield , [], [fac_kingdom_8]],
 ["s_h1_2", "Improved Highlander shield3", [("s_h1_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  500 , weight(3.5)|hit_points(370)|body_armor(16)|spd_rtng(100)|shield_width(60),imodbits_shield , [], [fac_kingdom_8]],
 ["s_h2", "Highlander shield1", [("s_h2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  500 , weight(3.5)|hit_points(300)|body_armor(16)|spd_rtng(100)|shield_width(60),imodbits_shield , [], [fac_kingdom_8]],
 ["s_h2_1", "Highlander shield1", [("s_h2_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  500 , weight(3.5)|hit_points(315)|body_armor(16)|spd_rtng(100)|shield_width(60),imodbits_shield, [], [fac_kingdom_8]],
 ["s_h2_2", "Highlander shield3", [("s_h2_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  500 , weight(3.5)|hit_points(330)|body_armor(16)|spd_rtng(100)|shield_width(60),imodbits_shield , [], [fac_kingdom_8]],

  ["dunpai1", "dunpai1", [("dunpai1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  500 , weight(3.5)|hit_points(360)|body_armor(20)|spd_rtng(100)|shield_width(100),imodbits_shield ,[], we_faction],
["dunpai2", "dunpai2", [("dunpai2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  500 , weight(3.5)|hit_points(360)|body_armor(20)|spd_rtng(100)|shield_width(100),imodbits_shield,[], we_faction ],
["dunpai3", "dunpai3", [("dunpai3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  500 , weight(3.5)|hit_points(360)|body_armor(20)|spd_rtng(100)|shield_width(100),imodbits_shield ,[], we_faction],
["dunpai4", "dunpai4", [("dunpai4",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  500 , weight(3.5)|hit_points(360)|body_armor(20)|spd_rtng(100)|shield_width(100),imodbits_shield ,[], we_faction],
["dunpai5", "dunpai5", [("dunpai5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  500 , weight(3.5)|hit_points(360)|body_armor(20)|spd_rtng(100)|shield_width(100),imodbits_shield ,[], we_faction],
["dunpai6", "dunpai6", [("dunpai6",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  500 , weight(3.5)|hit_points(360)|body_armor(20)|spd_rtng(100)|shield_width(100),imodbits_shield,[], we_faction ],
["dunpai7", "dunpai7", [("dunpai7",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  500 , weight(3.5)|hit_points(360)|body_armor(20)|spd_rtng(100)|shield_width(100),imodbits_shield ,[], we_faction],
["dunpai8", "dunpai8", [("dunpai8",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  500 , weight(3.5)|hit_points(360)|body_armor(20)|spd_rtng(100)|shield_width(100),imodbits_shield ,[], we_faction],

["mingduen", "mingduen",   [("mingduen" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  400 , weight(2.6)|hit_points(350)|body_armor(22)|spd_rtng(110)|shield_width(32)|shield_height(55),imodbits_shield, [], [fac_kingdom_7]],

["star_moon_shield", "star_moon_shield", [("star_moon_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  500 , weight(3.5)|hit_points(360)|body_armor(18)|spd_rtng(100)|shield_width(100),imodbits_shield , [], [fac_kingdom_12] ],

["cavalry_shield_pavise_15", "cavalry_shield_eastE", [("cavalry_shield_pavise_15",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  500 , weight(3.5)|hit_points(360)|body_armor(15)|spd_rtng(100)|shield_width(100),imodbits_shield , [], [fac_kingdom_13] ],
["tarch_a", "tarch_a", [("tarch_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  500 , weight(3.5)|hit_points(360)|body_armor(15)|spd_rtng(100)|shield_width(100),imodbits_shield , [], [fac_kingdom_6] ],
["tarch_b", "tarch_b", [("tarch_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  500 , weight(3.5)|hit_points(360)|body_armor(15)|spd_rtng(100)|shield_width(100),imodbits_shield , [], [fac_kingdom_6] ],

["spear_h_2-15m", "spear_shiled", [("spear_h_2-15m",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield ,  400 , weight(2.5)|hit_points(260)|body_armor(8)|spd_rtng(100)|shield_width(100),imodbits_shield ],

["india_shield_a", "native_shield_a",   [("native_shield_a" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  1000 , weight(2.6)|hit_points(350)|body_armor(22)|spd_rtng(110)|shield_width(32)|shield_height(55),imodbits_shield, [], [fac_kingdom_15] ],

["dal_turkiv", "dal_turkiv",   [("dal_turkiv" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  500 , weight(2.6)|hit_points(350)|body_armor(17)|spd_rtng(110)|shield_width(32)|shield_height(55),imodbits_shield, [], [fac_kingdom_17] ],
["shield_pavisei", "shield_pavisei",   [("shield_pavisei" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,  
510 , weight(4.5)|hit_points(430)|body_armor(17)|spd_rtng(81)|shield_width(43)|shield_height(100),imodbits_shield, [], [fac_kingdom_17] ],

["rundash", "rundash",   [("rundash" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  500 , weight(2.6)|hit_points(450)|body_armor(22)|spd_rtng(110)|shield_width(32)|shield_height(55),imodbits_shield, [], we_faction],

["aztec_shield", "aztec_shield",   [("aztec_shield" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  500 , weight(2.6)|hit_points(350)|body_armor(15)|spd_rtng(110)|shield_width(32)|shield_height(55),imodbits_shield, [], [fac_kingdom_15] ],
["aztec_shield333", "aztec_shield333",   [("aztec_shield333" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  500 , weight(2.6)|hit_points(350)|body_armor(15)|spd_rtng(110)|shield_width(32)|shield_height(55),imodbits_shield, [], [fac_kingdom_15] ],
["aztec_shield3", "aztec_shield3",   [("aztec_shield3" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  500 , weight(2.6)|hit_points(350)|body_armor(15)|spd_rtng(110)|shield_width(32)|shield_height(55),imodbits_shield, [], [fac_kingdom_15] ],
["aztec_shield4", "aztec_shield4",   [("aztec_shield4" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  500 , weight(2.6)|hit_points(350)|body_armor(15)|spd_rtng(110)|shield_width(32)|shield_height(55),imodbits_shield, [], [fac_kingdom_15] ],
["aztec_shield5", "aztec_shield5",   [("aztec_shield5" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  500 , weight(2.6)|hit_points(350)|body_armor(15)|spd_rtng(110)|shield_width(32)|shield_height(55),imodbits_shield, [], [fac_kingdom_15] ],
["aztec_shield6", "aztec_shield6",   [("aztec_shield6" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  500 , weight(2.6)|hit_points(350)|body_armor(15)|spd_rtng(110)|shield_width(32)|shield_height(55),imodbits_shield, [], [fac_kingdom_15] ],
["aztec_shield7", "aztec_shield7",   [("aztec_shield7" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  500 , weight(2.6)|hit_points(350)|body_armor(15)|spd_rtng(110)|shield_width(32)|shield_height(55),imodbits_shield, [], [fac_kingdom_15] ],
["aztec_shield8", "aztec_shield8",   [("aztec_shield8" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  500 , weight(2.6)|hit_points(350)|body_armor(15)|spd_rtng(110)|shield_width(32)|shield_height(55),imodbits_shield, [], [fac_kingdom_15] ],

["khen_rattan1", "khen_rattan",   [("khen_rattan" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  500 , weight(2.6)|hit_points(450)|body_armor(15)|spd_rtng(110)|shield_width(32)|shield_height(55),imodbits_shield, [], [fac_kingdom_18]],

 ["daming_tengpai", "DaMing_tengpai", [("DaMing_tengpai",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  397 , weight(3)|hit_points(360)|body_armor(15)|spd_rtng(61)|shield_width(46),imodbits_shield, [], [fac_kingdom_7]],

#shield



#["round_shield", "Round Shield", [("shield_round_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  64 , weight(2)|hit_points(400)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["nordic_shield", "Nordic Shield", [("shield_round_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  95 , weight(2)|hit_points(440)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
#["kite_shield",         "Kite Shield", [("shield_kite_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["kite_shield_", "Kite Shield", [("shield_kite_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["large_shield", "Large Shield", [("shield_kite_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  165 , weight(2.5)|hit_points(520)|body_armor(1)|spd_rtng(80)|shield_width(92),imodbits_shield ],
#["battle_shield", "Battle Shield", [("shield_kite_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  196 , weight(3)|hit_points(560)|body_armor(1)|spd_rtng(78)|shield_width(94),imodbits_shield ],
["fur_covered_shield",  "Fur Covered Shield", [("shield_kite_m",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  227 , weight(3.5)|hit_points(600)|body_armor(1)|spd_rtng(76)|shield_width(81),imodbits_shield ],
#["heraldric_shield", "Heraldric Shield", [("shield_heraldic",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  301 , weight(3.5)|hit_points(640)|body_armor(1)|spd_rtng(83)|shield_width(65),imodbits_shield ],
#["heater_shield", "Heater Shield", [("shield_heater_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  477 , weight(3.5)|hit_points(710)|body_armor(4)|spd_rtng(80)|shield_width(60),imodbits_shield ],
["steel_shield", "Steel Shield", [("shield_dragon",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  697 , weight(4)|hit_points(700)|body_armor(17)|spd_rtng(61)|shield_width(40),imodbits_shield ],
#["nomad_shield", "Nomad Shield", [("shield_wood_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  12 , weight(2)|hit_points(260)|body_armor(6)|spd_rtng(110)|shield_width(30),imodbits_shield ],

["plate_covered_round_shield", "Plate Covered Round Shield", [("shield_round_e",0)], itp_type_shield, itcf_carry_round_shield,  140 , weight(4)|hit_points(330)|body_armor(16)|spd_rtng(90)|shield_width(40),imodbits_shield ],
["leather_covered_round_shield", "Leather Covered Round Shield", [("shield_round_d",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  80 , weight(2.5)|hit_points(310)|body_armor(8)|spd_rtng(96)|shield_width(40),imodbits_shield ],
["hide_covered_round_shield", "Hide Covered Round Shield", [("shield_round_f",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  40 , weight(2)|hit_points(260)|body_armor(3)|spd_rtng(100)|shield_width(40),imodbits_shield ],

["shield_heater_c", "Heater Shield", [("shield_heater_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  277 , weight(3.5)|hit_points(410)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
#["shield_heater_d", "Heater Shield", [("shield_heater_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  477 , weight(3.5)|hit_points(710)|body_armor(4)|spd_rtng(80)|shield_width(60),imodbits_shield ],

#["shield_kite_g",         "Kite Shield g", [("shield_kite_g",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["shield_kite_h",         "Kite Shield h", [("shield_kite_h",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["shield_kite_i",         "Kite Shield i ", [("shield_kite_i",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["shield_kite_k",         "Kite Shield k", [("shield_kite_k",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],

["norman_shield_1",         "Kite Shield", [("norman_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_2",         "Kite Shield", [("norman_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_3",         "Kite Shield", [("norman_shield_3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_4",         "Kite Shield", [("norman_shield_4",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_5",         "Kite Shield", [("norman_shield_5",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_6",         "Kite Shield", [("norman_shield_6",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_7",         "Kite Shield", [("norman_shield_7",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_8",         "Kite Shield", [("norman_shield_8",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],

["tab_shield_round_a", "Old Round Shield", [("tableau_shield_round_5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
26 , weight(2.5)|hit_points(195)|body_armor(4)|spd_rtng(93)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_5", ":agent_no", ":troop_no")])]],
["tab_shield_round_b", "Plain Round Shield", [("tableau_shield_round_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
65 , weight(3)|hit_points(260)|body_armor(8)|spd_rtng(90)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_3", ":agent_no", ":troop_no")])]],
["tab_shield_round_c", "Round Shield", [("tableau_shield_round_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
105 , weight(3.5)|hit_points(310)|body_armor(12)|spd_rtng(87)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_round_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_round_d", "Heavy Round Shield", [("tableau_shield_round_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
210 , weight(4)|hit_points(350)|body_armor(15)|spd_rtng(84)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_round_e", "Huscarl's Round Shield", [("tableau_shield_round_4",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  
430 , weight(4.5)|hit_points(410)|body_armor(19)|spd_rtng(81)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_4", ":agent_no", ":troop_no")])]],

["tab_shield_kite_a", "Old Kite Shield",   [("tableau_shield_kite_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
33 , weight(2)|hit_points(165)|body_armor(5)|spd_rtng(96)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_kite_b", "Plain Kite Shield",   [("tableau_shield_kite_3" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
70 , weight(2.5)|hit_points(215)|body_armor(10)|spd_rtng(93)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_3", ":agent_no", ":troop_no")])]],
["tab_shield_kite_c", "Kite Shield",   [("tableau_shield_kite_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
156 , weight(3)|hit_points(265)|body_armor(13)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_kite_d", "Heavy Kite Shield",   [("tableau_shield_kite_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
320 , weight(3.5)|hit_points(310)|body_armor(18)|spd_rtng(87)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_kite_cav_a", "Horseman's Kite Shield",   [("tableau_shield_kite_4" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
205 , weight(2)|hit_points(165)|body_armor(14)|spd_rtng(103)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":agent_no", ":troop_no")])]],
["tab_shield_kite_cav_b", "Knightly Kite Shield",   [("tableau_shield_kite_4" ,0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,  
360 , weight(2.5)|hit_points(225)|body_armor(23)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":agent_no", ":troop_no")])]],

["tab_shield_heater_a", "Old Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
36 , weight(2)|hit_points(160)|body_armor(6)|spd_rtng(96)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_b", "Plain Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
74 , weight(2.5)|hit_points(210)|body_armor(11)|spd_rtng(93)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_c", "Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
160 , weight(3)|hit_points(260)|body_armor(14)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_d", "Heavy Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
332 , weight(3.5)|hit_points(305)|body_armor(19)|spd_rtng(87)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_cav_a", "Horseman's Heater Shield",   [("tableau_shield_heater_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
229 , weight(2)|hit_points(160)|body_armor(16)|spd_rtng(103)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_heater_cav_b", "Knightly Heater Shield",   [("tableau_shield_heater_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
390 , weight(2.5)|hit_points(220)|body_armor(23)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":agent_no", ":troop_no")])]],

["tab_shield_pavise_a", "Old Board Shield",   [("tableau_shield_pavise_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,  
60 , weight(3.5)|hit_points(280)|body_armor(4)|spd_rtng(89)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_pavise_b", "Plain Board Shield",   [("tableau_shield_pavise_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,  
114 , weight(4)|hit_points(360)|body_armor(8)|spd_rtng(85)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_pavise_c", "Board Shield",   [("tableau_shield_pavise_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,  
210 , weight(4.5)|hit_points(430)|body_armor(10)|spd_rtng(81)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_pavise_d", "Heavy Board Shield",   [("tableau_shield_pavise_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,  
370 , weight(5)|hit_points(550)|body_armor(14)|spd_rtng(78)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":agent_no", ":troop_no")])]],

["tab_shield_small_round_a", "Plain Cavalry Shield", [("tableau_shield_small_round_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
96 , weight(2)|hit_points(160)|body_armor(8)|spd_rtng(105)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_3", ":agent_no", ":troop_no")])]],
["tab_shield_small_round_b", "Round Cavalry Shield", [("tableau_shield_small_round_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  
195 , weight(2.5)|hit_points(200)|body_armor(14)|spd_rtng(103)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_small_round_c", "Elite Cavalry Shield", [("tableau_shield_small_round_2",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  
370 , weight(3)|hit_points(250)|body_armor(22)|spd_rtng(100)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_2", ":agent_no", ":troop_no")])]],


 #RANGED


#TODO:
["darts",         "Darts", [("dart_b",0),("dart_b_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_right_vertical|itcf_show_holster_when_drawn, 
155 , weight(4)|difficulty(1)|spd_rtng(95) | shoot_speed(28) | thrust_damage(22 ,  pierce)|max_ammo(7)|weapon_length(32),imodbits_thrown ],
["war_darts",         "War Darts", [("dart_a",0),("dart_a_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
285 , weight(5)|difficulty(1)|spd_rtng(93) | shoot_speed(27) | thrust_damage(25 ,  pierce)|max_ammo(7)|weapon_length(45),imodbits_thrown ],

["javelin",         "Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
300, weight(4)|difficulty(1)|spd_rtng(91) | shoot_speed(25) | thrust_damage(34 ,  pierce)|max_ammo(5)|weapon_length(75),imodbits_thrown ],
["javelin_melee",         "Javelin", [("javelin",0)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff, 
300, weight(1)|difficulty(0)|spd_rtng(95) |swing_damage(12, cut)| thrust_damage(14,  pierce)|weapon_length(75),imodbits_polearm ],

["throwing_spears",         "Throwing Spears", [("jarid_new_b",0),("jarid_new_b_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
525 , weight(3)|difficulty(2)|spd_rtng(87) | shoot_speed(22) | thrust_damage(44 ,  pierce)|max_ammo(4)|weapon_length(65),imodbits_thrown ],
["throwing_spear_melee",         "Throwing Spear", [("jarid_new_b",0),("javelins_quiver", ixmesh_carry)],itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff, 
525 , weight(1)|difficulty(1)|spd_rtng(91) | swing_damage(18, cut) | thrust_damage(23 ,  pierce)|weapon_length(75),imodbits_thrown ],

["jarid",         "Jarids", [("jarid_new",0),("jarid_quiver", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
560 , weight(2.75)|difficulty(2)|spd_rtng(89) | shoot_speed(24) | thrust_damage(45 ,  pierce)|max_ammo(5)|weapon_length(65),imodbits_thrown ],
["jarid_melee",         "Jarid", [("jarid_new",0),("jarid_quiver", ixmesh_carry)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff,
560 , weight(1)|difficulty(2)|spd_rtng(93) | swing_damage(16, cut) | thrust_damage(20 ,  pierce)|weapon_length(65),imodbits_thrown ],


#TODO:
#TODO: Heavy throwing Spear
["stones",         "Stones", [("throwing_stone",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_stone, 1 , weight(4)|difficulty(0)|spd_rtng(97) | shoot_speed(30) | thrust_damage(11 ,  blunt)|max_ammo(18)|weapon_length(8),imodbit_large_bag ],
#yifeng
["hawk", "hawk", [("hawk",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
490, weight(5)|difficulty(3)|spd_rtng(98) | shoot_speed(18) | thrust_damage(32,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown_minus_heavy , [], [fac_kingdom_15] ],
["hawkthrow", "hawk", [("hawk",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
490, weight(1)|difficulty(3)|spd_rtng(98) | swing_damage(25,cut)|weapon_length(53),imodbits_thrown_minus_heavy , [], [fac_kingdom_15] ],
["bgtomahawk_throw", "bgtomahawk_throw", [("bgtomahawk_throw",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
490, weight(5)|difficulty(3)|spd_rtng(98) | shoot_speed(18) | thrust_damage(32,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown_minus_heavy , [], [fac_kingdom_15] ],
["bgtomahawk", "bgtomahawk", [("bgtomahawk",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
490, weight(1)|difficulty(3)|spd_rtng(98) | swing_damage(25,cut)|weapon_length(53),imodbits_thrown_minus_heavy, [], [fac_kingdom_15] ],

["grenades", "Grenades", [("metal_grenade",0)],
itp_type_thrown |itp_merchandise|itp_primary, itcf_throw_stone,2500,weight(4)|difficulty(0)|spd_rtng(85) | shoot_speed(30) | thrust_damage(120 ,  blunt)|max_ammo(3)|weapon_length(8),imodbits_none,
[(ti_on_missile_hit, [
    (store_trigger_param_1, ":shooter_agent_no"),
	(init_position, pos51),
	(position_copy_origin, pos51, pos1), # Copy hit position for the script
	(call_script, "script_oim_deliver_granade_damage", ":shooter_agent_no", 150, 5), 
  ])]],

["throwing_knives", "Throwing Knives", [("throwing_knife",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife, 76 , weight(2.5)|difficulty(0)|spd_rtng(121) | shoot_speed(25) | thrust_damage(19 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_thrown ],
["throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife, 193 , weight(2.5)|difficulty(0)|spd_rtng(110) | shoot_speed(24) | thrust_damage(25 ,  cut)|max_ammo(13)|weapon_length(0),imodbits_thrown ],
#TODO: Light Trowing axe, Heavy Throwing Axe
["light_throwing_axes", "Light Throwing Axes", [("francisca",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
360, weight(5)|difficulty(2)|spd_rtng(99) | shoot_speed(18) | thrust_damage(35,cut)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy ],
["light_throwing_axes_melee", "Light Throwing Axe", [("francisca",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
360, weight(1)|difficulty(2)|spd_rtng(99)|weapon_length(53)| swing_damage(26,cut),imodbits_thrown_minus_heavy ],
["throwing_axes", "Throwing Axes", [("throwing_axe_a",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
490, weight(5)|difficulty(3)|spd_rtng(98) | shoot_speed(18) | thrust_damage(39,cut)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy ],
["throwing_axes_melee", "Throwing Axe", [("throwing_axe_a",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
490, weight(1)|difficulty(3)|spd_rtng(98) | swing_damage(29,cut)|weapon_length(53),imodbits_thrown_minus_heavy ],
["heavy_throwing_axes", "Heavy Throwing Axes", [("throwing_axe_b",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
620, weight(5)|difficulty(4)|spd_rtng(97) | shoot_speed(18) | thrust_damage(44,cut)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy ],
["heavy_throwing_axes_melee", "Heavy Throwing Axe", [("throwing_axe_b",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
620, weight(1)|difficulty(4)|spd_rtng(97) | swing_damage(32,cut)|weapon_length(53),imodbits_thrown_minus_heavy ],



["hunting_bow",         "Hunting Bow", [("hunting_bow",0),("hunting_bow_carry",ixmesh_carry)],itp_type_bow |itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 
17 , weight(1)|difficulty(0)|spd_rtng(100) | shoot_speed(52) | thrust_damage(15 ,  pierce),imodbits_bow ],
["short_bow",         "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 
58 , weight(1)|difficulty(1)|spd_rtng(97) | shoot_speed(55) | thrust_damage(18 ,  pierce  ),imodbits_bow ],
["nomad_bow",         "Nomad Bow", [("nomad_bow",0),("nomad_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
164 , weight(1.25)|difficulty(2)|spd_rtng(94) | shoot_speed(56) | thrust_damage(20 ,  pierce),imodbits_bow ],
["long_bow",         "Long Bow", [("long_bow",0),("long_bow_carry",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 
145 , weight(1.75)|difficulty(3)|spd_rtng(79) | shoot_speed(56) | thrust_damage(22 ,  pierce),imodbits_bow ],
["khergit_bow",         "Khergit Bow", [("khergit_bow",0),("khergit_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
269 , weight(1.25)|difficulty(3)|spd_rtng(90) | shoot_speed(57) | thrust_damage(21 ,pierce),imodbits_bow ],
["strong_bow",         "Strong Bow", [("strong_bow",0),("strong_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
437 , weight(1.25)|difficulty(3)|spd_rtng(88) | shoot_speed(58) | thrust_damage(23 ,pierce),imodbit_cracked | imodbit_bent | imodbit_masterwork ],
#yifeng
["new_long_bow",         "Long Bow", [("long_bow5",0),("long_bow5_carry",ixmesh_carry)],itp_type_bow|itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 
1008 , weight(1.5)|difficulty(4)|spd_rtng(80) | shoot_speed(62) | thrust_damage(28 ,pierce),imodbits_bow , [], [fac_kingdom_8]],
["hangong",         "Han Bow", [("hangong",0),("hangong_qiao", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
1037 , weight(1.25)|difficulty(3)|spd_rtng(91) | shoot_speed(60) | thrust_damage(26 ,pierce),imodbit_cracked | imodbit_bent | imodbit_masterwork , [], [fac_kingdom_7]],
["heavy_yumi",         "heavy_yumi", [("heavy_yumi",0),("heavy_yumi",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 
945 , weight(1.75)|difficulty(2)|spd_rtng(79) | shoot_speed(56) | thrust_damage(23 ,  pierce),imodbits_bow, [], [fac_kingdom_11] ],
["daming_bow",         "DaMing_bow", [("DaMing_bow",0),("DaMing_bow_case",ixmesh_carry)],itp_type_bow|itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left, 
428 , weight(1.5)|difficulty(3)|spd_rtng(91) | shoot_speed(60) | thrust_damage(26 ,pierce),imodbits_bow, [], [fac_kingdom_7] ],

["war_bow",         "War Bow", [("war_bow",0),("war_bow_carry",ixmesh_carry)],itp_type_bow|itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 
728 , weight(1.5)|difficulty(4)|spd_rtng(84) | shoot_speed(59) | thrust_damage(25 ,pierce),imodbits_bow ],
["hunting_crossbow", "Hunting Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
22 , weight(2.25)|difficulty(0)|spd_rtng(47) | shoot_speed(50) | thrust_damage(37 ,  pierce)|max_ammo(1),imodbits_crossbow ],
["light_crossbow", "Light Crossbow", [("crossbow_b",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
67 , weight(2.5)|difficulty(8)|spd_rtng(45) | shoot_speed(59) | thrust_damage(44 ,  pierce)|max_ammo(1),imodbits_crossbow ],
["crossbow",         "Crossbow",         [("crossbow_a",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
182 , weight(3)|difficulty(8)|spd_rtng(43) | shoot_speed(66) | thrust_damage(49,pierce)|max_ammo(1),imodbits_crossbow ],
#yifeng
["crossbow_shenbi", "Shengbi Crossbow", [("crossbow_shenbi",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
1000 , weight(3.75)|difficulty(10)|spd_rtng(40) | shoot_speed(68) | thrust_damage(70 ,pierce)|max_ammo(1),imodbits_crossbow , [], [fac_kingdom_7]],
["crossbow_tiaodeng", "Tiaodeng Crossbow", [("crossbow_tiaodeng",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
550 , weight(3)|difficulty(8)|spd_rtng(42) | shoot_speed(70) | thrust_damage(50 ,pierce)|max_ammo(1),imodbits_crossbow , [], [fac_kingdom_7]],

["lander_crossbow", "lander_crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
600 , weight(2.25)|difficulty(10)|spd_rtng(47) | shoot_speed(50) | thrust_damage(60 ,  pierce)|max_ammo(1),imodbits_crossbow ],

["china_cross", "china_cross", [("china_cross",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
2349 , weight(5)|difficulty(10)|spd_rtng(30) | shoot_speed(75) | thrust_damage(55 ,pierce)|max_ammo(10),imodbits_crossbow , [], [fac_kingdom_7] ],

["heavy_crossbow", "Heavy Crossbow", [("crossbow_c",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
349 , weight(3.5)|difficulty(9)|spd_rtng(41) | shoot_speed(68) | thrust_damage(58 ,pierce)|max_ammo(1),imodbits_crossbow ],
["sniper_crossbow", "Siege Crossbow", [("crossbow_c",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
683 , weight(3.75)|difficulty(10)|spd_rtng(37) | shoot_speed(70) | thrust_damage(63 ,pierce)|max_ammo(1),imodbits_crossbow ],

#yifeng musket
["musket_a", "Musket", [("rifle_musket",0),("rifle_musket_copy",ixmesh_carry)], itp_type_musket|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield| itp_ignore_gravity, itcf_shoot_musket|itcf_carry_crossbow_back|itcf_reload_musket, 1020, weight(3.75)|difficulty(0)|spd_rtng(25)|shoot_speed(140)|thrust_damage(70,pierce)|max_ammo(1)|accuracy(85), imodbits_none, 
[(ti_on_weapon_attack,[(play_sound,"snd_pistol_shot"),(position_move_x,pos1,0),(position_move_y,pos1,106),(particle_system_burst,"psys_musket_smoke",pos1,15),(particle_system_burst,"psys_musket_ogon",pos1,30),(particle_system_burst,"psys_musket_svet",pos1,30)])],[] ,we_faction],
#["musket_a_melee",         "musket_a", [("rifle_musket",0)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff|itcf_carry_crossbow_back, 
#200, weight(3.75)|difficulty(0)|spd_rtng(95) |swing_damage(15, blunt)| thrust_damage(8,  blunt)|weapon_length(75),imodbits_polearm ],

["karabin_a", "Karabin", [("karabin_batarey_good",0),("karabin_batarey_good",ixmesh_carry)], itp_type_musket|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield| itp_ignore_gravity, itcf_shoot_musket|itcf_carry_crossbow_back|itcf_reload_musket, 1820, weight(3.75)|difficulty(0)|spd_rtng(25)|shoot_speed(140)|thrust_damage(85,pierce)|max_ammo(1)|accuracy(85), imodbits_none, 
[(ti_on_weapon_attack,[(play_sound,"snd_pistol_shot"),(position_move_x,pos1,0),(position_move_y,pos1,106),(particle_system_burst,"psys_musket_smoke",pos1,15),(particle_system_burst,"psys_musket_ogon",pos1,30),(particle_system_burst,"psys_musket_svet",pos1,30)])],[] ,we_faction],
#["karabin_a_melee",         "karabin_a", [("karabin_batarey_good",0)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff|itcf_carry_crossbow_back, 
#300, weight(3.75)|difficulty(0)|spd_rtng(95) |swing_damage(20, blunt)| thrust_damage(12,  blunt)|weapon_length(75),imodbits_polearm ],

["karabin_b", "Karabin", [("karabin_batarey",0),("karabin_batarey",ixmesh_carry)], itp_type_musket|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield| itp_ignore_gravity, itcf_shoot_musket|itcf_carry_crossbow_back|itcf_reload_musket, 1820, weight(3.75)|difficulty(0)|spd_rtng(25)|shoot_speed(140)|thrust_damage(85,pierce)|max_ammo(1)|accuracy(85), imodbits_none, 
[(ti_on_weapon_attack,[(play_sound,"snd_pistol_shot"),(position_move_x,pos1,0),(position_move_y,pos1,106),(particle_system_burst,"psys_musket_smoke",pos1,15),(particle_system_burst,"psys_musket_ogon",pos1,30),(particle_system_burst,"psys_musket_svet",pos1,30)])],[] ,we_faction],
#["karabin_b_melee",         "karabin_b", [("karabin_batarey",0)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff|itcf_carry_crossbow_back, 
#300, weight(3.75)|difficulty(0)|spd_rtng(95) |swing_damage(20, blunt)| thrust_damage(12,  blunt)|weapon_length(75),imodbits_polearm ],

["3yuan", "3yuan", [("DaMing_sanyanchong",0),("DaMing_sanyanchong",ixmesh_carry)], itp_merchandise|itp_type_musket|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_next_item_as_melee, itcf_shoot_musket|itcf_carry_crossbow_back|itcf_reload_musket, 1820, weight(6.0)|difficulty(0)|spd_rtng(20)|shoot_speed(112)|thrust_damage(60,pierce)|max_ammo(3)|accuracy(65), imodbits_none, 
[(ti_on_weapon_attack,[(play_sound,"snd_pistol_shot"),(position_move_x,pos1,0),(position_move_y,pos1,106),(particle_system_burst,"psys_musket_smoke",pos1,15),(particle_system_burst,"psys_musket_ogon",pos1,30),(particle_system_burst,"psys_musket_svet",pos1,30)])],[fac_kingdom_7] ],
["3yuan_melee",  "DaMing_sanyanchong", [("DaMing_sanyanchong",0),("DaMing_sanyanchong",ixmesh_carry)], itp_type_two_handed_wpn|itp_wooden_parry|itp_two_handed|itp_primary, itcf_thrust_twohanded|itcf_overswing_twohanded|itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_horseback_overswing_right_onehanded|itcf_horseback_overswing_left_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_parry_forward_twohanded|itcf_parry_up_twohanded|itcf_parry_right_twohanded|itcf_parry_left_twohanded|itcf_carry_crossbow_back, 500 , weight(6.0)|difficulty(0)|spd_rtng(83)| weapon_length(110)|swing_damage(38 , blunt)| thrust_damage(22 ,  blunt),imodbits_polearm ],

["fonangji", "fonangji", [("fonangji",0),("fonangji",ixmesh_carry)], itp_type_musket|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_ignore_gravity, itcf_shoot_musket|itcf_carry_crossbow_back|itcf_reload_musket, 1820, weight(2.75)|difficulty(0)|spd_rtng(35)|shoot_speed(140)|thrust_damage(65,pierce)|max_ammo(1)|accuracy(85), imodbits_none, 
[(ti_on_weapon_attack,[(play_sound,"snd_pistol_shot"),(position_move_x,pos1,0),(position_move_y,pos1,106),(particle_system_burst,"psys_musket_smoke",pos1,15),(particle_system_burst,"psys_musket_ogon",pos1,30),(particle_system_burst,"psys_musket_svet",pos1,30)])],[fac_kingdom_7] ],
["Ming_qiang", "Ming_qiang", [("Ming_qiang",0),("Ming_qiang2",ixmesh_carry)], itp_type_musket|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield| itp_ignore_gravity, itcf_shoot_musket|itcf_carry_crossbow_back|itcf_reload_musket, 1820, weight(3.75)|difficulty(0)|spd_rtng(25)|shoot_speed(140)|thrust_damage(85,pierce)|max_ammo(1)|accuracy(85), imodbits_none, 
[(ti_on_weapon_attack,[(play_sound,"snd_pistol_shot"),(position_move_x,pos1,0),(position_move_y,pos1,106),(particle_system_burst,"psys_musket_smoke",pos1,15),(particle_system_burst,"psys_musket_ogon",pos1,30),(particle_system_burst,"psys_musket_svet",pos1,30)])],[fac_kingdom_7] ],
#["Ming_qiang_melee",         "Ming_qiang", [("Ming_qiang",0)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff|itcf_carry_crossbow_back, 
#300, weight(3.75)|difficulty(0)|spd_rtng(95) |swing_damage(20, blunt)| thrust_damage(12,  blunt)|weapon_length(85),imodbits_polearm ],

["daming_niaochong", "DaMing_niaochong", [("DaMing_niaochong",0),("DaMing_niaochong",ixmesh_carry)], itp_type_musket|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_ignore_gravity, itcf_shoot_musket|itcf_carry_crossbow_back|itcf_reload_musket, 1850, weight(3.75)|difficulty(0)|spd_rtng(25)|shoot_speed(140)|thrust_damage(87,pierce)|max_ammo(1)|accuracy(85), imodbits_none, 
[(ti_on_weapon_attack,[(play_sound,"snd_pistol_shot"),(position_move_x,pos1,0),(position_move_y,pos1,106),(particle_system_burst,"psys_musket_smoke",pos1,15),(particle_system_burst,"psys_musket_ogon",pos1,30),(particle_system_burst,"psys_musket_svet",pos1,30)])],[fac_kingdom_7] ],
#["daming_niaochong_melee",         "DaMing_niaochong", [("DaMing_niaochong",0)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff|itcf_carry_crossbow_back, 
#300, weight(3.75)|difficulty(0)|spd_rtng(95) |swing_damage(20, blunt)| thrust_damage(12,  blunt)|weapon_length(90),imodbits_polearm ],

##HolyAce
["niaochong", "niaochong", [("niaochong", 0), ("niaochong", ixmesh_carry)], itp_type_musket|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|
itp_ignore_gravity, itcf_shoot_musket|itcf_carry_crossbow_back|itcf_reload_musket, 1850, weight(3.75)|difficulty(0)|spd_rtng(25)|shoot_speed(140)|accuracy(85)|abundance
(100)|thrust_damage(87, pierce)|max_ammo(1), imodbits_none, 
[(ti_on_weapon_attack,[
(play_sound,"snd_pistol_shot"),
(position_move_x,pos1,0),
(position_move_y,pos1,106),
(particle_system_burst,"psys_musket_smoke",pos1,15),
(particle_system_burst,"psys_musket_ogon",pos1,30),
(particle_system_burst,"psys_musket_svet",pos1,30),
])
], 
],
#["niaochong_melee", "DaMing_niaochong", [("DaMing_niaochong", 0)], itp_type_polearm|itp_wooden_parry|itp_primary, itcf_thrust_polearm|itcf_overswing_polearm|
#itcf_slashright_polearm|itcf_slashleft_polearm|itcf_thrust_onehanded_lance|itcf_thrust_onehanded_lance_horseback|itcf_parry_forward_polearm|itcf_parry_up_polearm|
#itcf_parry_right_polearm|itcf_parry_left_polearm|itcf_carry_crossbow_back, 300, weight(3.75)|weapon_length(90)|difficulty(0)|spd_rtng(95)|abundance(100)|swing_damage(20, 
#lunt)|thrust_damage(12, blunt), imodbits_polearm, [] ],


 ["flintlock_rifle_1", "flintlock_rifle_1", [("flintlock_rifle_1",0),("flintlock_rifle_1",ixmesh_carry)], itp_type_musket|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_ignore_gravity, itcf_shoot_musket|itcf_carry_crossbow_back|itcf_reload_musket, 2820, weight(3.75)|difficulty(0)|spd_rtng(25)|shoot_speed(140)|thrust_damage(95,pierce)|max_ammo(1)|accuracy(85), imodbits_none, 
[(ti_on_weapon_attack,[(play_sound,"snd_pistol_shot"),(position_move_x,pos1,0),(position_move_y,pos1,106),(particle_system_burst,"psys_musket_smoke",pos1,15),(particle_system_burst,"psys_musket_ogon",pos1,30),(particle_system_burst,"psys_musket_svet",pos1,30)])],[] , we_faction],
# ["flintlock_rifle_1_melee",         "flintlock_rifle_1", [("flintlock_rifle_1",0)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff|itcf_carry_crossbow_back, 
#300, weight(3.75)|difficulty(0)|spd_rtng(95) |swing_damage(20, blunt)| thrust_damage(12,  blunt)|weapon_length(120),imodbits_polearm ],

 ["arquebus", "arquebus", [("arquebus",0),("arquebus",ixmesh_carry)], itp_type_musket|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield| itp_ignore_gravity, itcf_shoot_musket|itcf_carry_crossbow_back|itcf_reload_musket, 2620, weight(3.75)|difficulty(0)|spd_rtng(25)|shoot_speed(140)|thrust_damage(95,pierce)|max_ammo(1)|accuracy(90), imodbits_none, 
[(ti_on_weapon_attack,[(play_sound,"snd_pistol_shot"),(position_move_x,pos1,0),(position_move_y,pos1,106),(particle_system_burst,"psys_musket_smoke",pos1,15),(particle_system_burst,"psys_musket_ogon",pos1,30),(particle_system_burst,"psys_musket_svet",pos1,30)])],[], we_faction ],
# ["arquebus_melee",         "arquebus", [("arquebus",0)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff|itcf_carry_crossbow_back, 
#300, weight(3.75)|difficulty(0)|spd_rtng(95) |swing_damage(20, blunt)| thrust_damage(12,  blunt)|weapon_length(90),imodbits_polearm ],

 ["matchlock_1", "matchlock_1", [("matchlock_1",0),("matchlock_1",ixmesh_carry)], itp_type_musket|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_ignore_gravity, itcf_shoot_musket|itcf_carry_crossbow_back|itcf_reload_musket, 2720, weight(3.75)|difficulty(0)|spd_rtng(25)|shoot_speed(140)|thrust_damage(95,pierce)|max_ammo(1)|accuracy(85), imodbits_none, 
[(ti_on_weapon_attack,[(play_sound,"snd_pistol_shot"),(position_move_x,pos1,0),(position_move_y,pos1,106),(particle_system_burst,"psys_musket_smoke",pos1,15),(particle_system_burst,"psys_musket_ogon",pos1,30),(particle_system_burst,"psys_musket_svet",pos1,30)])],[], we_faction ],
#["matchlock_1_melee",         "matchlock_1", [("matchlock_1",0)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff|itcf_carry_crossbow_back, 
#300, weight(3.75)|difficulty(0)|spd_rtng(95) |swing_damage(20, blunt)| thrust_damage(12,  blunt)|weapon_length(90),imodbits_polearm ],

 ["matchlock_2", "matchlock_2", [("matchlock_2",0),("matchlock_2",ixmesh_carry)], itp_type_musket|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield| itp_ignore_gravity, itcf_shoot_musket|itcf_carry_crossbow_back|itcf_reload_musket, 2720, weight(3.75)|difficulty(0)|spd_rtng(25)|shoot_speed(140)|thrust_damage(95,pierce)|max_ammo(1)|accuracy(85), imodbits_none, 
[(ti_on_weapon_attack,[(play_sound,"snd_pistol_shot"),(position_move_x,pos1,0),(position_move_y,pos1,106),(particle_system_burst,"psys_musket_smoke",pos1,15),(particle_system_burst,"psys_musket_ogon",pos1,30),(particle_system_burst,"psys_musket_svet",pos1,30)])],[], we_faction ],
#["matchlock_2_melee",         "matchlock_2", [("matchlock_2",0)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff|itcf_carry_crossbow_back, 
#300, weight(3.75)|difficulty(0)|spd_rtng(95) |swing_damage(20, blunt)| thrust_damage(12,  blunt)|weapon_length(90),imodbits_polearm ],

#musket end

#yifeng pistol
["pistol_a", "Pistol", [("pistol_2stwol",0)], itp_type_pistol |itp_merchandise|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left, 1000 , weight(1.5)|difficulty(0)|spd_rtng(35) | shoot_speed(140) | thrust_damage(57 ,pierce)|max_ammo(2)|accuracy(75),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])],[],we_faction],
["pistol_b", "Pistol", [("pistol_2stwolB",0)], itp_type_pistol |itp_merchandise|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left, 930 , weight(1.5)|difficulty(0)|spd_rtng(35) | shoot_speed(140) | thrust_damage(55 ,pierce)|max_ammo(2)|accuracy(75),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])],[],we_faction],

 ["flintlock_pistol_elite", "elite Flintlock Pistol", [("flintlock_pistol_1",0)], itp_type_pistol |itp_merchandise|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left, 1530 , weight(1.5)|difficulty(0)|spd_rtng(48) | shoot_speed(135) | thrust_damage(68 ,pierce)|max_ammo(1)|accuracy(86),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])],[],we_faction],

["reitern_pistol_4s", "Flintlock Pistol", [("flintlock_pistol",0)], itp_type_pistol |itp_merchandise|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left, 730 , weight(1.5)|difficulty(0)|spd_rtng(50) | shoot_speed(130) | thrust_damage(60 ,pierce)|max_ammo(1)|accuracy(75),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])],[],we_faction],

#pistol
["flintlock_pistol", "Flintlock Pistol", [("flintlock_pistol",0)], itp_type_pistol |itp_merchandise|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left, 230 , weight(1.5)|difficulty(0)|spd_rtng(38) | shoot_speed(160) | thrust_damage(60 ,pierce)|max_ammo(1)|accuracy(65),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])],[] ,we_faction],

 ["torch",         "Torch", [("club",0)], itp_merchandise|itp_type_one_handed_wpn|itp_primary, itc_scimitar, 11 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(30 , blunt) | thrust_damage(0 ,  pierce),imodbits_none,
 [(ti_on_init_item, [(set_position_delta,0,60,0),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 10, 30),
])]],

["lyre",         "Lyre", [("lyre",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],
["lute",         "Lute", [("lute",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],

##["short_sword", "Short Sword",
## [("sword_norman",0),("sword_norman_scabbard", ixmesh_carry),("sword_norman_rusty",imodbit_rusty),("sword_norman_rusty_scabbard", ixmesh_carry|imodbit_rusty)],
## itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 183 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(75)|swing_damage(25 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],

["strange_armor",  "Strange Armor", [("samurai_armor",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs ,0, 1259 , weight(18)|abundance(160)|head_armor(0)|body_armor(38)|leg_armor(19)|difficulty(7) ,imodbits_armor , [], [fac_kingdom_11]],
["strange_boots",  "Strange Boots", [("samurai_boots",0)], itp_merchandise|itp_type_foot_armor | itp_attach_armature,0, 465 , weight(1)|abundance(160)|head_armor(0)|body_armor(0)|leg_armor(21)|difficulty(0) ,imodbits_cloth , [], [fac_kingdom_11]],
["strange_helmet", "Strange Helmet", [("samurai_helmet",0)], itp_merchandise|itp_type_head_armor   ,0, 824 , weight(2)|abundance(160)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate , [], [fac_kingdom_11]],
["strange_sword", "Strange Sword", [("katana",0),("katana_scabbard",ixmesh_carry)], itp_type_two_handed_wpn| itp_merchandise|itp_primary, itc_bastardsword|itcf_carry_katana|itcf_show_holster_when_drawn, 679 , weight(2.0)|difficulty(9)|spd_rtng(108) | weapon_length(95)|swing_damage(40 , cut) | thrust_damage(25 ,  pierce),imodbits_sword , [], [fac_kingdom_11]],
["strange_great_sword",  "Strange Great Sword", [("no_dachi",0),("no_dachi_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_merchandise|itp_primary, itc_nodachi|itcf_carry_sword_back|itcf_show_holster_when_drawn, 920 , weight(3.5)|difficulty(11)|spd_rtng(92) | weapon_length(125)|swing_damage(45 , cut) | thrust_damage(30 ,  pierce),imodbits_axe , [], [fac_kingdom_11]],
["strange_short_sword", "Strange Short Sword", [("wakizashi",0),("wakizashi_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_wakizashi|itcf_show_holster_when_drawn, 321 , weight(1.25)|difficulty(0)|spd_rtng(108) | weapon_length(65)|swing_damage(25 , cut) | thrust_damage(19 ,  pierce),imodbits_sword , [], [fac_kingdom_11]],
["court_dress", "Court Dress", [("court_dress",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["rich_outfit", "Rich Outfit", [("merchant_outf",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["khergit_guard_armor", "Khergit Guard Armor", [("lamellar_armor_a",0)], itp_type_body_armor|itp_covers_legs   ,0, 
3048 , weight(25)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(18)|difficulty(0) ,imodbits_armor ],
#["leather_steppe_cap_c", "Leather Steppe Cap", [("leather_steppe_cap_c",0)], itp_type_head_armor   ,0, 51 , weight(2)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["felt_steppe_cap", "Felt Steppe Cap", [("felt_steppe_cap",0)], itp_type_head_armor   ,0, 237 , weight(2)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["khergit_war_helmet", "Khergit War Helmet", [("tattered_steppe_cap_a_new",0)], itp_type_head_armor | itp_merchandise   ,0, 200 , weight(2)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["khergit_helmet", "Khergit Helmet", [("khergit_guard_helmet",0)], itp_type_head_armor   ,0, 361 , weight(2)|abundance(100)|head_armor(33)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
#["khergit_sword", "Khergit Sword", [("khergit_sword",0),("khergit_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 183 , weight(1.25)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(23 , cut) | thrust_damage(14 ,  pierce),imodbits_sword ],
["khergit_guard_boots",  "Khergit Guard Boots", [("lamellar_boots_a",0)], itp_type_foot_armor | itp_attach_armature,0, 254 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
["khergit_guard_helmet", "Khergit Guard Helmet", [("lamellar_helmet_a",0)], itp_type_head_armor |itp_merchandise   ,0, 433 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["khergit_cavalry_helmet", "Khergit Cavalry Helmet", [("lamellar_helmet_b",0)], itp_type_head_armor | itp_merchandise   ,0, 333 , weight(2)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

["black_hood", "Black Hood", [("hood_black",0)], itp_type_head_armor|itp_merchandise   ,0, 193 , weight(2)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["light_leather", "Light Leather", [("light_leather",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 352 , weight(5)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(7)|difficulty(0) ,imodbits_armor ],
["light_leather_boots",  "Light Leather Boots", [("light_leather_boots",0)], itp_type_foot_armor |itp_merchandise| itp_attach_armature,0, 91 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
["mail_and_plate", "Mail and Plate", [("mail_and_plate",0)], itp_type_body_armor|itp_covers_legs   ,0, 593 , weight(16)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(12)|difficulty(0) ,imodbits_armor ],
["light_mail_and_plate", "Light Mail and Plate", [("light_mail_and_plate",0)], itp_type_body_armor|itp_covers_legs   ,0, 532 , weight(10)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_armor ],

["byzantion_helmet_a", "Byzantion Helmet", [("byzantion_helmet_a",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["magyar_helmet_a", "Magyar Helmet", [("magyar_helmet_a",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["rus_helmet_a", "Rus Helmet", [("rus_helmet_a",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["sipahi_helmet_a", "Sipahi Helmet", [("sipahi_helmet_a",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["shahi", "Shahi", [("shahi",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["rabati", "Rabati", [("rabati",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

["tunic_with_green_cape", "Tunic with Green Cape", [("peasant_man_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ], 
["keys", "Ring of Keys", [("throwing_axe_a",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
240, weight(5)|spd_rtng(98) | swing_damage(29,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown ], 
["bride_dress", "Bride Dress", [("bride_dress",0)], itp_merchandise|itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["bride_crown", "Crown of Flowers", [("bride_crown",0)],  itp_merchandise|itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bride_shoes", "Bride Shoes", [("bride_shoes",0)], itp_merchandise|itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],

["practice_bow_2","Practice Bow", [("hunting_bow",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90) | shoot_speed(40) | thrust_damage(21, blunt),imodbits_bow ],
["practice_arrows_2","Practice Arrows", [("arena_arrow",0),("flying_arrow",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_missile],


["plate_boots", "Plate Boots", [("plate_boots",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_plate ], 

["heraldic_mail_with_surcoat_for_tableau", "{!}Heraldic Mail with Surcoat", [("heraldic_armor_new_a",0)], itp_type_body_armor |itp_covers_legs ,0,
 1, weight(22)|abundance(100)|head_armor(0)|body_armor(1)|leg_armor(1),imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])]],
["mail_boots_for_tableau", "Mail Boots", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1, weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],

##yifeng goods from new land
 ["rare_goods_1","good from new land", [("box_a",0)], itp_type_goods|itp_consumable, 0, 8000,weight(50)|abundance(60)|max_ammo(50),imodbits_none],
 ["rare_goods_2","good from new land1", [("box_a",0)], itp_type_goods|itp_consumable, 0,16000 ,weight(50)|abundance(60)|max_ammo(50),imodbits_none],
 ["rare_goods_3","good from new land2", [("box_a",0)], itp_type_goods|itp_consumable, 0, 24000,weight(50)|abundance(60)|max_ammo(50),imodbits_none],
 ["rare_goods_4","good from new land3", [("box_a",0)], itp_type_goods|itp_consumable, 0, 32000,weight(50)|abundance(60)|max_ammo(50),imodbits_none],
 ["rare_goods_5","good from new land4", [("box_a",0)], itp_type_goods|itp_consumable, 0, 40000,weight(50)|abundance(60)|max_ammo(50),imodbits_none],
 ["rare_goods_end","good from new land5", [("box_a",0)], itp_type_goods|itp_consumable, 0, 0,weight(50)|abundance(60)|max_ammo(50),imodbits_none],

  #maybe use
 ["maybe1", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 
 ["maybe2", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe3", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe4", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe5", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe6", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe7", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe8", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe9", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe10", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe11", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe12", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe13", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe14", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe15", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe16", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe17", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe18", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe19", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe20", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe21", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe25", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe23", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe24", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe25", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe26", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe27", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe28", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe29", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe30", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],

 ["maybe31", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe32", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe33", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe34", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe35", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe36", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe37", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe38", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe39", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe40", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe41", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe42", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe43", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe44", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe45", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe46", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe47", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe48", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe49", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe50", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],

["maybe51", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe52", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe53", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe54", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe55", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe56", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe57", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe58", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe59", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe60", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe501", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe502", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe503", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe504", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe505", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe506", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe507", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe508", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe509", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe510", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe5011", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe5022", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe5033", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe5044", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe5055", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe5066", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe5077", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe5088", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
 ["maybe5099", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["maybe5000", "no use", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1000, weight(3)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],

 ["items_end", "Items End", [("shield_round_a",0)], 0, 0, 1, 0, 0],
]
# modmerger_start version=201 type=2
try:
    component_name = "items"
    var_set = { "items" : items }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
