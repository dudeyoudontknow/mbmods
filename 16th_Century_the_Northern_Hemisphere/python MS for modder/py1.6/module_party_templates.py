from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
  ("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("enemy","Enemy",icon_gray_knight,0,fac_undeads,merchant_personality,[]),
  ("hero_party","Hero Party",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
  ("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,0,4)]),

  ("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

##  ("vaegir_nobleman","Vaegir Nobleman",icon_vaegir_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_vaegir_knight,2,6),(trp_vaegir_horseman,4,12)]),
##  ("swadian_nobleman","Swadian Nobleman",icon_gray_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_swadian_knight,2,6),(trp_swadian_man_at_arms,4,12)]),
# Ryan BEGIN
  ("looters","Looters",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_looter,3,45)]),
# Ryan END
  ("manhunters","Manhunters",icon_gray_knight,0,fac_manhunters,soldier_personality,[(trp_manhunter,9,40)]),
##  ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),

#  ("black_khergit_raiders","Black Khergit Raiders",icon_khergit_horseman_b|carries_goods(2),0,fac_black_khergits,bandit_personality,[(trp_black_khergit_guard,1,10),(trp_black_khergit_horseman,5,5)]),
  ("steppe_bandits","Cossack_robbers",icon_vaegir_knight|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_steppe_bandit,4,80),(trp_steppe_bandit1,1,20)]),
  ("taiga_bandits","Zunghar looters",icon_vaegir_knight|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_taiga_bandit,2,25),(trp_mongol_tribesman,2,55),(trp_mongol_horseman,1,20)]),
  ("desert_bandits","North_Africa_Pirates",icon_vaegir_knight|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_desert_bandit,3,70),(trp_africa_horseman,2,30)]),
  ("forest_bandits","Ikko-ikki",icon_axeman|carries_goods(2),0,fac_forest_bandits,bandit_personality,[(trp_forest_bandit,2,20),(trp_japan_tribesman,10,40)]),
  ("mountain_bandits","Chinese rebel soldiers",icon_axeman|carries_goods(2),0,fac_mountain_bandits,bandit_personality,[(trp_mountain_bandit,4,70),(trp_ming_infantry,1,30)]),
  ("sea_raiders","European_Pirates",icon_ship|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_sea_raider,20,80),(trp_sea_raider1,5,20)]),
