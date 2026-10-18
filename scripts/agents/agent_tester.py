from base_agent import BaseAgent
from my_agent import MyAgent
from sts2_env.run.run_manager import RunManager, SUPPORTED_CHARACTER_IDS
from sts2_env.core.rng import INT_MAX

import random

def main():
    agent = MyAgent()
    agent_tester = AgentTester(agent)
    agent_tester.test_agent()


class AgentTester:
    
    def __init__(self, agent: BaseAgent):
        self._agent = agent

    def _run_agent(self, mgr : RunManager):
        
        while not mgr.is_over:
            
            actions = mgr.get_available_actions()
            
            if not actions:
                print("\n  No available actions; stopping.")
                return 1
            
            action = self._agent.get_action(mgr)
            mgr.take_action(action)
            if mgr.get_combat_state():
                print(mgr.get_combat_state().player.current_hp)

        print(mgr.is_over)
        print(mgr.run_state.player.current_hp)
        print("  YOU WIN!" if mgr.player_won else "  YOU DIED.")
        return 0

    def test_agent(self):
        seed = random.randint(0, INT_MAX)
        mgr = RunManager(
                seed=seed,
                character_id=SUPPORTED_CHARACTER_IDS[0], ## ironclad
                ascension_level=0,
                start_with_neow=True,
            )
        return self._run_agent(mgr)

if __name__ == "__main__":
    main()