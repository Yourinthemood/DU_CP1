#DU P2 THE FINAL GAME (7 revisions) (3 bricks of code deleted because it didnt work) (aproximatley 13 hours of my time compiled into one decent text game) *pun intended
import random
import time

# ============================================
# GAME DATA
# ============================================

# Player stats (these change what you can accomplish)
player_stats = {
    "health": 100,
    "max_health": 100,
    "strength": 10,      # Affects basic attack damage
    "defense": 5,        # Reduces incoming damage
    "magic": 8,          # Affects spell damage
    "crowns": 0,
    "elixir": 3,
    "location": "training_camp",
    "visited_rooms": [],
    "defeated_enemies": [],
    "just_finished_battle": False  # Track if player just finished a battle
}

# Items that can be picked up and used
player_items = {
    "elixir_vial": False,    # Heals 50 HP when used
    "strength_potion": False, # Increases strength by 5
    "spell_scroll": False,    # Increases magic by 5
    "shield": False,          # Increases defense by 5
    "crown_key": False        # Unlocked final boss room
}

# Card collection (represents player's abilities)
player_cards = [
    ["Archers", "troop", 30, 50, 3],
    ["Goblins", "troop", 20, 30, 2],
    ["Turret", "building", 15, 100, 4]
]

# List of all locations (10 total with Healing Pool)
locations = [
    "training_camp",      # Starting area
    "goblin_stadium",     # First arena
    "bone_pit",          # Second arena  
    "barbarian_bowl",    # Third arena
    "spell_valley",      # Fourth arena
    "ice_peak_arena",    # Fifth arena
    "pekka_playhouse",   # Sixth arena
    "legendary_arena",   # Seventh arena
    "king_tower",        # Final boss
    "healing_pool"       # Healing location
]

# Room connections (non-linear paths)
room_connections = {
    "training_camp": ["goblin_stadium", "bone_pit", "healing_pool"],
    "goblin_stadium": ["training_camp", "barbarian_bowl", "spell_valley", "healing_pool"],
    "bone_pit": ["training_camp", "ice_peak_arena", "spell_valley", "healing_pool"],
    "barbarian_bowl": ["goblin_stadium", "pekka_playhouse", "healing_pool"],
    "spell_valley": ["goblin_stadium", "bone_pit", "legendary_arena", "healing_pool"],
    "ice_peak_arena": ["bone_pit", "legendary_arena", "healing_pool"],
    "pekka_playhouse": ["barbarian_bowl", "king_tower", "healing_pool"],
    "legendary_arena": ["spell_valley", "ice_peak_arena", "king_tower", "healing_pool"],
    "king_tower": ["pekka_playhouse", "legendary_arena"],
    "healing_pool": ["training_camp", "goblin_stadium", "bone_pit", "barbarian_bowl", 
                    "spell_valley", "ice_peak_arena", "pekka_playhouse", "legendary_arena"]
}

# Room descriptions and contents
room_data = {
    "training_camp": {
        "description": "A training ground for new warriors. Practice dummies line the walls.",
        "items": ["elixir_vial", "strength_potion"],
        "enemy": None,
        "crowns_needed": 0
    },
    "goblin_stadium": {
        "description": "The Goblin Stadium! Goblins cheer from the stands as their champion approaches.",
        "items": [],
        "enemy": "goblin_king",
        "crowns_needed": 0,
        "crowns_reward": 10
    },
    "bone_pit": {
        "description": "A pit filled with bones. Skeletons rattle in the darkness.",
        "items": ["spell_scroll"],
        "enemy": "skeleton_king",
        "crowns_needed": 10,
        "crowns_reward": 15
    },
    "barbarian_bowl": {
        "description": "A massive bowl-shaped arena. Barbarians roar from every direction.",
        "items": ["shield"],
        "enemy": "barbarian_king",
        "crowns_needed": 25,
        "crowns_reward": 20
    },
    "spell_valley": {
        "description": "A valley shimmering with magical energy. Wizards practice their craft.",
        "items": [],
        "enemy": "wizard_king",
        "crowns_needed": 35,
        "crowns_reward": 25
    },
    "ice_peak_arena": {
        "description": "An icy arena that chills to the bone. Ice spells freeze the air.",
        "items": ["elixir_vial"],
        "enemy": "ice_king",
        "crowns_needed": 45,
        "crowns_reward": 30
    },
    "pekka_playhouse": {
        "description": "P.E.K.K.A's Playhouse! Massive armored warriors await challengers.",
        "items": ["strength_potion"],
        "enemy": "pekka_king",
        "crowns_needed": 60,
        "crowns_reward": 35
    },
    "legendary_arena": {
        "description": "The Legendary Arena! Only the strongest dare to enter.",
        "items": ["crown_key"],
        "enemy": "legendary_king",
        "crowns_needed": 80,
        "crowns_reward": 50
    },
    "king_tower": {
        "description": "The King's Tower! The final challenge awaits at the top.",
        "items": [],
        "enemy": "final_king",
        "crowns_needed": 100,
        "crowns_reward": 100
    },
    "healing_pool": {
        "description": "A magical pool with healing waters. The water glows with restorative energy.",
        "items": [],
        "enemy": None,
        "crowns_needed": 0,
        "crowns_reward": 0
    }
}

