def string_reverse(word:str):
    final = ""
    for i in range(len(word) - 1, -1, -1):
        final = final + word[i]
        
    return final
print(string_reverse("Python"))
