# xác định khách có đến dự  tiệc muộn hay k
arrivales = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Forrd'] 
def party_late(arrivales, name):
    return name in arrivales
print(party_late(arrivales, name= "Gilbert"))
print(party_late(arrivales, name= ""))