# Enemy data
enemies = {
    "goblin_king": {"health": 80, "attack": 15, "defense": 5},
    "skeleton_king": {"health": 100, "attack": 20, "defense": 8},
    "barbarian_king": {"health": 120, "attack": 25, "defense": 12},
    "wizard_king": {"health": 90, "attack": 30, "defense": 6},
    "ice_king": {"health": 110, "attack": 22, "defense": 10},
    "pekka_king": {"health": 150, "attack": 35, "defense": 20},
    "legendary_king": {"health": 180, "attack": 40, "defense": 25},
    "final_king": {"health": 250, "attack": 50, "defense": 30}
}

# ============================================
# FUNCTIONS
# ============================================

def show_status():
    """Display player status"""
    print("\n" + "="*50)
    print(f"LOCATION: {player_stats['location'].replace('_', ' ').title()}")
    print(f"HEALTH: {player_stats['health']}/{player_stats['max_health']}")
    print(f"STRENGTH: {player_stats['strength']}")
    print(f"DEFENSE: {player_stats['defense']}")
    print(f"MAGIC: {player_stats['magic']}")
    print(f"ELIXIR: {player_stats['elixir']}/10")
    print(f"CROWNS: {player_stats['crowns']}")
    if player_stats["just_finished_battle"]:
        print("HEALING POOL AVAILABLE: Yes")
    else:
        print("HEALING POOL AVAILABLE: No (visit after battle)")
    print("="*50)

def show_items():
    """Show items player has collected"""
    print("\n--- ITEMS ---")
    has_items = False
    for item, owned in player_items.items():
        if owned:
            print(f"✓ {item.replace('_', ' ').title()}")
            has_items = True
    if not has_items:
        print("No items yet!")
    
    print("\n--- CARDS ---")
    for i, card in enumerate(player_cards, 1):
        print(f"{i}. {card[0]} (Cost: {card[4]}, Dmg: {card[2]})")

def increase_stats():
    """Increase player stats after battle - increases 3 different stats"""
    # This function increases multiple stats
    player_stats["strength"] += 2
    player_stats["defense"] += 1
    player_stats["magic"] += 1
    print("\nAfter the battle, you feel stronger!")
    print(f"Strength +2, Defense +1, Magic +1")

def pick_up_item(item_name):
    """Pick up an item from the room"""
    if not player_items[item_name]:
        player_items[item_name] = True
        print(f"\nYou picked up {item_name.replace('_', ' ').title()}!")
        return True
    else:
        print(f"\nYou already have {item_name.replace('_', ' ').title()}.")
        return False

def use_item(item_name):
    """Use an item from inventory"""
    if player_items[item_name]:
        if item_name == "elixir_vial":
            heal_amount = 50
            player_stats["health"] = min(player_stats["max_health"], player_stats["health"] + heal_amount)
            print(f"\nYou drink the elixir vial and heal {heal_amount} HP!")
            player_items[item_name] = False
            return True
            
        elif item_name == "strength_potion":
            player_stats["strength"] += 5
            print(f"\nYou drink the strength potion! Strength +5")
            player_items[item_name] = False
            return True
            
        elif item_name == "spell_scroll":
            player_stats["magic"] += 5
            print(f"\nYou study the spell scroll! Magic +5")
            player_items[item_name] = False
            return True
            
        elif item_name == "shield":
            player_stats["defense"] += 5
            print(f"\nYou equip the shield! Defense +5")
            player_items[item_name] = False
            return True
            
        elif item_name == "crown_key":
            print("\nThe Crown Key glows. It's needed to challenge the Final King.")
            return False
    else:
        print(f"\nYou don't have {item_name.replace('_', ' ')}.")
        return False

