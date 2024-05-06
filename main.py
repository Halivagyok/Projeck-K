kulcs_szo: str = input("Keyword: ")
plain: str = "".join(input("Plain text: ").split())
kulcs_szo2: str = ""
for i in range(0, len(plain)):
    kulcs_szo2 += kulcs_szo[i % len(kulcs_szo)]



titok_szo: str = input("abc elejére kerülő szó: ")


abcList = list(titok_szo) + [chr(i) for i in range(97, 123) if chr(i) not in titok_szo]
if len(plain) == len(kulcs_szo2):
    print(1)

big_list: list = []
temp_list: list = abcList
big_list += temp_list

for i in range(1, len(abcList)):

    temp_str: str = temp_list[0]
    temp_list.remove(temp_str)
    temp_list += temp_str
    big_list += temp_list



print(big_list)