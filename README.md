## Fetch VM Project
### Hello there 👋

<!--whoami -->
- 👋 Hi, I’m @vypr907!
- 👀 This is a project to automate deployment of some resources.
- 🌱 1 EC2 instance, 2 EBS volumes, and 2 users. YAML, Python, and Boto3. Let's go!

Find out more about me & feel free to connect with me here:


[![Linkedin Badge](https://img.shields.io/badge/-Steven_Laszloffy-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/stevenlaszloffy/)](https://www.linkedin.com/in/stevenlaszloffy/)
[![Medium Badge](https://img.shields.io/badge/Steven_Laszloffy-12100E?style=flat-square&logo=medium&logoColor=white&link=https://medium.com/@s.laszloffy)](https://medium.com/@s.laszloffy)
[![Gmail Badge](https://img.shields.io/badge/-steven.laszloffy@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:steven.laszloffy@gmail.com)](mailto:steven.laszloffy@gmail.com)

### Project Parameters
- create a YAML file to be consumed by my application.
- use Python and Boto3.
- No use of config management, provisioning, or IaC tools.
### Project Requirements
User must be able to:
- Run the program.
- Deploy the vm.
- SSH into the instance as 2 unique users.
- Read/Write to each of the 2 volumes.

The program, once run, should walk the user through deploying a Virtual Machine, as well as providing the access information to log in to the VM.

### My Plan
1. User runs program.
2. Program loads YAML config, but doesn't act yet. 
3. Program will prompt user for confirmation to deploy resources. 
4. Program will then display credentials for logging in.


**Full documentation will be located in FETCHVM.md.**