def use_healing_pool():
    """Use the healing pool to restore health"""
    if player_stats["location"] != "healing_pool":
        print("\nYou must be at the Healing Pool to use it!")
        return False
    
    if player_stats["health"] >= player_stats["max_health"]:
        print("\nYou are already at full health!")
        return False
    
    old_health = player_stats["health"]
    player_stats["health"] = player_stats["max_health"]  # Heal to max, but not above
    heal_amount = player_stats["health"] - old_health
    
    print(f"\nYou immerse yourself in the Healing Pool...")
    time.sleep(1)
    print(f"The magical waters restore {heal_amount} HP!")
    print(f"Your health is now {player_stats['health']}/{player_stats['max_health']}")
    
    # Reset the battle flag after healing
    player_stats["just_finished_battle"] = False
    
    return True

def describe_location():
    """Describe current location"""
    room = room_data[player_stats["location"]]
    print(f"\n{room['description']}")
    
    # Special description for Healing Pool
    if player_stats["location"] == "healing_pool":
        if player_stats["just_finished_battle"]:
            print("The healing waters call to you after your battle.")
        else:
            print("The waters are calm and inviting.")
    
    # Show items in room
    available_items = [item for item in room["items"] if not player_items[item]]
    if available_items:
        print("\nYou see items:")
        for i, item in enumerate(available_items, 1):
            print(f"{i}. {item.replace('_', ' ').title()}")

def get_available_moves():
    """Get available move options with numbers"""
    current_loc = player_stats["location"]
    available_moves = []
    
    print("\nWhere would you like to go?")
    option_num = 1
    
    for location in room_connections[current_loc]:
        crowns_needed = room_data[location]["crowns_needed"]
        if player_stats["crowns"] >= crowns_needed:
            available_moves.append(location)
            
            # Special indicator for Healing Pool
            if location == "healing_pool":
                if player_stats["just_finished_battle"]:
                    print(f"{option_num}. Healing Pool (Restore Health) ✓")
                else:
                    print(f"{option_num}. Healing Pool (No battles fought)")
            else:
                print(f"{option_num}. {location.replace('_', ' ').title()} (needs {crowns_needed} crowns) ✓")
        else:
            print(f"{option_num}. {location.replace('_', ' ').title()} (needs {crowns_needed} crowns) - Locked")
        
        option_num += 1
    
    return available_moves

def regular_combat(enemy_name):
    """Handle regular combat (non-boss)"""
    if enemy_name in player_stats["defeated_enemies"]:
        print(f"\nYou've already defeated the {enemy_name.replace('_', ' ')} here.")
        return True
    
    enemy = enemies[enemy_name]
    print(f"\n=== BATTLE START! ===")
    print(f"Enemy: {enemy_name.replace('_', ' ').title()}")
    
    enemy_health = enemy["health"]
    player_health = player_stats["health"]
    
    # Battle loop
    turn = 1
    while player_health > 0 and enemy_health > 0:
        print(f"\n--- Turn {turn} ---")
        print(f"Your HP: {player_health} | Enemy HP: {enemy_health}")
        print("\nChoose your action:")
        print("1. Basic Attack (Strength based)")
        print("2. Use Card (Elixir based)")
        print("3. Use Item")
        print("4. Defend (Reduce next attack)")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Please enter a number 1-4!")
            continue
        
        if choice == 1:
            # Basic attack using strength
            damage = player_stats["strength"] + random.randint(1, 10)
            actual_damage = max(1, damage - enemy["defense"])
            enemy_health -= actual_damage
            print(f"You attack for {damage} damage! ({actual_damage} after defense)")
            
        elif choice == 2:
            # Use a card if enough elixir
            if player_stats["elixir"] >= 3:
                player_stats["elixir"] -= 3
                card = random.choice(player_cards)
                damage = card[2] + player_stats["magic"] // 2
                actual_damage = max(1, damage - enemy["defense"])
                enemy_health -= actual_damage
                print(f"You use {card[0]} for {damage} damage! ({actual_damage} after defense, -3 elixir)")
            else:
                print("Not enough elixir! Need at least 3.")
                continue
                
        elif choice == 3:
            # Use item
            available_items = [item for item, owned in player_items.items() if owned]
            if available_items:
                print("\nAvailable items:")
                for i, item in enumerate(available_items, 1):
                    print(f"{i}. {item.replace('_', ' ').title()}")
                print("0. Cancel")
                
                try:
                    item_choice = int(input("Choose item number: "))
                    if item_choice == 0:
                        continue
                    if 1 <= item_choice <= len(available_items):
                        use_item(available_items[item_choice - 1])
                    else:
                        print("Invalid choice!")
                except ValueError:
                    print("Please enter a number!")
            else:
                print("No items available!")
            continue
            
        elif choice == 4:
            # Defend - reduces next attack
            print("You take a defensive stance. Next enemy attack will be reduced!")
            defense_bonus = True
        else:
            print("Invalid choice! Please enter 1-4.")
            continue
        
        # Enemy attacks (if still alive)
        if enemy_health > 0:
            enemy_damage = enemy["attack"] + random.randint(1, 10)
            if choice == 4:  # If player defended
                enemy_damage = max(1, enemy_damage - player_stats["defense"] - 5)
                print(f"Enemy attacks for {enemy_damage} damage (reduced by defense)!")
            else:
                enemy_damage = max(1, enemy_damage - player_stats["defense"])
                print(f"Enemy attacks for {enemy_damage} damage!")
            
            player_health -= enemy_damage
        
        turn += 1
        player_stats["elixir"] = min(10, player_stats["elixir"] + 1)  # Gain 1 elixir per turn
    
    # Battle result
    if player_health > 0:
        print(f"\n=== VICTORY! ===")
        print(f"You defeated the {enemy_name.replace('_', ' ')}!")
        player_stats["health"] = player_health
        player_stats["defeated_enemies"].append(enemy_name)
        player_stats["crowns"] += room_data[player_stats["location"]]["crowns_reward"]
        print(f"You earned {room_data[player_stats['location']]['crowns_reward']} crowns!")
        
        # Set flag that player just finished a battle (can use Healing Pool)
        player_stats["just_finished_battle"] = True
        
        increase_stats()  # Increase 3 different stats
        return True
    else:
        print(f"\n=== DEFEAT! ===")
        print(f"The {enemy_name.replace('_', ' ')} was too strong!")
        player_stats["health"] = 0
        return False

