import json
import os
import logging

class PlayerData:
    def __init__(self, filename):
        self.filename = filename
        self.players = self.load_data()
        logging.info(f"Data manager initialized. Loaded {len(self.players)} players.")

    def load_data(self):
        """Loads player data from the JSON file. If not found, creates an empty one."""
        if not os.path.exists(self.filename):
            return {}
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            logging.error(f"Could not read or parse {self.filename}. Starting with empty data.")
            return {}

    def save_data(self):
        """Saves the current player data to the JSON file."""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.players, f, indent=4, ensure_ascii=False)
        except Exception as e:
            logging.error(f"Failed to save data to {self.filename}: {e}")

    def get_player(self, user_id):
        """Retrieves a player's data by their user ID."""
        return self.players.get(str(user_id))

    def get_player_by_name(self, name):
        """Retrieves a player's data and ID by their username (case-insensitive)."""
        for pid, pdata in self.players.items():
            if pdata['username'].lower() == name.lower():
                return pid, pdata
        return None, None

    def create_player(self, user_id, username):
        """Creates a new player profile if one doesn't exist."""
        user_id_str = str(user_id)
        if user_id_str in self.players:
            return False  # Player already exists

        new_player = {
            'username': username,
            'location': 'slags_alley',
            'faction': None,
            'attributes': {'قدرت': 5, 'چابکی': 5, 'هوش': 5, 'زیرکی': 5, 'جذبه': 5},
            'skills': {'شمشیرزنی': 1, 'پنهان‌کاری': 1, 'متقاعدسازی': 1},
            'inventory': ['لباس مندرس', 'تکه نان خشک'],
            'bonds': {}  # Format: {'target_id': {'type': 'عشق', 'value': 10}}
        }
        self.players[user_id_str] = new_player
        self.save_data()
        logging.info(f"New player created: {username} ({user_id_str})")
        return True

    def get_players_in_room(self, location_id):
        """Returns a dictionary of player_id: player_data for a given location."""
        present_players = {}
        for pid, pdata in self.players.items():
            if pdata.get('location') == location_id:
                present_players[pid] = pdata
        return present_players
