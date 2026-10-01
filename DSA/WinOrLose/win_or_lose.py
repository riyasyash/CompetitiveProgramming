if __name__ == "__main__":
    n_test_cases = int(input())
    i = 0
    while (i < n_test_cases):
        n_count = int(input())
        v_energies = str(input())
        villain_energies = [int(i) for i in v_energies.split()]
        h_energies = str(input())
        hero_energies = [int(i) for i in h_energies.split()]
        count = 0
        print(f"villain {villain_energies}")
        print(f"hero {hero_energies}")
        while count < n_count:
            if max(hero_energies) <= max(villain_energies):
                print(f"{max(villain_energies)} -> {max(hero_energies)}")
                print("LOSE")
                break
            else:
                hero_energies.remove(max(hero_energies))
                villain_energies.remove((max(villain_energies)))
            count += 1
        if count == n_count:
            print("WIN")
        i += 1