def final_boss_combat():
    """Handle final boss combat - different from regular combat"""
    enemy_name = "final_king"
    enemy = enemies[enemy_name]
    
    # Check if player has crown key
    if not player_items["crown_key"]:
        print("\nThe King's Tower is locked! You need the Crown Key from the Legendary Arena.")
        return False
    
    print(f"\n=== FINAL BATTLE! ===")
    print("You face the FINAL KING in his tower!")
    
    enemy_health = enemy["health"]
    player_health = player_stats["health"]
    
    # Special boss mechanics
    boss_phase = 1
    
    while player_health > 0 and enemy_health > 0:
        print(f"\n--- Boss Phase {boss_phase} ---")
        print(f"Your HP: {player_health} | Final King HP: {enemy_health}")
        
        # Boss gets stronger each phase
        boss_attack = enemy["attack"] + (boss_phase * 5)
        
        print("\nChoose your strategy:")
        print("1. Full Attack (High risk, high reward)")
        print("2. Balanced Approach (Medium risk)")
        print("3. Defensive Stance (Low risk)")
        print("4. Use Special Item")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Please enter a number 1-4!")
            continue
        
        if choice == 1:
            # High risk attack
            hit_chance = random.random()
            if hit_chance > 0.3:  # 70% chance to hit
                damage = (player_stats["strength"] * 2) + random.randint(10, 20)
                actual_damage = max(1, damage - enemy["defense"])
                enemy_health -= actual_damage
                print(f"Your powerful attack hits for {damage} damage! ({actual_damage} after defense)")
            else:
                print("Your attack missed!")
                damage = 0
            
        elif choice == 2:
            # Balanced approach
            damage = player_stats["strength"] + player_stats["magic"] + random.randint(5, 15)
            actual_damage = max(1, damage - enemy["defense"])
            enemy_health -= actual_damage
            print(f"Your balanced attack deals {damage} damage! ({actual_damage} after defense)")
            
        elif choice == 3:
            # Defensive
            damage = player_stats["strength"] + random.randint(1, 10)
            actual_damage = max(1, damage - enemy["defense"])
            enemy_health -= actual_damage
            defense_bonus = player_stats["defense"] * 2
            print(f"Your cautious attack deals {damage} damage ({actual_damage} after defense), but you prepare to defend.")
            
        elif choice == 4:
            # Use items
            available_items = [item for item, owned in player_items.items() if owned and item != "crown_key"]
            if available_items:
                print("\nAvailable items:")
                for i, item in enumerate(available_items, 1):
                    print(f"{i}. {item.replace('_', ' ').title()}")
                print("0. Cancel")
                
                try:
                    item_choice = int(input("Choose item number: "))
                    if item_choice == 0:
                        continue
                    if 1 <= item_choice <= len(available_items):
                        use_item(available_items[item_choice - 1])
                    else:
                        print("Invalid choice!")
                except ValueError:
                    print("Please enter a number!")
            else:
                print("No usable items!")
            continue
        else:
            print("Invalid choice! Please enter 1-4.")
            continue
        
        # Boss attacks (gets stronger each phase)
        if enemy_health > 0:
            if choice == 3:  # If player was defensive
                boss_damage = max(1, boss_attack - (player_stats["defense"] * 2))
            else:
                boss_damage = max(1, boss_attack - player_stats["defense"])
            
            player_health -= boss_damage
            print(f"The Final King attacks for {boss_damage} damage!")
        
        # Boss phase change
        if enemy_health < enemy["health"] * 0.5 and boss_phase == 1:
            boss_phase = 2
            print("\nThe Final King enrages! His attacks grow stronger!")
        elif enemy_health < enemy["health"] * 0.25 and boss_phase == 2:
            boss_phase = 3
            print("\nThe Final King is desperate! He fights with everything he has!")
    
    # Battle result
    if player_health > 0:
        print("\n" + "="*50)
        print("CONGRATULATIONS! You defeated the FINAL KING!")
        print("You are now the true Clash Royale Champion!")
        print("="*50)
        player_stats["health"] = player_health
        player_stats["crowns"] += 100
        
        # Set flag that player just finished a battle (can use Healing Pool)
        player_stats["just_finished_battle"] = True
        
        return True
    else:
        print("\nThe Final King was too powerful...")
        player_stats["health"] = 0
        return False

