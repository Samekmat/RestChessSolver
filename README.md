# RestChessSolver
 
 https://rest-chess-solver.herokuapp.com/
 
🇵🇱
RestChessSolver to REST API wyświetlające wszystkie możliwe ruchy figury szachowej bazując na polu, na którym stoi, a także sprawdzające czy podany przez nas ruch z punktu A do punktu B jest możliwy. Bazowe założenie jest takie, iż podana figura jest aktualnie jedyną na całej szachownicy.
---
🇬🇧
RestChessSolver is a REST API that displays all available moves of chess figure, based on their starting field. It's also checking if given move from A to B direction is possible. Base assumption is that figure in the moment is all alone on the chess board.
-----

Ustawienie ładowania aplikacji / App settings:
  - Bash:
      - export FLASK_APP=app
      - flask run
  - CMD:
      - set FLASK_APP=app
      - flask run
  - PS:
      - $env:FLASK_APP = "app"
      - flask run

Uruchamianie aplikacji / Run the app:
 - flask run
 - py app.py

 Endpointy / Endpoints:
  - /api/v1/<string:chessFigure>/<string:currentField>
  - /api/v1/<string:chessFigure>/<string:currentField>/<string:destField>

  Dostępne metody / Available methods:
  - GET

  Zmiana portu / Port change:
  - flask run -p,--port [port]
