# bot.py

Aquí es donde ocurre la "magia". Se recorre la lista  `COMMANDS ` definida en `settings.py`
La lista contiene la ubicación de carpetas que contiene los comandos que se cargaran dinámicamente.<br>

`line 12, bot.py`
```python
for command in COMMANDS:
    sys.path.append(command)
    for file in glob(f'{command}*.py'):
        if file.endswith('__.py'):
            continue
        logging.info(f'Loading {file}')
        file = file.replace(f'{command}', '').replace('.py', '')
        module = __import__(file)
        
        bot.command(file)(getattr(module, file))
```

Los comandos son archivos python con una función con el mismo nombre del archivo. Su estructura básica es:
```python
async def name(ctx):
    pass
```

Si el archivo no contiene una función con el mismo nombre, se registrara en el log
. Puede haber casos que tengamos una comando abreviado y en nuestro código usamos el el
 nombre completo. Para solucionar esto, tiene que crear una variable con el nombre del archivo y definirla a la función.
 <br>
Ejemplo: `yt.py`
```python
async def search_youtube(ctx, *args):
    pass

yt = search_youtube
```
