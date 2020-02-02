#! /usr/bin/python3
import os
import sys

def limpiar():
	if(sys.platform.startswith('linux')):
		os.system("clear")
	else:
		os.system("cls")

def menu():
	print("0-Agregar usuario")
	print("1-Clonar proyecto")
	print("2-Reportar cambio")
	print("3-Comparar Local vs Remoto")
	print("4-Adaptar cambios remotos")
	print("5-Ver estado")
	print("6-Subir cambios")		
	acciones(input("\nOpción: "))

def acciones(opt):
	limpiar()
	if(opt is "0"):
		nombre=input("Usuario:")
		os.system("git config --global user.name '"+str(nombre)+"'")
		correo=input("Correo:")
		os.system("git config --global user.email '"+str(correo)+"'")
		os.system("git config --list")

	if(opt is "1"):
		repo=input("Link Repositorio:")
		os.system("git clone "+str(repo))
		if(sys.platform.startswith('linux')):
			os.system("mv scriptGit.py ./"+str(repo.split("/")[4].split(".")[0]))
		else:
			os.system("move scriptGit.py "+str(repo.split("/")[4].split(".")[0]))
		
		print("Script Movido!!!")
		
	if(opt is "2"):
		message=input("Descripción de cambio:")
		os.system("git status")
		os.system("git add .")
		os.system("git commit -m '"+str(message)+"'")
		os.system("git log --graph --oneline")
		
	if(opt is "3"):
		limpiar()
		os.system("git fetch")
		if(sys.platform.startswith('linux')):
			os.system("git difftool --tool=diffuse master origin/master")
		else:
			os.system("git diff master origin/master")
		
	if(opt is "4"):
		os.system("git merge")
		input()
		
	if(opt is "5"):
		os.system("git status")
		if(sys.platform.startswith('linux')):
			os.system("git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)%Creset' --abbrev-commit")
		else:
			os.system("git log --graph --oneline --decorate --all")
		
	if(opt is "6"):
		os.system("git push origin --all")

limpiar()
print("Script Git")

while(True):
	print("\n")
	menu()
