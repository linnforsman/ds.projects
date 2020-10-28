def open_dataset(file_name):

    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)

    return data


lord_linton_vocabulary = ["Love, Inhuman, Cannot Compute",
                          "3", "5", "7", "9", "gytr", "Jesus Christ Superstar", "Fucking Dismal."]


lord_linton_phrases = ["Your life's end is approaching.", "Die ", "You N'wah.", "You will suffer greatly.",
                       "I have you.", "You will die.", "Surrender your life to me, and I will end your pain.", "I've got a bone for you, come and get it!", "I've got a cure for your curse, right here!",
                       "Another day, another hundred piles of ore.", "May your ore be pure and your profits large",
                       "So old, so weary.", "The sun shines every day in hell"]


# Finance intelligence, intelligence is the ability to aquire, understand, and use knowledge.
# Information, especially secret information gathered about an actual or potential enemy or adversary.


seven_types_of_love = {"Eros", "Philia", "Storge",
                       "Apage", "Ludus", "Pragma", "Philautia"}


Love_Cataclyst = ["The Physical Body", "The Mind",
                  "Casual (Memories)", "Astral (Emotion)", "Survival Instinct", "Etheric (Unconscious)", "Soul", "Spirit"]

Eros = "Erotic Love"
Philia = "Affectionate Love"
Storge = "Familiar Love"
Ludus = "Playful Love"
Mania = "Obsessive Love"
Pragma = "Enduring Love"
Philautia = "Self Love"
Apage = "Selfless Love"
