# cac24162

Este proyecto de backend en Python y Flask se elaboró como trabajo integrador del curso de CAC 4.0 Backend.

## PASOS PARA CONFIGURAR VSCODE

Una vez descargados todos los archivos en tu pc, abre la carpeta descomprimida con VSCODE.

- source venv/Scripts/activate
- pip install -r requirements.txt
- python run.py

### PIP TRUCOS PARA REQUIREMENTS

Puedes verificar si las dependencias se instalaron correctamente utilizando el comando pip freeze. Este comando lista todas las bibliotecas instaladas en tu entorno virtual actual. Aquí te dejo cómo puedes hacerlo:

pip freeze

Este comando mostrará una lista de todas las bibliotecas instaladas junto con sus versiones. Puedes buscar en esta lista las bibliotecas que esperabas instalar desde tu archivo requirements.txt.

Si quieres verificar una biblioteca específica y su versión, puedes usar grep para filtrar los resultados. Por ejemplo, si quieres verificar si la biblioteca numpy se instaló correctamente, puedes hacerlo así:

pip freeze | grep numpy

Esto mostrará la versión de numpy instalada en tu entorno virtual, o no mostrará nada si numpy no está instalado.

### 🚀 Iniciar un entorno virtual y correr tu aplicación Flask en VSCode 🚀

1. **Crea un entorno virtual** 🌐:
   Abre la terminal en VSCode (View -> Terminal) y navega hasta el directorio de tu proyecto. Luego, crea un entorno virtual utilizando el siguiente comando:

   ```bash
   python -m venv venv
   ```

   Esto creará un nuevo directorio llamado `venv` en tu directorio de proyecto, que contendrá los archivos del entorno virtual.

2. **Activa el entorno virtual** 🔄:
   Ahora, necesitas activar el entorno virtual. En **Windows**, puedes hacerlo con el siguiente comando:

   ```bash
   **.\venv\Scripts\activate**
   ```

   En **macOS y Linux**, usa este comando:

   ```bash
   source venv/bin/activate
   ```

   Notarás que el nombre de tu entorno virtual aparece al principio de tu línea de comandos, indicando que el entorno está activo.

3. **Instala las dependencias** 📦:
   Con tu entorno virtual activado, puedes instalar las dependencias necesarias para tu proyecto. Flask y el conector MySQL para Python son comunes. Puedes instalarlos con pip:

   ```bash
   pip install flask mysql-connector-python
   ```

### IMPORTANTÍSIMO: VERIFICAR FLASK

pip install -U flask-cors
pip show flask_cors
pip install python-dotenv

### REQUIREMENTS.TXT    || 100PRE ACTUALIZAR!!!-

Desde tu código, creamos los requerimientos y posteriormente con esa lista descargamos todas las dependencias necesarias:
pip freeze > requirements.txt

   Si tienes un archivo `requirements.txt`, puedes instalar todas las dependencias a la vez con:

   pip install -r requirements.txt
   .
   .
4. **Configura la base de datos en MySQL Workbench** 🗄️:
   Asegúrate de que tu base de datos esté en ejecución y accesible a través de los detalles de conexión que has proporcionado en tu archivo `.env`.
5. **Ejecuta tu aplicación Flask** 🎉:
   Ahora, puedes ejecutar tu aplicación Flask. Asegúrate de que tu archivo `run.py` está configurado para ejecutar tu aplicación Flask cuando se llama directamente. Luego, puedes ejecutar tu aplicación con el siguiente comando:

   ```bash
   python run.py

Si hay problemas, asegurarse de configurar la instancia de aplicacion con el nombre correcto:
Si tu instancia de aplicación tiene un nombre diferente, puedes especificarlo usando la variable de entorno FLASK_APP. Por ejemplo, si tu instancia de aplicación se llama myapp en un archivo llamado main.py, puedes establecer la variable de entorno FLASK_APP de esta manera:

export FLASK_APP=app:myapp

Si tu aplicación es parte de un paquete, asegúrate de que estás ejecutando el comando flask run desde un lugar donde el paquete sea accesible, o ajusta tu PYTHONPATH.

Si estás utilizando una fábrica de aplicaciones, asegúrate de especificar el nombre de la función que crea y devuelve la instancia de la aplicación. Por ejemplo, si tienes una función llamada create_app que devuelve tu instancia de aplicación, puedes establecer la variable de entorno FLASK_APP de esta manera:

export FLASK_APP=app:create_app

pip install python-dotenv



   ```

¡Tu aplicación Flask ahora debería estar en ejecución y conectada a tu base de datos MySQL! 🎊

Este minitutorial lo realizamos con un ayudin de Copilot 😊
