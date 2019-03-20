matrica=[[" " for i in range(15)] for j in range(6)]

matrica[0][0]="Dan \ vreme"
matrica[1][0]="Ponedeljak"
matrica[2][0]="Utorak"
matrica[3][0]="Sreda"
matrica[4][0]="Cetvrtak"
matrica[5][0]="Petak"

matrica[0][1]="08:00-09:00"
matrica[0][2]="09:00-10:00"
matrica[0][3]="10:00-11:00"
matrica[0][4]="11:00-12:00"
matrica[0][5]="12:00-13:00"
matrica[0][6]="13:00-14:00"
matrica[0][7]="14:00-15:00"
matrica[0][8]="15:00-16:00"
matrica[0][9]="16:00-17:00"
matrica[0][10]="17:00-18:00"
matrica[0][11]="18:00-19:00"
matrica[0][12]="19:00-20:00"
matrica[0][13]="20:00-21:00"
matrica[0][14]="21:00-22:00"

for row in matrica:
    for elem in row:
        print(elem, end=' ')
    print("\n")

