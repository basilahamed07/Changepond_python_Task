def cars_models(carname,models,**others):
    print("car name: ",carname)
    print("car models",models)
    for keys,values in others.items():
        print(f"{keys} : {values}")
def main():
    cars_models("supra","2024",company = "toyoto", speed = 400, price = 1000000)
if __name__ == "__main__":
    main()
    