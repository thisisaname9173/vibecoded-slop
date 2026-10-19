def vibe_check(mood: str) -> str:
    vibes = {
        "good": "we're so back",
        "bad": "it's joever",
        "mid": "meh",
    }
    return vibes.get(mood, "idk bro")


if __name__ == "__main__":
    print(vibe_check("good"))
