Comando para instalar dependências
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

Comando para inicializar o banco de dados
```bash
flask --app app init-db
```

Comando para inicializar o sistema de rotinas
```bash
flask --app app init-routines
```

Comando para inicializar o aplicativo
```bash
flask --app app run --host=0.0.0.0
```