def move_to(location_index, available_moves):
    """Move player to chosen location"""
    if 1 <= location_index <= len(available_moves):
        new_location = available_moves[location_index - 1]
        room = room_data[new_location]
        
        player_stats["location"] = new_location
        if new_location not in player_stats["visited_rooms"]:
            player_stats["visited_rooms"].append(new_location)
        
        print(f"\nYou travel to {new_location.replace('_', ' ').title()}...")
        
        # Clear battle flag when moving to non-healing locations
        if new_location != "healing_pool":
            player_stats["just_finished_battle"] = False
            
        return True
    else:
        print("\nInvalid choice!")
        return False

def restart_game():
    """Reset the game state"""
    global player_stats, player_items, player_cards
    
    player_stats = {
        "health": 100,
        "max_health": 100,
        "strength": 10,
        "defense": 5,
        "magic": 8,
        "crowns": 0,
        "elixir": 3,
        "location": "training_camp",
        "visited_rooms": [],
        "defeated_enemies": [],
        "just_finished_battle": False
    }
    
    player_items = {
        "elixir_vial": False,
        "strength_potion": False,
        "spell_scroll": False,
        "shield": False,
        "crown_key": False
    }
    
    player_cards = [
        ["Archers", "troop", 30, 50, 3],
        ["Goblins", "troop", 20, 30, 2],
        ["Turret", "building", 15, 100, 4]
    ]
    
    print("\n" + "="*50)
    print("NEW GAME STARTED!")
    print("="*50)

