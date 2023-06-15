## APLICACION DE OOPS EN UN CRUD

DONDE USAMOS LOS PAQUETES DE PYTHON??

-   [PIP PYTHON](https://pypi.org/)
-   [PIP VIRTUALENV](https://pypi.org/project/virtualenv/)

*   PRIMERA PARTE VIRTTUALENV ==> AISLAMIENTO DE PACKAGES DE PYTHON EN UN ENTORNO DONDE PODAMOS BORRAR Y AGREGAR SIN AFECTAR A NUESTRA MAQUINA

    -   virtualenv <nombre_del_entorno>
    -   en windows => \<nombre_del_entorno>\Scripts\activate | en linux source ./<nombre_del_entorno>/bin/activate
    -   (si es necesario desactivarlo) deactivate
    -   para instalar paquetes es necesario utilizar los comandos pip install <nombre_pack>

*   GENERAR UN PAR DE CONCEPTOS NECESARIOS

    -   CONECTOR A UNA BASE DE DATOS (USANDO LOS GENERADOS POR UN PACKETE DE PYTHON Y QUE NOS PERMITA CONECTAR) (en este caso vamos a hacer de manera realista)
    -   ELECCION ==> [plataforma de railway](https://railway.app/)
    -   Obtenemos los datos de conexion a esa base de datos lo cual necesitamos una URI | PORT | PASS | USER

*   GENERAR UN GESTOR DE USUARIOS

    -   CLASS USER

*   DISTINTAS FORMAS :

    -   USANDO PY-MYSQL ==> FORMA BÁSICA USANDO CONSTRUCTORES DE QUERIES
    -   USANDO SQLALCHEMY ==> FORMA PROTEGIDA USANDO UNA ORM

*
