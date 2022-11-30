import boto3
import yaml

#to begin, let's create a boto3 client. This will allow
#us to interact with AWS resources.
myclient = boto3.client('ec2',region_name='us-east-2')


#let's go ahead and load our YAML config file into data
with open('config.yaml', 'r') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    
    #next we're going to pull values from the YAML file into variables for use
    #imgID = data['']


#def create_ec2(client,tags):
#    try:
#        client.run_instances(**data)
#        print("Started")
#    except:
#        print("Failed")

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
            #try:
            myclient.run_instances(**data)
                #print("Instance Started")
            #except:
                #print("Initialization Failed. Exiting.")

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