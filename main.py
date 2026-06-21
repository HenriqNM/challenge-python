athletes = []

technical_weights = [0.4, 0.3, 0.3]
physical_weights = [0.5, 0.3, 0.2]

def register_athlete(name: str, age: int, position: str, technical_scores: list, physical_scores: list) -> dict:
    technical_avg = 0
    physical_avg = 0

    for i in range(len(technical_weights)):
        technical_avg += technical_scores[i] * technical_weights[i]

    for i in range(len(physical_weights)):
        physical_avg += physical_scores[i] * physical_weights[i]

    final_score = (technical_avg * 0.6) + (physical_avg * 0.4)

    if final_score >= 7.0 and age <= 20:
        status = "aprovado"
    elif final_score >= 5.5 and age <= 20:
        status = "lista de espera"
    else:
        status = "reprovado"

    athlete = {
        "name": name,
        "age": age,
        "position": position,
        "technical_avg": technical_avg,
        "physical_avg": physical_avg,
        "final_score": final_score,
        "status": status
    }

    return athlete

def list_athletes():
    if not athletes:
        print("\nNenhum atleta cadastrado.")
        return

    print("\n" + "=" * 80)
    print(f"{'Nome':<25} | {'Idade':<5} | {'Posição':<12} | {'Média':<6} | {'Status'}")
    print("=" * 80)

    for athlete in athletes:
        print(
            f"{athlete['name']:<25} | {athlete['age']:<5} | {athlete['position']:<12} | {athlete['final_score']:<6} | {athlete['status']}")
    print("=" * 80)


def calculate_general_metrics():
    if not athletes:
        print("\nSem dados para gerar relatório.")
        return

    total_athletes = len(athletes)
    score_sum = 0
    approved_count = 0

    for athlete in athletes:
        score_sum += athlete['final_score']
        if athlete['status'] == "aprovado":
            approved_count += 1

    general_avg = score_sum / total_athletes
    approval_rate = (approved_count / total_athletes) * 100

    print("\n" + "-" * 40)
    print("      Resumo Geral      ")
    print("-" * 40)
    print(f"Total avaliado: {total_athletes}")
    print(f"Média das notas: {general_avg}")
    print(f"Aprovações: {approval_rate}%")
    print("-" * 40)

def main_menu():
    while True:
        print("\n--- Menu ---")
        print("[1] Cadastrar atleta")
        print("[2] Listar avaliados")
        print("[3] Ver estatísticas")
        print("[0] Sair")
        print("------------")

        option = input("Opção: ").strip()

        if option == "1":
            print("\nNova avaliação:")
            name = input("Nome: ").strip()

            try:
                age = int(input("Idade: "))
                position = input("Posição: ").strip()

                print("\nNotas técnicas:")
                passing = float(input("Passe: "))
                dribbling = float(input("Drible: "))
                shooting = float(input("Finalização: "))

                print("\nNotas físicas:")
                speed = float(input("Velocidade: "))
                stamina = float(input("Resistência: "))
                strength = float(input("Força: "))

                new_athlete = register_athlete(
                    name, age, position,
                    [passing, dribbling, shooting],
                    [speed, stamina, strength]
                )
                athletes.append(new_athlete)
                print(f"\nSalvo. Status: {new_athlete['status']}")

            except ValueError:
                print("\nErro: use apenas números para idade e notas.")

        elif option == "2":
            list_athletes()

        elif option == "3":
            calculate_general_metrics()

        elif option == "0":
            print("\nSaindo.")
            break
        else:
            print("\nOpção inválida.")

if __name__ == "__main__":
    main_menu()