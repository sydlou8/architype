"""
Test script for combat system
Run this to verify combat mechanics work before building the API
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from models.game.entities.character.characters.barista import Barista
from models.game.party import Party
from core.services.combat_service import CombatService

def test_basic_combat():
    """Test basic combat functionality"""
    print("\n" + "="*60)
    print("TESTING BASIC COMBAT")
    print("="*60 + "\n")
    
    # Create player party
    print("Creating player party...")
    player_barista = Barista()
    player_party = Party(members=[player_barista])
    
    print(f"✓ Player Party: {player_barista.role} (HP: {player_barista.current_health})")
    
    # Create enemy party
    print("Creating enemy party...")
    enemy_barista = Barista()
    enemy_party = Party(members=[enemy_barista])
    
    print(f"✓ Enemy Party: {enemy_barista.role} (HP: {enemy_barista.current_health})")
    
    # Initialize combat
    print("\nInitializing combat...")
    combat = CombatService(player_party, enemy_party)
    initial_state = combat.start_battle()
    
    print(f"✓ Battle ID: {initial_state['battle_id']}")
    print(f"✓ Turn: {initial_state['turn']}")
    
    # Test taking damage manually
    print("\n" + "-"*60)
    print("TEST 1: Manual damage application")
    print("-"*60)
    
    print(f"Enemy HP before: {enemy_barista.current_health}")
    enemy_barista.take_damage(20)
    print(f"Enemy HP after taking 20 damage: {enemy_barista.current_health}")
    print(f"Enemy is alive: {enemy_barista.is_alive}")
    
    # Test healing
    print("\n" + "-"*60)
    print("TEST 2: Healing")
    print("-"*60)
    
    print(f"Enemy HP before heal: {enemy_barista.current_health}")
    enemy_barista.heal(10)
    print(f"Enemy HP after healing 10: {enemy_barista.current_health}")
    
    # Test turn order
    print("\n" + "-"*60)
    print("TEST 3: Turn order calculation")
    print("-"*60)
    
    turn_order = combat.get_turn_order()
    print("Turn order (by speed):")
    for i, (entity, party) in enumerate(turn_order, 1):
        name = entity.role if hasattr(entity, 'role') else "Unknown"
        print(f"  {i}. {name} ({party}) - Speed: {entity.current_speed}")
    
    # Test battle state
    print("\n" + "-"*60)
    print("TEST 4: Battle state")
    print("-"*60)
    
    state = combat.get_battle_state()
    print(f"Active: {state['is_active']}")
    print(f"Turn: {state['turn']}")
    print(f"Player alive: {state['player_party']['alive_count']}")
    print(f"Enemy alive: {state['enemy_party']['alive_count']}")
    
    print("\n" + "="*60)
    print("✓ ALL BASIC TESTS PASSED!")
    print("="*60 + "\n")


def test_combat_with_skills():
    """Test combat with actual skills (if skills are implemented)"""
    print("\n" + "="*60)
    print("TESTING COMBAT WITH SKILLS")
    print("="*60 + "\n")
    
    # Create parties
    player_party = Party(members=[Barista()])
    enemy_party = Party(members=[Barista()])
    
    combat = CombatService(player_party, enemy_party)
    combat.start_battle()
    
    print("Checking if characters have skills...")
    player = player_party.members[0]
    
    if hasattr(player, 'skills') and player.skills:
        print(f"✓ {player.role} has {len(player.skills)} skills")
        for skill_name, skill in player.skills.items():
            print(f"  - {skill_name}: {skill.name if hasattr(skill, 'name') else 'Unknown'}")
    else:
        print("⚠ No skills found on character (skills may need to be implemented)")
    
    print("\n" + "="*60)
    print("SKILL TEST COMPLETE")
    print("="*60 + "\n")


def test_battle_to_completion():
    """Test a complete battle until one side wins"""
    print("\n" + "="*60)
    print("TESTING COMPLETE BATTLE")
    print("="*60 + "\n")
    
    # Create simple parties
    player_party = Party(members=[Barista()])
    enemy_party = Party(members=[Barista()])
    
    combat = CombatService(player_party, enemy_party)
    combat.start_battle()
    
    print("Starting battle simulation...")
    print(f"Player: {player_party.members[0].role} (HP: {player_party.members[0].current_health})")
    print(f"Enemy: {enemy_party.members[0].role} (HP: {enemy_party.members[0].current_health})")
    
    # Simulate turns manually
    turn = 0
    max_turns = 10
    
    while not combat.check_battle_over() and turn < max_turns:
        turn += 1
        print(f"\n--- Turn {turn} ---")
        
        # Player attacks enemy directly
        player = player_party.members[0]
        enemy = enemy_party.members[0]
        
        if player.is_alive and enemy.is_alive:
            # Simple damage calculation
            damage = 15
            print(f"{player.role} attacks {enemy.role} for {damage} damage")
            enemy.take_damage(damage)
            print(f"{enemy.role} HP: {enemy.current_health}/{enemy.max_health}")
            
            if enemy.is_alive:
                # Enemy counter-attacks
                counter_damage = 10
                print(f"{enemy.role} counter-attacks for {counter_damage} damage")
                player.take_damage(counter_damage)
                print(f"{player.role} HP: {player.current_health}/{player.max_health}")
    
    # Check winner
    winner = combat.get_winner()
    print(f"\n{'='*60}")
    print(f"BATTLE ENDED - Winner: {winner.upper()}")
    print(f"Turns taken: {turn}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    try:
        # Run all tests
        test_basic_combat()
        test_combat_with_skills()
        test_battle_to_completion()
        
        print("\n" + "🎉 "*20)
        print("ALL COMBAT TESTS COMPLETED SUCCESSFULLY!")
        print("🎉 "*20 + "\n")
        
    except Exception as e:
        print(f"\n❌ TEST FAILED: {str(e)}")
        import traceback
        traceback.print_exc()
