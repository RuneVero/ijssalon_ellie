def presenteer(mijn_dict, totaal):
    for key, value in mijn_dict.items():
        print(f"{key} : {value} euro")
    print("=" * 26)
    print(f"Totaal : {totaal} euro")