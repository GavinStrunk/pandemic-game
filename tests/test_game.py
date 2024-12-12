import pandemic_game.game as game


def test_init_infection_rate():
    game_state = game.initialize_game()
    assert game_state.infection_rate == 2


def test_init_num_outbreaks():
    game_state = game.initialize_game()
    assert game_state.num_outbreaks == 0


def test_init_disease_states():
    game_state = game.initialize_game()
    assert game_state.blue_disease_state == 'viral'
    assert game_state.red_disease_state == 'viral'
    assert game_state.yellow_disease_state == 'viral'
    assert game_state.black_disease_state == 'viral'


def test_init_world():
    game_state = game.initialize_game()
    assert len(game_state.world.cities) == 48
    assert len(game_state.world.graph.nodes) == 48

def test_init_cubes():
    game_state = game.initialize_game()
    assert game_state.num_blue_cubes == 24
    assert game_state.num_red_cubes == 24
    assert game_state.num_yellow_cubes == 24
    assert game_state.num_black_cubes == 24

def test_init_research_stations():
    game_state = game.initialize_game()
    assert game_state.num_research_stations == 6
