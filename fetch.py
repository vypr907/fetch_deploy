import boto3
import yaml

#let's go ahead and load our YAML config file into data
with open('config.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

def create_ec2(client,tags):
    try:
        client.run_instances(MaxCount=1,
                         MinCount=1,
                         ImageId="ami-02d1e544b84bf7502",
                         InstanceType="t2.micro",
                         TagSpecifications=tags,
                         #KeyName="private-ec2",
                         #SecurityGroups=["launch-wizard-6"],
                         #UserData=boot_apache2_script,
                         )
        print("Started")
    except:
        print("Failed")

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