def main():
    """Main game loop"""
    print("\n" + "="*50)
    print("CLASH ROYALE ADVENTURE")
    print("="*50)
    print("Travel through arenas, defeat kings, and collect crowns!")
    print("Find the Crown Key to challenge the Final King!")
    print("Visit the Healing Pool after battles to restore health.")
    print("="*50)
    
    game_active = True
    
    while game_active:  # MAIN LOOP
        # Check if player is dead
        if player_stats["health"] <= 0:
            print("\n=== GAME OVER ===")
            print("You have been defeated...")
            print("\n1. Play Again")
            print("2. Quit Game")
            
            try:
                choice = int(input("Enter your choice (1-2): "))
                if choice == 1:
                    restart_game()
                    continue
                elif choice == 2:
                    print("\nThanks for playing!")
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Please enter a number!")
            continue
        
        show_status()
        describe_location()
        
        current_room = room_data[player_stats["location"]]
        
        # Check for enemy encounter
        if current_room["enemy"] and current_room["enemy"] not in player_stats["defeated_enemies"]:
            if current_room["enemy"] == "final_king":
                if not final_boss_combat():
                    # Boss not defeated, show main menu
                    pass
            else:
                if not regular_combat(current_room["enemy"]):
                    # Enemy not defeated, show main menu
                    pass
        
        # Show available items to pick up
        available_items = [item for item in current_room["items"] if not player_items[item]]
        
        # Main action menu
        print("\n" + "="*30)
        print("MAIN MENU")
        print("="*30)
        print("What would you like to do?")
        
        option_number = 1
        options = []
        
        # Option 1: Move to new location
        print(f"{option_number}. Move to another arena")
        options.append("move")
        option_number += 1
        
        # Option 2: Use Healing Pool (if at healing pool)
        if player_stats["location"] == "healing_pool":
            print(f"{option_number}. Use Healing Pool (Restore Health)")
            options.append("heal")
            option_number += 1
        
        # Option 3: Pick up items (if available)
        if available_items:
            print(f"{option_number}. Pick up items")
            options.append("pickup")
            option_number += 1
        
        # Option 4: Use items (if have any)
        if any(player_items.values()):
            print(f"{option_number}. Use items")
            options.append("use")
            option_number += 1
        
        # Option 5: Show status
        print(f"{option_number}. Show detailed status")
        options.append("status")
        option_number += 1
        
        # Option 6: Show items/cards
        print(f"{option_number}. Show inventory and cards")
        options.append("inventory")
        option_number += 1
        
        # Option 7: Quit
        print(f"{option_number}. Quit game")
        options.append("quit")
        
        print("="*30)
        
        try:
            choice = int(input(f"Enter your choice (1-{option_number}): "))
        except ValueError:
            print("Please enter a number!")
            time.sleep(1)
            continue
        
        if 1 <= choice <= len(options):
            action = options[choice - 1]
            
            if action == "move":
                available_moves = get_available_moves()
                if available_moves:
                    try:
                        move_choice = int(input(f"\nEnter destination number (1-{len(available_moves)}): "))
                        move_to(move_choice, available_moves)
                    except ValueError:
                        print("Please enter a number!")
                else:
                    print("\nNo destinations available! You need more crowns.")
                    
            elif action == "heal" and player_stats["location"] == "healing_pool":
                use_healing_pool()
                input("\nPress Enter to continue...")
                    
            elif action == "pickup" and available_items:
                print("\nAvailable items to pick up:")
                for i, item in enumerate(available_items, 1):
                    print(f"{i}. {item.replace('_', ' ').title()}")
                
                try:
                    item_choice = int(input(f"Enter item number to pick up (1-{len(available_items)}): "))
                    if 1 <= item_choice <= len(available_items):
                        pick_up_item(available_items[item_choice - 1])
                    else:
                        print("Invalid choice!")
                except ValueError:
                    print("Please enter a number!")
                    
            elif action == "use":
                available_items_list = [item for item, owned in player_items.items() if owned]
                if available_items_list:
                    print("\nAvailable items to use:")
                    for i, item in enumerate(available_items_list, 1):
                        print(f"{i}. {item.replace('_', ' ').title()}")
                    print("0. Cancel")
                    
                    try:
                        item_choice = int(input("Enter item number to use: "))
                        if item_choice == 0:
                            continue
                        if 1 <= item_choice <= len(available_items_list):
                            use_item(available_items_list[item_choice - 1])
                        else:
                            print("Invalid choice!")
                    except ValueError:
                        print("Please enter a number!")
                else:
                    print("\nNo items to use!")
                    
            elif action == "status":
                show_status()
                input("\nPress Enter to continue...")
                
            elif action == "inventory":
                show_items()
                input("\nPress Enter to continue...")
                
            elif action == "quit":
                print("\nThanks for playing!")
                break
                
        else:
            print("Invalid choice! Please select a valid option.")
        
        # Check for game completion
        if "final_king" in player_stats["defeated_enemies"]:
            print("\n" + "="*50)
            print("YOU HAVE COMPLETED THE GAME!")
            print(f"Total Crowns: {player_stats['crowns']}")
            print(f"Arenas Conquered: {len(player_stats['defeated_enemies'])}")
            print(f"Items Collected: {sum(player_items.values())}")
            print("="*50)
            
            print("\n1. Play Again")
            print("2. Quit Game")
            
            try:
                final_choice = int(input("Enter your choice (1-2): "))
                if final_choice == 1:
                    restart_game()
                elif final_choice == 2:
                    print("\nThanks for playing!")
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Please enter a number!")
            
            time.sleep(1)

# ============================================
# START GAME
# ============================================

if __name__ == "__main__":
    main()
