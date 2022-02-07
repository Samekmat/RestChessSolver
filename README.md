# RestChessSolver

Ustawienie ładowania aplikacji:
  - Bash:
      - export FLASK_APP=app
      - flask run
  - CMD:
      - set FLASK_APP=app
      - flask run
  - PS:
      - $env:FLASK_APP = "app"
      - flask run

Uruchamianie aplikacji:
 - flask run
 - py app.py

 Endpointy:
  - /api/v1/<string:chessFigure>/<string:currentField>
  - /api/v1/<string:chessFigure>/<string:currentField>/<string:destField>

  Dostępne metody:
  - GET

  Zmiana portu:
    flask run
  - -p,--port [port]
