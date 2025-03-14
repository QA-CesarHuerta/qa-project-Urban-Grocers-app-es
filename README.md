# Pruebas para el parámetro name al crear un kit para el usuario o usuaria en Urban Grocers
## _Sprint 7 / César Enrique Aburto Huerta - Cohorte 21_
## Paquetes necesarios

Se requieren los siguientes paquetes para correr las pruebas pytest y crear solicitudes http.<br>
Asegurate de ubicarte en la carpeta del proyecto, puedes usar 'cd', antes de ejecutar los los siguientes comandos.

- **Pytest:** utiliza la terminal para instalar el paquete correspondiente pytest. 
```sh
  pip install pytest
```
- **Requests:** instala este paquete con el mismo comando usando el nombre correspondiente del paquete 
```sh
  pip install requests
```
## Url de la solicitud
Antes de proceder con las pruebas asegurate de actualizar `URL_SERVICE` en **configuration.py** con una Url activa del servidor de _TripleTen_.<br>
>Nota: No borrar ' / ' al final de la Url, el resto de las variables se ajustaron para que copiar y pegar la Url sea mas practico ya que por defecto<br>
> al iniciar el servidor el Url viene con esta ' / ' al final
## Correr las pruebas
- Ejecutar el comando `pytest` ideal para verificar rápidamente si las pruebas pasan o fallan, sin demasiados detalles adicionales.<br>
- El comando `pytest -v` "Verbose Mode" es ideal para depuración o escenarios en los que deseas un desglose detallado del estado de cada prueba.<br>
- Para ejecutar las pruebas con el botón "Run" asegurarse de hacerlo con la opción **Current File** seleccionando **create_kit_name_kit_test**<br>
también puede añadir una nueva configuración: **Edit configurations... > Add new configuration > Python test > pytest**
> Nota: Es posible que se añada automaticamente una opción en `Run`, esto porque en el proyecto se hace uso del siguiente código:
```python
if __name__ == '__main__':
    print('El string para el "name" del kit se ve así:\n' + test2_name)
```
> esto permite que `print` no se ejecute cuando se hace una referencia a travez de `import` y solo se ejecute cunado se especifica
## Parametros de prueba "name"
Los valores del atributo "name" se añadieron como variables en **data.py** para mejorar la lectura del código

| Prueba     | Valor           |
|------------|-----------------|
| test1_name | "a"             |
| test2_name | "Abcd..." = 511 |
| test3_name | " "             |
| test4_name | "Acbd..." = 512 |
| test5_name | '"№%@",'        |
| test6_name | " A aa"         |
| test7_name | "123"           |
| test8_name | kit_body = { }  |
| test9_name | 123             |