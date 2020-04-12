def recite(start_verse, end_verse):
    if start_verse == end_verse:
        return [_get_verse(start_verse)]

    verses = []
    for i in range(start_verse, end_verse+1):
        verses.append(_get_verse(i))
    return verses


def _get_verse(start_verse):
    days = {
        "1": "first",
        "2": "second",
        "3": "third",
        "4": "fourth",
        "5": "fifth",
        "6": "sixth",
        "7": "seventh",
        "8": "eighth",
        "9": "ninth",
        "10": "tenth",
        "11": "eleventh",
        "12": "twelfth",
    }
    last_verse = "a Partridge in a Pear Tree." if start_verse == 1 else "and a Partridge in a Pear Tree."
    verse = [
        f"On the {days.get(str(start_verse))} day of Christmas my true love gave to me: ",
        "twelve Drummers Drumming, ",
        "eleven Pipers Piping, ",
        "ten Lords-a-Leaping, ",
        "nine Ladies Dancing, ",
        "eight Maids-a-Milking, ",
        "seven Swans-a-Swimming, ",
        "six Geese-a-Laying, ",
        "five Gold Rings, ",
        "four Calling Birds, ",
        "three French Hens, ",
        "two Turtle Doves, ",
        f"{last_verse}"
    ]
    first_verse = verse[0]

    return first_verse + "".join(verse[-start_verse:])
