# SDE program
# teacher/student select program with responses

# Ronnie Selles
# 2022

#   Wanneer je het programma start komt er een input in de console waarin je vervolgens student of teacher in kan vullen.

#       creational design pattern:
#       Factory design pattern 
#       
#   Het programma maakt een nieuwe person aan door middel van de PersonFactory                  
#   de PersonFactory called dan naar de Observer en naar de Proxy van de gekozen PersonType

#       behavioural design pattern:
#       observer design pattern 
#
#   De observer kijkt naar de personfactory
#   De observer maakt een random state aan met een range van 0 tot 10
#   vervolgens is er dus een bepaalde kans dat de observer reageert
#   dit doet hij door te kijken of de state kleiner is dan 5
#   Als de state kleiner is dan 5 print de observer een reactie op basis van welke PersonType je hebt gekozen

#       structural design pattern:
#       Proxy design pattern 
#
#   De Proxy's van Student en Teacher zitten tussen de PersonFactory en de classes Student en Teacher in
#   In dit voorbeeld zorgen deze proxy's ervoor dat er een extra line geprint wordt voordat de uiteindelijke person_method in 
#   de Student en Teacher classes uitgevoerd wordt. Er komt dus eerst een reactie te staan zoals: Hello there student! 
#   en daarna pas dat je student geselecteerd hebt

#       Samengevat
#   Het programma zorgt er dus op een ingewikkelde manier voor dat er op een bepaalde volgorde reacties worden uitgeprint.
#   Het idee is dat een andere student(observer) tegen een medestudent eerst een reactie geeft wanner er een student of teacher binnen komt lopen.
#   En daarna Hallo zegt tegen jou.
#   Tenslotte krijg je nog een confirm melding welk Type je gekozen hebt.
