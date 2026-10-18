from base_agent import BaseAgent

from sts2_env.run.run_manager import RunManager
    
# Phase constants
PHASE_MAP_CHOICE = "MAP_CHOICE"
PHASE_COMBAT = "COMBAT"
PHASE_CARD_REWARD = "CARD_REWARD"
PHASE_BOSS_RELIC = "BOSS_RELIC"
PHASE_SHOP = "SHOP"
PHASE_REST_SITE = "REST_SITE"
PHASE_EVENT = "EVENT"
PHASE_TREASURE = "TREASURE"
PHASE_RUN_OVER = "RUN_OVER"

## Base class for an agent. Recieves a game state as an input and returns an action.
class MyAgent(BaseAgent):

    def __init__(self):
        pass

    def get_action(self, mgr : RunManager):
        if mgr.phase == PHASE_COMBAT:
            return self._get_combat_action(mgr)
        actions = mgr.get_available_actions()
        return actions[0]

    def _get_combat_action(self, mgr : RunManager):
        actions = mgr.get_available_actions()
        return actions[-1]