##yifeng
  ("african_tribesman","african_tribesmen",icon_axeman|carries_goods(2),0,fac_african_tribesman,bandit_personality,[(trp_sh_recruit,20,100),(trp_sh_footman,5,40),(trp_sh_skirmisher,5,30)]),

    ("wokou","Japanese Pirates",icon_ship|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_wokou,5,80)]),

	    ("indu","Indic Pirates",icon_ship|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_deli_skirmisher,10,70),(trp_deli_sergeant,2,30)]),

			    ("indian","Indian tribesmen",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_aifootman,5,55),(trp_aihorseman,2,20),(trp_aiinfantry,5,25)]),

  ("deserters","Deserters",icon_vaegir_knight|carries_goods(3),0,fac_deserters,bandit_personality,[]),
    
  ("merchant_caravan","Merchant Caravan",icon_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,15,35)]),
  ("troublesome_bandits","Troublesome Bandits",icon_axeman|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,15,105)]),
  ("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,88),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
  ("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

  ("village_farmers","Village Farmers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,6,16)]),

  ("spy_partners", "Unremarkable Travellers", icon_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_caravan_guard,10,30)]),
  ("runaway_serfs","Runaway Serfs",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,7), (trp_peasant_woman,3,3)]),
  ("spy", "Ordinary Townsman", icon_gray_knight|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
  ("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),
##  ("conspirator", "Conspirators", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator,3,4)]),
##  ("conspirator_leader", "Conspirator Leader", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator_leader,1,1)]),
##  ("peasant_rebels", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,bandit_personality,[(trp_peasant_rebel,33,97)]),
##  ("noble_refugees", "Noble Refugees", icon_gray_knight|carries_goods(12)|pf_quest_party,0,fac_noble_refugees,merchant_personality,[(trp_noble_refugee,3,5),(trp_noble_refugee_woman,5,7)]),

  ("forager_party","Foraging Party",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("scout_party","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
  ("patrol_party","Patrol",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_commoners,soldier_personality,[]),
#  ("war_party", "War Party",icon_gray_knight|carries_goods(3),0,fac_commoners,soldier_personality,[]),
  ("messenger_party","Messenger",icon_gray_knight|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("raider_party","Raiders",icon_gray_knight|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
  ("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
  ("kingdom_caravan_party","Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,12,40)]),
  ("prisoner_train_party","Prisoner Train",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("default_prisoners","Default Prisoners",0,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

  ("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),


# Caravans
  ("center_reinforcements","Reinforcements",icon_axeman|carries_goods(16),0,fac_commoners,soldier_personality,[(trp_townsman,5,30),(trp_watchman,4,20)]),  

  ("kingdom_hero_party","War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  
# Reinforcements
  # each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
  # less-modernised templates are generally includes 7-14 troops in total, 
  # med-modernised templates are generally includes 5-10 troops in total, 
  # high-modernised templates are generally includes 3-5 troops in total
# windmelodie begin yifeng V1.4
  ("kingdom_0_reinforcements_a", "{!}kingdom_0_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_kingdom_recruit,7,10),(trp_kingdom_militia,6,10)]),
  ("kingdom_0_reinforcements_b", "{!}kingdom_0_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_kingdom_footman,3,6),(trp_kingdom_skirmisher,2,3),(trp_kingdom_infantry,2,5),(trp_kingdom_man_at_arms,2,4),(trp_kingdom_crossbowman,1,3)]),
  ("kingdom_0_reinforcements_c", "{!}kingdom_0_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_kingdom_knight,1,3),(trp_kingdom_sergeant,1,3),(trp_kingdom_sharpshooter,1,3)]), 
# windmelodie end
  ("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_bannere,1,2),(trp_swadian_recruit,6,9),(trp_swadian_militia,3,7),(trp_swadian_skirmisher,1,3)]),
  ("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_swadian_retinue,3,5),(trp_swadian_footman,2,4),(trp_swadian_crossbowman,1,3),(trp_swadian_sharpshooter,1,3),(trp_swadian_pikeman,2,5)]),
  ("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_knight,1,3),(trp_swadian_man_at_arms,1,2),(trp_swadian_sergeant,2,4),(trp_swadian_infantry,1,1)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)

  ("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_banneree,1,2),(trp_vaegir_recruit,5,9),(trp_vaegir_footman,3,7),(trp_vaegir_skirmisher,2,4)]),#yifeng
  ("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_vaegir_veteran,3,6),(trp_vaegir_skirmisher,2,5),(trp_vaegir_marksman,1,2),(trp_vaegir_horseman,2,3),(trp_vaegir_archer,2,3)]),
  ("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_knight,1,1),(trp_vaegir_archer,1,3),(trp_vaegir_marksman,1,2),(trp_vaegir_guard,1,3)]),

  ("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_bannere,1,2),(trp_khergit_tribesman,5,9),(trp_summer_footman,3,5),(trp_khergit_skirmisher,2,5)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,2,4),(trp_summer_sharpshooter,2,5),(trp_summer_infantry,3,5),(trp_khergit_horse_archer,1,3),(trp_summer_pikeman1,1,2)]),
  ("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_summer_lancer_guard,1,2),(trp_khergit_lancer,1,2),(trp_khergit_veteran_horse_archer,2,3),(trp_summer_crossbowman,1,3)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  ("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_bannere,1,2),(trp_nord_recruit,6,9),(trp_nord_footman,4,6),(trp_nord_huntsman,2,4)]),
  ("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_trained_footman,3,7),(trp_hench_hackbuteer,2,5),(trp_nord_archer,2,4),(trp_nord_veteran_archer,2,5)]),
  ("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_champion,1,2),(trp_nord_veteran,1,2),(trp_nord_warrior,2,3),(trp_hench_halberdman,2,3),(trp_nord_veteran_archer,1,2)]),

  ("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_bannere,1,2),(trp_rhodok_tribesman,6,9),(trp_rhodok_spearman,3,7),(trp_rhodok_trained_crossbowman,1,3)]),
  ("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_trained_spearman,4,7),(trp_rhodok_sergeant,2,5),(trp_rhodok_veteran_crossbowman,2,5),(trp_rhodok_trained_crossbowman,2,4)]),
  ("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_veteran_spearman,2,4),(trp_rhodok_crossbowman,1,3),(trp_rhodok_sharpshooter,1,3)]), 

  ("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_bannera,1,2),(trp_sarranid_recruit,6,9),(trp_sarranid_footman,3,6),(trp_sarranid_archer,2,4)]),
  ("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sarranid_horseman,2,4),(trp_sarranid_veteran_footman,1,4),(trp_sarranid_skirmisher,2,4),(trp_sarranid_spearman,2,4),(trp_sarranid_sipahi,1,2)]),
  ("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sarranid_sipahi_cavalry,1,2),(trp_sarranid_light_horseman,1,2),(trp_sarranid_guard,1,2),(trp_sarranid_mamluke,1,2),(trp_sarranid_master_archer,1,2)]),
##yifeng
  ("kingdom_7_reinforcements_a", "{!}kingdom_7_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_bannerc,1,2),(trp_ming_skirmisher,6,12),(trp_ming_infantry,6,12),(trp_ming_archer,4,10)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_7_reinforcements_b", "{!}kingdom_7_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_ming_lancer,4,8),(trp_ming_horse_archer,3,6),(trp_ming_sanqianying_cavalry,3,6),(trp_ming_gunner,3,8),(trp_ming_infantry1,4,10)]),
  ("kingdom_7_reinforcements_c", "{!}kingdom_7_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_ming_veteran_horse_archer,3,5),(trp_ming_footman,3,5),(trp_divine_engine_division_ming_musketeers,2,4),(trp_divine_engine_division_ming_cavalry,2,4),(trp_ming_dismounted_imperial_guard,2,4),(trp_jingyiwei111,2,4)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
 ##HolyAce
  ("kingdom_7_reinforcements_d", "{!}kingdom_7_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_dongcang,6,10)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)


  ("kingdom_8_reinforcements_a", "{!}kingdom_8_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_bannere,1,2),(trp_england_tribesman,6,9),(trp_england_footman,3,5),(trp_england_skirmisher,3,6)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_8_reinforcements_b", "{!}kingdom_8_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_england_sharpshooter,2,4),(trp_england_footman,1,3),(trp_england_horse_archer,1,2),(trp_england_veteran_horse_archer,4,7),(trp_england_horseman,2,4)]),
  ("kingdom_8_reinforcements_c", "{!}kingdom_8_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_england_lancer_guard,1,2),(trp_england_lancer,1,2),(trp_england_pikeman1,1,3),(trp_england_sergeant,1,2),(trp_england_crossbowman,1,2)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  ("kingdom_9_reinforcements_a", "{!}kingdom_9_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_bannere,1,2),(trp_spain_tribesman,6,9),(trp_spain_footman,3,6),(trp_spain_skirmisher,2,5)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_9_reinforcements_b", "{!}kingdom_9_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_spain_horseman,1,3),(trp_spain_sharpshooter,3,5),(trp_spain_infantry,1,2),(trp_spain_horse_archer,4,6),(trp_spain_veteran_horse_archer,1,3)]),
  ("kingdom_9_reinforcements_c", "{!}kingdom_9_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_spain_lancer_guard,1,2),(trp_spain_lancer,1,2),(trp_spain_pikeman1,1,3),(trp_spain_sergeant,1,2),(trp_spain_horse_archer,2,4)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
 
  ("kingdom_10_reinforcements_a", "{!}kingdom_10_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_mongol_tribesman,5,9),(trp_mongol_skirmisher,4,7),(trp_mongol_horseman,4,6)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_10_reinforcements_b", "{!}kingdom_10_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_mongol_skirmisher,8,11),(trp_mongol_horseman,6,9)]),#mogol
  ("kingdom_10_reinforcements_c", "{!}kingdom_10_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_mongol_veteran_horse_archer,2,5),(trp_mongol_lancer,3,5)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
  ##HolyAce
  ("kingdom_10_reinforcements_d", "{!}kingdom_10_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_mongol_lancer_guard,2,4)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  ("kingdom_11_reinforcements_a", "{!}kingdom_11_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_bannerj,1,2),(trp_japan_tribesman,6,9),(trp_japan_horseman,2,5),(trp_japan_skirmisher,2,4)]),
  ("kingdom_11_reinforcements_b", "{!}kingdom_11_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_japan_footman,3,4),(trp_japan_horseman,2,5),(trp_japan_skirmisher,3,6),(trp_japan_sharpshooter,3,5)]),
  ("kingdom_11_reinforcements_c", "{!}kingdom_11_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_japan_lancer_guard,1,2),(trp_japan_lancer,1,2),(trp_japan_crossbowman,1,4),(trp_japan_crossbowman1,2,3)]), 
  ##HolyAce
  ("kingdom_11_reinforcements_d", "{!}kingdom_11_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_japan_ninja,4,6)]), 
 
  ("kingdom_12_reinforcements_a", "{!}kingdom_12_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_bannera,1,2),(trp_safavid_tribesman,6,9),(trp_safavid_horseman,2,4),(trp_safavid_skirmisher,2,5)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_12_reinforcements_b", "{!}kingdom_12_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_safavid_horseman,3,5),(trp_safavid_skirmisher,2,4),(trp_safavid_lancer,2,5),(trp_safavid_infantry,2,4)]),#saf
  ("kingdom_12_reinforcements_c", "{!}kingdom_12_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_safavid_lancer_guard,1,2),(trp_safavid_sergeant,1,3),(trp_safavid_horse_archer,2,4)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
 
  ("kingdom_13_reinforcements_a", "{!}kingdom_13_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_banneree,1,2),(trp_poland_lithuania_tribesman,6,9),(trp_poland_lithuania_skirmisher,3,6),(trp_poland_lithuania_horseman,2,4)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_13_reinforcements_b", "{!}kingdom_13_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_poland_lithuania_footman,3,5),(trp_poland_lithuania_lancer,2,4),(trp_poland_lithuania_horse_archer,2,4),(trp_poland_lithuania_sharpshooter,1,3),(trp_poland_lithuania_infantry,2,3)]),
  ("kingdom_13_reinforcements_c", "{!}kingdom_13_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_poland_lithuania_sergeant,1,2),(trp_poland_lithuania_lancer_guard,2,3),(trp_poland_lithuania_crossbowman,1,3),(trp_poland_lithuania_veteran_horse_archer,2,3)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
 
  ("kingdom_14_reinforcements_a", "{!}kingdom_14_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_bannera,1,2),(trp_africa_tribesman,6,9),(trp_africa_horseman,2,6),(trp_africa_skirmisher,2,3)]), #Khergits are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_14_reinforcements_b", "{!}kingdom_14_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_africa_horseman,3,6),(trp_africa_skirmisher,2,3),(trp_africa_lancer,2,5),(trp_africa_infantry,2,4)]),
  ("kingdom_14_reinforcements_c", "{!}kingdom_14_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_africa_lancer_guard,1,3),(trp_africa_sergeant,2,4),(trp_africa_horse_archer,1,2)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  ("kingdom_15_reinforcements_a", "{!}kingdom_15_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_aitribeman,5,9),(trp_aihunter,4,7),(trp_aiinfantry,4,6)]), #15 are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_15_reinforcements_b", "{!}kingdom_15_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_aihunter,6,8),(trp_aiinfantry,4,6),(trp_aifootman,3,5)]),
  ("kingdom_15_reinforcements_c", "{!}kingdom_15_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_aifootman,2,3),(trp_aihorseman,1,3),(trp_ai_sergeant,1,2)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  ("kingdom_16_reinforcements_a", "{!}kingdom_16_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_bannere,1,2),(trp_pol_tribesman,5,9),(trp_pol_skirmisher,4,7),(trp_pol_infantry,4,6)]), #16 are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_16_reinforcements_b", "{!}kingdom_16_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_pol_skirmisher,4,6),(trp_pol_raider_horseman,3,4),(trp_pol_infantry,3,4),(trp_pol_horseman,3,5)]),
  ("kingdom_16_reinforcements_c", "{!}kingdom_16_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_pol_lancer,3,4),(trp_pol_sergeant,2,3),(trp_pol_gunner,2,3)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  ("kingdom_17_reinforcements_a", "{!}kingdom_17_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_deli_tribesman,5,9),(trp_deli_skirmisher,4,7),(trp_deli_militia,4,6)]), #17 are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_17_reinforcements_b", "{!}kingdom_17_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_deli_skirmisher,4,6),(trp_deli_militia,6,8),(trp_deli_horse_archer,3,5)]),
  ("kingdom_17_reinforcements_c", "{!}kingdom_17_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_eliphant,2,3),(trp_deli_horse_archer,1,2),(trp_deli_lancer_guard,1,3),(trp_deli_sergeant,2,3)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  ("kingdom_18_reinforcements_a", "{!}kingdom_18_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_se_farmer,5,9),(trp_se_skirmisher,4,7),(trp_se_archer,4,6)]), #18 are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_18_reinforcements_b", "{!}kingdom_18_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_se_skirmisher,7,9),(trp_se_archer,3,5),(trp_se_archer11,3,5)]),
  ("kingdom_18_reinforcements_c", "{!}kingdom_18_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_eliphant,2,3),(trp_se_lancer_guard,1,2),(trp_se_sergeant,1,3),(trp_se_archer11,1,2)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

#  ("kingdom_19_reinforcements_a", "{!}kingdom_19_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_korea_tribesman,3,5),(trp_korea_skirmisher,4,8)]), #19 are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
#  ("kingdom_19_reinforcements_b", "{!}kingdom_19_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_korea_horseman,5,8),(trp_korea_lancer,5,8),(trp_korea_infantry,4,6)]),
#  ("kingdom_19_reinforcements_c", "{!}kingdom_19_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_korea_horseman,4,6),(trp_korea_infantry,6,10),(trp_korea_sergeant,6,8)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
  ("kingdom_19_reinforcements_a", "{!}kingdom_19_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_korea_tribesman,5,9),(trp_korea_skirmisher,3,6),(trp_korea_horseman,4,7)]), #19 are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_19_reinforcements_b", "{!}kingdom_19_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_korea_archer,2,5),(trp_korea_light_cavalry,2,5),(trp_korea_infantry,2,5),(trp_korea_gunner,1,2)]),
  ("kingdom_19_reinforcements_c", "{!}kingdom_19_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_korea_royal_guard,1,2),(trp_korea_lancer,1,2),(trp_korea_sergeant,1,2),(trp_korea_gunner,1,2)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

##HolyAce
  ("kingdom_20_reinforcements_a", "{!}kingdom_20_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nvzhen_tribesman,6,11),(trp_nvzhen_sizu,5,9),(trp_nvzhen_jumazu,5,9)]), #20 are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_20_reinforcements_b", "{!}kingdom_20_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nvzhen_jumazu,4,7),(trp_nvzhen_sizu,4,7),(trp_nvzhen_skirmisher,3,6),(trp_nvzhen_lancer,3,6)]),
  ("kingdom_20_reinforcements_c", "{!}kingdom_20_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nvzhen_sergeant,2,4),(trp_nvzhen_qingjiabushe,2,4),(trp_nvzhen_horse_archer,1,2),(trp_nvzhen_horse_archer_red,1,2)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)
  ("kingdom_20_reinforcements_d", "{!}kingdom_20_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_nvzhen_duduhuweihuoqiang,1,2),(trp_nvzhen_duduhuwei,1,2)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  ("kingdom_21_reinforcements_a", "{!}kingdom_21_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_kazakh_tribesman,6,12),(trp_kazakh_lancer,5,8)]), #21are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_21_reinforcements_b", "{!}kingdom_21_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_kazakh_tribesman,4,7),(trp_kazakh_lancer,3,6),(trp_kazakh_lancer_guard,2,5)]),
  ("kingdom_21_reinforcements_c", "{!}kingdom_21_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_kazakh_lancer,2,3),(trp_kazakh_lancer_guard,2,4),(trp_kazakh_horse_archer,1,2)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  ("kingdom_22_reinforcements_a", "{!}kingdom_22_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_crimia_horseman,6,12),(trp_crimia_horse_archer,5,8)]), #22 are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_22_reinforcements_b", "{!}kingdom_22_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_crimia_horseman,4,7),(trp_crimia_horse_archer,3,5),(trp_crimia_lighthorseman,3,6)]),
  ("kingdom_22_reinforcements_c", "{!}kingdom_22_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_crimia_horse_archer,2,3),(trp_crimea_lancer,2,4),(trp_crimia_infantry,1,2)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  ("kingdom_23_reinforcements_a", "{!}kingdom_23_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_bannera,1,2),(trp_mamalik_recruit,6,9),(trp_mamalik_footman,2,6),(trp_mamalik_skirmisher,3,6)]), #22 are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_23_reinforcements_b", "{!}kingdom_23_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_mamalik_footman,3,5),(trp_africa_skirmisher,4,5),(trp_mamalik_skirmisher,2,5),(trp_sarranid_bedouin,3,5),(trp_mamalik_shooter,2,4)]),
  ("kingdom_23_reinforcements_c", "{!}kingdom_23_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sarranid_mamluke1,1,2),(trp_mamalik_guard,1,3),(trp_mamalik_shooter,2,3),(trp_mamalik_horsearcher,1,3)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  ("kingdom_24_reinforcements_a", "{!}kingdom_24_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_scottish_tribesman,3,5),(trp_scottish_skirmisher,4,9),(trp_scottish_archer,4,9)]), #22 are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_24_reinforcements_b", "{!}kingdom_24_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_scottish_skirmisher,4,7),(trp_scottish_archer,2,5),(trp_scottish_swordman,2,4),(trp_scottish_lancer,1,2)]),
  ("kingdom_24_reinforcements_c", "{!}kingdom_24_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_scottish_knight,1,2),(trp_scottish_sergeant,2,4),(trp_scottish_gunner,2,3),(trp_scottish_lancer,1,2)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  ("kingdom_25_reinforcements_a", "{!}kingdom_25_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_aztec_tribesman,6,9),(trp_aztec_skirmisher,2,7),(trp_aztec_archer,3,8)]), #22 are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_25_reinforcements_b", "{!}kingdom_25_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_aztec_skirmisher,6,9),(trp_aztec_archer,4,6),(trp_aztec_gurad,2,6)]),
  ("kingdom_25_reinforcements_c", "{!}kingdom_25_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_aztec_jaguar,3,5),(trp_aztec_warrior,2,5),(trp_aztec_gurad,2,5)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  ("kingdom_26_reinforcements_a", "{!}kingdom_26_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_maya_tribesman,6,9),(trp_maya_skirmisher,2,7),(trp_maya_archer,3,8)]), #22 are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_26_reinforcements_b", "{!}kingdom_26_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_maya_skirmisher,6,9),(trp_maya_archer,4,6),(trp_maya_warrior,2,5)]),
  ("kingdom_26_reinforcements_c", "{!}kingdom_26_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_maya_jaguar,3,6),(trp_maya_warrior,2,4),(trp_maya_archer,2,5)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  ("kingdom_27_reinforcements_a", "{!}kingdom_27_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_bannere,1,2),(trp_livonia_tribesman,6,9),(trp_livonia_skirmisher,4,8)]), #22 are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_27_reinforcements_b", "{!}kingdom_27_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_livonia_skirmisher,6,10),(trp_livonia_lancer,1,2),(trp_livonia_sergeant,2,3),(trp_khergit_skirmisher,2,4),(trp_khergit_horse_archer,2,3)]),
  ("kingdom_27_reinforcements_c", "{!}kingdom_27_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_livonia_lancer,5,8),(trp_livonia_sergeant,5,8)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  ("kingdom_28_reinforcements_a", "{!}kingdom_28_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_bannere,1,2),(trp_hospital_tribesman,6,9),(trp_hospital_skirmisher,4,8)]), #22 are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_28_reinforcements_b", "{!}kingdom_28_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_hospital_skirmisher,8,12),(trp_hospital_lancer,1,2),(trp_hospital_sergeant,2,4),(trp_nord_archer,3,4),(trp_nord_veteran_archer,3,4)]),
  ("kingdom_28_reinforcements_c", "{!}kingdom_28_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_hospital_lancer,5,8),(trp_hospital_monk,2,3),(trp_hospital_sergeant,5,8)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

#yifeng 1.5                                                                                           #13,21   10,19  ,08,13
  ("kingdom_29_reinforcements_a", "{!}kingdom_29_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sh_recruit,6,10),(trp_sh_footman,3,5),(trp_sh_skirmisher,3,6)]), #22 are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_29_reinforcements_b", "{!}kingdom_29_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sh_light_horseman,3,5),(trp_sh_veteran_footman,2,5),(trp_sh_footman,4,6),(trp_sh_skirmisher,2,4)]),
  ("kingdom_29_reinforcements_c", "{!}kingdom_29_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sh_mamluke,2,3),(trp_sh_archer,2,3),(trp_sh_light_horseman,2,4),(trp_sh_veteran_footman,2,4)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  ("kingdom_30_reinforcements_a", "{!}kingdom_30_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_incan_recruit,5,9),(trp_incan_footman,5,8),(trp_incan_skirmisher,4,6)]), #22 are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_30_reinforcements_b", "{!}kingdom_30_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_incan_footman,6,11),(trp_incan_h_footman,4,8)]),
  ("kingdom_30_reinforcements_c", "{!}kingdom_30_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_incan_h_footman,4,7),(trp_incan_nobleman,4,6)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  ("kingdom_31_reinforcements_a", "{!}kingdom_31_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_saf_recruit,8,10),(trp_saf_spearman,3,5),(trp_soa_recruit,3,4),(trp_saf_skirmisher,2,3)]), #22 are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_31_reinforcements_b", "{!}kingdom_31_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_soa_spearman,6,10),(trp_saf_footman,2,4),(trp_soa_skirmisher,2,3)]),
  ("kingdom_31_reinforcements_c", "{!}kingdom_31_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_saf_footman,4,6),(trp_soa_footman,2,3),(trp_soa_horseman,2,3)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  ("kingdom_32_reinforcements_a", "{!}kingdom_32_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_saf_recruit,10,12),(trp_saf_spearman,4,6),(trp_saf_skirmisher,3,4)]), #22 are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_32_reinforcements_b", "{!}kingdom_32_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_saf_spearman,6,10),(trp_saf_footman,4,6)]),
  ("kingdom_32_reinforcements_c", "{!}kingdom_32_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_saf_footman,4,6),(trp_saf_skirmisher,4,6)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  ("kingdom_33_reinforcements_a", "{!}kingdom_33_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_bannera,1,2),(trp_soa_recruit,6,8),(trp_soa_spearman,2,3),(trp_soa_skirmisher,2,3)]), #22 are a bit less-powered thats why they have a bit more 2nd upgraded(trp_khergit_skirmisher) than non-upgraded one(trp_khergit_tribesman).
  ("kingdom_33_reinforcements_b", "{!}kingdom_33_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_soa_footman,4,5),(trp_soa_horseman,3,4),(trp_soa_spearman,4,7)]),
  ("kingdom_33_reinforcements_c", "{!}kingdom_33_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_soa_guard,2,3),(trp_soa_horsearcher,2,3),(trp_soa_lancer,2,3),(trp_africa_skirmisher,5,6)]), #Khergits are a bit less-powered thats why they have a bit more troops in their modernised party template (4-7, others 3-5)

  #yifeng 1.5 
  
##  ("kingdom_1_reinforcements_a", "kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_swadian_footman,3,7),(trp_swadian_skirmisher,5,10),(trp_swadian_militia,11,26)]),
##  ("kingdom_1_reinforcements_b", "kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_swadian_man_at_arms,5,10),(trp_swadian_infantry,5,10),(trp_swadian_crossbowman,3,8)]),
##  ("kingdom_1_reinforcements_c", "kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_knight,2,6),(trp_swadian_sergeant,2,5),(trp_swadian_sharpshooter,2,5)]),
##
##  ("kingdom_2_reinforcements_a", "kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_vaegir_veteran,3,7),(trp_vaegir_skirmisher,5,10),(trp_vaegir_footman,11,26)]),
##  ("kingdom_2_reinforcements_b", "kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_vaegir_horseman,4,9),(trp_vaegir_infantry,5,10),(trp_vaegir_archer,3,8)]),
##  ("kingdom_2_reinforcements_c", "kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_knight,3,7),(trp_vaegir_guard,2,5),(trp_vaegir_marksman,2,5)]),
##
##  ("kingdom_3_reinforcements_a", "kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,3,7),(trp_khergit_skirmisher,5,10),(trp_khergit_tribesman,11,26)]),
##  ("kingdom_3_reinforcements_b", "kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_veteran_horse_archer,4,9),(trp_khergit_horse_archer,5,10),(trp_khergit_horseman,3,8)]),
##  ("kingdom_3_reinforcements_c", "kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_lancer,3,7),(trp_khergit_veteran_horse_archer,2,5),(trp_khergit_horse_archer,2,5)]),
##
##  ("kingdom_4_reinforcements_a", "kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_trained_footman,3,7),(trp_nord_footman,5,10),(trp_nord_recruit,11,26)]),
##  ("kingdom_4_reinforcements_b", "kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_veteran,4,9),(trp_nord_warrior,5,10),(trp_nord_footman,3,8)]),
##  ("kingdom_4_reinforcements_c", "kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_champion,1,3),(trp_nord_veteran,2,5),(trp_nord_warrior,2,5)]),
##
##  ("kingdom_5_reinforcements_a", "kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_spearman,3,7),(trp_rhodok_crossbowman,5,10),(trp_rhodok_tribesman,11,26)]),
##  ("kingdom_5_reinforcements_b", "kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_trained_spearman,4,9),(trp_rhodok_spearman,5,10),(trp_rhodok_crossbowman,3,8)]),
##  ("kingdom_5_reinforcements_c", "kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_sergeant,3,7),(trp_rhodok_veteran_spearman,2,5),(trp_rhodok_veteran_crossbowman,2,5)]),



  ("steppe_bandit_lair" ,"Lair(maybe bug)",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_steppe_bandit,15,58)]),
  ("taiga_bandit_lair","Lair(maybe bug)",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_taiga_bandit,15,58)]),
  ("desert_bandit_lair" ,"Lair(maybe bug)",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_desert_bandit,15,58)]),
  ("forest_bandit_lair" ,"Camp(maybe bug)",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_forest_bandit,15,58)]),
  ("mountain_bandit_lair" ,"Hideout(maybe bug)",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_mountain_bandit,15,58)]),
  ("sea_raider_lair","Camp(maybe bug)",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_sea_raider,15,50)]),
  ("looter_lair","Hideout(maybe bug)",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,15,25)]),
  
  ("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,50)]),

  ("leaded_looters","Band of robbers",icon_axeman|carries_goods(8)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_looter_leader,1,1),(trp_looter,3,3)]),

## ZZ
("merchant_manhunters","Bank's Killers",icon_gray_knight,0,fac_manhunters,soldier_personality,[(trp_manhunter,10,50),(trp_slaver_chief,1,10),(trp_hired_blade,1,10),(trp_mercenary_crossbowman,5,20)]),  
## ZZ 

#recruiter kit begin yifeng
   ("recruiter","Recruiter",icon_gray_knight|pf_show_faction,0,fac_neutral,merchant_personality,[(trp_recruiter,1,1)]),
#recruiter kit end
]
# modmerger_start version=201 type=2
try:
    component_name = "party_templates"
    var_set = { "party_templates" : party_templates }
    from modmerger import modmerge
    modmerge(var_set)
except:
    raise
# modmerger_end
