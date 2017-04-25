import sys
import time
sys.path.append("../..")
import game
import othello
game.game=othello
sys.path.append("Joueurs")
import joueur_aleatoire
import premier_coup_valide

joueur1 = joueur_aleatoire
joueur2 = premier_coup_valide

def joue():
  	start_time = time.time()
  	global joueur1
     	global joueur2
   	nbPartie=0
  	nbPartieTotal=100
  	victoireDe1=0
  	victoireDe2=0

	for nbPartie in range(0,nbPartieTotal):
		jeu=game.initialiseJeu()
		it=0
  		print("Partie no : "+str(nbPartie))
		while((it<4)and(not(game.finJeu(jeu)))):
			coup=debutalea(jeu)
			game.joueCoup(jeu,coup)
			it+=1
   			
		while(not(game.finJeu(jeu))):
			coup=saisieCoup(jeu)
			game.joueCoup(jeu,coup)
			it+=1
		#point_victoire=game.getScores(jeu)
		g=game.getGagnant(jeu)
		if(g==1):
        		victoireDe1+=1
  		if(g==2):
        		victoireDe2+=1
        	#print("Match ["+str(point_victoire[0])+":"+str(point_victoire[1])+"]")
        		
  		if (nbPartie==(nbPartieTotal/2)-1):
   			print("Joueur 1 a gagne : "+str(victoireDe1)+" et le Joueur 2 : "+str(victoireDe2)+" avec "+str((nbPartieTotal/2)-victoireDe2-victoireDe1)+" partie(s) nulle(s)")
     			print("Joueur 1 devient joueur 2 et joueur 2 devient joueur 1") 
			temp=joueur1
			joueur1=joueur2
   			joueur2=temp
   			temp2=victoireDe1
   			victoireDe1=victoireDe2
   			victoireDe2=temp2
  		nbPartie+=1

	print("Joueur 1 a gagne : "+str(victoireDe2)+" et le Joueur 2 : "+str(victoireDe1)+" avec "+str(nbPartieTotal-victoireDe2-victoireDe1)+" partie(s) nulle(s)")
	print("En "+str(time.time()-start_time)+" seconde(s).")
 
def saisieCoup(jeu):
	j=game.getJoueur(jeu)
	if(j==1):
		j=joueur1
	else:
		j=joueur2
	coup=j.saisieCoup(game.getCopieJeu(jeu))
	return coup

def debutalea(jeu):
	coup=Joueur_random.saisieCoup(game.getCopieJeu(jeu))
	return coup

joue()
