def main() -> None:
    print(story(*user_input()))


def user_input() ->list:
    noun : str = input("Enter a noun: ")
    verb: str = input("Enter a verb: ")
    noun2: str = input("Enter a noun: ")
    verb2: str = input("Enter a verb: ")
    return [noun.casefold().title(), verb, noun2.casefold().upper(), verb2]

def story(noun1 ,verb1, noun2, verb2) ->str:
    story = f"""
    Once upon a time, There was a {noun1} who loved to {verb1} all day long.
    One day, {noun2} walked into the room and caught the {noun1} in the act.

    {noun2}: "What are you doing?"
    {noun1}: "I'm just coding, What's the big deal?"
    {noun2}: "Well, it's not everyday that you see a {noun1} {verb2} in the middle of the day"
    {noun1}: "I guess you are right, Maybe i should take a break."
    {noun2}: "That's probbably a good idea. Why don't we go hide instead?"
    {noun1}: "Sure! That sounds fun."

    And so, {noun2} and the {noun1} went to hide and had a great time.
    The end
    """
    return story

if __name__ =="__main__":
    main()