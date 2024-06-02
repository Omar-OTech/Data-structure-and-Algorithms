def solution(text, ending):
    main_str = len(text)
    end_str = len(ending)
    if main_str < end_str:
        return False
    else:
        return text[main_str - end_str:] == ending
# 1st solution
    # return text.endswith(ending)
# 2nd solution






print("samurai", "ai") # True
print("sumo", "omo") # False
print("ninja", "ja") # True
print("sensei", "sei") # True
print("ronin", "onin") # True
print("kempo", "po") # False
print("kendo", "do") # True
print("kenjutsu", "tsu") # True
print("kungfu", "fu") # True
print("karate", "te") # True
print("taekwondo", "do") # True
print("hapkido", "do") # True
print("hwarang", "rang") # True
print("muaythai", "ai") # True
print("silat", "lat") # True
print("capoeira", "ra") # False