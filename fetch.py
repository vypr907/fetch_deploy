import boto3

# menu

def main():
    print("Welcome to the EC2 Deploy-o-matic!")

    #validation loop for boolDeploy
    while True:
        boolDeploy = input("Would you like to deploy your instance? (y/n) ")
        if boolDeploy.lower() == 'y':
            print(boolDeploy)
            print("deploying instance!")

            #insert deployment here

            #display user information here
            break
        elif boolDeploy == 'n':
            print("You've selected No")
            break
        else:
            print("Sorry, please select 'y' or 'n'!")
            continue

    print("Thank you for using vyprTECH CSi's EC2 Deploy-o-matic!")


if __name__=="__main__":
    main()