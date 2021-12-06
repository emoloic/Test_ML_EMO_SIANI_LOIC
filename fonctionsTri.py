def tri_shaker(liste):
    """
        Cette fonction effectue le tri dichotomique de la liste passé en argument.
        Elle affiche à la fin les éléments de la liste qui sont triés.
    """
    permutation,sens,position= True,1,0
    debut,fin = 0,len(liste)-2
    while permutation == True:
        permutation = False
        while (position<fin and sens==1) or (position>debut and sens==-1):
            # Test si echange
            if liste[position] > liste[position + 1]:
                permutation = True
                # On echange les deux elements
                liste[position], liste[position + 1] = \
                liste[position + 1],liste[position]
            position = position + sens
        # On change le sens du parcours
        if sens==1:
            fin = fin - 1
        else:
            debut = debut + 1
        sens = -sens
    # Conversion des éléments de notre liste en String
    conversion = [str(i) for i in liste] 
    print("Shaker {}".format(' '.join(conversion)))

def recherche_dichotomique(liste,indice_premier,indice_dernier,valeur_recherchee):
    """
        Fonction de recherche dichotomique
        Elle prend en entrée 04 arguments comme suit:
            - liste: La liste des éléments
            - indice_premier: L'indice du premier élément de la liste 
            - indice_dernier: L'indice du dernier élément de la liste 
            - valeur_recherchee: L'élément à rechercher dans la liste 
        Elle retourne l'index de l'élément recherché dans la liste 
        NB: Si valeur_recherchee ne s'y trouve pas:
                si valeur_recherchee est supérieure à la dernière valeur de la liste ,elle renvoie indice_dernier+1
                sinon, elle renvoie l'index de la première valeur supérieure à la valeur cherchée.
    """
    if valeur_recherchee>liste[indice_dernier]:
        return indice_dernier+1
    while indice_premier!=indice_dernier:
        indice_milieu=(indice_premier+indice_dernier)//2
        if valeur_recherchee<=liste[indice_milieu]:
            indice_dernier=indice_milieu
        else:
            indice_premier=indice_milieu+1
    return indice_premier

def tri_dichotomique(liste):
    """
        Cette fonction effectue le tri dichotomique de la liste passé en argument.
        Elle affiche à la fin les éléments de la liste qui sont triés.
    """
    for i in range(1,len(liste)):
        if liste[i]<liste[i-1]:
            index_valeur = recherche_dichotomique(liste,0,i-1,liste[i])
            liste.insert(index_valeur,liste.pop(i))
    # Conversion des éléments de notre liste en String
    conversion = [str(i) for i in liste] 
    print("Dichotomique {}".format(' '.join(conversion)))