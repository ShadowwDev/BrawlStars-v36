import json
from Utils.Helpers import Helpers
from Files.CsvLogic.Characters import Characters
from Files.CsvLogic.Skins import Skins
from Files.CsvLogic.Cards import Cards

class Player:
    try:
        config = open('config.json', 'r')
        content = config.read()
    except FileNotFoundError:
        Helpers().create_config()
        config = open('config.json', 'r')
        content = config.read()

    settings = json.loads(content)

    skins_id = Skins().get_skins_id()
    brawlers_id = Characters().get_brawlers_id()

    ID = 0
    token = 'SomeRandomToken'

    name = settings['Username']
    profile_icon = settings['Thumbnail']
    name_color = settings['NameColor']
    trophies = settings['Trophies']
    high_trophies = settings['HighestTrophies']
    trophy_reward = settings['TrophyRoadReward']
    exp_points = settings['ExperiencePoints']
    gems = settings['Gems']
    resources = [{'ID': 1, 'Amount': settings['BrawlBoxTokens']}, {'ID': 8, 'Amount': settings['Gold']},
                 {'ID': 9, 'Amount': settings['BigBoxTokens']}, {'ID': 10, 'Amount': settings['StarPoints']}]
    region = settings['Region']
    content_creator = settings['SupportedContentCreator']
    home_brawler = settings['HomeBrawler']
    theme_id = settings['ThemeID']
    environment = settings['Environment']

    db = None

    unlocked_skins = skins_id
    brawlers_unlocked = brawlers_id

    brawlers_card_id = []
    for x in brawlers_unlocked:
        brawlers_card_id.append(Cards().get_unlock_by_brawler_id(x))

    brawlers_spg = Cards().get_spg_id()

    def_trophies = settings['BrawlersTrophies']
    def_high_trophies = settings['BrawlersHighestTrophies']

    brawlers_trophies = {}
    for x in brawlers_id:
        brawlers_trophies.update({f'{x}': def_trophies})

    brawlers_high_trophies = {}
    for x in brawlers_id:
        brawlers_high_trophies.update({f'{x}': def_high_trophies})

    def_level = settings['BrawlersLevel'] - 1

    brawlers_level = {}
    for x in brawlers_id:
        brawlers_level.update({f'{x}': def_level})

    def_pp = settings['BrawlersPowerPoints']

    brawlers_powerpoints = {}
    for x in brawlers_id:
        brawlers_powerpoints.update({f'{x}': def_pp})

    clients = {}

    def __init__(self, device):
        self.device = device