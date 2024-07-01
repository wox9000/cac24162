# cac24162

PASOS PARA CONFIGURAR VSCODE

- source venv/Scripts/activate
- pip install -r requirements.txt

## PIP TRUCOS PARA REQUIREMENTS

Puedes verificar si las dependencias se instalaron correctamente utilizando el comando pip freeze. Este comando lista todas las bibliotecas instaladas en tu entorno virtual actual. Aquí te dejo cómo puedes hacerlo:

pip freeze

Este comando mostrará una lista de todas las bibliotecas instaladas junto con sus versiones. Puedes buscar en esta lista las bibliotecas que esperabas instalar desde tu archivo requirements.txt.

Si quieres verificar una biblioteca específica y su versión, puedes usar grep para filtrar los resultados. Por ejemplo, si quieres verificar si la biblioteca numpy se instaló correctamente, puedes hacerlo así:

pip freeze | grep numpy

Esto mostrará la versión de numpy instalada en tu entorno virtual, o no mostrará nada si numpy no está instalado.
