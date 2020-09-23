# GitComands

## Probando comandos - Tutorial

## Repositorio Local
Primero abrimos la terminal y nos dirigimos a la carpeta de nuestro proyecto ,
debemos identificarnos para ello configuramos nuestro user y email
### git config --global user.name "Jose" 
configuramos nuestro nombre de nuestro repositorio local para indentificarnos 
### git config --global user.email "josecari19999@gmail.com" 
configuramos nuestro nombre de nuestro email
### git init 
inicializamos nuestro repositorio
### git status 
vemos el estado de los archivos
### git add [nombre del archivo] --
prepara el archivo dado
### git add --all 
prepara todos  los archivos de la carpeta 
### git commit  -m "Realizando prueba"
añade los archivos en el branch master como "Realizando prueba"

### Git log 
muestra la información de los commit hechos 

### Git diff 
muestra las modificaciones que has realizado en los archivos 
### Git reset HEAD [archivo]  
elimina los cambios realizados en un archivo

## Git en repositorio Remoto

## git push -u oringin master    
usamos este comando para enviar las confirmaciones realizadas en su rama local a un repositorio remoto


git remote set-url origin https://github.com/your/repository

