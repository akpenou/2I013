import sys
sys.path.append("..")
sys.path.append("../..")
import game



def initPlateau():
	"""void->plateau
	initialise le plateau
	"""
	#Plateau:list[list[int]]
    plateau = [ [ 4 for x in range(6) ] for y in range(2) ]
	return plateau
	
	
def initScores():
	"""void->tuple[int,int]
	initialise score
	"""
	return [0, 0]
	
def finJeu(jeu):
    score = game.getScores(jeu)
    print ('awele - finjeu - liste coups valides:', game.getCoupsValides(jeu))
    return not len(game.getCoupsValides(jeu)) or score[0] >= 25 or score[1] >= 25
	
def getCoupsValides(jeu):
        a=adversaireAffame(jeu)
        cp=coups(jeu)#retourne la liste des cases du joueur contenant au moins une graine       
        if(a==False):
            return cp
            
        v=[]
        for coup in cp:
                c=coup[1]
                l=coup[0]
                g=game.getCaseVal(jeu,l,c)
                if l==0:
                        if g>c:
                                v.append(coup)

                else :
                        if g>=(6-c):
                                v.append(coup)
        return v



def joueCoups(jeu,coup):
        v=game.getCaseVal(jeu,coup[0],coup[1])
        game.setCaseVal(jeu,coup[0],coup[1],0)
        distribue(jeu,coup,v)
        game.addCoupJoue(jeu,coup)
        game.changeJoueur(jeu)
        game.razCoupsValides(jeu)

	
def distribue(jeu,coup,nb):
    c=coup
    
    liste=[]
    while (nb > 0) :            
        c=nextCase(jeu,c,True)
        if c[0]==coup[0] and c[1]==coup[1]:
            continue
        game.addCaseVal(jeu,c[0],c[1],1)
        nb-=1
        
    while peutManger(jeu,c):
        v=game.getCaseVal(jeu,c[0],c[1])
        liste.append(v)
        game.setCaseVal(jeu,c[0],c[1],0)
        game.addScore(jeu,game.getJoueur(jeu),v)
        c=nextCase(jeu,c,False)
        
    if(len(liste)>0) and adversaireAffame(jeu):
            n=1
            while(n<=len(liste)):
                c=nextCase(jeu,c,True)
                g=liste[-n]
                game.setCaseVal(jeu,c[0],c[1],g)
                game.addScore(jeu,game.getJoueur(jeu),-g)  
                n+=1
       

def peutManger(jeu,c):
	""""jeu * Pair[nat nat] -> bool
        Retourne vrai si on peut manger le contenu de la case:
            - c'est une case appartenant a l'adversaire du joueur courant
            - La case contient 2 ou 3 graines
        """
	if c[0]==(game.getJoueur(jeu)-1):
		return False
	v=game.getCaseVal(jeu,c[0],c[1])
	if(v!=2)and(v!=3):
		return False
	return True
	

def adversaireAffame(jeu):
	j=game.getJoueur(jeu)
	j=j%2+1 #on recupere le joueur adverse
	for i in range (0,6):
		coup=game.getCaseVal(jeu,j-1,i)
		if coup!=0 :
			return False
	return True
	
            
            
def nextCase(jeu,coup,antihoraire=True):
        sens=1
        if (antihoraire):
        	if(coup[0]==1):
        		case= coup[1]+sens #dans le cas ou on se trouve sur la 2eme ligne
                if(coup[0]==0):
                	case=coup[1]-sens #dans le cas ou on se trouve sur la 1ere ligne
                if(case<0 and coup[0]==0): #dans le cas ou on se trouve dans la 1ere ligne 1ere colonne dans le sens -1
                	return [1,0]
                if(case>5 and coup[0]==1):
                	return [0,5]
                return[coup[0],case]
                
        else :
        	if(coup[0]==1):
        		case= coup[1]-sens #dans le cas ou on se trouve sur la 2eme ligne
                if(coup[0]==0):
                	case=coup[1]+sens #dans le cas ou on se trouve sur la 1ere ligne 
                if(case<0 and coup[0]==1):
                	return [0,0]
                if(case>5 and coup[0]==1):
                	return [1,5]
		return [coup[0],case]        
        
         
def coups(jeu):
	liste= []
	j=game.getJoueur(jeu)
	for i in range (0,6):
		v=game.getCaseVal(jeu,j-1,i)
		if(v!=0):
			liste.append([j-1,i])
	return liste
	

def finalisePartie(jeu):
    """jeu->void
        Met a jour les scores des joueurs en prenant en compte les graines restantes sur le plateau
    """
    p=game.getPlateau(jeu)
    g1=reduce(lambda a,b: a+b,p[0])
    g2=reduce(lambda a,b: a+b,p[1])
    game.addScore(jeu,1,g1)
    game.addScore(jeu,2,g2)
