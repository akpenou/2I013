import sys
sys.path.append("..")
sys.path.append("../..")
import game


def initPlateau():
    return [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,2,0,0,0],[0,0,0,2,1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
	
def initScores():
    return [2,2]
    
def finJeu(jeu):
    return len(game.getCoupsValides(jeu))==0
    	
def coups(jeu):
    j=game.getJoueur(jeu)
    if(j==2):
        j=1
    else:
        j=2
    s = {str(x) for l in range(0,7) for c in range(0,7) for x in entourageVide(jeu,[l,c]) if game.getCaseVal(jeu,l,c)==j}
    return [eval(x) for x in s]
    
    
def getCoupsValides(jeu):
    cps=coups(jeu)
    return [x for x in cps if len(encadrement(jeu,x,False)) > 0]

def entourageVide(jeu,case):
    ret=[]
    l=case[0]
    c=case[1]
    if(l>0):
        if(game.getCaseVal(jeu,l-1,c)==0):
            ret.append([l-1,c])
        if(c>0):
            if(game.getCaseVal(jeu,l-1,c-1)==0):
                ret.append([l-1,c-1])
        if(c>7):
            if(game.getCaseVal(jeu,l-1,c+1)==0):
                ret.append([l-1,c+1])

    if(l<7):
        if(game.getCaseVal(jeu,l+1,c)==0):
            ret.append([l+1,c])
            if(c>0):
                if(game.getCaseVal(jeu,l+1,c-1)==0):
                    ret.append([l+1,c-1])
            if(c>7):
                if(game.getCaseVal(jeu,l+1,c+1)==0):
                    ret.append([l+1,c+1])

    if(c>0):
        if(game.getCaseVal(jeu,l,c-1)==0):
            ret.append([l,c-1])

    if(c<7):
        if(game.getCaseVal(jeu,l,c+1)==0):
            ret.append([l,c+1])

    return ret



def encadrement(jeu,case,tous=True):
    ret=[]
    for l in [-1,0,1]:
        for c in [-1,0,1]:
            if(not((l==0)and (c==0))):
                if encadre(jeu,case[0],case[1],l,c):
                    ret.append([l,c])
                    if(not tous):
                        return ret
    return ret


def encadre(jeu,l,c,ml,mc):
    i=0
    j=game.getJoueur(jeu)
    while True :
        l+=ml
        c+=mc
        if(l>7) or (l<0) or (c>7) or (c<0):
            return False
        v=game.getCaseVal(jeu,l,c)
        if(v==j):
            if(i==0) :
                return False
            else :
                return True
        if(v==0):
            return False
        i=i+1
    return False
            

def joueCoup(jeu,Coup):
    game.getCoupsJoues(jeu).append(Coup)
    j=game.getJoueur(jeu)
    s=game.getScores(jeu)
    e=encadrement(jeu,Coup,True)
    adv=j%2+1
    for d in e:
            l=Coup[0]
            c=Coup[1]
            while True:
                l+=d[0]
                c+=d[1]
                if game.getCaseVal(jeu,l,c)==j :
                    break;
                game.setCaseVal(jeu,Coup[0],Coup[1],j)
                game.setCaseVal(jeu,l,c,j)
                s[j-1]+=1
                s[adv-1]-=1
    s[j-1]+=1
    game.changeJoueur(jeu)
    game.razCoupsValides(jeu)
