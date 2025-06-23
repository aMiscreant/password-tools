#!/usr/bin/env python3
import argparse
from datetime import datetime

# Canadian phone prefixes, feel free to expand
area_codes = [
    '204', '226', '249', '289', '343', '365', '416', '437',
    '519', '548', '604', '613', '647', '705', '807', '905'
]

# Realistic seasonal/year combos
seasons = [
    'winter', 'spring', 'summer', 'fall', 'autumn',
    'Winter', 'Spring', 'Summer', 'Fall', 'Autumn',
    'win', 'spr', 'sum', 'fal', 'aut',  # Abbreviations
    'WINTER', 'SPRING', 'SUMMER', 'FALL', 'AUTUMN',  # All caps
    'rainy', 'dry', 'wet', 'monsoon',  # Tropical regions
    'Rainy', 'Dry', 'Wet', 'Monsoon',
    'snowfall', 'heatwave', 'coldfront', 'thaw',  # Events
    'Snowfall', 'Heatwave', 'Coldfront', 'Thaw',
    'equinox', 'solstice', 'Equinox', 'Solstice'
]

# Months
months = [
    "january", "february", "march", "april", "may", "june",
    "july", "august", "september", "october", "november", "december",
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Holidays (Capitalized and lowercase)
holidays = [
    "christmas", "newyear", "halloween", "thanksgiving", "easter",
    "labourday", "canadaday", "victoriaday", "boxingday", "goodfriday",
    "remembranceday", "nationalday", "independenceday", "valentines", "hanukkah", "diwali", "eid", "ramadan",
    "Christmas", "NewYear", "Halloween", "Thanksgiving", "Easter",
    "LabourDay", "CanadaDay", "VictoriaDay", "BoxingDay", "GoodFriday",
    "RemembranceDay", "NationalDay", "IndependenceDay", "Valentines", "Hanukkah", "Diwali", "Eid", "Ramadan"
]

popular_names = [
    # Male (lowercase)
    "liam", "noah", "jack", "oliver", "lucas", "logan", "james", "benjamin", "ethan", "alexander",
    "william", "jacob", "michael", "daniel", "sebastian", "matthew", "joshua", "ryan", "nathan", "david",

    # Female (lowercase)
    "olivia", "emma", "charlotte", "amelia", "ava", "sophia", "chloe", "mia", "ella", "isla",
    "grace", "emily", "hannah", "scarlett", "nora", "zoey", "lily", "sarah", "madison", "aria",

    # Male (Capitalized)
    "Liam", "Noah", "Jack", "Oliver", "Lucas", "Logan", "James", "Benjamin", "Ethan", "Alexander",
    "William", "Jacob", "Michael", "Daniel", "Sebastian", "Matthew", "Joshua", "Ryan", "Nathan", "David",

    # Female (Capitalized)
    "Olivia", "Emma", "Charlotte", "Amelia", "Ava", "Sophia", "Chloe", "Mia", "Ella", "Isla",
    "Grace", "Emily", "Hannah", "Scarlett", "Nora", "Zoey", "Lily", "Sarah", "Madison", "Aria"
]

# Special global events (password themes people often use)
special_events = [
    "covid", "pandemic", "quarantine", "worldcup", "olympics", "election",
    "blackfriday", "cybermonday", "metaverse", "elonmusk", "moonlanding", "coldwar",
    "Ukraine", "Russia", "Trump", "Biden", "NASA", "Bitcoin", "Ethereum", "GameofThrones",
    "fifa", "FIFA", "WWDC", "CES", "Eurovision", "SuperBowl", "Oscars", "Grammys",
    "COVID", "Pandemic", "Quarantine", "WorldCup", "Olympics", "Election",
    "BlackFriday", "CyberMonday", "Metaverse", "ElonMusk", "MoonLanding", "ColdWar"
]

sport_teams_hockey = [
    # Lowercase
    "canadiens", "mapleleafs", "bruins", "rangers", "islanders", "flyers", "penguins", "capitals",
    "hurricanes", "panthers", "lightning", "senators", "sabres", "redwings", "bluejackets", "devils",
    "blackhawks", "wild", "predators", "blues", "avalanche", "stars", "jets", "coyotes",
    "ducks", "kings", "sharks", "flames", "oilers", "kraken", "goldenknights", "canucks",

    # Capitalized
    "Canadiens", "MapleLeafs", "Bruins", "Rangers", "Islanders", "Flyers", "Penguins", "Capitals",
    "Hurricanes", "Panthers", "Lightning", "Senators", "Sabres", "RedWings", "BlueJackets", "Devils",
    "Blackhawks", "Wild", "Predators", "Blues", "Avalanche", "Stars", "Jets", "Coyotes",
    "Ducks", "Kings", "Sharks", "Flames", "Oilers", "Kraken", "GoldenKnights", "Canucks"
]

sport_teams_football = [
    # Lowercase
    "patriots", "bills", "dolphins", "jets", "ravens", "bengals", "browns", "steelers",
    "texans", "colts", "jaguars", "titans", "broncos", "chiefs", "raiders", "chargers",
    "cowboys", "eagles", "commanders", "giants", "bears", "lions", "packers", "vikings",
    "falcons", "panthers", "saints", "buccaneers", "cardinals", "rams", "49ers", "seahawks",

    # Capitalized
    "Patriots", "Bills", "Dolphins", "Jets", "Ravens", "Bengals", "Browns", "Steelers",
    "Texans", "Colts", "Jaguars", "Titans", "Broncos", "Chiefs", "Raiders", "Chargers",
    "Cowboys", "Eagles", "Commanders", "Giants", "Bears", "Lions", "Packers", "Vikings",
    "Falcons", "Panthers", "Saints", "Buccaneers", "Cardinals", "Rams", "49ers", "Seahawks"
]


sport_teams_basketball = [
    # Lowercase
    "raptors", "celtics", "knicks", "nets", "sixers", "bucks", "bulls", "cavaliers",
    "pacers", "pistons", "hawks", "hornets", "heat", "magic", "wizards",
    "nuggets", "timberwolves", "thunder", "blazers", "jazz", "warriors", "lakers", "clippers",
    "suns", "kings", "mavericks", "spurs", "rockets", "grizzlies", "pelicans",

    # Capitalized
    "Raptors", "Celtics", "Knicks", "Nets", "Sixers", "Bucks", "Bulls", "Cavaliers",
    "Pacers", "Pistons", "Hawks", "Hornets", "Heat", "Magic", "Wizards",
    "Nuggets", "Timberwolves", "Thunder", "Blazers", "Jazz", "Warriors", "Lakers", "Clippers",
    "Suns", "Kings", "Mavericks", "Spurs", "Rockets", "Grizzlies", "Pelicans"
]


years = [str(y) for y in range(datetime.now().year - 125, datetime.now().year + 1)]

# --- Guess Generators ---
def isp_default_guesses(essid):
    essid = essid.upper()
    guesses = []

    if essid.startswith("BELL"):
        base = essid.replace("BELL", "")
        if base.isdigit():
            guesses += [f"{p}{base}" for p in ["BELL", "bell", "Bell"]]
    elif essid.startswith("VIRGIN"):
        base = essid.replace("VIRGIN", "")
        guesses += [f"{p}{base}pass" for p in ["virgin", "VIRGIN"]]
    elif "ROGERS" in essid:
        base = essid.split("ROGERS")[-1]
        if base.isdigit():
            guesses += [f"{p}{base}" for p in ["ROGERS", "rogers", "Rogers"]]
        guesses += ["rogers1234", "rogerswifi"]

    guesses += [essid.lower() + s for s in ["123", "2024", "!@#"]]
    return guesses

def phone_number_guesses(area):
    return [f"{area}{i}" for i in range(1000000, 1001000)]

def street_guesses(street):
    return [street.lower() + suffix for suffix in ["123", "!", "@", "#", "2024"]]

def season_guesses():
    return [f"{s}{y}" for s in seasons for y in years]

def month_guesses():
    return [f"{m}{y}" for m in months for y in years]

def holiday_guesses():
    return [f"{h}{y}" for h in holidays for y in years]

def name_guesses():
    return [f"{name}{y}" for name in popular_names for y in years]

def event_guesses():
    return [f"{event}{y}" for event in special_events for y in years]

def sports_guesses():
    all_teams = sport_teams_hockey + sport_teams_football + sport_teams_basketball
    return [f"{team}{y}" for team in all_teams for y in years]

# --- Master Guess Generator ---
def generate_guesses(args):
    all_guesses = set()

    if args.essid:
        all_guesses.update(isp_default_guesses(args.essid))
    if args.area:
        all_guesses.update(phone_number_guesses(args.area))
    if args.street:
        all_guesses.update(street_guesses(args.street))
    if args.seasons:
        all_guesses.update(season_guesses())
    if args.months:
        all_guesses.update(month_guesses())
    if args.holidays:
        all_guesses.update(holiday_guesses())
    if args.names:
        all_guesses.update(name_guesses())
    if args.events:
        all_guesses.update(event_guesses())
    if args.sports:
        all_guesses.update(sports_guesses())

    return sorted(all_guesses)

# --- CLI ---
def main():
    parser = argparse.ArgumentParser(description="Real-life password list generator for Wi-Fi cracking.")
    parser.add_argument("-e", "--essid", help="Target ESSID (e.g. BELL123456)")
    parser.add_argument("-a", "--area", help="Area code (e.g. 416)")
    parser.add_argument("-s", "--street", help="Street name (e.g. Main, KingWest)")
    parser.add_argument("-o", "--output", help="Save to file")

    # New argument switches
    parser.add_argument("--seasons", action="store_true", help="Include seasonal guesses")
    parser.add_argument("--months", action="store_true", help="Include month/year combinations")
    parser.add_argument("--holidays", action="store_true", help="Include holiday-based guesses")
    parser.add_argument("--names", action="store_true", help="Include popular names + years")
    parser.add_argument("--events", action="store_true", help="Include global event-related patterns")
    parser.add_argument("--sports", action="store_true", help="Include sports teams + years")

    args = parser.parse_args()
    guesses = generate_guesses(args)

    if args.output:
        with open(args.output, 'w') as f:
            for pw in guesses:
                f.write(pw + "\n")
        print(f"[+] Saved {len(guesses)} passwords to {args.output}")
    else:
        print("\n[+] Generated Guesses:")
        for pw in guesses:
            print(f" → {pw}")
        print(f"\n[✓] Total: {len(guesses)} guesses")


if __name__ == "__main__":
    main()