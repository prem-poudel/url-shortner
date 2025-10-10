def convert_to_base62(num):
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(characters)
    if num == 0:
        return characters[0]
    
    result = ""
    while num > 0:
        num, rem = divmod(num, base)
        result = characters[rem] + result
    return result
