# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def print_star_names(targets):
	for name in targets:
		print(name)
print_star_names(targets)
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def print_names_and_types(targets):
	for name, info in targets.items():
		print(name, "-", info["Spectral Type"])
print_names_and_types(targets)
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def stars_dimmer_than(targets, limit = .1):
	result = []
	for name, info in targets.items():
		if info["Magnitude"] > limit:
			result.append(name)
	return result
print(stars_dimmer_than(targets))
# 4) Look up another target, add all the necessary information to the targets list. 
targets["Arcturus"] = {
	"RA" : "14h 15 m 39.7 s",
	"Dec" : "+19° 10′ 56″",
	"Magnitude": -0.05,
	"Spectral Type": "K0III"
}
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
import re

def dec_to_degrees(dec):
    """Turns a Dec string like '+38° 47′ 01″' into decimal degrees."""
    deg, minutes, seconds = [float(x) for x in re.findall(r"\d+(?:\.\d+)?", dec)]
    value = deg + minutes / 60 + seconds / 3600
    if dec.strip().startswith("-"):
        value = -value
    return value

def closest_to_20(targets):
    best_name = None
    best_distance = None
    best_mag = None
    for name, info in targets.items():
        distance = abs(dec_to_degrees(info["Dec"]) - 20)
        mag = info["Magnitude"]
        if best_name is None or distance < best_distance or (distance == best_distance and mag < best_mag):
            best_name = name
            best_distance = distance
            best_mag = mag
    return best_name

print(closest_to_20(targets))
# 6) What is your favorite constellation?
favorite_constellation = "The Big Dipper"
print("My favorite constellation is", favorite_constellation)
