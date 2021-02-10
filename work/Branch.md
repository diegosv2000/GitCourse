## Branch 👋

El termino de branch o rama se podria definir como la linea temporal a lo largo de nuestro trabajo.
No obstante nosotros podemos generar una rama a esta linea que parte de un commit en particular y generar
un trabajo parelo a la rama Master/Main , como se ve en la imagen.

<p align="center">

<img src="../src_/branch.png" width="500"/>

<p align="center"></p>

</p align="center">

una de las ventajas que puedes tener al utilizar es las branch puede ser al poder probar un cambio en el código sin 
alterar la rama principal , y también con la opción de volver a la rama principal o aplicar un merge , es muy útil cuando se trabaja con otros programadores.

## Ejemplo 

Se creo una carpeta prueba_branch en el trabajo y dentro de ella esta el archivo `prueba.py` como se ve en la imagen.

<p align="center">

<img src="../src_/prueba.png" width="500"/>

<p align="center"></p>

</p align="center">

ahora en la terminal creamos una brach con el comando  `git branch` + Branchname , en este caso llamaremos mewbranch
siguiente a ello con `git branch` vemos las ramas creadas en este caso tenemos la main y newbranch , pero estamos ubicados en la branch main , entonces si queremos cambiarnos de branch  con el comando `git checkout`+name podemos cambiarnos como se ve en la imágen.

<p align="center">

<img src="../src_/branch1.png" width="700"/>

<p align="center"></p>

</p align="center">

Si nos situamos en el algoritmo de  `prueba.py` este constara de una funcón de encriptamiento llamada cifrado de julio césar donde estamos situados en la main.


<p align="center">

<img src="../src_/mainci.png" width="700"/>

<p align="center"></p>

</p align="center">

si nos cambiamos de rama y alteramos el archivo prueba tendremos.

<p align="center">

<img src="../src_/newbranch.png" width="800"/>

<p align="center"></p>

</p align="center">

utilizamos `git log --oneline` para ver el commit de la nueva rama
<p align="center">

<img src="../src_/log.png" width="800"/>

<p align="center"></p>

</p align="center">


y ahora volvemos a la main y veremos 
<p align="center">

<img src="../src_/main.png" width="800"/>

<p align="center"></p>

</p align="center">

y para borrar una branch con el comando `git branch -D` + name

<p align="center">

<img src="../src_/deletebranch.png" width="800"/>

<p align="center"></p>

</p align="center">
