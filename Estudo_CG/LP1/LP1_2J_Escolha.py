voto = input("Escreva seu voto: ")

match voto:
    case "20":
        print("Você votou Marcelo Bernart")
    case "30":
        print("Você votou Pernalonga")
    case "40":
        print("Você votou Marcelo Patolino")
    case _:
        print("Você votou nulo")