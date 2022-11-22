import boto3

# menu

def main():
    print("Welcome to the EC2 Deploy-o-matic!")
    boolDeploy = input("Would you like to deploy your instance? (y/n) ")

    #validation loop for boolDeploy
    while True:
        try:
            boolDeploy = input("Would you like to deploy your instance? (y/n) ")

        except ValueError:
            print("I'm sorry, please enter 'y' or 'n': ")
            continue
        else:
            print("deploying instance!")
            break

        